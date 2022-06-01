from parser.tools.utils.stack import Stack
from parser.tools.semantics.quadruple import Quadruple

from .memory_segment import MemorySegment
from parser.tools.semantics.function_directory import FunctionDirectory

class VirtualMachine:
    def __init__(self, func_dir, const_tab, program_name) -> None:
        # instruction pointer
        self.ip = 0
        self.function_directory = func_dir
        self.constants_table = const_tab
        
        global_func = func_dir.search_function(func_dir.program_name)

        global_int_count = global_func.local_int_counter
        global_float_count = global_func.local_float_counter
        global_string_count = global_func.local_string_counter
        print(global_int_count)
        self.global_mem = MemorySegment(global_int_count,
                                        global_float_count, 
                                        global_string_count)

        print(self.global_mem.__dict__)
        self.stack_segment = Stack()

    def exec(self, quadruples):
        n = len(quadruples)

        # mientras haya cuadruplos por ejecutar
        while self.ip < n:
            quad = quadruples[self.ip]
            if quad.op == '+':
                pass
            elif quad.op == '-':
                pass
            elif quad.op == '*':
                pass
            elif quad.op == '/':
                pass
            elif quad.op == '=':
                pass
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
            elif quad.op == '=':
                pass
            elif quad.op == '&&':
                pass
            elif quad.op == '||':
                pass
            elif quad.op == 'goto':
                self.ip = quad.result


 
