from numpy import source
from parser.parser import parser, function_directory, constants_table, quadruples 
from vm.vm import VirtualMachine

class Bubba:
    def __init__(self) -> None:
        pass

    def run(self, source_code):
        parser.parse(source_code)
        vm = VirtualMachine(function_directory, constants_table)


if __name__ == '__main__':

    bubba = Bubba()

    f = open('./tests/test6.txt')
    s = f.read()

    bubba.run(s)
