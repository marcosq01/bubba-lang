

from operator import eq, add, sub, truediv, mul
from parser.tools.utils.stack import Stack
from parser.tools.semantics.quadruple import Quadruple
from parser.tools.utils.constants import * 
from parser.tools.error import Error

from .memory_segment import MemorySegment
from parser.tools.semantics.function_directory import FunctionDirectory

class VirtualMachine:
    def __init__(self, func_dir, const_tab) -> None:
        # instruction pointer
        self.ip = 0
        self.function_directory = func_dir
        self.constants_table = {}

        # se voltea la tabla de constantes
        for k in const_tab.table:
            self.constants_table[const_tab.table[k].address] = k
        
        global_func = func_dir.search_function(func_dir.program_name)

        global_int_count = global_func.local_int_counter
        global_float_count = global_func.local_float_counter
        global_string_count = global_func.local_string_counter
        global_temp_int_count = global_func.temp_int_counter 
        global_temp_float_count = global_func.temp_float_counter 
        global_temp_string_count = global_func.temp_string_counter 

        self.global_mem = MemorySegment(global_int_count,
                                        global_float_count, 
                                        global_string_count,
                                        global_temp_int_count,
                                        global_temp_float_count,
                                        global_temp_string_count)

        self.stack_segment = Stack()
        self.current_memory = None

    def get_value_from_address(self, addr):

        # globales 
        if addr >= GLOBAL_INT_START and addr < GLOBAL_INT_START + GLOBAL_INT_FREE:
            return self.global_mem.local_int[addr - GLOBAL_INT_START]
        elif addr >= GLOBAL_FLOAT_START and addr < GLOBAL_FLOAT_START + GLOBAL_FLOAT_FREE:
            return self.global_mem.local_float[addr - GLOBAL_FLOAT_START]
        elif addr >= GLOBAL_STRING_START and addr < GLOBAL_STRING_START + GLOBAL_STRING_FREE:
            return self.global_mem.local_string[addr - GLOBAL_STRING_START]

        # locales


        # temporales globales
        if addr >= TEMP_INT_START and addr < TEMP_INT_START + TEMP_INT_FREE:
            return self.global_mem.temp_int[addr - TEMP_INT_START]
        elif addr >= TEMP_FLOAT_START and addr < TEMP_FLOAT_START +TEMP_FLOAT_FREE:
            return self.global_mem.temp_float[addr - TEMP_FLOAT_START]
        elif addr >= TEMP_STRING_START and addr < TEMP_STRING_START + TEMP_STRING_FREE:
            return self.global_mem.temp_string[addr - TEMP_STRING_START]

        # temporales locales

        # constantes
        if addr >= CONST_INT_START and addr < CONST_STRING_START + CONST_STRING_FREE:
            return self.constants_table[addr]
    

    def set_value_in_address(self, val, addr):
        # globales 
        if addr >= GLOBAL_INT_START and addr < GLOBAL_INT_START + GLOBAL_INT_FREE:
            self.global_mem.local_int[addr - GLOBAL_INT_START] = int(val)
        elif addr >= GLOBAL_FLOAT_START and addr < GLOBAL_FLOAT_START + GLOBAL_FLOAT_FREE:
            self.global_mem.local_float[addr - GLOBAL_FLOAT_START] = float(val)
        elif addr >= GLOBAL_STRING_START and addr < GLOBAL_STRING_START + GLOBAL_STRING_FREE:
            self.global_mem.local_string[addr - GLOBAL_STRING_START] = val

        # locales


        # temporales globales
        if addr >= TEMP_INT_START and addr < TEMP_INT_START + TEMP_INT_FREE:
            self.global_mem.temp_int[addr - TEMP_INT_START] = int(val)
        elif addr >= TEMP_FLOAT_START and addr < TEMP_FLOAT_START +TEMP_FLOAT_FREE:
            self.global_mem.temp_float[addr - TEMP_FLOAT_START] = float(val)
        elif addr >= TEMP_STRING_START and addr < TEMP_STRING_START + TEMP_STRING_FREE:
            self.global_mem.temp_string[addr - TEMP_STRING_START] = val

        # temporales locales

        # constantes


    def binary_operation(self, l, r, op):
        left = self.get_value_from_address(l)
        right = self.get_value_from_address(r)
    
        if op == truediv:
            if right == 0:
                Error("Division de cero.") 

        return op(left, right)


    def exec(self, quadruples):
        n = len(quadruples)

        # mientras haya cuadruplos por ejecutar
        while self.ip < n:
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
                pass
            elif quad.op == '>=':
                pass
            elif quad.op == '<':
                pass
            elif quad.op == '<=':
                pass
            elif quad.op == '!=':
                pass
            elif quad.op == '&&':
                pass
            elif quad.op == '||':
                pass
            elif quad.op == 'print':
                val = self.get_value_from_address(quad.result)
                print(val)
                self.ip += 1
            elif quad.op == 'goto':
                self.ip = quad.result
        
        print(self.global_mem.__dict__)


 
