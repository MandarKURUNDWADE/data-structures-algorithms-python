class TreeNode:
    def __init__(self,data):
        self.data = data
        self.leftchild = None
        self.rightchild = None

newBT = TreeNode(input())
leftchild = TreeNode(input())
rightchild = TreeNode(input())
newBT.leftchild = leftchild
newBT.rightchild = rightchild

def preOrderTraversal(rootNode):
    if not rootNode:
        return 
    print(rootNode.data)
    preOrderTraversal(rootNode.leftchild)
    preOrderTraversal(rootNode.rightchild)

print("-----------------")

preOrderTraversal(newBT)