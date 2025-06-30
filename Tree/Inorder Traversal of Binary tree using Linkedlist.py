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

print("----------------------")

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftchild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightchild)


inOrderTraversal(newBT)