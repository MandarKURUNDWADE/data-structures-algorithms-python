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

def postOrderTraversal(rootNode):
    if not rootNode:
        return 
    postOrderTraversal(rootNode.leftchild)
    postOrderTraversal(rootNode.rightchild)
    print(rootNode.data)

postOrderTraversal(newBT)