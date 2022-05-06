class Constant:
    def __init__(self, c, a) -> None:
        self.constant = c
        self.address = a

class ConstantsTable:
    def __init__(self) -> None:
        self.table ={}
    
    def add_constant(self, c, a):
        self.table[c] = Constant(c,a)
    
    def has_constant(self, c):
        return c in self.table
    
    def get_constant(self, c):
        return self.table[c]

