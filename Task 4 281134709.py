class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()
    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]
    def is_empty(self):
        return len(self.items) == 0
    
def is_balanced(expression):
    stack = Stack()
    pairs = {')': '(', '}': '{', ']': '['}
    for char in expression:
        if char in "({[":
            stack.push(char)
        elif char in ")}]":
            top = stack.pop()
            if top != pairs[char]:
                return False
    return stack.is_empty()
if __name__ == "__main__":
    expressions = [
        "{[()]}",
        "((()))",
        "{[()]})",
        "[(])",
        "(()",
        "(){[]}"
    ]
    for exp in expressions:
        if is_balanced(exp):
            print(f"Expression '{exp}' is Balanced")
        else:
            print(f"Expression '{exp}' is NOT Balanced")


