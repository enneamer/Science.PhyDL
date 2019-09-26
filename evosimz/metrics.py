import ete3
import numpy

__all__ = [
    'neighbour_join',
    'normalized_robinson_foulds',
    'robinson_foulds',
    'correct_tree_count',
]


def neighbour_join(adjacency, node_names=None):
    """Use neighbour joining to build a phylogenetic tree.

    Parameters
    ----------
    adjacency : numpy.ndarray
        The adjacency matrix of all the species.
    node_names : list[str]
        A list of node names. By default, it is "node#".

    Returns
    -------
    ete3.Tree
        The constructed tree.
    """
    numpy.fill_diagonal(adjacency, 0.0)
    adjacency = adjacency.clip(max=1000000.0)
    adjacency = (adjacency + adjacency.T) / 2
    node_count = adjacency.shape[0]
    if node_names is None:
        node_names = ['taxon' + str(i) for i in range(node_count)]
    nodes = [ete3.TreeNode(name=name) for name in node_names]
    while len(nodes) > 1:
        q = adjacency * (len(nodes) - 2)
        q -= adjacency.sum(axis=0, keepdims=True)
        q -= adjacency.sum(axis=1, keepdims=True)
        numpy.fill_diagonal(q, float('+inf'))
        i, j = numpy.unravel_index(numpy.argmin(q), q.shape)
        dist_i = 0.5 * adjacency[i, j]
        if len(nodes) > 2:
            dist_i += (0.5 * (adjacency[i, :].sum() - adjacency[j, :].sum())
                       / (len(nodes) - 2))
        dist_j = adjacency[i, j] - dist_i
        new_node = ete3.TreeNode()
        new_node.add_child(nodes[i], name=nodes[i].name, dist=dist_i)
        new_node.add_child(nodes[j], name=nodes[j].name, dist=dist_j)
        mask = numpy.ones(len(nodes), dtype='?')
        mask[i] = False
        mask[j] = False
        new_adjacency = numpy.zeros((len(nodes) - 1, len(nodes) - 1))
        new_adjacency[:-1, :-1] = adjacency[mask, :][:, mask]
        new_adjacency[-1, :-1] = 0.5 * (
                adjacency[i, mask] + adjacency[j, mask] - adjacency[i, j]
        )
        new_adjacency[:-1, -1] = new_adjacency[-1, :-1]
        nodes.remove(new_node.children[0])
        nodes.remove(new_node.children[1])
        nodes.append(new_node)
        adjacency = new_adjacency
    return nodes[0]


def normalized_robinson_foulds(tree, prediction):
    """Calculate the normalized Robinson-Foulds score.

    Parameters
    ----------
    tree : ete3.PhyloTree
        The truth tree.
    prediction : ete3.PhyloTree
        The predicted tree.

    Returns
    -------
    float
        The normalized Robinson-Foulds score between the truth and
        predicted trees. It is the raw Robinson-Foulds score divided by
        the maximal Robinson-Foulds score possible for the tree.
    """
    score, max_score = tree.robinson_foulds(prediction,
                                            unrooted_trees=True)[:2]
    return score / max_score


def robinson_foulds(tree, prediction):
    """Calculate the Robinson-Foulds score.

    Parameters
    ----------
    tree : ete3.PhyloTree
        The truth tree.
    prediction : ete3.PhyloTree
        The predicted tree.

    Returns
    -------
    float
        The Robinson-Foulds score between the truth and predicted trees.
    """
    return tree.robinson_foulds(prediction, unrooted_trees=True)[0]


def correct_tree_count(tree, prediction):
    """Return 1 if the tree is correct.

    Parameters
    ----------
    tree : ete3.PhyloTree
        The truth tree.
    prediction : ete3.PhyloTree
        The predicted tree.

    Returns
    -------
    float
        1.0 if the tree is correct, 0.0 otherwise.
    """
    score = tree.robinson_foulds(prediction, unrooted_trees=True)[0]
    return 1.0 if score == 0 else 0.0


class BatchScorer:
    """A scorer for prediction batches."""

    def __init__(self, tree_builder, *metrics):
        """Create a BatchScorer.

        Parameters
        ----------
        tree_builder : callable
            A function to build a tree from the score matrix.
        metrics : list[callable]
            A list of scoring metric functions to score the tree.
        """
        self.tree_builder = tree_builder
        self.metrics = metrics

    def __call__(self, predictions, trees):
        """Score all the predictions in the batch.

        Parameters
        ----------
        predictions : torch.Tensor
            The output of the neural network model.
        trees : list[ete3.Tree]
            The truth.

        Returns
        -------
        list[float]
            The average scores of all the predictions in the batch.
        """
        scores = [0.0 for __ in self.metrics]
        predictions = predictions.cpu().data.numpy()
        for prediction, tree in zip(predictions, trees):
            predicted_tree = self.tree_builder(prediction)
            for i, metric in enumerate(self.metrics):
                scores[i] += metric(tree, predicted_tree)
        return [score for score in scores]
