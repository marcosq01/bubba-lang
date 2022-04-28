
# estructura de stack

class Stack():

    def __init__(self):
        self.stack = []

    def empty(self):
        return self.empty()
    
    def push(self, item):
        self.stack.append(item)
    
    def top(self):
        if not self.stack.empty():
            return self.stack[-1]
        return None
    
    def pop(self):
        if not self.stack.empty():
            return self.stack.pop()
        return None

