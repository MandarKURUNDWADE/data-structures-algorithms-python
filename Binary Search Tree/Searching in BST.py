class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def insertNode(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue)
    return "The node has been successfully inserted"


def searchNode(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        print("The Value is Found")
    elif nodeValue < rootNode.data:
        if rootNode.leftChild.data == nodeValue:
            print("The Value is Found")
        else:
            searchNode(rootNode.leftChild,nodeValue)
    else:
        if rootNode.rightChild.data == nodeValue:
            print("The Value is found")
        else:
            searchNode(rootNode.rightChild, nodeValue)

# Time Complexity - (logN)
# Space Complexity - (logN)

    
newBST = BSTNode(None)
insertNode(newBST,input())
insertNode(newBST,input())
insertNode(newBST,input())
insertNode(newBST,input())
insertNode(newBST,input())

searchNode(newBST,input())