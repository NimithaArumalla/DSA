class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def postorder_traversal(node):
    if node is None:
        return 
    postorder_traversal(node.left)
    postorder_traversal(node.right)
    print(node.data,end="->")
    
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

postorder_traversal(root)