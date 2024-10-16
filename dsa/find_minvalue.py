class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def min_value(head):
    minval=head.data
    currentnode=head.next
    while currentnode:
        if currentnode.data>minval:
            minval=currentnode.data
        currentnode=currentnode.next
    return minval

node1=Node(10)
node2=Node(2)
node3=Node(32)
node4=Node(43)

node1.next=node2
node2.next=node3
node3.next=node4

print(min_value(node1))