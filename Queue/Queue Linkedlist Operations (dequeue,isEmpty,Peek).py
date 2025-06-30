
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)
    
class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode

            curNode = curNode.next

class Queue:
    def __init__(self):
        self.linkedlist = Linkedlist()

    def __str__(self):
        values = [str(x) for x in self.linkedlist]
        return ' '.join(values)

    def isEmpty(self):
        if self.linkedlist.head == None:
            return True
        else:
            return False

        
    def enqueue(self,value):
        newNode = Node(value)

        if self.linkedlist.head == None:
            self.linkedlist.head = newNode
            self.linkedlist.tail = newNode

        else:
            self.linkedlist.tail.next = newNode
            self.linkedlist.tail = newNode

    def dequeue(self):
        if self.isEmpty():
            return "there is not any node in the queue"
        else:
            tempNode = self.linkedlist.head
            if self.linkedlist.head == self.linkedlist.tail:
                self.linkedlist.head = None
                self.linkedlist.tail = None
            else:
                self.linkedlist.head = self.linkedlist.head.next

            return tempNode

    def peek(self):
        if self.isEmpty():
            return "there is not any node in the queue"
        else:
            return self.linkedlist.head


customQueue = Queue()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue)
print(customQueue.peek())
print(customQueue)