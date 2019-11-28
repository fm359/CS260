#!/usr/bin/env python

class cell:
	def __init__(self):
		self.element = None
		self.next = None

class pointerlist:
	def __init__(self):
		self.head = None
		self.pos = None

	#returns the first element in the list
	def first(self):
		return self.head

	#returns the last element in the list
	def end(self):
		if self.head is None and self.pos is None:
			return None
		else:
			c = self.head
			while c.next:
				c = c.next
			return c

	#returns the element of cell pointer p
	def retrieve(self,p):
		c = self.first()
		for i in range(0,p+1):
			if c.next is not None:
				c = c.next
		return c.element

	#returns pointer to cell containing element x in given list (-1 if not found)
	def locate(self,x):
		index = 0;
		c = self.first()
		while c:
			if c.element == x:
				return index
			index += 1
			c = c.next
		return -1

	#returns pointer to the next cell of the cell pointer p
	#"next" is a reserved name in python, this is the next best thing
	def next_position(self, c):
		return c.next

	#returns pointer to the previous cell of the cell pointer p
	def previous(self,p):
		c = self.first()
		while c:
			if c.next == p:
				return c
			c = c.next
		return None

	#inserts element x into position of cell pointed by p
	def insert(self,x,p):
		if p is None:
			c = cell()
			c.element = x
			c.next = None
			self.head = c
			self.pos = self.head
		elif (p == self.first() and self.first() != self.end()) or p == 0:
			c = cell()
			c.element = x
			c.next = self.head
			self.head = c
			self.pos = self.head
		else:
			c = cell()
			c.element = x
			tmp = self.first()
			while tmp and p > 1:
				tmp = tmp.next
				p -= 1
			c.next = tmp.next
			tmp.next = c

	#deletes the element and cell containing it at cell pointed by p
	def delete(self,p):
		temp = self.first()
		if p == 0:
			self.head = temp.next
		elif p == self.end():
			if temp.next == None:
				self.makenull()
			else:
				while temp.next.next:
					temp = temp.next
				temp.next = None
		else :
			while self.previous(p) > 0 :
				temp = temp.next
				p = self.previous(p)
			t1 = temp
			t2 = temp.next
			if t2.next != None:
			    t1.next = t2.next
		self.pos = self.head

	#makes specified list empty
	def makenull(self):
		self.head = None
		self.pos = None

	def printlist(self):
		c = self.first()
		if c is None:
			print "Empty Pointer List"
		else:
			while c:
				print c.element
				c = c.next

#pointerlist tests

print "pointerlist.py tests"
print
print "head insertion:"
test = pointerlist()
test.insert(1,0)
test.insert(2,0)
test.insert(3,0)
test.insert(4,0)
test.insert(5,0)
print "list should be [5 4 3 2 1]:"
test.printlist()

print "delete first and last elements (should be 4 3 2)"
test.delete(0)
test.delete(test.end())
test.printlist()
print
print "return pointer to first cell and its element, 4:"
print test.first(), "element:", test.first().element
print
print "return pointer to next cell from 4 and its element (should be 3)"
c = test.first()
print test.next_position(c), "element: ", test.next_position(c).element
print
print "return pointer to last cell and its element (should be 2)"
print test.end(), "element:", test.end().element
print
print "previous cell from 2 (should be 3)"
c = test.end()
print test.previous(c), "element: ", test.previous(c).element
print "3 is located at index (should be 1)", test.locate(3)
print "At index 2, the element (should be 2)", test.retrieve(2)

print "Make list empty and printlist (should return empty)"
test.makenull()
test.printlist()
print
print
