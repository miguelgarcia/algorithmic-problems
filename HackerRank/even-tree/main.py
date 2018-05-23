#!/bin/python3

import math
import os
import random
import re
import sys

class Node:
    def __init__(self):
        self.child = []
        self.even = 1

    def calc_even(self):
        self.even = (1 + sum(map(lambda t: t.calc_even(), self.child))) % 2
        return self.even

    def removable_edges(self, with_parent):
        # Take into account if this node has a parent
        even = (self.even + with_parent) % 2
        if even == 1:
            # Cant subdivide in trees with even nodes count
            return 0

        ret = 0
        for n in self.child:
            if n.even == 0:
                # The number of nodes that the tree with this node as root has and 
                # the tree with n as root has are both even.
                # Thus the edge from this node to n can be removed keeping both with
                # an even number of nodes.
                # +1 for this edge and take into account the removable edges of
                # the subtree with n as root.
                ret += 1 + n.removable_edges(with_parent=0)
            else:
                # Edge can not be removed
                # Sum the removable edges of the subtree with n as root but, take
                # account that this node changes n "evennes"
                ret += n.removable_edges(with_parent=1)
        
        return ret

if __name__ == '__main__':
    tree_nodes, tree_edges = map(int, input().split())

    tree_from = [0] * tree_edges
    tree_to = [0] * tree_edges

    for i in range(tree_edges):
        tree_from[i], tree_to[i] = map(int, input().split())

    # Write your code here.

    # Build a directed tree
    nodes = []
    for _ in range(0, tree_nodes):
        nodes.append(Node())

    for i in range(0, len(tree_from)):
        a = min(tree_from[i], tree_to[i])-1
        b = max(tree_from[i], tree_to[i])-1
        nodes[a].child.append(nodes[b])

    # Calc for each node if the subtree with it as root has an even number of nodes
    nodes[0].calc_even()

    # Calc max removable edges to create only even subtrees
    print(nodes[0].removable_edges(with_parent=0))

