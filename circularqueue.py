class CircularQueue:
  def __init__(self, capacity):
    self.capacity = capacity
    self.items = [None] * capacity  
    self.front = self.rear = -1  

  
  def enqueue(self, item):
    if self.isFull():
      print("Queue overflow")
      return
    if self.front == -1:  
      self.front = 0
    self.rear = (self.rear + 1) % self.capacity  
    self.items[self.rear] = item

  
  def dequeue(self):
    if self.isEmpty():
      print("Queue underflow")
      return None
    item = self.items[self.front]
    if self.front == self.rear:  
      self.front = self.rear = -1
    else:
      self.front = (self.front + 1) % self.capacity  
    return item

  
  def isEmpty(self):
    return self.front == -1

  
  def isFull(self):
    return (self.rear + 1) % self.capacity == self.front

my_queue = CircularQueue(2)
my_queue.enqueue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())


