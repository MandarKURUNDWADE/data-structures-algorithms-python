# how to use collection as a fifo queue

from collections import deque

customQueue = deque(maxlen=3)
print(customQueue)

customQueue.append(1)
customQueue.append(2)
customQueue.append(3)
print(customQueue)

# prints out the right most element from the queue
print(customQueue.popleft())

print(customQueue)

print(customQueue.clear())