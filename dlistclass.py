#this is imported and used in the dlistpush.py 
#creating class node
class Node:

    #constructor for Node class and assigning the values to the node
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None


class dllist:

    #consructor for linked list class and assingnig the head value
    def __init__(self):
        self.head=None
