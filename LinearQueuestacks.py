class QueueUsingStacks:
  def __init__(self):
    self.stack1 = []
    self.stack2 = []


  def enqueue(self, item):
    self.stack1.append(item)


  def dequeue(self):
    if self.isEmpty():
      print("Queue underflow")
      return None

    if not self.stack2:
      while self.stack1:
        self.stack2.append(self.stack1.pop())
    return self.stack2.pop()

  def isEmpty(self):
    return not self.stack1 and not self.stack2

my_queue = QueueUsingStacks()
my_queue.enqueue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)

print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue()) 
