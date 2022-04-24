
from enum import Enum

class Type(Enum):
    INT = 1
    FLOAT = 2
    STRING = 3
    ERROR = 4

class Operation(Enum):
    PLUS = 1
    MINUS = 2
    MULTIPLICATION = 3
    DIVISION = 4
    GREATER = 5
    GREATEREQ = 6
    LESS = 7
    LESSEQ = 8
    NOTEQUAL = 9
    EQUAL = 10
    AND = 11
    OR = 12



class semantic_cube():

    def __init__(self):
        self.cube = {
            
            # None es error

            Type.INT : {
                Type.INT : {
                    Operation.PLUS : Type.INT,
                    Operation.MINUS : Type.INT,
                    Operation.MULTIPLICATION : Type.INT,
                    Operation.DIVISION : Type.INT,
                    Operation.GREATER : Type.INT,
                    Operation.GREATEREQ : Type.INT,
                    Operation.LESS : Type.INT,
                    Operation.LESSEQ : Type.INT,
                    Operation.NOTEQUAL : Type.INT,
                    Operation.EQUAL : Type.INT,
                    Operation.AND : Type.INT,
                    Operation.OR : Type.INT
                },
                Type.FLOAT : {
                    Operation.PLUS : Type.INT,
                    Operation.MINUS : Type.INT,
                    Operation.MULTIPLICATION : Type.INT,
                    Operation.DIVISION : Type.INT,
                    Operation.GREATER : Type.INT,
                    Operation.GREATEREQ : Type.INT,
                    Operation.LESS : Type.INT,
                    Operation.LESSEQ : Type.INT,
                    Operation.NOTEQUAL : Type.INT,
                    Operation.EQUAL : Type.INT,
                    Operation.AND : None,
                    Operation.OR : None
                },
                Type.STRING : {
                    Operation.PLUS : None,
                    Operation.MINUS : None,
                    Operation.MULTIPLICATION : None,
                    Operation.DIVISION : None,
                    Operation.GREATER : None,
                    Operation.GREATEREQ : None,
                    Operation.LESS : None,
                    Operation.LESSEQ : None,
                    Operation.NOTEQUAL : None,
                    Operation.EQUAL : None,
                    Operation.AND : None,
                    Operation.OR : None
                }
            },

            Type.FLOAT : {
                Type.INT: {
                    Operation.PLUS : Type.INT,
                    Operation.MINUS : Type.INT,
                    Operation.MULTIPLICATION : Type.INT,
                    Operation.DIVISION : Type.INT,
                    Operation.GREATER : Type.INT,
                    Operation.GREATEREQ : Type.INT,
                    Operation.LESS : Type.INT,
                    Operation.LESSEQ : Type.INT,
                    Operation.NOTEQUAL : Type.INT,
                    Operation.EQUAL : Type.INT,
                    Operation.AND : None,
                    Operation.OR : None
                },
                Type.FLOAT : {
                    Operation.PLUS : Type.FLOAT,
                    Operation.MINUS : Type.FLOAT,
                    Operation.MULTIPLICATION : Type.FLOAT,
                    Operation.DIVISION : Type.FLOAT,
                    Operation.GREATER : Type.INT,
                    Operation.GREATEREQ : Type.INT,
                    Operation.LESS : Type.INT,
                    Operation.LESSEQ : Type.INT,
                    Operation.NOTEQUAL : Type.INT,
                    Operation.EQUAL : Type.INT,
                    Operation.AND : None,
                    Operation.OR : None
                },
                Type.STRING : {
                    Operation.PLUS : None,
                    Operation.MINUS : None,
                    Operation.MULTIPLICATION : None,
                    Operation.DIVISION : None,
                    Operation.GREATER : None,
                    Operation.GREATEREQ : None,
                    Operation.LESS : None,
                    Operation.LESSEQ : None,
                    Operation.NOTEQUAL : None,
                    Operation.EQUAL : None,
                    Operation.AND : None,
                    Operation.OR : None
                }
            },

            Type.STRING : {
                Type.INT : {
                    Operation.PLUS : None,
                    Operation.MINUS : None,
                    Operation.MULTIPLICATION : None,
                    Operation.DIVISION : None,
                    Operation.GREATER : None,
                    Operation.GREATEREQ : None,
                    Operation.LESS : None,
                    Operation.LESSEQ : None,
                    Operation.NOTEQUAL : None,
                    Operation.EQUAL : None,
                    Operation.AND : None,
                    Operation.OR : None
                },
                Type.FLOAT : {
                    Operation.PLUS : None,
                    Operation.MINUS : None,
                    Operation.MULTIPLICATION : None,
                    Operation.DIVISION : None,
                    Operation.GREATER : None,
                    Operation.GREATEREQ : None,
                    Operation.LESS : None,
                    Operation.LESSEQ : None,
                    Operation.NOTEQUAL : None,
                    Operation.EQUAL : None,
                    Operation.AND : None,
                    Operation.OR : None
                },
                Type.STRING : {
                    Operation.PLUS : None,
                    Operation.MINUS : None,
                    Operation.MULTIPLICATION : None,
                    Operation.DIVISION : None,
                    Operation.GREATER : Type.INT,
                    Operation.GREATEREQ : Type.INT,
                    Operation.LESS : Type.INT,
                    Operation.LESSEQ : Type.INT,
                    Operation.NOTEQUAL : Type.INT,
                    Operation.EQUAL : Type.INT,
                    Operation.AND : None,
                    Operation.OR : None
                }
            }
        }

    def type_check(self, left, right, op):

        # tyoe check de los operandos (left, right ) y la operacion (op)

        # e.g. INT + INT produce un INT

        return self.cube[left][right][op]
