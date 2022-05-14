
#importing the dlistclass which has the structure definition of class
from dlistclass import *

#importing the dlistprint class which has the operation of printing the dlist
from dlistprint import *

#importing the dlistpushOperationclass which has the operation of pushing an element into the dlist
from dlistpushOperation import *


#importing the  dlistsize class which has the operation of counting the size of list
from dlistsize import *

#imprting the dlistdeletion class which has the operation of deletion 
from dllistdeletion import deleteNode

#creating an instance to the dlist class 
d=dllist()

#creating the instance to the pushOperation class
p=pushOperation()

#creating an instance to the printList class
lp=printList()


#creating an instance to the dlistsize class
ls=sizeoflist()

#creating an instance to the dlistdeletion class
ld=deleteNode()

for i in range(9):
    n=Node(i)
    p.insertInOrder(d,n)
lp.print(d)

n=Node(9)
p.insertInOrder(d,n)

n=Node(9)
p.push(d,n)
lp.print(d)

n=Node(10)
p.insertInOrder(d,n)

lp.print(d)
print(ls.size(d))

ld.delete(d,12)
lp.print(d)

   