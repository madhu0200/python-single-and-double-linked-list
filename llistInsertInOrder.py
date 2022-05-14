class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def push(self,data):
        new=Node(data)
        new.next=self.head
        self.head=new
        llist.print()
    def insertat(self,newdata,data):
        new=Node(data)
        last=self.head
        while(last.data == newdata):
            last=last.next
        last=last.next
        new.next=last.next
        last.next=new
        llist.print()
    def append(self,data):
        new=Node(data)
        if self.head is None:
            self.head=new
            return
        last=self.head
        while(last.next):
            last=last.next
        last.next=new
        llist.print()
    def print(self):
        print('\n')
        last=self.head
        while(last):
            print(last.data,end='-->')
            last=last.next
if __name__=='__main__':
    llist=LinkedList()
    llist.append(6)
    llist.append(7)
    llist.insertat(7,8)
    llist.push(9)
    llist.print()