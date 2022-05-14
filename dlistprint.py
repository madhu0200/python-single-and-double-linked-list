#this is imported and used in the dlistpush.py 
class printList:
    def print(self,self1):
            print('\n')
            if(self1.head is None):
                print("list is empty")
                return
            last=self1.head

            #printing the double linked list
            print("from front to last")
            while(last.next is not None):
                print(last.data,end=' <--> ')
                last=last.next
            print(last.data,end='\n')

            #printing the riverse of a double linked list
            print("last to from front")
            while(last.prev is not None):
                print(last.data,end=' <--> ')
                last=last.prev
            print(last.data,end='\n')
