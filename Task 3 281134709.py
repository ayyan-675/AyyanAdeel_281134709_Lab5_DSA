class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if self.is_empty():
            return "Stack is empty! Cannot pop."
        return self.items.pop()
    def is_empty(self):
        return len(self.items) == 0

def reverse_string(input_string):
    stack = Stack()
    for char in input_string:
        stack.push(char)
    reversed_str = ""
    while not stack.is_empty():
        reversed_str += stack.pop()
    return reversed_str

if __name__ == "__main__":
    test_cases = ["hello", "Python", "Stack", "12345"]
    for s in test_cases:
        print(f"Original: {s}  -->  Reversed: {reverse_string(s)}")

