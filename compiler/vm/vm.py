

from operator import eq, add, sub, truediv, mul, ge, gt, le, lt, eq, ne, and_, or_, not_
from parser.tools.utils.stack import Stack
from parser.tools.semantics.quadruple import Quadruple
from parser.tools.utils.constants import * 
from parser.tools.error import Error

from .memory_segment import MemorySegment
from .execution_context import ExecutionContext
from parser.tools.semantics.function_directory import FunctionDirectory

class VirtualMachine:
    def __init__(self, func_dir, const_tab) -> None:
        # instruction pointer
        self.ip = 0
        self.function_directory = func_dir

        # la tabla de constantes es un diccionario
        self.constants_table = {}
        # se voltea la tabla de constantes
        for k in const_tab.table:
            self.constants_table[const_tab.table[k].address] = k
        
        global_func = func_dir.search_function(func_dir.program_name)

        global_int_count = global_func.local_int_counter
        global_float_count = global_func.local_float_counter
        global_string_count = global_func.local_string_counter
        global_object_attr_count = global_func.local_object_attr_counter
        global_temp_int_count = global_func.temp_int_counter 
        global_temp_float_count = global_func.temp_float_counter 
        global_temp_string_count = global_func.temp_string_counter 

        self.global_mem = MemorySegment(global_int_count,
                                        global_float_count, 
                                        global_string_count,
                                        global_object_attr_count,
                                        global_temp_int_count,
                                        global_temp_float_count,
                                        global_temp_string_count)

        self.execution_stack = Stack()
        self.current_memory = self.global_mem

    def get_value_from_address(self, addr):
        if isinstance(addr, tuple):
            addr = self.get_value_from_address(addr[1])

        # globales (locales)
        if addr >= GLOBAL_INT_START and addr < GLOBAL_INT_START + GLOBAL_INT_FREE:
            return self.global_mem.local_int[addr - GLOBAL_INT_START]
        elif addr >= GLOBAL_FLOAT_START and addr < GLOBAL_FLOAT_START + GLOBAL_FLOAT_FREE:
            return self.global_mem.local_float[addr - GLOBAL_FLOAT_START]
        elif addr >= GLOBAL_STRING_START and addr < GLOBAL_STRING_START + GLOBAL_STRING_FREE:
            return self.global_mem.local_string[addr - GLOBAL_STRING_START]

        # globales objetos
        if addr >= GLOBAL_OBJECT_START and addr < GLOBAL_OBJECT_START + GLOBAL_OBJECT_FREE:
            return self.global_mem.local_obj_attr[addr - GLOBAL_OBJECT_START]

        # locales objetos
        if addr >= LOCAL_OBJECT_START and addr < LOCAL_OBJECT_START + LOCAL_OBJECT_FREE:
            return self.current_memory.local_obj_attr[addr - LOCAL_OBJECT_START]

        # locales
        if addr >= LOCAL_INT_START and addr < LOCAL_INT_START + LOCAL_INT_FREE:
            return self.current_memory.local_int[addr - LOCAL_INT_START]
        elif addr >= LOCAL_FLOAT_START and addr < LOCAL_FLOAT_START + LOCAL_FLOAT_FREE:
            return self.current_memory.local_float[addr - LOCAL_FLOAT_START]
        elif addr >= LOCAL_STRING_START and addr < LOCAL_STRING_START + LOCAL_STRING_FREE:
            return self.current_memory.local_string[addr - LOCAL_STRING_START]

        # temporales locales
        if addr >= TEMP_INT_START and addr < TEMP_INT_START + TEMP_INT_FREE:
            return self.current_memory.temp_int[addr - TEMP_INT_START]
        elif addr >= TEMP_FLOAT_START and addr < TEMP_FLOAT_START + TEMP_FLOAT_FREE:
            return self.current_memory.temp_float[addr - TEMP_FLOAT_START]
        elif addr >= TEMP_STRING_START and addr < TEMP_STRING_START + TEMP_STRING_FREE:
            return self.current_memory.temp_string[addr - TEMP_STRING_START]


        # constantes
        if addr >= CONST_INT_START and addr < CONST_STRING_START + CONST_STRING_FREE:
            return self.constants_table[addr]
    

    def set_value_in_address(self, val, addr):
        if isinstance(addr, tuple):
            addr = self.get_value_from_address(addr[1])

        # globales 
        if addr >= GLOBAL_INT_START and addr < GLOBAL_INT_START + GLOBAL_INT_FREE:
            self.global_mem.local_int[addr - GLOBAL_INT_START] = int(val)
        elif addr >= GLOBAL_FLOAT_START and addr < GLOBAL_FLOAT_START + GLOBAL_FLOAT_FREE:
            self.global_mem.local_float[addr - GLOBAL_FLOAT_START] = float(val)
        elif addr >= GLOBAL_STRING_START and addr < GLOBAL_STRING_START + GLOBAL_STRING_FREE:
            self.global_mem.local_string[addr - GLOBAL_STRING_START] = val

        # globales objetos
        if addr >= GLOBAL_OBJECT_START and addr < GLOBAL_OBJECT_START + GLOBAL_OBJECT_FREE:
            self.global_mem.local_obj_attr[addr - GLOBAL_OBJECT_START] = val
        
        # locales objetos
        if addr >= LOCAL_OBJECT_START and addr < LOCAL_OBJECT_START + LOCAL_OBJECT_FREE:
            self.current_memory.local_obj_attr[addr - LOCAL_OBJECT_START] = val



        # locales
        if addr >= LOCAL_INT_START and addr < LOCAL_INT_START + LOCAL_INT_FREE:
            self.current_memory.local_int[addr - LOCAL_INT_START] = int(val)
        elif addr >= LOCAL_FLOAT_START and addr < LOCAL_FLOAT_START + LOCAL_FLOAT_FREE:
            self.current_memory.local_float[addr - LOCAL_FLOAT_START] = float(val)
        elif addr >= LOCAL_STRING_START and addr < LOCAL_STRING_START + LOCAL_STRING_FREE:
            self.current_memory.local_string[addr - LOCAL_STRING_START] = val

        # current_mem

        # temporales locales
        if addr >= TEMP_INT_START and addr < TEMP_INT_START + TEMP_INT_FREE:
            self.current_memory.temp_int[addr - TEMP_INT_START] = int(val)
        elif addr >= TEMP_FLOAT_START and addr < TEMP_FLOAT_START + TEMP_FLOAT_FREE:
            self.current_memory.temp_float[addr - TEMP_FLOAT_START] = float(val)
        elif addr >= TEMP_STRING_START and addr < TEMP_STRING_START + TEMP_STRING_FREE:
            self.current_memory.temp_string[addr - TEMP_STRING_START] = val

        
        # constantes


    def binary_operation(self, l, r, op):
        left = self.get_value_from_address(l)
        right = self.get_value_from_address(r)
    
        if op == truediv:
            if right == 0:
                Error("Division de cero.") 

        res = op(left, right)

        if op == and_:
            res = left and right
        if op == or_:
            res = left or right

        return res


    def exec(self, quadruples):
        n = len(quadruples)

        # mientras haya cuadruplos por ejecutar
        while self.ip < n:

            # si hay mas de 5000 llamadas en el stack, error
            if self.execution_stack.size() >= 5000:
                Error("Execution Stack overflow")

            quad = quadruples[self.ip]
            if quad.op == '+':
                result = self.binary_operation(quad.left, quad.right, add)
                self.set_value_in_address(result, quad.result)
                self.ip += 1

            elif quad.op == '-':
                result = self.binary_operation(quad.left, quad.right, sub)
                self.set_value_in_address(result, quad.result)
                self.ip += 1

            elif quad.op == '*':
                result = self.binary_operation(quad.left, quad.right, mul)
                self.set_value_in_address(result, quad.result)
                self.ip += 1

            elif quad.op == '/':
                result = self.binary_operation(quad.left, quad.right, truediv)
                self.set_value_in_address(result, quad.result)
                self.ip += 1

            elif quad.op == '=':
                left = self.get_value_from_address(quad.left)
                self.set_value_in_address(left, quad.result)
                self.ip += 1

            elif quad.op == '>':
                result = self.binary_operation(quad.left, quad.right, gt)
                self.set_value_in_address(result, quad.result)
                self.ip += 1

            elif quad.op == '>=':
                result = self.binary_operation(quad.left, quad.right, ge)
                self.set_value_in_address(result, quad.result)
                self.ip += 1

            elif quad.op == '<':
                result = self.binary_operation(quad.left, quad.right, lt)
                self.set_value_in_address(result, quad.result)
                self.ip += 1

            elif quad.op == '<=':
                result = self.binary_operation(quad.left, quad.right, le)
                self.set_value_in_address(result, quad.result)
                self.ip += 1

            elif quad.op == '!=':
                result = self.binary_operation(quad.left, quad.right, ne)
                self.set_value_in_address(result, quad.result)
                self.ip += 1
            elif quad.op == '==':
                result = self.binary_operation(quad.left, quad.right, eq)
                self.set_value_in_address(result, quad.result)
                self.ip += 1

            elif quad.op == '&&':
                result = self.binary_operation(quad.left, quad.right, and_)
                self.set_value_in_address(result, quad.result)
                self.ip += 1

            elif quad.op == '||':
                result = self.binary_operation(quad.left, quad.right, or_)
                self.set_value_in_address(result, quad.result)
                self.ip += 1

            elif quad.op == '!':
                val = not self.get_value_from_address(quad.right)
                
                self.set_value_in_address(val, quad.result)
                self.ip += 1

            elif quad.op == 'print':
                val = self.get_value_from_address(quad.result)
                if val == "\\n":
                    print()
                else:
                    print(val, end="")
                self.ip += 1
            
            elif quad.op == 'input':
                if quad.left == 'string':
                    quad.left = 'str'

                val = input()
                try:
                    val = eval(quad.left)(val)
                except ValueError:
                    Error("Type de input incompatible con la variable")
                
                self.set_value_in_address(eval(quad.left)(val), quad.result)
                self.ip += 1

            elif quad.op == 'goto':
                self.ip = quad.result

            elif quad.op == 'gotof':
                condition = self.get_value_from_address(quad.left)
                if not condition:
                    self.ip = quad.result
                else:
                    self.ip += 1
    
            elif quad.op == 'verify':
                expr_val = self.get_value_from_address(quad.result)
                if quad.left != None:
                    len_val = self.get_value_from_address(quad.left)
                else:
                    len_val = self.get_value_from_address(quad.right)

                if expr_val < 0 or expr_val >= len_val:
                    Error("Acceso incorrecto a valor de arreglo")
                
                self.ip += 1
            elif quad.op == 'address':
                val = self.get_value_from_address(quad.right)
                self.set_value_in_address(quad.left + val, quad.result)
                self.ip += 1
            
            elif quad.op == 'era':
                
                func_name = quad.result

                func = self.function_directory.search_function(func_name)

                # obtener contabilizacion de variables en funcioj
                ti = func.temp_int_counter
                tf = func.temp_float_counter
                ts = func.temp_string_counter
                li = func.local_int_counter
                lf = func.local_float_counter
                ls = func.local_string_counter
                loa = func.local_object_attr_counter

                # crear memoria
                # pero sin actualizar la memoria actual
                # esa se va a actualizar

                new_mem = MemorySegment(li, lf, ls, loa, ti, tf, ts)

                self.execution_stack.push(new_mem)

                self.ip += 1

            elif quad.op == 'parameter':
                new_mem = self.execution_stack.top()

                val = self.get_value_from_address(quad.left)

                # en este punto tenemos '3' memorias 'activas'

                # global, actual, y la nueva (est?? en top de stack)

                # asignar el val a la nueva memoria
                # Unicamente revisar las locales, ya que los parametros siempre son variables locales
                addr = quad.result

                if addr >= LOCAL_INT_START and addr < LOCAL_INT_START + LOCAL_INT_FREE:
                    new_mem.local_int[addr - LOCAL_INT_START] = int(val)
                elif addr >= LOCAL_FLOAT_START and addr < LOCAL_FLOAT_START + LOCAL_FLOAT_FREE:
                    new_mem.local_float[addr - LOCAL_FLOAT_START] = float(val)
                elif addr >= LOCAL_STRING_START and addr < LOCAL_STRING_START + LOCAL_STRING_FREE:
                    new_mem.local_string[addr - LOCAL_STRING_START] = val
 
                self.ip += 1

            elif quad.op == 'gosub':

                # se crea el contexto de la memoria actual, junto con el ip + 1
                old_exec_ctx = ExecutionContext(self.current_memory, self.ip + 1)

                # la actual ahora es la 'nueva' que se encontraba en el top del stack, se hace pop
                self.current_memory = self.execution_stack.pop()

                # se guarda en el stack la vieja
                self.execution_stack.push(old_exec_ctx)

                # mover el ip al primer cuadruplo de la nueva funcion llamada
                self.ip = quad.result
            

            elif quad.op == 'endfunc':

                # se 'mata' la memoria actual
                # y guardamos el top del stack
                exec_ctx = self.execution_stack.pop()

                # se actualiza el ip y la actual
                self.ip = exec_ctx.address
                self.current_memory = exec_ctx.memory

            elif quad.op == 'endprogram':
                exit()


        
        # print("global mem", self.global_mem.__dict__)


 
