import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

def insertNodeAtTail(head, data):
    class node:
        def __init__(self, data=None):
            self.data = data
            self.next = None
    
    new_node = node(data)
            
    if head == None:
        new_node.next = head
        return new_node
    else:
        running = True
        current_node = head
        while running:
            if current_node.next == None:
                running = False
            else:
                current_node = current_node.next
                
        current_node.next = new_node
        
        return head
    

# Given the pointer to the head node of a linked list, change the next pointers of the nodes so that their order 
# lis reversed. The head pointer given may be null meaning that the initial list is empty.

def reversePrint(llist):
    # Write your code here
    if llist == None:
        print('')
        
    else:
        lista = []
        running = True
        current_node = llist
        
        while running:
            lista.append(current_node.data)
            if current_node.next == None:
                running = False
            else:
                current_node = current_node.next
    
    for i in range(len(lista)):
        print(lista[-1-i])



    # Write your code here
    head = llist
    
    if head == None:
        return head
        
    else:
        current_node = head
        last_node = None
        run = True
        while run:
            
            next_node = current_node.next
            
            current_node.next = last_node
            
            last_node = current_node
            
            current_node = next_node
            
            if next_node == None:
                break
        
        
        return last_node
    

# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
def diagonalDifference(arr):
    # Write your code here
    l_diagonal = 0
    r_diagonal = 0
    
    for i in range(len(arr)):
        l_diagonal += arr[i][i]
        r_diagonal += arr[-1-i][i]
        
    return abs(l_diagonal - r_diagonal)


def plusMinus(arr):
    # Write your code here
    positive = 0
    negative = 0
    zero = 0
    
    for x in arr:
        if x > 0:
            positive += 1
        elif x < 0:
            negative += 1
        else:
            zero += 1
            
    print('{:.6f}'.format(positive/len(arr)))
    print('{:.6f}'.format(negative/len(arr)))
    print('{:.6f}'.format(zero/len(arr)))


# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. 
# Then print the respective minimum and maximum values as a single line of two space-separated long integers.
def miniMaxSum(arr):
    # Write your code here
    maior = 0
    total = sum(arr)
    menor = total
    
    for i in range(len(arr)):
        s = total - arr[i]
        if s > maior:
            maior = s
        if s < menor:
            menor = s    
    
    
    
    print(f'{menor} {maior}')

# Given a time in -hour AM/PM format, convert it to military (24-hour) time.
def timeConversion(s):
    # Write your code here
    hour, minute, seconds = s.split(':')
    hour = int(hour)
    am_pm = seconds[-2:]
    seconds = seconds[:-2]


    if am_pm == 'AM':
        if hour == 12:
            hour = '00'
        else:
            hour = '{:02d}'.format(hour)

    if am_pm == 'PM':
        if hour != 12:
            hour = str(hour + 12)
        else:
            hour = '{:02d}'.format(hour)

    return ':'.join((hour, minute, seconds))


# print(timeConversion('06:40:03AM'))


def mergeLists(head1, head2):
    run  = True

    class node:
        def __init__(self, data=None):
            self.data = data
            self.next = None
    
    # Defining the head
    next1 = head1.next
    next2 = head2.next
    
    if next1.data <= next2.data:
        head = head1
    else:
        head = head2
            
    while run == True:
        
        if head1.next != None and head.next != None:
            next1 = head1.next
            next2 = head2.next
            print(next1.data)

            if next1.data <= next2.data:
                # head = head1
                head.next = next1
                next1.next = next2
                head = next2
            else:
                # head = head2
                head.next = next2
                next2.next = next1
                head = next1
                
            head1 = head1.next
            head2 = head2.next
        
        else:
            run = False
            
    return head
            
# Given pointers to the heads of two sorted linked lists, merge them into a single, 
# sorted linked list. Either head pointer may be null meaning that the corresponding list is empty.

def mergeLists(head1, head2):
            
    
    head = SinglyLinkedList()
    
    run = True
    
    data = []
    
    while head1 != None:
        data.append(head1.data)
        head1 = head1.next
        
    while head2 != None:
        data.append(head2.data)
        head2 = head2.next
        
    data.sort()
    
    for d in data:
        head.insert_node(d)
        
    return head.head


# Delete the node at a given position in a linked list and return a reference to the head node. 
# The head is at position 0. The list may be empty after you delete the node. In that case, return a null value.
def deleteNode(llist, position):
    # Write your code here
    if position == 0:
        llist = llist.next
        return llist
    
    current = llist
    
    for _ in range(position - 1):
        current = current.next
    
    next_node = current.next
    next_node = next_node.next
    
    current.next = next_node

    return llist

# You are given the pointer to the head node of a sorted linked list, 
# where the data in the nodes is in ascending order. 
# Delete nodes and return a sorted list with each distinct value in the original list. 
# The given head pointer may be null indicating that the list is empty.
def removeDuplicates(llist):
    # Write your code here
    if llist == None:
        return llist
    
    current = llist
    run = True
    while run:
        
        data = current.data
        next_node = current.next
        if next_node != None:
            if data == next_node.data:
                current.next = next_node.next
                next_node = next_node.next
            else:
                current = next_node
                data = current.data
                
                current.next
                
                if current == None:
                    run = False
                    
        else:
            run = False
            
    return llist


def findMergeNode(head1, head2):
    data1 = []
    run = True
    while run:
        data1.append(head1.data)
        if head1.next != None:
            head1 = head1.next
        else:
            run = False
            
    run = True
    
    while run:
        if head2.data in data1:
            return head2.data
        else:
            head2 = head2.next
            if head2 == None:
                run = False
                
    return None
    
    # data2 = {}
    # run = True
    # while run:
    #     if head2 != None:
    #         if head2.data in data1:
    #             data2[data1.index(head2.data)] = head2.data
    #             head2 = head2.next
    #         else:
    #             head2 = head2.next
    #     else:
    #         run = False
                
    # return data2[min(data2.keys())]
# import sys
# data = []
# with open(sys.argv[1], 'r') as file:
#     for line in file:
#         data.append(int(line))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        index = int(input())

        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)
            
        ptr1 = llist1.head;
        ptr2 = llist2.head;

        for i in range(llist1_count):
            if i < index:
                ptr1 = ptr1.next
                
        for i in range(llist2_count):
            if i != llist2_count-1:
                ptr2 = ptr2.next

        ptr2.next = ptr1

        result = findMergeNode(llist1.head, llist2.head)

        fptr.write(str(result) + '\n')

    fptr.close()
