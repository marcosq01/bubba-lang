
from ply import lex

# TODO falta el regex de VSTRING
# TODO line numbers??


# Lista de tokens

reserved = {
    'prog' : 'PROG',
    'main' : 'MAIN',
    'float' : 'FLOAT',
    'int' : 'INT',
    'string' : 'STRING',
    'print' : 'PRINT',
    'vars' : 'VARS',
    'if' : 'IF',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'for' : 'FOR',
    'step' : 'STEP',
    'return' : 'RETURN',
    'class' : 'CLASS',
    'extends' : 'EXTENDS',
    'func' : 'FUNC',
    'void' : 'VOID',
    'input' : 'INPUT',
    'to' : 'TO'
}

tokens = [

    'DOT',
    'COMMA',
    'LPAR',
    'RPAR',
    'LBRACE',
    'RBRACE',
    'LBRACKET',
    'RBRACKET',
    'SEMICOLON',

    'PLUS',
    'MINUS',
    'MUL',
    'DIV',

    'GREATER',
    'GREATEREQ',
    'LESS',
    'LESSEQ',
    'EQUAL',

    'COLON',
    'QUOTE',

    'AND',
    'OR',
    'NOT',

    'EQEQUAL',
    'NOTEQUAL',

    # integer values
    'VINTEGER',
    # float values
    'VFLOAT',

    # string in ""
    'VSTRING',

    # identifiers
    'ID',

    # comment lines
    'COMMENT'
] + list(reserved.values())


# Expresiones regulares para tokens simples

t_DOT = r'\.'
t_COMMA = r','
t_LPAR = r'\('
t_RPAR = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_SEMICOLON = r';'
t_PLUS = r'\+'
t_MINUS = r'-'
t_MUL = r'\*'
t_DIV = r'/'
t_GREATER = r'>'
t_LESS = r'<'
t_LESSEQ = r'<='
t_EQUAL = r'='
t_COLON = r':'
t_QUOTE = r'"'
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_EQEQUAL = r'=='
t_NOTEQUAL = r'!='



# para comentarios
def t_COMMENT(t):
    r'\#.*'
    pass
    # No return value. Token discarded

# VFLOAT debe ir antes de INTEGER
def t_VFLOAT(t):
    r'[0-9]+\.[0-9]+'
    t.value = float(t.value)
    return t

def t_VINTEGER(t):
    r'[0-9]+'
    try:
        t.value = int(t.value)
    except ValueError:
        # Error numero grande
        print("error")
    return t

def t_ID(t):
    r'[a-zA-Z][a-zA-Z\d]*'
    t.type = reserved.get(t.value, 'ID')
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# ignored characters (spaces and tabs)
t_ignore = ' \t'

 # Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)



# build lexer
lexer = lex.lex()




# Test it out
# data = '''
# # 
# prog sapito :  
# main(){
#     print (a) ;
# }
# '''

# lexer.input(data)

# while True:
#     tok = lexer.token()
#     if not tok:
#         break
#     print(tok)