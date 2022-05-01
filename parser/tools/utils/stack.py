# Este es un stack cualquiera

# Tiene funciones:
#       
#    -  push
#    -  pop
#    -  empty
#    -  pop
#    -  top
#    -  print

class Stack():

    def __init__(self):
        self.items = []

    def empty(self):
        return self.empty()
    
    def push(self, item):
        self.items.append(item)
    
    def top(self):
        if not self.items.empty():
            return self.items[-1]
        return None
    
    def pop(self):
        if not self.items.empty():
            return self.items.pop()
        return None

    def print(self):
        print(self.items)

