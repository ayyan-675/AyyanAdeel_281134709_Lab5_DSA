class Queue:
    def __init__(self):
        self.items = []  
    def enqueue(self, item):
        self.items.append(item)  
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty! Cannot dequeue."
        return self.items.pop(0)  
    def front(self):
        if self.is_empty():
            return "Queue is empty! Nothing at front."
        return self.items[0]
    def is_empty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)

if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(5)
    queue.enqueue(15)
    queue.enqueue(25)
    print("Front element:", queue.front())
    print("Dequeued:", queue.dequeue())
    print("Dequeued:", queue.dequeue())
    print("Current size:", queue.size())
    print("Is queue empty?", queue.is_empty())
    print("Dequeued:", queue.dequeue())

