#!/usr/bin/env python

#NOTE: self is the first method argument for all methods as it is proper convention for python
#For "undefined" results, None is returned or error message printed

class cell:
	def __init__(self):
		self.element = None
		self.next = None

class pointerstack:
	def __init__(self):
		self.head = None

	#returns the element at the top of the specified stack
	def top(self):
		if self.empty():
			print "Error retrieving top: stack is empty."
		else:
			return self.head.element

	#deletes the element at the top of the specified stack
	#does not return the element as per the book
	def pop(self):
		if self.empty():
			print "Error popping element: stack is empty."
		else:
			self.head = self.head.next

	#adds the specified element x to the top of the stack
	def push(self,x):
		if self.empty():
			new = cell()
			new.element = x
			self.head = new
		else:
			new = cell()
			new.element = self.head.element
			new.next = self.head.next
			self.head.element = x
			self.head.next = new

	#returns true if stack is empty, false otherwise
	def empty(self):
		if self.head is None:
			return True
		else:
			return False

	#makes the specified stack empty by moving the stack pointer to the top
	#skips manually deleting every element
	def makenull(self):
		self.head = None

#pointerstack.py tests

n = 10

print "Creating new stack, is it empty?"
stk = pointerstack()
print stk.empty()

print "Iterated insert of 10 elements into stack"
for i in range(0,n):
	stk.push(i)

print "Attempting to print top of stack, which should be 9..."
print stk.top()
print "Attempting to pop 3 elements, top should then be 6..."
stk.pop()
stk.pop()
stk.pop()
print stk.top()
print "Is stack empty now?"
print stk.empty()
print "Popping last 7 elements. Empty now?"
stk.pop()
stk.pop()
stk.pop()
stk.pop()
stk.pop()
stk.pop()
stk.pop()
print stk.empty()
print "What's the top element though?"
print stk.top()
print "Pushing a few elements, then making stack empty through makenull.."
stk.push(1)
stk.push(2)
stk.push(3)
stk.makenull()
stk.pop()