class TrieNode:
    def __init__(self):
        self.children  = {}
        self.enfofString = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insertString(self,word):
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node == None:
                node =  TrieNode()
                current.children.update({ch:node})
            current = node
        current.endofString = True
        print("Successfully Inserted")
    def searchString(self,word):
        currentNode = self.root
        for i in word:
            node = currentNode.children.get(i)
            if node == None:
                return False
            currentNode = node
        if  currentNode.endofString == True:
            return True
        else:
            return False
# Space Complexity - O(1)
# Time Complexity- O(m)
newTrie = Trie()
newTrie.insertString(input())
newTrie.insertString(input())
print(newTrie.searchString(input()))