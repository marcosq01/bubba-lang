
#
from ply import yacc
from lexer import tokens
#
from tools.utils.stack import Stack
from tools.semantics.semantic_cube import SemanticCube
from tools.semantics.quadruple import Quadruple
from tools.semantics.vars_table import VarsTable, VariableContext
from tools.semantics.function_directory import FunctionDirectory, FunctionContext
from tools.error import Error
from tools.address_manager import AddressManager
#


# TODO agregar precedence en caso de ser necesario
# TODO algunas reglas tienen mal el orden (se ejecutan las de la derecha primero)
#      o sea esta bien la sintaxis pero en el orden de shift estan mal (queremos
#      que vaya de izquierda a derecha
# TODO revisar que en funciones NO VOID tengan al menos un return
# TODO las constantes
# TODO las temporales
# TODO los cuadruplos de las expresiones
# TODO checar los tipos con los operandos y operadores

# Algunas variables de utilidad (stacks, listas, tablas, etc):
# por el momento son muy simples pero despues se anadiran mas propiedades

# Cubo semantico
cube = SemanticCube()

function_directory = FunctionDirectory()

# este puede contener (+, -, /, *)
operator_stack = Stack()

# este puede contener (a, b, 1, var, etc)
operands_stack = Stack()

# stack para los types del stack de operandos
types_stack = Stack()

# estos serian cuadruplos para 'main' (por el momento)
quadruples = []

# el administrador de direcciones
addr_manager = AddressManager()



program_name = None
current_type_var_declaration = None

current_function = None
current_vars_table = None
current_function_type = None


# -----------------------------------------------------------------
# Gramatica

def p_program(p):
    'program : PROG ID x_add_prog_to_funcdir COLON paux program_vars program_funcs'
    function_directory.print()
    pass

def p_paux(p):
    '''
        paux : classr paux
             | empty
    '''
    pass

def p_program_vars(p):
    '''
        program_vars : varsr 
                     | empty
    '''
    pass

def p_program_funcs(p):
    '''
        program_funcs : mainr
                      | funcs mainr
    '''
    pass

def p_funcs(p):
    '''
        funcs : funcr
              | funcs funcr
    '''
    pass


def p_mainr(p):
    'mainr : MAIN x_add_main_to_func_dir LPAR RPAR LBRACE body RBRACE'
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

def p_lid(p):
    '''
        lid : var_dec x_declare_variable 
            | var_dec x_declare_variable COMMA lid 
    '''
    pass

def p_var_dec(p):
    '''
        var_dec : ID
                | ID LBRACKET VINTEGER RBRACKET
                | ID LBRACKET VINTEGER COMMA VINTEGER RBRACKET
    '''
    # return var_id
    p[0] = p[1]



def p_var(p):
    '''
        var : var_id 
            | var_id var_brackets
    '''
    pass

def p_var_id(p):
    '''
        var_id : ID
               | ID DOT ID
    '''
    pass

