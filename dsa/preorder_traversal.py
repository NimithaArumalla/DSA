class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def preorder_traversal(node):
    if node is None:
        return 
    print(node.data,end="->")
    preorder_traversal(node.left)
    preorder_traversal(node.right)
root=TreeNode('R')
nodeA=TreeNode('a')
nodeB=TreeNode('b')
nodeC=TreeNode('c')
nodeD=TreeNode('d')
nodeE=TreeNode('e')
nodeF=TreeNode('f')

root.left=nodeA
root.right=nodeB

nodeA.left=nodeC
nodeA.right=nodeD

nodeB.left=nodeE
nodeB.right=nodeF

preorder_traversal(root)