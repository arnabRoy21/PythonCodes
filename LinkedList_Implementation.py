#!/usr/bin/env python
# coding: utf-8

# In[8]:


class Node:
    def __init__(self, data):
        self.data = data
        self.nextptr = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def push(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            currNode = self.head
            while(currNode.nextptr != None):
                currNode = currNode.nextptr
            currNode.nextptr = Node(data)
            
    def pop(self):
        currNode = self.head
        prevNode = None
        while(currNode.nextptr != None):
            prevNode = currNode
            currNode = currNode.nextptr
        prevNode.nextptr = None

    def printList(self):
        currNode = self.head
        if(currNode == None):
            print('List is Empty!!')
            return
        while(currNode):
            print(currNode.data,"--->",end = '')
            currNode = currNode.nextptr
    
if __name__ == '__main__':
    ans = 0
    llist = LinkedList()
    while(ans != 4):
        print('\n\nEnter 1 to push')
        print('Enter 2 to pop')
        print('Enter 3 to display list')
        print('Enter 4 to quit')
        ans = (int(input('Input choice: ')))
        if(ans == 1):
            llist.push(int(input('Enter data: ')))
        if(ans == 2):
            llist.pop()
        if(ans == 3):
            llist.printList()

            
            
    







# In[ ]:




