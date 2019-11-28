#!/usr/bin/env python

from arraylist import *

#Exercise 2.4, using arraylist from PA1

#concatenates an arraylist of arraylists
def concat(lists):
	concat_list = arraylist()
	i = 0
	while i < lists.end():
		l = lists.retrieve(i)
		for j in range(0,l.end()):
			elem = l.retrieve(j)
			concat_list.insert(elem, concat_list.end())
		i += 1
	return concat_list

print "mergelists.py merged_lists"
print
print "Concatonate 3 arraylists:"
print "Should print 0 1 2 3 4 5 6 7 8 9 10"
test_list1 = arraylist()
test_list1.insert(0, 0)
test_list1.insert(1, 1)
test_list1.insert(2, 2)
test_list1.insert(3, 3)
test_list2 = arraylist()
test_list2.insert(4, 0)
test_list2.insert(5, 1)
test_list2.insert(6, 2)
test_list2.insert(7, 3)
test_list3 = arraylist()
test_list3.insert(8, 0)
test_list3.insert(9, 1)
test_list3.insert(10, 2)
concat_lists = arraylist()
concat_lists.insert(test_list1, 0)
concat_lists.insert(test_list2, 1)
concat_lists.insert(test_list3, 2)
concat_lists = concat(concat_lists)
for i in range(0, concat_lists.end()):
	print concat_lists.retrieve(i)
