
class semantic_cube():

    def __init__(self):
        self.cube = {
            
            # None es error

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
                    '&&' : None,
                    '||' : None
                },
                'string' : {
                    '+' : None,
                    '-' : None,
                    '*' : None,
                    '/' : None,
                    '>' : None,
                    '>=' : None,
                    '<' : None,
                    '<=' : None,
                    '!=' : None,
                    '=' : None,
                    '&&' : None,
                    '||' : None
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
                    '&&' : None,
                    '||' : None
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
                    '&&' : None,
                    '||' : None
                },
                'string' : {
                    '+' : None,
                    '-' : None,
                    '*' : None,
                    '/' : None,
                    '>' : None,
                    '>=' : None,
                    '<' : None,
                    '<=' : None,
                    '!=' : None,
                    '=' : None,
                    '&&' : None,
                    '||' : None
                }
            },

            'string' : {
                'int' : {
                    '+' : None,
                    '-' : None,
                    '*' : None,
                    '/' : None,
                    '>' : None,
                    '>=' : None,
                    '<' : None,
                    '<=' : None,
                    '!=' : None,
                    '=' : None,
                    '&&' : None,
                    '||' : None
                },
                'float' : {
                    '+' : None,
                    '-' : None,
                    '*' : None,
                    '/' : None,
                    '>' : None,
                    '>=' : None,
                    '<' : None,
                    '<=' : None,
                    '!=' : None,
                    '=' : None,
                    '&&' : None,
                    '||' : None
                },
                'string' : {
                    '+' : None,
                    '-' : None,
                    '*' : None,
                    '/' : None,
                    '>' : 'int',
                    '>=' : 'int',
                    '<' : 'int',
                    '<=' : 'int',
                    '!=' : 'int',
                    '=' : 'int',
                    '&&' : None,
                    '||' : None
                }
            }
        }

    def type_check(self, left, right, op):

        # tyoe check de los operandos (left, right ) y la operacion (op)

        # e.g. INT + INT produce un INT

        return self.cube[left][right][op]
