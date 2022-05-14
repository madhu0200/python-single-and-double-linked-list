class sizeoflist:
    def size(self,self1):
        size=0
        temp=self1.head
        while(temp is not None):
            size+=1
            temp=temp.next
        return size