class Stack:
    def __init__(self, items=[], limit=100):
        self.stack = []
        self.items = items
        self.limit = limit
        for item in items:
            self.stack.append(item)

    # def isEmpty(self):
    #     pass
        
    def isEmpty(self):
        return True if len(self.stack) == 0 else False       

    def push(self, item):
        if len(self.stack) < self.limit:
            self.stack.append(item)
            return self
        else:
            print("Stack is full. Cannot push item.")

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            print("Stack is empty. Cannot pop item.")
            return None

    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            print("Stack is empty. Cannot peek item.")
            return None

    def size(self):
        return len(self.stack)

    def full(self):
        return True if len(self.stack) == self.limit else False         

    def search(self, target):
        if target in self.stack:
            return len(self.stack) - self.stack.index(target) - 1
        else:
            return -1
