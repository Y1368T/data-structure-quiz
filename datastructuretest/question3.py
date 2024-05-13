class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def is_empty(self):
        return len(self.stack1) == 0 and len(self.stack2) == 0

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")

        if len(self.stack2) == 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")

        if len(self.stack2) == 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())

        return self.stack2[-1]

    def size(self):
        return len(self.stack1) + len(self.stack2)



okkk = Queue()
okkk.enqueue(7)
okkk.enqueue(28)
okkk.enqueue(34)
print("Peek:", okkk.peek())
print("Size:", okkk.size())
print("Dequeued item:", okkk.dequeue())
print("Is empty?", okkk.is_empty())