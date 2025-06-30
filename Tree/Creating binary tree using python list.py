class BinaryTree:
    def __init__(self,size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

newBT = BinaryTree(8)

# Time Complexity - 0(1)
# Space Complexity - 0(n)