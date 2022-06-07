from fileinput import filename
from parser.parser import parser, function_directory, constants_table, quadruples 
import sys
from vm.vm import VirtualMachine

class Bubba:
    def __init__(self) -> None:
        pass

    def run(self, source_code):
        parser.parse(source_code)
        vm = VirtualMachine(function_directory, constants_table)
        vm.exec(quadruples)

if __name__ == '__main__':

    bubba = Bubba()

    file_name = str(sys.argv[1])
    f = open('./' + file_name)
    s = f.read()

    bubba.run(s)
