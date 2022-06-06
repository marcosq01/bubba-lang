

class Quadruple:

    def __init__(self, op, left, right, result) -> None:
        self.op = op
        self.left = left
        self.right = right
        self.result = result

    def set_result(self, x):
        self.result = x


    def print(self):

        return str("  " + self.op + (" " * ( 12 - len(str(self.op)))) + str(self.left) + (" " * (22 - len(str(self.left)))) + str(self.right) + (" " * (15 - len(str(self.left)))) + str(self.result))

