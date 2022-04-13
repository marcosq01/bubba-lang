#!/usr/bin/env python3
import sys
from antlr4 import *
from bubbaGrammarParser import bubbaGrammarParser
from bubbaGrammarLexer import bubbaGrammarLexer
from bubbaGrammarListener import bubbaGrammarListener

import sys


def main():
    listTests = ["test.txt","test2.txt","test3.txt", "test4.txt", "test5.txt"]
    for x in listTests:
        print( '\n'+ x +' Errors:\n')
        parser = bubbaGrammarParser(CommonTokenStream(bubbaGrammarLexer(FileStream(x))))
        tree = parser.program()
    
        bubbaCode = bubbaGrammarListener()
        walker = ParseTreeWalker()
        walker.walk(bubbaCode, tree)


      


if __name__ == '__main__':
    main()
