#!/usr/bin/env python
# coding: utf-8

# ***Implementing the following DS in Python***
# 1. Stack Using Array
# 2. Stack using Linked List
# 3. Queue using Array
# 4. Queue using Linked List
# 5. Priority Queue
# 6. Circular Queue

# In[2]:


# 1. Stack Using Array
class StackArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = [None] * capacity
        self.top = -1

    def push(self, item):
        if self.top < self.capacity - 1:
            self.top += 1
            self.stack[self.top] = item
        else:
            print("Stack overflow. Cannot push element.")

    def pop(self):
        if self.top >= 0:
            popped_item = self.stack[self.top]
            self.top -= 1
            return popped_item
        else:
            print("Stack underflow. Cannot pop element.")

    def is_empty(self):
        return self.top == -1

    def peek(self):
        if not self.is_empty():
            return self.stack[self.top]

    def size(self):
        return self.top + 1

stack = StackArray(5)

stack.push(1)
stack.push(2)
stack.push(3)

print("Stack: ", stack.stack)
print("Pop:", stack.pop())
print("Pop:", stack.pop())
print("Peek:", stack.peek())
print("Size:", stack.size())
print("Is Empty:", stack.is_empty())


# In[3]:


# 2. Stack using Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.is_empty():
            popped_item = self.top.data
            self.top = self.top.next
            return popped_item
        else:
            print("Stack Underflow. Cannot pop from an empty stack.")
            return None

    def is_empty(self):
        return self.top is None

    def peek(self):
        if not self.is_empty():
            return self.top.data
        else:
            print("Stack is empty.")
            return None

    def size(self):
        current = self.top
        count = 0
        while current:
            count += 1
            current = current.next
        return count

stack = StackLinkedList()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

print("Stack size:", stack.size())

print("Popped item:", stack.pop())
print("Popped item:", stack.pop())

print("Is the stack empty?", stack.is_empty())

print("Peek at the top of the stack:", stack.peek())

print("Stack size after pops:", stack.size())


# In[5]:


# 3. Queue using Array]
class QueueArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1

    def enqueue(self, item):
        if (self.rear + 1) % self.capacity == self.front:
            print("Queue Overflow. Cannot enqueue element:", item)
        elif self.is_empty():
            self.front = self.rear = 0
            self.queue[self.rear] = item
        else:
            self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow. Cannot dequeue from an empty queue.")
        elif self.front == self.rear:
            item = self.queue[self.front]
            self.front = self.rear = -1
            return item
        else:
            item = self.queue[self.front]
            self.front = (self.front + 1) % self.capacity
            return item

    def is_empty(self):
        return self.front == -1 and self.rear == -1

    def front(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            return self.queue[self.front]

    def size(self):
        if self.is_empty():
            return 0
        elif self.front <= self.rear:
            return self.rear - self.front + 1
        else:
            return self.capacity - (self.front - self.rear) + 1

queue = QueueArray(5)

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)

print("Queue after enqueues:", queue.queue)

print("Dequeued item:", queue.dequeue())
print("Dequeued item:", queue.dequeue())

print("Queue after dequeues:", queue.queue)

print("Is the queue empty?", queue.is_empty())

print("Size of the queue:", queue.size())


# In[6]:


# 4. Queue using Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, item):
        new_node = Node(item)
        if not self.rear:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if not self.front:
            print("Queue is empty. Cannot dequeue.")
            return None

        popped_item = self.front.data
        self.front = self.front.next

        if not self.front:
            self.rear = None

        return popped_item

    def is_empty(self):
        return self.front is None

    def front_item(self):
        if not self.is_empty():
            return self.front.data

    def size(self):
        current = self.front
        count = 0
        while current:
            count += 1
            current = current.next
        return count

queue = QueueLinkedList()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Front of the queue:", queue.front_item())
print("Queue size:", queue.size())

print("Dequeued item:", queue.dequeue())
print("Dequeued item:", queue.dequeue())

print("Is the queue empty?", queue.is_empty())


# In[7]:


# 5. Priority Queue
import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def enqueue(self, item, priority):
        heapq.heappush(self.heap, (priority, item))

    def dequeue(self):
        if not self.is_empty():
            return heapq.heappop(self.heap)[1]

    def is_empty(self):
        return len(self.heap) == 0

    def peek(self):
        if not self.is_empty():
            return self.heap[0][1]

    def size(self):
        return len(self.heap)

priority_queue = PriorityQueue()

priority_queue.enqueue("Task 1", 3)
priority_queue.enqueue("Task 2", 1)
priority_queue.enqueue("Task 3", 2)

print("Peek at the front of the priority queue:", priority_queue.peek())
print("Size of the priority queue:", priority_queue.size())

print("Dequeued item:", priority_queue.dequeue())
print("Dequeued item:", priority_queue.dequeue())

print("Is the priority queue empty?", priority_queue.is_empty())


# In[10]:


class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1

    def enqueue(self, item):
        if (self.rear + 1) % self.capacity == self.front:
            print("Queue is full. Cannot enqueue.")
        elif self.is_empty():
            self.front = self.rear = 0
            self.queue[self.rear] = item
        else:
            self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
        elif self.front == self.rear:
            item = self.queue[self.front]
            self.front = self.rear = -1
            return item
        else:
            item = self.queue[self.front]
            self.front = (self.front + 1) % self.capacity
            return item

    def is_empty(self):
        return self.front == -1 and self.rear == -1

    def get_front(self):
        if not self.is_empty():
            return self.queue[self.front]

    def size(self):
        if self.is_empty():
            return 0
        elif self.front <= self.rear:
            return self.rear - self.front + 1
        else:
            return self.capacity - (self.front - self.rear) + 1

circular_queue = CircularQueue(5)

circular_queue.enqueue(1)
circular_queue.enqueue(2)
circular_queue.enqueue(3)
circular_queue.enqueue(4)
circular_queue.enqueue(5)

print("Front of the circular queue:", circular_queue.get_front())
print("Size of the circular queue:", circular_queue.size())

print("Dequeued item:", circular_queue.dequeue())
print("Dequeued item:", circular_queue.dequeue())

print("Is the circular queue empty?", circular_queue.is_empty())


# In[ ]:




