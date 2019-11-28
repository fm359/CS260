#!/usr/bin/env python

import queue


class HuffmanNode(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    # returns children of node
    def children(self):
        return self.left, self.right


# creates a leaf node for each symbol and adds it to the priority queue
# while there is more than one node, removes two highest nodes, creates
# internal node with children, adds new node to queue, and returns root
def create_tree(freq):
    priority_q = queue.PriorityQueue()
    for value in freq:
        priority_q.put(value)
    while priority_q.qsize() > 1:
        l, r = priority_q.get(), priority_q.get()
        huff_node = HuffmanNode(l, r)
        priority_q.put((l[0]+r[0], huff_node))
    return priority_q.get()

# walks down the tree to the leaves and assigns a code to each symbol
def walk_down_tree(tree_node, prefix="", code_symbol={}):
    if isinstance(tree_node[1].left[1], HuffmanNode):
        walk_down_tree(tree_node[1].left, prefix + "0", code_symbol)
    else:
        code_symbol[tree_node[1].left[1]] = prefix + "0"
    if isinstance(tree_node[1].right[1], HuffmanNode):
        walk_down_tree(tree_node[1].right, prefix + "1", code_symbol)
    else:
        code_symbol[tree_node[1].right[1]] = prefix + "1"
    return code_symbol

print ("huffman.py tests")
print ()

frequencies = [
    (12.345, 'a'), (3.566, 'b'), (7.346, 'c'),  (4.677, 'd'),
    (1.469, 'e'),  (2.228, 'f'), (9.568, 'g'),  (13.346, 'h'),
    (5.567, 'i'),  (0.153, 'j'), (0.747, 'k'),  (8.545, 'l'),
    (7.342, 'm'),  (6.749, 'n'), (11.345, 'o'), (10.566, 'p'),
    (22.356, 'q'), (5.987, 'r'), (7.676, 's'),  (9.056, 't'),
    (2.758, 'u'),  (1.037, 'v'), (3.235, 'w'),  (0.444, 'x'),
    (1.974, 'y'),  (1.111, 'z')]

node = create_tree(frequencies)
print(node)

code = walk_down_tree(node)
for i in sorted(frequencies, reverse=True):
    print(i[1], '{:6.2f}'.format(i[0]), code[i[1]])
