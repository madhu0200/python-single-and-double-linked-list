class pushOperation:
    
    def push(self,self1,new):
          
        #if the head node is none making the new node to head
        if(self1.head is None):
          
            self1.head=new
            print("inserted",new.data)
        else:
            
            #if the head node is not none traversing the node and making the next to the last node
            temp=self1.head
            while(temp.next is not None ):
                temp=temp.next
            temp.next=new
            new.prev=temp
            print("iinserted",temp.next.data)
    
    def insertInOrder(self,self1,new):
        if(self1.head is None): 
            self1.head=new
            print("item inserted ",new.data)
            return
        elif(self1.head.data<new.data):
            temp=self1.head
            while(temp.next is not None):
                if(temp.data==new.data):
                    print("iitem already exists: ",new.data)
                    return
                if(temp.data<new.data):
                    last=temp
                    temp=temp.next
                else:
                    temp.next=new
                    new.prev=temp
                    last=last.next
                    new.next=last
                    print("iitem inserted ",new.data)
                    return
                if (temp is None):
                    temp=temp.next
                    temp.next=new
                    new.prev=temp
            else:
                temp.next=new
                new.prev=temp
                new.next=None
        else:
            new.next=self1.head
            new.prev=None
            self1.head.prev=new
            self1.head=new
            print("iitem inserted ",new.data)
