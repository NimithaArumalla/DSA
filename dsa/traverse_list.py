class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def traverse(head):
    currentnode=head
    while currentnode:
        print(currentnode.data,end="->")
        currentnode=currentnode.next

    print("null")

node1=Node(1)
node2=Node(2)
node3=Node(3)
node4=Node(4)

node1.next=node2
node2.next=node3
node3.next=node4

traverse(node2)