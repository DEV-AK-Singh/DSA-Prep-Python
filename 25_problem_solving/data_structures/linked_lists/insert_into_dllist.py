#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)
 
def sortedInsert(head, data):  
    if head is None or head.data >= data:  
        node = DoublyLinkedListNode(data)  
        node.next = head  
        if head is not None:  
            head.prev = node  
        node.prev = None  
        return node  
    
    curr = head  

    while curr.next is not None and curr.next.data < data:  
        curr = curr.next  
    node = DoublyLinkedListNode(data)  
    node.next = curr.next  

    if curr.next is not None:  
        curr.next.prev = node  
    node.prev = curr  
    curr.next = node  
    
    return head
 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sortedInsert(llist.head, data)

        print_doubly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()
