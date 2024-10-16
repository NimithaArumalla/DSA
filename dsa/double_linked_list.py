class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

node1=Node(1)
node2=Node(2)
node3=Node(3)
node4=Node(4)

node1.next=node2
node2.next=node3
node3.next=node4

node2.prev=node1
node3.prev=node2
node4.prev=node3

currentnode=node1

while currentnode:
    print(currentnode.data,end="->")
    currentnode=currentnode.next
print("null")

currentnode=node4

while currentnode:
    print(currentnode.data,end="<-")
    currentnode=currentnode.prev
print("null")