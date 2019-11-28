#!/usr/bin/env python

class arraylist:
	def __init__(self):
		self.maxlength = 1000
		self.elements = [None]*self.maxlength
		self.last = 0

	#accepts a list and returns position of first element of the list as int 0
	def first(self):
		return 0

	#accepts a list and returns position of last element of the list
	def end(self):
		return self.last

	#returns the element of the given list at integer position p
	def retrieve(self,p):
		if p > self.last:
			return None
		else :
			return self.elements[p]

	#returns the integer position of the element x in the given list
	def locate(self,x):
		for i in range(0,self.last):
			if self.elements[i] == x:
				return i

	#returns the integer position that follows the specified position p in the list
	#"next" is a reserved name in python
	def next_position(self, p):
		if p + 1 >= self.last:
			return None
		else:
			return p + 1

	#returns the integer position that precedes the specified position p in the list
	def previous(self,p):
		if p > self.last or p == 0:
			return None
		else:
			return p - 1

	#inserts element x at position p in the specified list
	def insert(self,x,p):
		if p > self.last:
			print "Cannot insert at position", p, "index out of range"
		elif p == self.last:
			self.elements[p] = x
			self.last = self.last + 1
		else:
			self.elements[p+1:self.last+1] = self.elements[p:self.last]
			self.elements[p] = x
			self.last = self.last + 1

	#delete the element at position p from the list
	def delete(self,p):
		if p <= self.last and p >= 0:
			for i in range(p,self.last):
				self.elements[i-1] = self.elements[i]
			self.last = self.last - 1
		else:
			print "Cannot delete at index", p, ", index out of range"

	#makes specified list empty
	def makenull(self):
		self.elements = [None]*self.maxlength
		self.last = 0
