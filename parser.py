
#
from ply import yacc
from lexer import tokens
#
from semantic_cube import SemanticCube
from quadruple import Quadruple
from vars_table import VarsTable, VariableContext
from function_directory import FunctionDirectory, FunctionContext
#


# TODO agregar precedence en caso de ser necesario
# TODO algunas reglas tienen mal el orden (se ejecutan las de la derecha primero)
# .    o sea esta bien la sintaxis pero en el orden de shift estan mal (queremos
# .    que vaya de derecha a izquierda

def p_program(p):
    'program : PROG ID COLON paux paux2 paux3 mainr'
    print("programa", p[2], "creado")
    p[0] = p[2]


def p_paux(p):
    '''
        paux : classr paux
             | empty
    '''
    pass

def p_paux2(p):
    '''
        paux2 : varsr 
              | empty
    '''
    pass

def p_paux3(p):
    '''
        paux3 : paux3 methods
              | empty
    '''
    pass

def p_mainr(p):
    'mainr : MAIN LPAR RPAR LBRACE body RBRACE'
    pass

def p_whiler(p):
    'whiler : WHILE LPAR expression RPAR LBRACE stmts RBRACE'
    pass

def p_forr(p):
    'forr : FOR foraux TO foraux foraux2 LBRACE stmts RBRACE'
    pass

def p_foraux(p):
    '''
        foraux : VINTEGER
               | ID
    '''
    pass

def p_foraux2(p):
    '''
        foraux2 : STEP
                | foraux
                | empty
    '''
    pass

def p_statement(p):
    '''
        statement : assign
                  | call SEMICOLON
                  | if
                  | if_else
                  | forr
                  | whiler
                  | output
                  | inputr
                  | returnr
    '''
    pass

def p_lid(p):
    '''
        lid : var_dec 
            | var_dec COMMA lid 
    '''
    pass

def p_var_dec(p):
    '''
        var_dec : ID
                | ID LBRACKET VINTEGER RBRACKET
                | ID LBRACKET VINTEGER COMMA VINTEGER RBRACKET
    '''
    v.append(p[1])

def p_var(p):
    'var : ID varaux varaux2'
    pass

def p_varaux(p):
    '''
        varaux : DOT ID
               | empty
    '''
    pass

def p_varaux2(p):
    '''
        varaux2 : LBRACKET expression varaux3 RBRACKET
                | empty
    '''
    pass

def p_varaux3(p):
    '''
        varaux3 : COMMA expression
                | empty
    '''
    pass

def p_assign(p):
    'assign : var EQUAL expression SEMICOLON'
    pass

def p_factor(p):
    '''
        factor : MINUS factor_val
               | PLUS factor_val
               | factor_val
    '''
    pass

def p_factor_val(p):
    '''
        factor_val : LPAR expression RPAR
                   | var_cte
                   | call
                   | var
    '''
    pass

def p_term(p):
    '''
        term : factor
             | factor MUL term
             | factor DIV term
    '''
    pass

def p_exp(p):
    '''
        exp : term
            | term PLUS exp
            | term MINUS exp
    '''
    pass

def p_aexp(p):
    '''
        aexp : exp
             | exp aexp_rel_ops exp
    '''

    pass


def p_aexp_rel_ops(p):
    '''
        aexp_rel_ops : GREATER
                     | LESS
                     | EQEQUAL
                     | NOTEQUAL
                     | GREATEREQ
                     | LESSEQ
    '''
    pass

def p_bexp(p):
    '''
        bexp : aexp
             | aexp AND bexp
    '''
    pass

def p_expression(p):
    '''
        expression : bexp
                   | bexp OR expression
    '''
    pass

def p_funcr(p):
    'funcr : FUNC type_simple ID LPAR funcaux RPAR LBRACE body RBRACE'
    pass

def p_funcaux(p):
    '''
        funcaux : args
                | empty
    '''
    pass

def p_classr(p):
    'classr : CLASS ID class_extends LBRACE varsr methods RBRACE SEMICOLON'
    pass

def p_class_extends(p):
    '''
        class_extends : EXTENDS ID
                      | empty
    '''

def p_output(p):
    'output : PRINT LPAR expression output_a RPAR SEMICOLON'
    pass

def p_output_a(p):
    '''
        output_a : COMMA expression output_a
                 | empty
    '''
    pass

def p_inputr(p):
    'inputr : INPUT LPAR var input_a RPAR SEMICOLON'
    pass

def p_input_a(p):
    '''
        input_a : COMMA var input_a
                | empty
    '''
    pass

def p_body(p):
    'body : body_a stmts'
    pass

def p_body_a(p):
    '''
        body_a : varsr
               | empty
    '''
    pass

def p_varsr(p):
    '''
        varsr : VARS vars_a
    '''
    pass

v = []

def p_vars_a(p):
    '''
        vars_a : vars_a var_type np COLON lid SEMICOLON
               | var_type np COLON lid SEMICOLON
    '''
    global v
    if (len(p) == 6):
        print(6)
        print(v)
        v = []
    elif len(p) == 7:
        print(7)
        print(v)
        v = []

def p_np(p):
    'np :'
    print("type: ", p[-1])

def p_var_type(p):
    '''
        var_type : INT
                 | FLOAT
                 | STRING
                 | ID
    '''
    p[0] = p[1]
    pass

def p_args(p):
    'args : type_simple COLON ID args_a'
    pass

def p_args_a(p):
    '''
        args_a : COMMA args
               | empty
    '''
    pass

def p_type_simple(p):
    '''
        type_simple : INT
                    | FLOAT
                    | STRING
    '''
    pass

def p_call(p):
    '''
        call : ID call_b
             | ID DOT ID call_b
    '''
    pass

def p_call_b(p):
    '''
        call_b : LPAR params RPAR
               | LPAR RPAR
    '''

def p_params(p):
    '''
        params : expression COMMA params
               | expression
    '''
    pass

def p_var_cte(p):
    '''
        var_cte : VINTEGER
                | VFLOAT
                | VSTRING
    '''
    pass

def p_voidr(p):
    'voidr : FUNC VOID ID LPAR void_a RPAR LBRACE body RBRACE'
    pass

def p_void_a(p):
    '''
        void_a : args
               | empty
    '''
    pass

def p_methods(p):
    '''
        methods : methods voidr 
                | methods funcr 
                | empty
    '''
    pass


def p_if_else(p):
    'if_else : IF LPAR expression RPAR LBRACE stmts RBRACE ELSE LBRACE stmts RBRACE SEMICOLON'
    pass

def p_if(p):
    'if : IF LPAR expression RPAR LBRACE stmts RBRACE SEMICOLON'
    pass

def p_returnr(p):
    '''
        returnr : RETURN expression SEMICOLON
                | RETURN SEMICOLON
    '''
    pass

def p_stmts(p): 
    '''
        stmts : stmts statement
              | empty
    '''
    pass







# esta regla es para mas claridad en el codigo (gramatica)
# no hace nada
def p_empty(p):
    'empty :'
    pass

def p_error(p):
    print("Syntax error.")


parser = yacc.yacc()



# correr un ejemplo 

s = ''' 

prog karen:

main() {
    vars int : a, b, c; float:x,y,y[1];
}
'''

result = parser.parse(s)

print(result)