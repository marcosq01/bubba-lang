from unittest import addModuleCleanup
from parser.tools.semantics.constants_table import Constant, ConstantsTable

from parser.ply import yacc

from parser.lexer import tokens

from parser.tools.utils.stack import Stack

from parser.tools.semantics.semantic_cube import SemanticCube
from parser.tools.semantics.quadruple import Quadruple
from parser.tools.semantics.vars_table import VarsTable, VariableContext
from parser.tools.semantics.function_directory import FunctionDirectory, FunctionContext

from parser.tools.error import Error

from parser.tools.address_manager import AddressManager



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

# Stack para los staltos
jumps_stack = Stack()

# estos serian cuadruplos para 'main' (por el momento)
quadruples = []

#Tabla de constantes
constants_table = ConstantsTable()

# el administrador de direcciones
addr_manager = AddressManager()


current_type_var_declaration = None

current_function = None
current_vars_table = None
current_function_type = None
current_var_name = None
current_var = None

# Este stack es para los accesos a elementos de matrices que estan anidados
# ejemplo: matriz[x, a + arr[0, 1]]
vars_stack = Stack()


# este stack es para llamadas a funciones dentro de llamadas
# ejemplo:  f(g(a()) + h())
call_stack = Stack()

function_args_pointer = 0
current_function_call_name = None
current_function_return=0 
in_params = False

prog_name = None




# --------------------------------------------------------------------------------------------
# Gramatica

def p_program(p):
    'program : PROG ID x_add_prog_to_funcdir COLON paux program_vars program_funcs'
    function_directory.print()
    for i in range(len(quadruples)):
        print(i, quadruples[i].__dict__)
    for i in constants_table.table:
        print(constants_table.table[i].__dict__)
    


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
    '''mainr : MAIN x_add_main_to_func_dir LPAR RPAR x_func_init_addr x_goto_main LBRACE stmts RBRACE
             | MAIN x_add_main_to_func_dir LPAR RPAR x_func_init_addr x_goto_main LBRACE RBRACE 
    '''
    pass

def p_whiler(p):
    'whiler : WHILE x_while_start LPAR expression RPAR x_generate_gotoF LBRACE stmts RBRACE x_end_while'
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
        lid : var_dec
            | var_dec COMMA lid 
    '''
    pass

def p_var_dec(p):
    '''
        var_dec : ID x_declare_variable 
                | ID x_declare_variable x_set_is_array_1d LBRACKET VINTEGER x_set_first_len x_add_constant_arr_size RBRACKET x_array_get_addrs
                | ID x_declare_variable x_set_is_array_1d LBRACKET VINTEGER x_set_first_len x_add_constant_arr_size COMMA VINTEGER x_set_second_len x_add_constant_arr_size RBRACKET x_matrix_get_addrs
    '''
    p[0] = p[1]


def p_var(p):
    '''
        var : var_id x_add_Var_to_stack x_check_var_dimension_normal
            | var_id x_add_Var_to_stack var_brackets
    '''
    p[0]=p[1]


def p_var_id(p):
    '''
        var_id : ID
               | ID DOT ID
    '''
    p[0]=p[1]


def p_var_brackets(p):
    '''
        var_brackets : x_push_vars_stack LBRACKET x_check_first_dimension expression RBRACKET x_is_array x_check_first_bounds x_end_array_bracket x_pop_vars_stack
                     | x_push_vars_stack LBRACKET x_check_first_dimension expression COMMA x_check_second_dimension x_check_first_bounds expression RBRACKET x_check_second_bounds x_end_matrix_bracket x_pop_vars_stack
    '''
    pass

def p_assign(p):
    'assign : var EQUAL x_add_op_to_stack expression x_assignment_op SEMICOLON'
    pass


def p_factor(p):
    '''
        factor : MINUS factor_val x_generate_neg_quad
               | PLUS factor_val
               | factor_val 
    '''
    pass

def p_x_generate_neg_quad(p):
    'x_generate_neg_quad :'

    # En este punto tenemos el operador y su tipo en el top de los stacks
    # Se generará uncuadruplo que sea (-, 0, addr, temp)
    # primero se busca la constante 0 en la tabla de const
    # se agrega si es necesario

    if not constants_table.has_constant(0):
        addr_0 = addr_manager.get_const_int(1)
        constants_table.add_constant(0, addr_0)
    constant_0 = constants_table.get_constant(0)
    addr_0 = constant_0.address

    # obtener operando y tipo
    op = operands_stack.pop()
    t = types_stack.pop()

    if t == 'string':
        Error("No hay strings negativos")
    elif t == 'int':
        current_function.temp_int_counter += 1
        addr = addr_manager.get_temp_int(1)
    elif t == 'float':
        current_function.temp_float_counter += 1
        addr = addr_manager.get_temp_float(1)

    q = Quadruple('-', addr_0, op, addr)
    quadruples.append(q)

    operands_stack.push(addr)
    types_stack.push(t)


def p_factor_val(p):
    '''
        factor_val : LPAR x_add_op_to_stack expression RPAR x_pop_Lpar_from_stack 
                   | var_cte
                   | call
                   | var
    '''
    pass

def p_term(p):
    '''
        term : factor x_pop_MulD_of_stack
             | factor x_pop_MulD_of_stack MUL x_add_op_to_stack term
             | factor x_pop_MulD_of_stack DIV x_add_op_to_stack term
    '''
    pass

def p_exp(p):
    '''
        exp : term x_pop_PLUSM_of_stack
            | term x_pop_PLUSM_of_stack PLUS x_add_op_to_stack exp
            | term x_pop_PLUSM_of_stack MINUS x_add_op_to_stack exp
    '''
    pass

def p_aexp(p):
    '''
        aexp : exp 
             | exp aexp_rel_ops x_add_op_to_stack exp x_comparison_op
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
    p[0] = p[1]

