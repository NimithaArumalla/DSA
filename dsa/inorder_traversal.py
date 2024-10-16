class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def inorder_traversal(node):
    if node is None:
        return 
    inorder_traversal(node.left)
    print(node.data,end="->")
    inorder_traversal(node.right)
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

inorder_traversal(root)