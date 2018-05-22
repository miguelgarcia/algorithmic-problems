#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    g_nodes, g_edges = map(int, input().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().split())

    # Write your code here.
    # Sort edges
    edges = []
    for i in range(0, len(g_from)):
        edges.append([g_weight[i], g_from[i]+g_to[i], g_from[i], g_to[i]])
    
    edges.sort()
    edges = map(lambda e: [e[0], e[2], e[3]], edges)

    trees = [] # Keep partial trees, each tree has an associated list of nodes and
               # the sum of the weights of the edges in the tree.
    tree_idx = [None] * (g_nodes+1) # Map nodes to associated tree
    for e in edges:
        w = e[0]
        tree_v = tree_idx[e[1]]
        tree_u = tree_idx[e[2]]

        if tree_v is None and tree_u is None:
            # Case two nodes not in any tree
            tree = dict(w=w,nodes=[e[1], e[2]])
            trees.append(tree)
            tree_idx[e[1]] = len(trees)-1
            tree_idx[e[2]] = len(trees)-1
        elif tree_v is None and tree_u is not None:
            # Case one node in an existing tree, the other not in any tree
            tree = trees[tree_u]
            tree["nodes"].append(e[1])
            tree_idx[e[1]] = tree_u
            tree["w"] += w
        elif tree_u is None and tree_v is not None:
            # Case one node in an existing tree, the other not in any tree
            tree = trees[tree_v]
            tree["nodes"].append(e[2])
            tree_idx[e[2]] = tree_v
            tree["w"] += w
        elif tree_v != tree_u:
            # Two nodes in different trees, must merge the trees adding the new edge
            tree = trees[tree_v]
            tree["w"] += w + trees[tree_u]["w"]
            for idx in trees[tree_u]["nodes"]:
                tree_idx[idx] = tree_v
                if idx not in tree["nodes"]:
                    tree["nodes"].append(idx)
            trees[tree_u] = None
        if len(tree["nodes"]) == g_nodes:
            break
    print(tree["w"])