def p_bexp(p):
    '''
        bexp : aexp x_AND_op
             | aexp AND x_add_op_to_stack bexp x_AND_op
    '''
    pass

def p_expression(p):
    '''
        expression : bexp x_OR_op 
                   | bexp OR x_add_op_to_stack expression x_OR_op 
    '''
    pass

def p_funcr(p):
    '''
        funcr : FUNC func_type x_set_current_function_type ID x_insert_new_function LPAR RPAR x_func_init_addr LBRACE body RBRACE x_add_endfunc 
              | FUNC func_type x_set_current_function_type ID x_insert_new_function LPAR x_set_true_params params x_set_false_params RPAR x_func_init_addr LBRACE body RBRACE x_add_endfunc
    '''
    pass

def p_x_set_true_params(p):
    'x_set_true_params :'
    global in_params
    in_params = True


def p_x_set_false_params(p):
    'x_set_false_params :'
    global in_params
    in_params = False
    

def p_params(p):
    '''
        params : type_simple x_add_param x_var_dec_set_curr_type COLON ID x_declare_variable
               | type_simple x_add_param x_var_dec_set_curr_type COLON ID x_declare_variable COMMA params
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
    'output : PRINT LPAR expression x_print_expr output_a RPAR SEMICOLON'
    pass

def p_output_a(p):
    '''
        output_a : COMMA expression x_print_expr output_a
                 | empty
    '''
    pass

def p_inputr(p):
    'inputr : INPUT LPAR var RPAR SEMICOLON'
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
        call : call_id x_verify_func x_push_par LPAR x_points_null RPAR x_push_call_value x_pop_par
             | call_id x_verify_func x_push_par LPAR args x_points_null RPAR x_push_call_value x_pop_par
    '''
    pass

    

def p_x_push_par(p):
    'x_push_par :'
    operator_stack.push('(')

def p_x_pop_par(p):
    'x_pop_par :'
    operator_stack.pop()

    # se actualiza current call name
    call_stack.pop()
    global current_function_call_name
    current_function_call_name = call_stack.top()

def p_x_push_call_value(p):
    'x_push_call_value :'
    global_func = function_directory.search_function(prog_name)
    global_vars_table = global_func.get_vars_table()

    global_var = global_vars_table.search_var(current_function_call_name)

    # si se llamó a una funcion void, simplemente salirnos porque no hay
    # nada que hacere en el stack de operandos
    if global_var == None:
        return

    # assign
    if global_var.type == 'int':
        new_addr = addr_manager.get_temp_int(1)
        current_function.temp_int_counter += 1
    elif global_var.type == 'float':    
        new_addr = addr_manager.get_temp_float(1)
        current_function.temp_float_counter += 1
    elif global_var.type == 'string':
        new_addr = addr_manager.get_temp_string(1)
        current_function.temp_string_counter += 1

    q = Quadruple('=', global_var.address, None, new_addr)
    quadruples.append(q)

    operands_stack.push(new_addr)
    types_stack.push(global_var.type)


