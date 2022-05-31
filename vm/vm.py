from fcntl import F_GET_SEALS
from sre_parse import GLOBAL_FLAGS
from ..parser.tools.utils.stack import Stack
from ..parser.tools.semantics.quadruple import Quadruple


from memory_segment import MemorySegment
from parser.tools.semantics.function_directory import FunctionDirectory

class VirtualMachine:
    def __init__(self, func_dir, const_tab) -> None:
        # instruction pointer
        self.function_directory = func_dir
        self.constants_table = const_tab
        self.ip = 0

        global_int_count = self.function_directory.local_int_counter
        global_float_count = self.function_directory.local_float_counter
        global_string_count = self.function_directory.local_string_counter

        self.global_mem = MemorySegment(global_int_count,
                                        global_float_count, 
                                        global_string_count)

        self.stack_segment = Stack()

    def exec(self, quadruples):
        n = len(quadruples)
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


 
