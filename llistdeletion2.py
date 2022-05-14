#from pickletools import read_string1


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
            #llist.print()
            return
        last=self.head
        while(last.next):
            last=last.next
        last.next=new
        #llist.print()
    def print(self):
        print('\n')
        last=self.head
        while(last):
            print(last.data,end='-->')
            last=last.next
    def delete(self,data):
        #if the head is to delete
        temp=self.head
        if(self.head is None):
            return

        if(temp.data==data):
            print("\n %d deleted "%(self.head.data))
            self.head=temp.next
            temp=None
            llist.print()
            return
        #for finding the node
        while(temp.data!=data):
            prev=temp
            temp=temp.next
        #if node is last
        if(temp.next is None):
            prev.next=None
            print("\n %d deleted "%(temp.data))
            temp=None
            return
        #if node is not last on
       #temp=temp.next
        prev.next=temp.next
        print("\n %d deleted "%(temp.data))
        temp=None
        return
    def delindex(self,data):
        if self.head is  None:
            return
        temp=self.head
        index=0
        while(index!=data):
            index+=1
            prev=temp
            if(temp.next is not None):
                temp=temp.next
            else:
                print("index out of bounds ")
                return
        prev.next=temp.next
        temp=None
        return

        
if __name__=='__main__':
    llist=LinkedList()
    for i in range(8):
        llist.append(i)
    llist.print()
    llist.delete(0)
    llist.delete(7)
    llist.delete(4)
    llist.delete(1)
    llist.delindex(4)
    llist.print()