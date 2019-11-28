#!/usr/bin/env python

class node:
	def __init__(self):
		self.labl = None
		self.children = []
		self.par = None #None if root

	#returns the parent of the node
	def parent(self):
		return self.par

	#returns the leftmost child of the node
	def leftmost_child(self):
		return self.children[0]

	#returns the right sibling of the node
	def right_sibling(self):
		try:
			return self.par.children[(self.par.children.index(self))+1]
		except IndexError:
			return None # return None if last sibling

	#returns the label of the node
	def label(self):
		return self.labl

	#returns the root of the tree for the current node
	def root(self):
		root = self
		while root.par != None:
			root = self.par
		return root

	#makes the tree null
	def makenull(self):
		self.labl = None
		self.children = []
		self.par = None #should be None if root

#makes a new node with label v and gives it i children
#which are the roots of trees specified in list Ti

#i=0,1,2,3
def createi(v, Ti):
	if len(Ti) >= 4:
		raise("loctree.createi: maximum 3 children allowed")
	else:
		tree = node()
		tree.labl = v
		for child_tree in Ti:
			tree.children.append(child_tree)
			child_tree.par = tree
		return tree

def main():
	print "loctree.py tests"
	print
	print "Create empty tree with label 'a':"
	test_list = []
	tree = createi("a", test_list)
	print "Return parent (should be None):"
	print
	tree.parent()
	print "Return children (should be None):"
	for child in tree.children:
		print child
	print "Should have no children"
	print
	print "Create tree with three nodes, where root is labeled 'a' and nodes 'b','c','d'"
	tree1 = createi("b", test_list)
	tree2 = createi("c", test_list)
	tree3 = createi("d", test_list)
	test_list.append(tree1)
	test_list.append(tree2)
	test_list.append(tree3)
	tree = createi("a", test_list)
	print "Root is now:", tree.root(), "Label:", tree.root().label()
	for child in tree.children:
		label = child.label()
		parent = child.root()
		print child, "Label:", label, "Parent label:", parent
	node = tree.leftmost_child()
	print "Leftmost child of 'a' is:", node, "Label:", node.label()
	node = node.right_sibling()
	print "Right sibling of leftmost child is:", node, "Label:", node.label()
	node = node.right_sibling()
	print "Right sibling of right sibling is:", node, "Label:", node.label()
	print "Last child reached, another right_sibling call should return None:"
	node = node.right_sibling()
	print "Right sibling of the leftmost child is:", node
	print
	print "Test makenull on tree (nothing should print):"
	tree.makenull()
	for child in tree.children:
		label = child.label()
		parent = child.root()
		print child, "Label:", label, "Parent label:", parent

if __name__ == '__main__':
	main()