def p_var_brackets(p):
    '''
        var_brackets : LBRACKET expression RBRACKET
                     | LBRACKET expression COMMA expression RBRACKET
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
    '''
        funcr : FUNC func_type x_set_current_function_type ID x_insert_new_function LPAR RPAR LBRACE body RBRACE
              | FUNC func_type x_set_current_function_type ID x_insert_new_function LPAR params RPAR LBRACE body RBRACE
    '''
    pass

def p_params(p):
    '''
        params : type_simple x_var_dec_set_curr_type COLON ID x_declare_variable
               | type_simple x_var_dec_set_curr_type COLON ID x_declare_variable COMMA params
    '''
    pass

def p_func_type(p):
    '''
        func_type : INT
                  | FLOAT
                  | STRING
                  | VOID
    '''
    p[0] = p[1]

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
    '''
        body : varsr stmts
             | varsr
             | stmts
             | empty
    '''
    pass

# TODO Vars tiene que estar entre {} , cambiarlo despues porque hay problema aqui
def p_varsr(p):
    '''
        varsr : VARS x_set_current_vars_table LBRACE vars_a RBRACE
    '''
    pass

v = []

def p_vars_a(p):
    '''
        vars_a : var_type x_var_dec_set_curr_type COLON lid SEMICOLON
               | vars_a var_type x_var_dec_set_curr_type COLON lid SEMICOLON
    '''
    pass

def p_var_type(p):
    '''
        var_type : INT
                 | FLOAT
                 | STRING
                 | ID
    '''
    p[0] = p[1]

def p_type_simple(p):
    '''
        type_simple : INT
                    | FLOAT
                    | STRING
    '''
    p[0] = p[1]
    pass

def p_call(p):
    '''
        call : call_id LPAR RPAR
             | call_id LPAR args RPAR
    '''
    pass

def p_call_id(p):
    '''
        call_id : ID
                | ID DOT ID
    '''
    pass

def p_args(p):
    '''
        args : expression
             | expression COMMA args
    '''
    pass

def p_var_cte(p):
    '''
        var_cte : VINTEGER
                | VFLOAT
                | VSTRING
    '''
    pass


def p_methods(p):
    '''
        methods : methods funcr 
                | funcr
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
        stmts : statement
              | stmts statement
    '''
    pass



# Puntos neuralgicos ----------------------------------------------

# empiezan con p_x_*(p):


def p_x_add_prog_to_funcdir(p):
    'x_add_prog_to_funcdir :'
    # Obtener el nombre del programa
    global program_name
    program_name = p[-1]

    # 'Funcion' actual es program_name
    # esto es para guardar las variables globales
    global current_function 

    # Insertar el programa como si fuera una funcion, este tiene
    # la tabla de variables globales
    function_directory.insert_function(FunctionContext(program_name, 'program', VarsTable()))
    print(function_directory.__dict__)

    # La funcion actual es 'programa'
    current_function = function_directory.search_function(program_name)



# Actualizar current_type para la creacion de variables
def p_x_var_dec_set_curr_type(p):
    'x_var_dec_set_curr_type : '
    global current_type_var_declaration
    current_type_var_declaration = p[-1]
    print(current_type_var_declaration)


def p_x_declare_variable(p):
    'x_declare_variable :'
    var_name = p[-1]
    print(var_name)
    # Esto por mientras es para variables que no son arreglos
    # Tenemos que buscar la variable en la tabla de variables actual
    # Si ya existe, marcamos error
    if current_vars_table.has_var(var_name):
        Error("Variable doblemente declarada.")
    else:
        # Ponemos la variable en la tabla de variables
        addr = None
        # del directorio sacar el tipo
        t_func = current_function.type
        t_var = current_type_var_declaration
        scope = None
        print("TFUNC Y TVAR")
        print(t_func, t_var)
        # estas son las globales
        if t_func == 'program':
            if t_var == 'int':
                addr = addr_manager.get_global_int(1)
            elif t_var == 'float':
                addr = addr_manager.get_global_float(1)
            elif t_var == 'string':
                addr = addr_manager.get_global_string(1)

        # estas son las locales
        else:
            if t_var == 'int':
                addr = addr_manager.get_local_int(1)
            elif t_var == 'float':
                addr = addr_manager.get_local_float(1)
            elif t_var == 'string':
                addr = addr_manager.get_local_string(1)

        # TODO clases y arreglos


        var = VariableContext(p[-1], current_type_var_declaration, addr) 
        current_vars_table.insert_var(var)
        print("TABLA VARIABLES: ")
        print(current_vars_table.__dict__)


def p_x_set_current_vars_table(p):
    'x_set_current_vars_table :'
    global current_vars_table
    current_vars_table = current_function.get_vars_table()

def p_x_set_current_function_type(p):
    'x_set_current_function_type :'
    global current_function_type
    current_function_type = p[-1]


def p_x_insert_new_function(p):
    'x_insert_new_function :'
    func_name = p[-1]

    # Revisar que no haya sido declarada otra funcion con este nombre
    # o que no sea main
    if function_directory.has_function(func_name):
        Error("Funcion ya ha sido declarada")

    # Agregarla al directorio de funciones
    global current_vars_table
    global current_function
    current_vars_table = VarsTable()
    current_function = FunctionContext(func_name, current_function_type, current_vars_table)
    function_directory.insert_function(current_function)
    print("Nueva funcion: ")
    print(function_directory.__dict__)

    # actualizar las direcciones locales y temporales 
    addr_manager.reset()
 
def p_x_add_main_to_func_dir(p):
    'x_add_main_to_func_dir :'
    if function_directory.has_function('main'):
        Error("Funcion ya ha sido declarada")
    
    global current_vars_table, current_function
    current_vars_table = VarsTable()
    current_function = FunctionContext('main', 'main', current_vars_table)
    function_directory.insert_function(current_function)
    addr_manager.reset()
    








# esta regla es para mas claridad en el codigo (gramatica)
# no hace nada
def p_empty(p):
    'empty :'
    pass

def p_error(p):
    print("Syntax error on line", p.lexer.lineno)
    # TODO el numero de lineas
    exit()


parser = yacc.yacc()

f = open("./tests/test.txt")


# correr un ejemplo 
s = f.read()

result = parser.parse(s)
