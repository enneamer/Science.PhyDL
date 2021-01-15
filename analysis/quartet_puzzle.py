#!/usr/bin/env python

import itertools
import os
import random
import re
import subprocess
import sys

import ete3

out_dir = 'results/'
trueq_dir = 'trueq'
con_dir = 'consensus'
true_treefile = 'tree.nw'
nrep = 100
paup_str = (f'set maxtrees=10001;\n'
            f'execute ../DIR/all.nex;\n'
            f'contree all /strict=no majrule=yes le50=yes treefile=DIR_maj.tre;\n'
            f'quit;')
next_ret = re.compile(r'tree\s+MajRule\s+=\s+\[\&R\]\s+(.+;)\n')

def main():
    print('load data ...')
    if not os.path.isdir(out_dir):
        subprocess.call(['mkdir', out_dir])
    if not os.path.isdir(f'{out_dir}{trueq_dir}'):
        subprocess.call(['mkdir', f'{out_dir}{trueq_dir}'])
    if not os.path.isdir(f'{out_dir}{con_dir}'):
        subprocess.call(['mkdir', f'{out_dir}{con_dir}'])
    true_tree = ete3.Tree(true_treefile, format=0)
    true_qtree_list, true_label_list = get_true_qtrees(true_tree)
    n_quartet = len(true_qtree_list)
    for qtree in true_qtree_list:
        qtree.unroot()

    # true quartet trees
    print('get true quartet topologies ...')
    pred_topo_list = [get_topo(true_qtree_list[x], true_label_list[x]) for x in range(n_quartet)]
    q_dict = dict(zip([frozenset(x) for x in pred_topo_list], list(range(len(pred_topo_list)))))
    taxon_set = set([])
    __ = [taxon_set.update(set(x)) for x in pred_topo_list]
    taxon_list = sorted(list(taxon_set))
    random.seed(1075)
    print(f'puzzling {nrep} times based on true quartets ...')
    rf_dis_true = []
    final_trees = []
    for i in range(nrep):
        final_tree = quartet_puzzle(pred_topo_list, q_dict, taxon_list)
        # print(final_tree)
        with open(f'{out_dir}{trueq_dir}/{i}.nw', 'w') as f:
            print(final_tree.write(format=9), file=f)
        print(i, end=' ', flush=True)
        rf_dis_true.append(final_tree.robinson_foulds(true_tree, unrooted_trees=True)[:2])
        final_trees.append(final_tree.write(format=9))
    print()
    with open(f'{out_dir}{trueq_dir}/rf', 'w') as f:
        print('\n'.join([f'{x[0]}\t{x[1]}' for x in rf_dis_true]), file=f)
    with open(f'{out_dir}{trueq_dir}/all.nex', 'w') as f:
        print('BEGIN TREES;', file=f)
        print('\n'.join([f'\tTree tree{x} = {y}' for x, y in enumerate(final_trees)]), file=f)
        print('END;', file=f)
    os.chdir(f'{out_dir}{con_dir}')
    with open(f'{trueq_dir}_paup', 'w') as f:
        print(re.sub('DIR', trueq_dir, paup_str), file=f)
    subprocess.call(['paup', f'{trueq_dir}_paup'])
    with open(f'{trueq_dir}_maj.tre') as f:
        next_re = next_ret.search(f.read())
        if next_re:
            nw_str = next_re.group(1)
        else:
            sys.exit(f'no ret match {trueq_dir}!')
    with open(f'{trueq_dir}_maj.nw', 'w') as f:
        print(nw_str, file=f)
    os.chdir('../../')


def get_true_qtrees(tree):
	qtree_list, label_list = [], []
	for qtaxa in itertools.combinations([x.name for x in tree.get_leaves()], 4):
		qtree = tree.copy('deepcopy')
		qtree.prune(qtaxa)
		qtree.unroot()
		qtaxa = qtree.get_leaves()
		for taxon in qtaxa[1:]:
			if taxon.up == qtaxa[0].up:
				label = qtaxa.index(taxon)
				break
		qtree_list.append(qtree)
		label_list.append(label)
	return qtree_list, label_list


def get_topo(tree, label):
    leaves = [x.name for x in tree.get_leaves()]
    others = [1, 2, 3]
    others.remove(label)
    return (leaves[0], leaves[label], leaves[others[0]], leaves[others[1]])


def get_topo_from_list(leaves, label):
    others = [1, 2, 3]
    others.remove(label)
    return (leaves[0], leaves[label], leaves[others[0]], leaves[others[1]])


def get_ij(topo, taxon):
    if topo.index(taxon) < 2:
        return tuple(topo[2:4])
    else:
        return tuple(topo[:2])


def mark_tree(tree, ij_list):
    for node in tree.traverse():
        node.support = 0
    leaves = [x.name for x in tree.get_leaves()]
    for nodei, nodej in ij_list:
        if not (nodei in leaves and nodej in leaves):
            continue
        nodei = tree & nodei
        nodej = tree & nodej
        mrca = tree.get_common_ancestor((nodei, nodej))
        for node in (nodei, nodej):
            while node.up != mrca and node != mrca:
                node.support += 1
                node = node.up
            if node.up == mrca:
                node.support += 1
    least_nodes = [tree.children[0], ]
    for node in tree.traverse():
        if node == tree:
            continue
        if node.support < least_nodes[0].support:
            least_nodes = [node, ]
        elif node.support == least_nodes[0].support:
            least_nodes.append(node)
    return random.choice(least_nodes)


def insert_taxon(tree, node, taxon):
    ancestor = node.up
    node.detach()
    break_point = ancestor.add_child()
    break_point.add_child(name=taxon)
    break_point.add_child(child=node)


def quartet_puzzle(topo_list, q_dict, taxon_list):
    new_taxon_list = taxon_list[:]
    random.shuffle(new_taxon_list)
    while not frozenset(new_taxon_list[:4]) in q_dict:
        random.shuffle(new_taxon_list)
    init_topo = topo_list[q_dict[frozenset(new_taxon_list[:4])]]
    tree = ete3.Tree(f'(({init_topo[0]}, {init_topo[1]}),({init_topo[2]}, {init_topo[3]}));')
    for taxon in new_taxon_list[4:]:
        ij_list = [get_ij(topo_list[q_dict[x]], taxon) for x in q_dict if taxon in x]
        least_node = mark_tree(tree, ij_list)
        # print(tree)
        # print([x.support for x in tree.traverse('preorder')], least_node.support)
        insert_taxon(tree, least_node, taxon)
    return tree


if __name__ == '__main__':
    main()