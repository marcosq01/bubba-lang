
from re import A
from ply import yacc
from lexer import tokens

from semantic_cube import SemanticCube
from quadruple import Quadruple
from vars_table import VarsTable, VariableContext
from function_directory import FunctionDirectory, FunctionContext



# TODO agregar precedence en caso de ser necesario
# TODO agregar puntos neuralgicos SOLO los que son necesarios
#      hasta el momento

def p_program(p):
    'program : PROG ID COLON paux paux2 paux3 main'
    print("programa", p[2], "creado")


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
        paux3 : methods paux3
              | empty
    '''
    pass

def p_main(p):
    'main : MAIN LPAR RPAR LBRACE body RBRACE'
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
                  | expression
                  | forr
                  | whiler
                  | output
                  | inputr
                  | returnr
    '''
    pass

def p_lid(p):
    'lid : ID lidaux SEMICOLON'
    pass

def p_lidaux(p):
    'lidaux : laux laux2'
    pass

def p_laux(p):
    '''
        laux : COMMA ID laux
             | empty    
    '''
    pass

def p_laux2(p):
    '''
        laux2 : LBRACKET VINTEGER maux RBRACKET laux
              | empty
    '''
    pass

def p_maux(p):
    '''
        maux : COMMA VINTEGER
             | empty
    '''
    pass

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
    'factor : faux faux2'
    pass

def p_faux(p):
    '''
        faux : PLUS
             | MINUS
             | empty
    '''
    pass

def p_faux2(p):
    '''
        faux2 : var_cte
             | call
             | LPAR expression RPAR
             | var
    '''
    pass

def p_term(p):
    'term : factor termaux'
    pass

def p_termaux(p):
    '''
        termaux : MUL term
                | DIV term
                | empty
    '''
    pass

def p_exp(p):
    'exp : term expaux'
    pass

def p_expaux(p):
    '''
        expaux : PLUS exp
               | MINUS exp
               | empty
    '''
    pass

def p_aexp(p):
    'aexp : exp aexpaux'
    pass

def p_aexpaux(p):
    '''
        aexpaux : aexps exp
                | empty
    '''
    pass

def p_aexps(p):
    '''
        aexps : GREATER
              | LESS
              | EQEQUAL
              | NOTEQUAL
              | GREATEREQ
              | LESSEQ
    '''
    pass

def p_bexp(p):
    'bexp : aexp bexpaux'
    pass

def p_bexpaux(p):
    '''
        bexpaux : AND bexp
                | empty
    '''
    pass

def p_expression(p):
    'expression : bexp expressionaux'
    pass

def p_expressionaux(p):
    '''
        expressionaux : OR expression
                      | empty
    '''
    pass

def p_funcr(p):
    'funcr : FUNC type_simple ID LPAR funcaux RPAR LBRACE body RETURN expression SEMICOLON RBRACE'
    pass

def p_funcaux(p):
    '''
        funcaux : args
                | empty
    '''
    pass

def p_classr(p):
    'classr : CLASS ID class_a LBRACE varsr class_b RBRACE SEMICOLON'
    pass

def p_class_a(p):
    '''
        class_a : EXTENDS ID
                | empty
    '''
    pass

def p_class_b(p):
    '''
        class_b : methods
                | empty
    '''
    pass

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

def p_vars(p):
    'varsr : VARS vars_a COLON lid vars_b'
    pass

def p_vars_a(p):
    '''
        vars_a : ID
               | type_simple
    '''
    pass

def p_vars_b(p):
    '''
        vars_b : varsr
               | empty
    '''
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
    'call : ID call_a LPAR call_b LPAR'
    pass

def p_call_a(p):
    '''
        call_a : DOT ID
               | empty
    '''
    pass

def p_call_b(p):
    '''
        call_b : params
               | empty
    '''
    pass

def p_params(p):
    'params : expression params_a'
    pass

def p_params_a(p):
    '''
        params_a : COMMA params
                 | empty
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
        methods : voidr
                | funcr
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
        returnr : expression
                | empty
    '''
    pass

def p_stmts(p): 
    '''
        stmts : statement stmts
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

s = ''' 
prog sapito ;
'''

result = parser.parse(s)

print(result)

