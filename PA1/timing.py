#!/usr/bin/python

from arraylist import arraylist
from pointerlist import pointerlist
from arraystack import arraystack
from pointerstack import pointerstack
import time

N = 1000

# List front insertion
def list_head_insertion():
	test_list = []
	for i in range(N):
		test_list.insert(0, i)

start_time = time.time()
list_head_insertion()
end_time = time.time()
print("List data structure head insertion time for 1000 elements (millisecond): ", end_time * 1000 - start_time * 1000)

# Arraylist head insertion
def arraylist_head_insertion():
	test_list = arraylist()
	for i in range(N):
		test_list.insert(i, 0)

start_time = time.time()
arraylist_head_insertion()
end_time = time.time()
print("Arraylist head insertion time for 1000 elements (millisecond): ", end_time * 1000 - start_time * 1000)

# Pointerlist head insertion
def pointerlist_head_insertion():
	test_list = pointerlist()
	for i in range(N):
		test_list.insert(i, 0)

start_time = time.time()
pointerlist_head_insertion()
end_time = time.time()
print("Pointerlist head insertion time for 1000 elements (millisecond): ", end_time * 1000 - start_time * 1000)

# List tail insertion
def library_tail_insertion():
	test_list = []
	for i in range(N):
		test_list.append(i)

start_time = time.time()
library_tail_insertion()
end_time = time.time()
print("List data structure tail insertion time for 1000 elements (millisecond): ", end_time * 1000 - start_time * 1000)

# Arraylist tail insertion
def arraylist_tail_insertion():
	test_list = arraylist()
	for i in range(N):
		test_list.insert(i, test_list.end())

start_time = time.time()
arraylist_tail_insertion()
end_time = time.time()
print("Arraylist tail insertion time for 1000 elements (millisecond): ", end_time * 1000 - start_time * 1000)

# Pointerlist tail insertion
def pointerlist_tail_insertion():
	test_list = pointerlist()
	for i in range(N):
		test_list.insert(i, test_list.end())

start_time = time.time()
pointerlist_tail_insertion()
end_time = time.time()
print("Pointerlist tail insertion time for 1000 elements (millisecond): ", end_time * 1000 - start_time * 1000)

# List traversal
def library_traversal(test_list):
	for i in range(len(test_list)):
		x = test_list[i]

test_list = [0] * N
start_time = time.time()
library_traversal(test_list)
end_time = time.time()
print("List data structure traversal time for 1000 elements (millisecond): ", end_time * 1000 - start_time * 1000)

# Arraylist traversal
def arraylist_traversal(test_list):
	i = test_list.first()
	while (i < test_list.end()-1):
		x = test_list.retrieve(i)
		i = test_list.next_position(i)

test_list = arraylist()
for i in range(N):
	test_list.insert(i, 0)
start_time = time.time()
arraylist_traversal(test_list)
end_time = time.time()
print("Arraylist traversal time for 1000 elements (millisecond): ", end_time * 1000 - start_time * 1000)

# Pointerlist traversal
def pointerlist_traversal(test_list):
	p = test_list.first()
	while (p is not test_list.end()):
		p = p.next

test_list = pointerlist()
for i in range(N):
	test_list.insert(i, 0)
start_time = time.time()
pointerlist_traversal(test_list)
end_time = time.time()
print("Pointerlist traversal time for 1000 elements (millisecond): ", end_time * 1000 - start_time * 1000)

# List head deletion
def library_head_deletion(test_list):
	for i in range(len(test_list)):
		del test_list[0]

test_list = [0] * N
start_time = time.time()
library_head_deletion(test_list)
end_time = time.time()
print("List data structure head deletion time for 1000 elements (millisecond): ", end_time * 1000 - start_time * 1000)

# Arraylist head deletion
def arraylist_head_deletion(test_list):
	for i in range(N):
		test_list.delete(0)

test_list = arraylist()
for i in range(N):
	test_list.insert(i, 0)
