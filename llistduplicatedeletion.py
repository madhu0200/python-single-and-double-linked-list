


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def top(self):
        if(self.head is None ):
            return 1
        else:
            return 0
    def append(self,data):
        new=Node(data)
        if llist.top():
            self.head=new
            #llist.print()
            return
        last=self.head
        while(last.next):
            last=last.next
        last.next=new
        #llist.print()
    def print(self):
        if llist.top():
            print("list is empty")
            return
        print('\n')
        last=self.head
        while(last):
            print(last.data,end='-->')
            last=last.next
    def removeduplicates(self):
 
        ptr1 = None
        ptr2 = None
        dup = None
        ptr1 = self.head
 
        # Pick elements one by one
        while (ptr1 != None and ptr1.next != None):
 
            ptr2 = ptr1
 
            # Compare the picked element with rest
            # of the elements
            while (ptr2.next != None):
 
                # If duplicate then delete it
                if (ptr1.data == ptr2.next.data):
 
                    # Sequence of steps is important here
                    dup = ptr2.next
                    ptr2.next = ptr2.next.next
                    llist.print()
                else:
                    ptr2 = ptr2.next
 
            ptr1 = ptr1.next
    def deleteList(self):
        #returning if the head is null
        if llist.top:
            return
        while(self.head.next is not None):
            prev=self.head.next
            del self.head.data
            self.head=prev
        self.head = None
           # llist.print()
    # for counting the number of linked list
    def count(self):
        if llist.top():
            return
        temp=self.head
        count=0
        while(temp.next is not None):
            temp=temp.next
            count+=1
        return count
    # for printing the middle of the linked list
    def getMiddle(self):
        if llist.top():
            return
        temp=self.head
        count=llist.count()/2
        while(count):
            temp=temp.next
            count-=1
        print("middle element is %d"%(temp.data))
        #llist.print()
    # to search the given element
    def search(self,data):
        if(llist.top()):
            return
        temp=self.head
        while(temp.next is not None):
            if(data== temp.data):
                print("search is found")
                return 1
            else:
                temp=temp.next
        return 0
    def swap(self,x,y):
        if x == y:
            return
 
        # Search for x (keep track of prevX and CurrX)
        prevX = None
        currX = self.head
        while currX != None and currX.data != x:
            prevX = currX
            currX = currX.next
 
        # Search for y (keep track of prevY and currY)
        prevY = None
        currY = self.head
        while currY != None and currY.data != y:
            prevY = currY
            currY = currY.next
 
        # If either x or y is not present, nothing to do
        if currX == None or currY == None:
            return
        # If x is not head of linked list
        if prevX != None:
            prevX.next = currY
            llist.print()
        else:  # make y the new head
            self.head = currY
 
        # If y is not head of linked list
        if prevY != None:
            prevY.next = currX
            llist.print()
        else:  # make x the new head
            self.head = currX
 
        # Swap next pointers
        temp = currX.next
        llist.print()
        currX.next = currY.next
        llist.print()
        currY.next = temp
        llist.print()
    #to reverse a linked list
    def reverse(self):
        if(llist.top()):
            return
        print("reversing")
        temp=self.head
        prev=None
        while(temp is not None):
            next=temp.next
            temp.next=prev
            prev=temp
            temp=next
        self.head=prev
        llist.print()
 
        
            


if __name__=='__main__':
    llist=LinkedList()
    llist.append(1)
    for i in range(1,8):
        llist.append(i)
        if(i==6):
            llist.append(i)
    llist.append(4)
    llist.print()
    llist.removeduplicates()
    llist.search(6)
    llist.swap(4,6)
    llist.getMiddle()
    llist.reverse()
    llist.deleteList()
    llist.print()
    