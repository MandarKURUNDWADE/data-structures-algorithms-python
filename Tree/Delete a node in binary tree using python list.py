class BinaryTree:
    def __init__(self,size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    def insertNode(self,value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "the binary tree is full"

        self.customList[self.lastUsedIndex + 1] = value
        self.lastUsedIndex += 1
        return "the value has been successfully inserted"

    def deleteNode(self,value):
        if self.lastUsedIndex == 0:
            return "There is not any node "

        for i in range(1,self.lastUsedIndex+1):
            if self.customList[i] == value:
                self.customList[i] == self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return "the Node has been successfully deleted"

newBT = BinaryTree(8)
newBT.insertNode(input())
newBT.insertNode(input())
newBT.insertNode(input())
newBT.insertNode(input())
newBT.insertNode(input())


newBT.deleteNode(input())