class Node:

    def __init__(self,data):
        self.data=data
        self.next=None


class LinkedList:

    def __init__(self):
        self.head=None

    def append(self,data):
        new=Node(data)
        if self.head is None:
            self.head=new
            llist.print()
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


    def deletefirst(self):
        temp=self.head
        temp=temp.next
        print("\ndeleted %d"%(self.head.data))
        self.head=None
        self.head=temp
    

    def delete(self,data):
        last=self.head
        prev=last
        while(last.data!=data):
            prev=last
            last=last.next
        prev.next=last.next
        last=None
        llist.print()
        
        
    def dellast(self):
        last=self.head
        while(last.next):
            prev=last
            last=last.next
            print("%d"%(last.data))
        print("\ndeleted %d"%(last.data))
        prev.next=None
        last=None
        
        
llist=LinkedList()
for i in range(8):
    llist.append(i)
llist.print()
llist.deletefirst()
llist.dellast()
llist.delete(1)
llist.print()