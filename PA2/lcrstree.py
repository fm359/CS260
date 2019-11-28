#!/usr/bin/env python

from copy import *

class node:
	def __init__(self):
		self.labl = None
		self.left_child = None
		self.right_sib = None
		self.par = None

	#returns the parent of the node
	def parent(self):
		return self.par

	#returns the leftmost child of the node
	def leftmost_child(self):
		return self.left_child

	#returns the right sibling of the node
	def right_sibling(self):
		if self.right_sib is None:
			return node() # null tree
		else:
			return self.right_sib

	#returns the label of the node
	def label(self):
		return self.labl

	# returns the root of the tree for the current node
	def root(self):
		root = self
		while root.par != None:
			root = root.par
		return root

	#makes the tree null
	def makenull(self):
		self.labl = None
		self.left_child = None
		self.right_sib = None
		self.par = None

#creates a lcrs tree from two specified child nodes and a given label
#if T1 and T2 are None, then creates a tree with specified label but no children
def createi(v, T1, T2):
	if T1 is None and T2 is None:
		tree = node()
		tree.labl = v
	elif T1 is not None and T2 is not None:
		tree = node()
		tree.labl = v;
		tree.left_child = T1
		tree.left_child.par = tree
		tree.left_child.rs = T2
		tree.left_child.rs.par = tree
	else:
		raise("2nd and 3rd arguments must both be either None or a lcrstree")
	return tree

print "lcrstree.py tests"
print
print "Create tree with root 'a' and children 'b' and 'c'"
tree = createi('a', createi('b', None, None), createi('c', None, None))
print "Test label"
print tree.label()
print "Test parent"
print tree.leftmost_child().parent(), "Label:", tree.leftmost_child().parent().label()
print "Test leftmost_child"
print tree.leftmost_child(), "Label:", tree.leftmost_child().label()
print "Test right_sibling"
print tree.leftmost_child().right_sibling(), "Label:", tree.leftmost_child().right_sibling().label()
print "Create a new tree whose children are two copies of the original tree. Root should be 'root'"
tree2 = deepcopy(tree)
tree = createi("root", tree, tree2)
print "From first leftmost child:"
print tree.leftmost_child().root(), tree.leftmost_child().root().label()
print "From second leftmost child:"
print tree.leftmost_child().leftmost_child().root(), tree.leftmost_child().leftmost_child().root().label()
