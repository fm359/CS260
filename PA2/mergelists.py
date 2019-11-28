#!/usr/bin/env python

from arraylist import *

#Exercise 2.3, using arraylist from PA1

#sorts all elements of the given arraylist
def insertionsort(List):
    for i in range(0, List.end()):
        j = i
        while j > 0 and List.retrieve(j) < List.retrieve(j - 1):
            List.elements[j], List.elements[j - 1] = List.elements[j - 1], List.elements[j]
            j -= 1

#merges and sorts two arraylists
def mergetwolists(L1,L2):
    merged_list = L1
    for i in range(0,L2.end()):
        elem = L2.retrieve(i)
        merged_list.insert(elem, merged_list.end())
    insertionsort(merged_list)
    return merged_list

#merges and sorts an arraylist of arraylists
def mergenlists(Lists):
    merged_list = arraylist()
    i = 0
    while i < Lists.end():
        list = Lists.retrieve(i)
        for j in range(0,list.end()):
            elem = list.retrieve(j)
            merged_list.insert(elem, merged_list.end())
        i += 1
    insertionsort(merged_list)
    return merged_list

print "mergelists.py merged_lists"
print
print "Merge two sorted lists, both [a,b,c,d,e]:"
print "Should return a a b b c c d d e e"
test_list1 = arraylist()
test_list1.insert("a", 0)
test_list1.insert("b", 1)
test_list1.insert("c", 2)
test_list1.insert("d", 3)
test_list1.insert("e", 4)
test_list1 = mergetwolists(test_list1, test_list1)
for i in range(0, test_list1.end()):
    print test_list1.retrieve(i)
print
print "Merge n sorted lists with numbers as elements:"
print "Should return numbers 0 - 10"
test_list1 = arraylist()
test_list1.insert(0, 0)
test_list1.insert(2, 1)
test_list1.insert(6, 2)
test_list1.insert(8, 3)
test_list2 = arraylist()
test_list2.insert(1, 0)
test_list2.insert(5, 1)
test_list2.insert(3, 2)
test_list2.insert(9, 3)
test_list3 = arraylist()
test_list3.insert(4, 0)
test_list3.insert(10, 1)
test_list3.insert(7, 2)
merged_lists = arraylist()
merged_lists.insert(test_list1, 0)
merged_lists.insert(test_list2, 1)
merged_lists.insert(test_list3, 2)
merged_lists = mergenlists(merged_lists)
for i in range(0, merged_lists.end()):
    print merged_lists.retrieve(i)
