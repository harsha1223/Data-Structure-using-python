class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self,value):
        self.queue.append(value)
    def dequeue(self):
        self.queue.pop()
    def display(self):
        print(self.queue)

a = Queue()
a.enqueue(5)
a.enqueue(10)
a.enqueue(15)
a.display()
a.dequeue()
a.display()