def p_call_id(p):
    '''
        call_id : ID
                | ID DOT ID
    '''
    p[0]=p[1]

def p_args(p):
    '''
        args : expression x_check_parameters
             | expression x_check_parameters COMMA args
    '''
    pass

def p_var_cte(p):
    '''
        var_cte : VINTEGER x_add_constants_table_i
                | VFLOAT x_add_constants_table_f
                | VSTRING x_add_constants_table_s
    '''
    pass


def p_methods(p):
    '''
        methods : methods funcr 
                | funcr
    '''
    pass


def p_if_else(p):
    'if_else : IF LPAR expression RPAR x_generate_gotoF LBRACE stmts RBRACE x_else ELSE LBRACE stmts RBRACE SEMICOLON x_end_if'
    pass

def p_if(p):
    'if : IF LPAR expression RPAR x_generate_gotoF LBRACE stmts RBRACE SEMICOLON x_end_if'
    pass

def p_returnr(p):
    '''
        returnr : RETURN expression x_check_type_func SEMICOLON x_funcr_return
                | RETURN x_check_void_func SEMICOLON x_funcr_return_void
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


    # goto a main
    quadruples.append(Quadruple("goto", None, None, None))
    jumps_stack.push(0)
    
    # Obtener el nombre del programa
    global current_function
    global prog_name
    prog_name = p[-1]

    function_directory.program_name = p[-1]
    # 'Funcion' actual es program_name
    # esto es para guardar las variables globales

    # Insertar el programa como si fuera una funcion, este tiene
    # la tabla de variables globales
    function_directory.insert_function(FunctionContext(prog_name, 'program', VarsTable()))

    # La funcion actual es 'programa'
    current_function = function_directory.search_function(prog_name)



# Actualizar current_type para la creacion de variables
def p_x_var_dec_set_curr_type(p):
    'x_var_dec_set_curr_type : '
    global current_type_var_declaration
    current_type_var_declaration = p[-1]


def p_x_declare_variable(p):
    'x_declare_variable :'
    var_name = p[-1]
    global current_var_name
    current_var_name = var_name
    # Esto por mientras es para variables que no son arreglos
    # Tenemos que buscar la variable en la tabla de variables actual
    # Si ya existe, marcamos error
    if current_vars_table.has_var(var_name):
        Error("Variable doblemente declarada.")
    elif current_function.name == var_name:
        Error("Variable "+var_name+ " no se puede llamar igual que la función.")
    else:
        # Ponemos la variable en la tabla de variables
        addr = None
        # del directorio sacar el tipo
        t_func = current_function.type
        t_var = current_type_var_declaration
        # estas son las globales
        if t_func == 'program':
            if t_var == 'int':
                addr = addr_manager.get_global_int(1)
                current_function.local_int_counter += 1
            elif t_var == 'float':
                addr = addr_manager.get_global_float(1)
                current_function.local_float_counter += 1
            elif t_var == 'string':
                current_function.local_string_counter += 1
                addr = addr_manager.get_global_string(1)

        # estas son las locales
        else:

            if t_var == 'int':
                addr = addr_manager.get_local_int(1)
                current_function.local_int_counter += 1
 
            elif t_var == 'float':
                addr = addr_manager.get_local_float(1)
                current_function.local_float_counter += 1
            elif t_var == 'string':
                addr = addr_manager.get_local_string(1)
                current_function.local_string_counter += 1
            if in_params:
                params_addresses = current_function.params_addresses
                params_addresses.append(addr)

        # TODO clases y arreglos


        var = VariableContext(p[-1], current_type_var_declaration, addr) 
        current_vars_table.insert_var(var)
    
    global current_var
    current_var = var
    p[0] = var_name


def p_x_set_current_vars_table(p):
    'x_set_current_vars_table :'
    global current_vars_table
    current_vars_table = current_function.get_vars_table()

def p_x_set_current_function_type(p):
    'x_set_current_function_type :'
    global current_function_type
    global current_function_return
    current_function_type = p[-1]
    current_function_return = 0


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

    # declarar la variable global si no es void
    if current_function_type != 'void':

        global_func = function_directory.search_function(prog_name)
        global_vars_table = global_func.get_vars_table()

        if global_vars_table.has_var(func_name):
            Error("Funcion con mismo nombre de variable global`")

        if current_function_type == 'int':
            addr = addr_manager.get_global_int(1)
            global_func.local_int_counter += 1
        elif current_function_type == 'float':
            addr = addr_manager.get_global_float(1)
            global_func.local_float_counter += 1
        elif current_function_type == 'string':
            global_func.local_string_counter += 1
            addr = addr_manager.get_global_string(1)
        
        var = VariableContext(func_name, current_function_type, addr)
        global_vars_table.insert_var(var)
        
    # actualizar las direcciones locales y temporales 
    addr_manager.reset()
 
def p_x_add_main_to_func_dir(p):
    'x_add_main_to_func_dir :'
    if function_directory.has_function('main'):
        Error("Funcion ya ha sido declarada")
    
    global current_vars_table, current_function 
    current_function = function_directory.search_function(prog_name)
    current_vars_table = current_function.get_vars_table()
    # current_function = FunctionContext('main', 'main', current_vars_table)
    # function_directory.insert_function(current_function)
    addr_manager.reset()
    
# Agregar la variable a nuestra pila
def p_x_add_Var_to_stack(p):
    'x_add_Var_to_stack :'
    #Buscar la variable en el directorio
    varname = p[-1]
    #Revisar que la variable se encuentra en las vars locales
    if current_vars_table.has_var(varname):
        #guardar la variable del directorio
        varData = current_vars_table.search_var(varname)
    else:
        #Obtener la tabla de variables globales
        globalfunc = function_directory.search_function(prog_name)
        globalvars = globalfunc.get_vars_table()
        #Revisar que la variable se encuentra en las vars globales
        if globalvars.has_var(varname):
            #guardar la variable del directorio
            varData = globalvars.search_var(varname)
        #Si no existe se marca error
        else:
            Error ("Variable no ha sido declarada")

    global current_var_name, current_var
    current_var_name = varname
    current_var = varData
    #pushear la direccion al stack de operandos
    operands_stack.push(varData.address)
    #pushear el tipo al stack de tipos
    types_stack.push(varData.type)

    # return nombre de la variable
    p[0] = varname



#Agregar operador al stack
def p_x_add_op_to_stack(p):
    'x_add_op_to_stack :'
    #pushear el operador al stack de operador
    operator_stack.push(p[-1])

# Popea * / de la pila
def p_x_pop_MulD_of_stack(p):
    'x_pop_MulD_of_stack :'
    if(operator_stack.top() == '*' or operator_stack.top() == '/'):
        r = operands_stack.pop()
        l = operands_stack.pop()
        rt = types_stack.pop()
        lt = types_stack.pop()
        op = operator_stack.pop()
        ft = cube.type_check(lt,rt,op)

        if(ft!='error'):
            if (ft=='int'):
                result =  addr_manager.get_temp_int(1)
                current_function.temp_int_counter += 1
            elif (ft=='float'):
                result =  addr_manager.get_temp_float(1)
                current_function.temp_float_counter += 1
            else :
                result =  addr_manager.get_temp_string(1)
                current_function.temp_string_counter += 1

            quadruples.append(Quadruple(op,l,r,result))
            operands_stack.push(result)
            types_stack.push(ft)
        else:
            Error("Tipos no compartibles")

# Popea + - de la pila
def p_x_pop_PLUSM_of_stack(p):
    'x_pop_PLUSM_of_stack :'
    if(operator_stack.top() == '+' or operator_stack.top() == '-'):
        r = operands_stack.pop()
        l = operands_stack.pop()
        rt = types_stack.pop()
        lt = types_stack.pop()
        op = operator_stack.pop()
        ft = cube.type_check(lt,rt,op)


        if(ft!='error'):
            if (ft=='int'):
                result =  addr_manager.get_temp_int(1)
                current_function.temp_int_counter += 1
            elif (ft=='float'):
                result =  addr_manager.get_temp_float(1)
                current_function.temp_float_counter += 1
            else :
                result =  addr_manager.get_temp_string(1)
                current_function.temp_string_counter += 1

            quadruples.append(Quadruple(op,l,r,result))
            operands_stack.push(result)
            types_stack.push(ft)

        else:
            Error("Tipos no compartibles")

def p_x_assignment_op(p):
    'x_assignment_op :'
    if(operator_stack.top() == '='):
        r = operands_stack.pop()
        l = operands_stack.pop()
        rt = types_stack.pop()
        lt = types_stack.pop()
        op = operator_stack.pop()
        ft = cube.type_check(lt,rt,op)


        if(ft!='error'):
            #Para la asignacion se debe seguir el patron
            # = expresion None VaraAsignar
            quadruples.append(Quadruple(op,r,None,l))
        else:
            Error("Tipos no compartibles")

def p_x_comparison_op(p):
    'x_comparison_op :'
    if(operator_stack.top() in [">", "<", "!=","==", ">=", "<="]):
        r = operands_stack.pop()
        l = operands_stack.pop()
        rt = types_stack.pop()
        lt = types_stack.pop()
        op = operator_stack.pop()
        ft = cube.type_check(lt,rt,op)


        if(ft!='error'):
            if (ft=='int'):
                result =  addr_manager.get_temp_int(1)
                current_function.temp_int_counter += 1
            elif (ft=='float'):
                result =  addr_manager.get_temp_float(1)
                current_function.temp_float_counter += 1
            else:
                result =  addr_manager.get_temp_string(1)
                current_function.temp_string_counter += 1

            quadruples.append(Quadruple(op,l,r,result))
            operands_stack.push(result)
            types_stack.push(ft)
        else:
            Error("Tipos no compartibles")
            
def p_x_AND_op(p):
    'x_AND_op :'
    if operator_stack.top() == "&&":
        r = operands_stack.pop()
        l = operands_stack.pop()
        rt = types_stack.pop()
        lt = types_stack.pop()
        op = operator_stack.pop()
        ft = cube.type_check(lt,rt,op)


        if(ft!='error'):
            if (ft=='int'):
                result =  addr_manager.get_temp_int(1)
                current_function.temp_int_counter += 1

            elif (ft=='float'):
                result =  addr_manager.get_temp_float(1)
                current_function.temp_float_counter += 1

            else:
                result =  addr_manager.get_temp_string(1)
                current_function.temp_string_counter += 1

            
            quadruples.append(Quadruple(op,l,r,result))
            operands_stack.push(result)
            types_stack.push(ft)
        else:
            Error("Tipos no compartibles")

def p_x_OR_op(p):
    'x_OR_op :'

    if operator_stack.top() == "||":
        r = operands_stack.pop()
        l = operands_stack.pop()
        rt = types_stack.pop()
        lt = types_stack.pop()
        op = operator_stack.pop()
        ft = cube.type_check(lt,rt,op)


        if(ft!='error'):
            if (ft=='int'):
                result =  addr_manager.get_temp_int(1)
                current_function.temp_int_counter += 1
            elif (ft=='float'):
                result =  addr_manager.get_temp_float(1)
                current_function.temp_float_counter += 1
            else:
                result =  addr_manager.get_temp_string(1)
                current_function.temp_string_counter += 1

            
            quadruples.append(Quadruple(op,l,r,result))
            operands_stack.push(result)
            types_stack.push(ft)
        else:
            Error("Tipos no compartibles")

#quitar parentesis izquierdo del stack
def p_x_pop_Lpar_from_stack(p):
    'x_pop_Lpar_from_stack :'
      #popear el operador
    operator_stack.pop()


def p_x_end_if(p):
    'x_end_if :'
    # sacamos el salto
    end = jumps_stack.pop()
    q=quadruples[end]
    q.set_result(len(quadruples))


def p_x_else(p):
    'x_else :'
    quadruples.append(Quadruple("goto", None, None, None))
    false = jumps_stack.pop()
    jumps_stack.push(len(quadruples)-1)
    q=quadruples[false]
    q.set_result(len(quadruples))

def p_x_while_start(p):
    'x_while_start :'
    jumps_stack.push(len(quadruples))

def p_x_generate_gotoF(p):
    'x_generate_gotoF :'
    # revisar que la expresion sea int
    typecond = types_stack.pop()
    valuecond = operands_stack.pop()
    if typecond!= 'int':
        Error("Tipo de condición no válida")
        #guardar el cuadruplo con el salto
    quadruples.append(Quadruple("gotof", valuecond, None, None))
    jumps_stack.push(len(quadruples)-1)

def p_x_end_while(p):
    'x_end_while :'
    # sacamos el salto
    end = jumps_stack.pop()
    returnW= jumps_stack.pop()
    quadruples.append(Quadruple("goto", None, None, returnW))
    q=quadruples[end]
    q.set_result(len(quadruples))

def p_x_add_constant_arr_size(p):
    'x_add_constant_arr_size :'
    c = p[-1]
    if not constants_table.has_constant(c):
        a = addr_manager.get_const_int(1)
        constants_table.add_constant(c, a)


def p_x_add_constants_table_i(p):
    'x_add_constants_table_i :'
    c = p[-1]
    if not constants_table.has_constant(c):
        a = addr_manager.get_const_int(1)
        constants_table.add_constant(c, a)
    else:
        aux= constants_table.get_constant(c)
        a= aux.address
    operands_stack.push(a)
    types_stack.push('int')


def p_x_add_constants_table_f(p):
    'x_add_constants_table_f :'
    c = p[-1]
    if not constants_table.has_constant(c):
        a = addr_manager.get_const_float(1)
        constants_table.add_constant(c, a)
    else:
        aux= constants_table.get_constant(c)
        a= aux.address
    operands_stack.push(a)
    types_stack.push('float')

def p_x_add_constants_table_s(p):
    'x_add_constants_table_s :'
    c = p[-1]
    if not constants_table.has_constant(c):
        a = addr_manager.get_const_string(1)
        constants_table.add_constant(c, a)
    else:
        aux= constants_table.get_constant(c)
        a= aux.address
    operands_stack.push(a)
    types_stack.push('string')

def p_x_func_init_addr(p):
    'x_func_init_addr :'
    current_function.initial_address = len(quadruples)

def p_x_add_endfunc(p):
    'x_add_endfunc :'
    if(current_function_type!= "void" and not current_function_return):
     Error("La función no regresa ningún valor")
    quadruples.append(Quadruple('endfunc', None, None, None))

def p_x_verify_func(p):
    'x_verify_func :'
    if function_directory.has_function(p[-1]):
        global current_function_call_name
        global function_args_pointer
        function_args_pointer = 0
        current_function_call_name = p[-1]

        # se agrega el nombre al stack de llamadas
        call_stack.push(p[-1])
        quadruples.append(Quadruple('era', None, None, p[-1]))
    else:
        Error("Función no existe")

def p_x_check_parameters(p):
    'x_check_parameters :'
    global function_args_pointer
    argument= operands_stack.pop()
    argumentType= types_stack.pop()
    f = function_directory.search_function(current_function_call_name)
    if function_args_pointer >= len(f.signature):
        Error("Demasiados argumentos para llamada a funcion \"" + f.name + "\"")
    if f.signature[function_args_pointer] ==argumentType:
        p_a = f.params_addresses
        # address del parametro:
        addr = p_a[function_args_pointer]
        quadruples.append(Quadruple('parameter', argument, None, addr))
        function_args_pointer +=1
    else:
        Error("Tipos incompatibles en llamada a funcion \"" + f.name + "\"")

def p_x_points_null(p):
    'x_points_null :'
    f = function_directory.search_function(current_function_call_name)
    if not function_args_pointer >= len(f.signature):
        Error("Numero de argumentos inconsistente en llamada a funcion \"" + f.name + "\"")
    quadruples.append(Quadruple('gosub', current_function_call_name, None,f.initial_address))

def p_x_add_param(p):
    'x_add_param :'
    c= current_function.signature
    c.append(p[-1])
    p[0] = p[-1]

def p_x_print_expr(p):
    'x_print_expr :'
    quadruples.append(Quadruple('print', None, None,operands_stack.top()))
    operands_stack.pop()
    types_stack.pop()

def p_x_funcr_return(p):
    'x_funcr_return :'
    global current_function_return
    current_function_return = 1

    # asignar a la variable global de la funcion el ultimo operando
    global_func = function_directory.search_function(prog_name)
    global_vars_table = global_func.get_vars_table()

    global_var = global_vars_table.search_var(current_function.name)
    var_addr = global_var.address
    expr = operands_stack.top()
    q = Quadruple('=', expr, None, var_addr)
    quadruples.append(q)

    q2 = Quadruple('endfunc', None, None, None)
    quadruples.append(q2)

    #

    operands_stack.pop()
    types_stack.pop()

def p_x_funcr_return_void(p):
    'x_funcr_return_void :'
    # generar cuadruplo de endfunc para salirnos de la funcion inmediatamente
    q = Quadruple('endfunc', None, None, None)
    quadruples.append(q)


def p_x_set_is_array_1d(p):
    'x_set_is_array_1d :'
    var = current_vars_table.search_var(p[-1])
    var.is_array = 1



# TODO asignar bien todas las direcciones en arreglos y matrices

def p_x_array_get_addrs(p):
    'x_array_get_addrs :'
    # cuantos tiene el array
    n = current_var.first_len
    # type de la variable
    t = current_var.type
    t_func = current_function.type
    if t_func == 'program':
            # consumimos n - 1 locales porque ya se consumió 1 en la declaracion
        if t == 'int':
            addr_manager.get_global_int(n - 1)
            current_function.local_int_counter += n - 1
        elif t == 'float':
            addr_manager.get_global_float(n - 1)
            current_function.local_float_counter += n - 1
        elif t == 'string':
            addr_manager.get_global_string(n - 1)
            current_function.local_string_counter += n - 1
    else:
        # consumimos n - 1 locales porque ya se consumió 1 en la declaracion
        if t == 'int':
            addr_manager.get_local_int(n - 1)
            current_function.local_int_counter += n - 1
        elif t == 'float':
            addr_manager.get_local_float(n - 1)
            current_function.local_float_counter += n - 1
        elif t == 'string':
            addr_manager.get_local_string(n - 1)
            current_function.local_string_counter += n - 1


def p_x_matrix_get_addrs(p):
    'x_matrix_get_addrs :'
    # cuantos tiene la matriz
    n = current_var.first_len
    m = current_var.second_len
    # type de la variable
    t = current_var.type
    t_func = current_function.type

    if t_func == 'program':
    # consumimos n - 1 locales porque ya se consumió 1 en la declaracion
        if t == 'int':
            addr_manager.get_global_int(n * m - 1)
            current_function.local_int_counter += n * m - 1
        elif t == 'float':
            addr_manager.get_global_float(n * m - 1)
            current_function.local_float_counter += n * m - 1
        elif t == 'string':
            addr_manager.get_global_string(n * m - 1)
            current_function.local_string_counter += n * m - 1
    else:
            # consumimos n - 1 locales porque ya se consumió 1 en la declaracion
        if t == 'int':
            addr_manager.get_local_int(n - 1)
            current_function.local_int_counter += n * m- 1
        elif t == 'float':
            addr_manager.get_local_float(n - 1)
            current_function.local_float_counter += n * m - 1
        elif t == 'string':
            addr_manager.get_local_string(n - 1)
            current_function.local_string_counter += n * m - 1



def p_x_set_first_len(p):
    'x_set_first_len :'
    var = current_vars_table.search_var(current_var_name)
    var.first_len = p[-1]
    p[0] = p[-1]
    
def p_x_set_second_len(p):
    'x_set_second_len :'
    var = current_vars_table.search_var(current_var_name)
    var.second_len = p[-1]
    var.is_array = 2
    p[0] = p[-1]
    

def p_x_check_var_dimension_normal(p):
    'x_check_var_dimension_normal :'
    global current_var
    if current_var.is_array != 0:
        Error("Variable \'" + current_var.name + "\' es un arreglo")
    current_var = vars_stack.top()
    

def p_x_is_array(p):
    'x_is_array :'
    if current_var.is_array != 1:
        Error("Dimensiones de la variable \'" + current_var.name + "\' no coinciden") 


def p_x_check_first_bounds(p):
    'x_check_first_bounds :'
    # primero checar las dimensiones
    # por ejemplo tenemos variable B[1,2] y una expresion B[1]
    expr = operands_stack.top()
    expr_type = types_stack.top()
    # operands_stack.pop()
    # types_stack.pop()

    if expr_type != 'int':
        Error("Expresión dentro de indexación debe ser tipo int")

    # necesito la constante del tamano del array (primera dimension y segunda dimension)
    first_len = current_var.first_len
    constant_first_len = constants_table.get_constant(first_len)
    addr_first_len = constant_first_len.address
    
    # generar el cuadruplo de 'verify'

    q = Quadruple('verify', addr_first_len, None, expr)
    quadruples.append(q)


def p_x_check_second_bounds(p):
    'x_check_second_bounds :'
    # primero checar las dimensiones
    # por ejemplo tenemos variable B[1,2] y una expresion B[1]
    expr = operands_stack.top()
    expr_type = types_stack.top()
    # operands_stack.pop()
    # types_stack.pop()

    if expr_type != 'int':
        Error("Expresión dentro de indexación debe ser tipo int")

    # necesito la constante del tamano del array (primera dimension y segunda dimension)

    second_len = current_var.second_len
    constant_second_len = constants_table.get_constant(second_len)

    addr_second_len = constant_second_len.address
    # generar el cuadruplo de 'verify'

    q = Quadruple('verify', None, addr_second_len, expr)
    quadruples.append(q)


def p_x_end_matrix_bracket(p):
    'x_end_matrix_bracket :'
    # en este punto tenemos en el stack de operandos (Direcciones) lo siguiente:
    # [direccion_base,  fila, columna]
    # tenemos que hacer la formula fila * col_len + columna  + direccion base
    # o sea tenemos que hacer TRES cuadruplos + uno para verificar

    # pop dos veces al types stack, ya no necesitamos esos valores
    types_stack.pop()
    types_stack.pop()

    col_addr = operands_stack.pop()
    row_addr = operands_stack.pop()
    base_dir_addr = operands_stack.pop()
    curr_var_type = types_stack.pop()

    # obtener el address de num columas, es decir var.second_len
    col_len = current_var.second_len
    const = constants_table.get_constant(col_len)   
    col_len_addr = const.address

    # generar los cuadruplos
    a1 = addr_manager.get_temp_int(1)
    current_function.temp_int_counter += 1
    q1 = Quadruple('*', row_addr, col_len_addr, a1)

    a2 = addr_manager.get_temp_int(1)
    current_function.temp_int_counter += 1
    q2 = Quadruple('+', a1, col_addr, a2)

    # ahora el cuadruplo del offset
    res_addr = addr_manager.get_temp_int(1)
    current_function.temp_int_counter += 1
    operands_stack.push(('pointer', res_addr))
    types_stack.push(curr_var_type)
    q3 = Quadruple('address', base_dir_addr, a2, res_addr)
    quadruples.append(q1)
    quadruples.append(q2)
    quadruples.append(q3)

    operator_stack.pop()

def p_x_end_array_bracket(p):
    'x_end_array_bracket :'
    # primero checar las dimensiones
    # por ejemplo tenemos variable B[1,2] y una expresion B[1]

    expr = operands_stack.top()
    expr_type = types_stack.top()
    operands_stack.pop()
    types_stack.pop()

    # aqui se crea el cuadruplo para verificar que este en el rango del array

    # primero obtenemos el address de la constante del tamano del array


    curr_var_addr = operands_stack.pop()
    curr_var_type = types_stack.pop()
    # el address se guarda en un tuple para que la vm sepa que es una direccion
    # se le pone un temporal int al valor de esa direccion
    new_addr = addr_manager.get_temp_int(1)
    current_function.temp_int_counter += 1
    operands_stack.push(('pointer', new_addr))
    types_stack.push(curr_var_type)
    q = Quadruple('address', curr_var_addr, expr, new_addr)

    quadruples.append(q)
    operator_stack.pop()
    

def p_x_push_vars_stack(p):
    'x_push_vars_stack :'
    vars_stack.push(current_var)
    operator_stack.push('[')
    
def p_x_pop_vars_stack(p):
    'x_pop_vars_stack :'
    vars_stack.pop()
    global current_var
    current_var = vars_stack.top()


def p_x_check_first_dimension(p):
    'x_check_first_dimension :'
    if not current_var.is_array >= 1:
        # TODO mensaje de error
        Error("Variable \'" + current_var.name + "\' dimensiones no coinciden")


def p_x_check_second_dimension(p):
    'x_check_second_dimension :'
    global current_var
    current_var = vars_stack.top()
    if current_var.is_array != 2:
        # TODO mensaje de error
        Error("Variable \'" + current_var.name + "\' dimensiones no coinciden")

    # aqui tambien se checa que este en el rango 


def p_x_check_type_func(p):
    'x_check_type_func :'

    if current_function.type == 'void':
        Error("Funcion " + current_function.name + " es void y no puede regresar valores.")

    if current_function.type != types_stack.top():
        Error("El valor regresado no coincide con el indicado en la función.")

def p_x_check_void_func(p):
    'x_check_void_func :'
    if current_function.type != 'void':
        Error("Return en funcion tipo \'" + current_function.type + "\' debe retornar un valor.")

def p_x_goto_main(p):
    'x_goto_main :'

    # se pone la direccion del primer cuadruplo de main
    goto_main = jumps_stack.pop()
    q = quadruples[goto_main]
    q.set_result(len(quadruples))


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


# f = open("././tests/test6.txt")


# # correr un ejemplo 
# s = f.read()

# result = parser.parse(s)
# print(result)