start_time = time.time()
arraylist_head_deletion(test_list)
end_time = time.time()
print("Arraylist head deletion time for 1000 elements (millisecond): ", end_time * 1000 - start_time * 1000)

# Pointerlist head deletion
def pointerlist_head_deletion(test_list):
	for i in range(N):
		test_list.delete(0)

test_list = pointerlist()
for i in range(N):
	test_list.insert(i, 0)
start_time = time.time()
pointerlist_head_deletion(test_list)
end_time = time.time()
print("Pointerlist head deletion time for 1000 elements (millisecond): ", end_time * 1000 - start_time * 1000)

# List tail deletion
def library_tail_deletion(test_list):
	for i in range(len(test_list)):
		del test_list[len(test_list) - 1]

test_list = [0] * N
start_time = time.time()
library_tail_deletion(test_list)
end_time = time.time()
print("List data structure tail deletion time for 1000 elements (millisecond): ", end_time * 1000 - start_time * 1000)

# Arraylist tail deletion
def arraylist_tail_deletion(test_list):
	for i in range(N):
		test_list.delete(test_list.end() - 1)

test_list = arraylist()
for i in range(N):
	test_list.insert(i, 0)
start_time = time.time()
arraylist_tail_deletion(test_list)
end_time = time.time()
print("Arraylist tail deletion time for 1000 elements (millisecond): ", end_time * 1000 - start_time * 1000)

# Pointerlist tail deletion
def pointerlist_tail_deletion(test_list):
	for i in range(N):
		test_list.delete(test_list.previous(test_list.end()))

test_list = pointerlist()
for i in range(N):
	test_list.insert(i, 0)
start_time = time.time()
pointerlist_tail_deletion(test_list)
end_time = time.time()
print("Pointerlist tail deletion time for 1000 elements (millisecond): ", end_time * 1000 - start_time * 1000)

# Stack insertion
def stack_push():
	test_stack = []
	for i in range(N):
		test_stack.append(i)

start_time = time.time()
stack_push()
end_time = time.time()
print("Stack data structure push insertion time for 1000 elements (millisecond): ", end_time * 1000 - start_time * 1000)

# Arraystack insertion
def arraystack_push():
	test_stack = arraystack()
	for i in range(N):
		test_stack.push(i)

start_time = time.time()
arraystack_push()
end_time = time.time()
print("Arraystack push insertion time for 1000 elements (millisecond): ", end_time * 1000 - start_time * 1000)

# Pointerstack insertion
def pointerstack_push():
	test_stack = pointerstack()
	for i in range(N):
		test_stack.push(i)

start_time = time.time()
pointerstack_push()
end_time = time.time()
print("Pointerstack push insertion time for 1000 elements (millisecond): ", end_time * 1000 - start_time * 1000)

# Stack deletion
def stack_deletion(test_stack):
	while (len(test_stack) is not 0):
		test_stack.pop()

test_stack = [0] * N
start_time = time.time()
stack_deletion(test_stack)
end_time = time.time()
print("Stack data structure pop deletion time for 1000 elements (millisecond): ", end_time * 1000 - start_time * 1000)

# Arraystack deletion
def arraystack_deletion(test_stack):
	while (test_stack.empty() is False):
		test_stack.pop()

test_stack = arraystack()
for i in range(N):
	test_stack.push(i)
start_time = time.time()
arraystack_deletion(test_stack)
end_time = time.time()
print("Arraystack pop deletion time for 1000 elements (millisecond): ", end_time * 1000 - start_time * 1000)

# Pointerstack deletion
def pointerstack_deletion(test_stack):
	while (test_stack.empty() is False):
		test_stack.pop()

test_stack = pointerstack()
for i in range(N):
	test_stack.push(i)
start_time = time.time()
pointerstack_deletion(test_stack)
end_time = time.time()
print("Pointerstack pop deletion time for 1000 elements (millisecond): ", end_time * 1000 - start_time * 1000)
