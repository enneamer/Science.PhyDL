#!/usr/bin/env python3

"""Quartet tree classification

* Model: Convolutional neural network with basic residual connections
  and batch normalization.
* Training data:
    * 100000 pre-simulated trees using training2.
    * Each epoch uses randomly sampled 1000 trees.
    * The batch size is 16.
* Validation data: 2000 pre-simulated trees using training2.
* Optimizer: Adam with an initial learning rate of 0.001.
"""

import pathlib
import pickle

import fire
import logbook
import numpy
import torch.autograd
import torch.nn
import torch.optim
import torch.utils.data

import evosimz
import evosimz.common
import evosimz.model
import evosimz.simulators

_LOG = logbook.Logger(__name__)

_MODEL_PATH = (pathlib.Path(__file__) / '../../data/models').resolve()

_BATCH_SIZE = 16

_TRAINING_SIZE = 2000


def train(warm_start=None, device='cuda', worker_count=4):
    """Train a model.

    Parameters
    ----------
    warm_start : int
        Continue training from the specified epoch.
    device : str
        The device for training. By default, it use any GPU devices.
    worker_count : int
        The number of CPU workers for data preparation.
    """
    output_path = _MODEL_PATH / pathlib.Path(__file__).stem
    output_path.mkdir(exist_ok=True, parents=True)
    training_data, validation_data = _prepare_data(worker_count)
    log_handler = logbook.FileHandler(str(output_path / 'train.log'),
                                      mode='w', level='DEBUG', bubble=True)
    with log_handler.threadbound():
        model, optimizer, score_records = _load_model(
            output_path, device, warm_start
        )
        if device == 'cuda':
            fast_model = torch.nn.DataParallel(model).to(device)
        else:
            fast_model = model
        loss_function = torch.nn.CrossEntropyLoss(reduction='sum')
        epoch = len(score_records)
        while epoch < 500 or not evosimz.model.is_stagnant(score_records, 7):
            epoch = len(score_records)
            _LOG.debug(f'Epoch {epoch}.')
            fast_model.train()
            sample_count, score = 0, 0.0
            optimizer.zero_grad()
            for i, (_a, x, _b, y) in enumerate(training_data):
                sample_count += x.size()[0]
                x = x.to(device, non_blocking=True)
                y = y.to(device, non_blocking=True)
                loss = loss_function(fast_model(x), y)
                loss.backward()
                score += float(loss)
                optimizer.step()
                optimizer.zero_grad()
            _LOG.debug(f'Training loss: {score / sample_count}')
            fast_model.eval()
            sample_count, score = 0, 0.0
            with torch.autograd.no_grad():
                for __, x, __, y in validation_data:
                    # y = torch.cat(y, dim=0)
                    sample_count += x.size()[0]
                    x = x.to(device, non_blocking=True)
                    y = y.to(device, non_blocking=True)
                    score += float(loss_function(fast_model(x), y))
            score /= sample_count
            _LOG.debug(f'Validation loss: {score}')
            score_records.append(score)
            torch.save([model, optimizer, score_records],
                       (output_path / f'{epoch}.pickle'))


def _prepare_data(worker_count):
    """Prepare the data file.

    Parameters
    ----------
    worker_count : int
        The number of CPU workers for data preparation.

    Returns
    -------
    torch.utils.data.DataLoader
        The training data loader.
    torch.utils.data.DataLoader
        The testing data loader.
    """
    training_dataset = evosimz.QuartetDataset('training2')
    training_sampler = torch.utils.data.RandomSampler(
        training_dataset, replacement=True, num_samples=_TRAINING_SIZE,
    )
    training_data = torch.utils.data.DataLoader(
        training_dataset,
        sampler=training_sampler,
        batch_size=_BATCH_SIZE,
        num_workers=worker_count,
        collate_fn=evosimz.Collator('amino acid', sample_sites=True),
        pin_memory=True,
    )
    validation_data = torch.utils.data.DataLoader(
        evosimz.QuartetDataset('training2_validation'),
        num_workers=worker_count,
        collate_fn=evosimz.Collator('amino acid', sample_sites=False),
        pin_memory=True,
    )
    return training_data, validation_data


def _load_model(output_path, device, warm_start):
    """Load models from the file.

    If there is no model files to load, prepare a new model.

    Parameters
    ----------
    output_path : pathlib.Path
        The output folder for model training.
    device : str
        The device.
    warm_start : int | NoneType
        The epoch of the model to load. If it is None, then generate a
        new model.

    Returns
    -------
    _Model
        The neural network model.
    torch.optim.Adam
        An network optimizer.
    list[float]
        Validation scores of all previous epochs.
    """
    if warm_start is None:
        model = _Model().to(device, non_blocking=True)
        optimizer = torch.optim.Adam(model.parameters(), lr=0.001,
                                     weight_decay=1e-5)
        evosimz.model.initialize_weights(model)
        score_records = []
    else:
        model, optimizer, score_records = torch.load(
            (output_path / f'{warm_start}.pickle').open('rb'),
            map_location=torch.device(device),
        )
    return model, optimizer, score_records


