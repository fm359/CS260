#!/usr/bin/env python

class arraystack:
	def __init__(self):
		self.maxlength = 1000
		self.top = self.maxlength
		self.elements = [None]*self.maxlength

	#returns the element at the top of the given stack
	def top(self):
		if self.empty():
			print "Stack is empty."
		else:
			return self.elements[self.top]

	#deletes the element at the top of the specified stack
	def pop(self):
		if self.empty():
			print "Stack is empty."
		else:
			self.top = self.top + 1

	#inserts the given element x to the top of the stack
	def push(self,x):
		if self.top == 0:
			print "Stack is full."
		else:
			self.top = self.top - 1
			self.elements[self.top] = x

	#returns true if stack is empty, otherwise false
	def empty(self):
		if(self.top >= self.maxlength):
			return True
		else:
			return False

	#makes the specified stack empty by moving the stack pointer to the top
	def makenull(self):
		self.top = self.maxlength
		return

#arraystack.py tests

n = 10

print "Creating new stack, is it empty?"
stk = arraystack()
print stk.empty()

print "Iterated insert of 10 elements into stack"
for i in range(0,n):
	stk.push(i)

print "Attempting to print top of stack, which should be 9..."
print stk.top
print "Attempting to pop 3 elements, top should then be 6..."
stk.pop()
stk.pop()
stk.pop()
print stk.top
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
print stk.top
print "Pushing a few elements, then making stack empty through makenull.."
stk.push(1)
stk.push(2)
stk.push(3)
stk.makenull()
stk.pop()