# TODO int + float yyyy float + int   ---->   float
# TODO  int / float  yyyy flaot / int ----> float
class SemanticCube():
 # TODO agregar el == y cambiar las multiplicaciones de int y float
    def __init__(self):
        self.cube = {
            
            'int' : {
                'int' : {
                    '+' : 'int',
                    '-' : 'int',
                    '*' : 'int',
                    '/' : 'int',
                    '>' : 'int',
                    '>=' : 'int',
                    '<' : 'int',
                    '<=' : 'int',
                    '!=' : 'int',
                    '=' : 'int',
                    '&&' : 'int',
                    '||' : 'int'
                },
                'float' : {
                    '+' : 'int',
                    '-' : 'int',
                    '*' : 'int',
                    '/' : 'int',
                    '>' : 'int',
                    '>=' : 'int',
                    '<' : 'int',
                    '<=' : 'int',
                    '!=' : 'int',
                    '=' : 'int',
                    '&&' : 'error',
                    '||' : 'error'
                },
                'string' : {
                    '+' : 'error',
                    '-' : 'error',
                    '*' : 'error',
                    '/' : 'error',
                    '>' : 'error',
                    '>=' : 'error',
                    '<' : 'error',
                    '<=' : 'error',
                    '!=' : 'error',
                    '=' : 'error',
                    '&&' : 'error',
                    '||' : 'error'
                }
            },

            'float' : {
                'int': {
                    '+' : 'int',
                    '-' : 'int',
                    '*' : 'int',
                    '/' : 'int',
                    '>' : 'int',
                    '>=' : 'int',
                    '<' : 'int',
                    '<=' : 'int',
                    '!=' : 'int',
                    '=' : 'int',
                    '&&' : 'error',
                    '||' : 'error'
                },
                'float' : {
                    '+' : 'float',
                    '-' : 'float',
                    '*' : 'float',
                    '/' : 'float',
                    '>' : 'int',
                    '>=' : 'int',
                    '<' : 'int',
                    '<=' : 'int',
                    '!=' : 'int',
                    '=' : 'int',
                    '&&' : 'error',
                    '||' : 'error'
                },
                'string' : {
                    '+' : 'error',
                    '-' : 'error',
                    '*' : 'error',
                    '/' : 'error',
                    '>' : 'error',
                    '>=' : 'error',
                    '<' : 'error',
                    '<=' : 'error',
                    '!=' : 'error',
                    '=' : 'error',
                    '&&' : 'error',
                    '||' : 'error'
                }
            },

            'string' : {
                'int' : {
                    '+' : 'error',
                    '-' : 'error',
                    '*' : 'error',
                    '/' : 'error',
                    '>' : 'error',
                    '>=' : 'error',
                    '<' : 'error',
                    '<=' : 'error',
                    '!=' : 'error',
                    '=' : 'error',
                    '&&' : 'error',
                    '||' : 'error'
                },
                'float' : {
                    '+' : 'error',
                    '-' : 'error',
                    '*' : 'error',
                    '/' : 'error',
                    '>' : 'error',
                    '>=' : 'error',
                    '<' : 'error',
                    '<=' : 'error',
                    '!=' : 'error',
                    '=' : 'error',
                    '&&' : 'error',
                    '||' : 'error'
                },
                'string' : {
                    '+' : 'string',
                    '-' : 'error',
                    '*' : 'error',
                    '/' : 'error',
                    '>' : 'int',
                    '>=' : 'int',
                    '<' : 'int',
                    '<=' : 'int',
                    '!=' : 'int',
                    '=' : 'int',
                    '&&' : 'error',
                    '||' : 'error'
                }
            }
        }

    def type_check(self, left, right, op):

        # tyoe check de los operandos (left, right ) y la operacion (op)

        # e.g. INT + INT produce un INT

        return self.cube[left][right][op]
