#!/usr/bin/env python

class cell:
	def __init__(self):
		self.element = None
		self.next = None

class pointerqueue:
	def __init__(self):
		self.front = cell()
		self.front.next = None
		self.rear = self.front

	#returns the first element of the queue
	def FRONT(self):
		if self.EMPTY():
			print "Queue is empty"
		else:
			return self.front.next.element

	#inserts element at the end of the queue
	def ENQUEUE(self, elem):
		self.rear.next = cell()
		self.rear = self.rear.next
		self.rear.element = elem
		self.rear.next = None

	#deletes the first element of the specified queue
	def DEQUEUE(self):
		if self.EMPTY():
			print "Queue is empty"
		else:
			self.front = self.front.next

	#returns true if the queue is empty
	def EMPTY(self):
		if self.front == self.rear:
			return True
		else:
			return False

	#makes the queue empty
	def MAKENULL(self):
		self.front = cell()
		self.front.next = None
		self.rear = self.front

print "pointerqueue.py tests"
print
print "Initialize queue..."
test = pointerqueue()
print "Check if queue is empty (should be true)... ", test.EMPTY()
print "Insert an element of value '1'..."
test.ENQUEUE(1)
print "Check if queue is empty (should be false)... ", test.EMPTY()
print "The front is", test.FRONT()
print "Enqueue values '2' and '3' and dequeue once..."
test.ENQUEUE(2)
test.ENQUEUE(3)
test.DEQUEUE()
print "The front is now", test.FRONT()
print "Check if queue is empty (should be false)... ", test.EMPTY()
print "Dequeue last two elements..."
test.DEQUEUE()
test.DEQUEUE()
print "Check if queue is empty (should be true)... ", test.EMPTY()
print "The front is", test.FRONT()
print "Dequeue empty queue..."
test.DEQUEUE()
print "Test MAKENULL on queue with elements 'a' 'b' and 'c'..."
test.ENQUEUE('a')
test.ENQUEUE('b')
test.ENQUEUE('c')
print "Front should be 'a' before MAKENULL. It is", test.FRONT()
test.MAKENULL()
print "After MAKENULL..."
print test.FRONT()
print "Check if queue is empty (should be true)... ", test.EMPTY()
test.DEQUEUE()