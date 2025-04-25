class Queue:
    def __init__(self):
        self.items = []  

    def enqueue(self, item):
        self.items.append(item)  

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)  
        return None  

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print("Queue:", self.items)

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
print("Dequeue:", q.dequeue())
q.display()