def predict(epoch, testing_dataset, output_path, device='cpu'):
    """Apply a pre-trained model for prediction.

    Parameters
    ----------
    epoch : int
        The epoch index of a pre-trained model.
    testing_dataset : str
        The name of a testing dataset.
    output_path : pathlib.Path | str
        A folder for results output.
    device : str
        The device for predicting. By default, it use any GPU devices.
    """
    model_path = _MODEL_PATH / pathlib.Path(__file__).stem / f'{epoch}.pickle'
    model = torch.load(model_path, map_location=torch.device(device))[0]
    testing_data = torch.utils.data.DataLoader(
        evosimz.QuartetDataset(testing_dataset),
        num_workers=0,
        collate_fn=evosimz.Collator('amino acid'),
        pin_memory=True,
    )
    output_path = pathlib.Path(output_path)
    evosimz.model.ensure_clean_folder(output_path)
    log_handler = logbook.FileHandler(str(output_path / 'predict.log'),
                                      mode='w', level='DEBUG', bubble=True)
    with log_handler.threadbound(), torch.autograd.no_grad():
        model.eval()
        conformations = []
        results = []
        truths = []
        for __, x, order, truth in testing_data:
            x = x.to(device, non_blocking=True)
            order = order.to(device, non_blocking=True)
            score = evosimz.model.sort_quartet_scores(model(x), order)
            individuals = score.argmax(dim=1).flatten()
            major_vote = numpy.array([(individuals == x).sum() for x in range(3)]).argmax()
            mean_score = score.mean(dim=0).cpu().data.numpy()
            # results.append(mean_score)
            # conformations.append(mean_score.argmax())
            results.append(score)
            conformations.append(major_vote)
            truths.append(truth[0].cpu().data.numpy())
        pickle.dump(results, (output_path / 'raw_results.pickle').open('wb'))
        pickle.dump(conformations, (output_path / 'results.pickle').open('wb'))
        pickle.dump(truths, (output_path / 'truths.pickle').open('wb'))


def list_loss():
    """List the current validation loss data."""
    model_dir = _MODEL_PATH / pathlib.Path(__file__).stem
    epoch = 0
    model_path = (model_dir / f'{epoch}.pickle')
    while model_path.exists():
        epoch += 1
        model_path = (model_dir / f'{epoch}.pickle')
    if epoch == 0:
        raise RuntimeError('no model found')
    model_path = (model_dir / f'{epoch - 1}.pickle')
    score_records = torch.load(str(model_path),
                               map_location=torch.device('cpu'))[2]
    print('Epoch', 'Validation loss', sep='\t')
    for epoch, loss in enumerate(score_records):
        print(epoch, loss, sep='\t')


class _Model(torch.nn.Module):
    """A neural network model to predict phylogenetic trees."""

    def __init__(self):
        """Create a neural network model."""
        super().__init__()
        self.conv = torch.nn.Sequential(
            torch.nn.Conv1d(80, 80, 1, groups=20),
            torch.nn.BatchNorm1d(80),
            torch.nn.ReLU(),
            torch.nn.Conv1d(80, 32, 1),
            torch.nn.BatchNorm1d(32),
            torch.nn.ReLU(),
            _ResidueModule(32),
            _ResidueModule(32),
            torch.nn.AvgPool1d(2),
            _ResidueModule(32),
            _ResidueModule(32),
            torch.nn.AvgPool1d(2),
            _ResidueModule(32),
            _ResidueModule(32),
            torch.nn.AvgPool1d(2),
            _ResidueModule(32),
            _ResidueModule(32),
            torch.nn.AdaptiveAvgPool1d(1),
        )
        self.classifier = torch.nn.Linear(32, 3)

    def forward(self, x):
        """Predict phylogenetic trees for the given sequences.

        Parameters
        ----------
        x : torch.Tensor
            One-hot encoded sequences.

        Returns
        -------
        torch.Tensor
            The predicted adjacency trees.
        """
        x = x.view(x.size()[0], 80, -1)
        x = self.conv(x).squeeze(dim=2)
        return self.classifier(x)


class _ResidueModule(torch.nn.Module):

    def __init__(self, channel_count):
        super().__init__()
        self.layers = torch.nn.Sequential(
            torch.nn.Conv1d(channel_count, channel_count, 1),
            torch.nn.BatchNorm1d(channel_count),
            torch.nn.ReLU(),
            torch.nn.Conv1d(channel_count, channel_count, 1),
            torch.nn.BatchNorm1d(channel_count),
            torch.nn.ReLU(),
        )

    def forward(self, x):
        return x + self.layers(x)


if __name__ == '__main__':
    logbook.StderrHandler(bubble=True).push_application()
    fire.Fire()
