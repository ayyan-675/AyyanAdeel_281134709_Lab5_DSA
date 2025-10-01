class Stack:
    def __init__(self):
        self.i = []   
    def push(self, item):
        self.i.append(item)
    def pop(self):
        if self.is_empty():
            return "Stack is empty! Cannot pop."
        return self.i.pop()
    def peek(self):
        if self.is_empty():
            return "Stack is empty! Nothing to peek."
        return self.i[-1]
    def is_empty(self):
        return len(self.i) == 0
    def size(self):
        return len(self.i)

if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Top element:", stack.peek())
    print("Popped:", stack.pop())
    print("Popped:", stack.pop())
    print("Current size:", stack.size())
    print("Is stack empty?", stack.is_empty())
    print("Popped:", stack.pop())

    