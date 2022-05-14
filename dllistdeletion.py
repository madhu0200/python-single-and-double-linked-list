#this is imported and used in the dlistpush.py 
from dlistsize import sizeoflist
s=sizeoflist()
class deleteNode:
    def delete(self,self1,n):
        size=s.size(self1)
        if(size):

            if size >= n:
                #if head node has to delete 
                if n==1:
                    temp=self1.head
                    self1.head=self1.head.next
                    self1.head.prev=None
                    temp.next=None
                    temp=None


                #if node n in nth position
                elif s.size(self1) > n:
                    temp=self1.head
                    while(temp.next and n-1):
                        prev1=temp
                        temp=temp.next
                        n-=1
                    prev1.next=temp.next
                    temp=temp.next
                    temp.prev=prev1

                #if node n is the last node
                elif s.size(self1) ==n :
                    temp=self1.head
                    while(temp.next is not None):
                        prev1=temp
                        temp=temp.next
                    prev1.next=None
                    temp=None
            else:
                print("out of list limit ")
                
        else:
            print("no nodes to delete ")
        
