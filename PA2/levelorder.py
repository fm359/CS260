#!/usr/bin/env python

from loctree import *

#Exercise 3.10, using loctree

#prints the level order representation of the given tree
def levelorder(tree):
	current_level = [tree.root()]
	while current_level:
		next_level = []
		for n in current_level:
			print n.label()
			for child in n.children:
				next_level.append(child)
		print
		current_level = next_level

print "levelorder.py tests"
print
test_list = []
tree1 = createi("e",test_list)
tree2 = createi("f",test_list)
tree3 = createi("g",test_list)
tree4 = createi("h",test_list)
tree5 = createi("i",test_list)
tree6 = createi("j",test_list)

tree1 = createi("b",[tree1,tree2])
tree2 = createi("c",[tree3,tree4])
tree3 = createi("d",[tree5,tree6])
test_list.append(tree1)
test_list.append(tree2)
test_list.append(tree3)

tree = createi("a",test_list)

levelorder(tree)
