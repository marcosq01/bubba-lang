# Generated from bubbaGrammar.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\63")
        buf.write("\u0135\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t")
        buf.write("\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r")
        buf.write("\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23")
        buf.write("\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\35")
        buf.write("\3\35\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3\"\3\"")
        buf.write("\3\"\3#\3#\3#\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3&\3&\3&\3")
        buf.write("&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3)")
        buf.write("\3)\3)\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3")
        buf.write(",\3,\3,\3,\3,\3,\3-\3-\3-\3.\3.\3/\3/\3\60\3\60\7\60\u010d")
        buf.write("\n\60\f\60\16\60\u0110\13\60\3\60\3\60\3\61\3\61\7\61")
        buf.write("\u0116\n\61\f\61\16\61\u0119\13\61\6\61\u011b\n\61\r\61")
        buf.write("\16\61\u011c\3\62\6\62\u0120\n\62\r\62\16\62\u0121\3\63")
        buf.write("\6\63\u0125\n\63\r\63\16\63\u0126\3\63\3\63\6\63\u012b")
        buf.write("\n\63\r\63\16\63\u012c\3\64\6\64\u0130\n\64\r\64\16\64")
        buf.write("\u0131\3\64\3\64\2\2\65\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[\2]\2_/a\60c\61e")
        buf.write("\62g\63\3\2\6\3\2\62;\4\2C\\c|\7\2GGQQSSVW``\5\2\13\f")
        buf.write("\17\17\"\"\2\u0139\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2")
        buf.write("_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2")
        buf.write("\3i\3\2\2\2\5n\3\2\2\2\7s\3\2\2\2\ty\3\2\2\2\13}\3\2\2")
        buf.write("\2\r\u0084\3\2\2\2\17\u008a\3\2\2\2\21\u008f\3\2\2\2\23")
        buf.write("\u0092\3\2\2\2\25\u0097\3\2\2\2\27\u0099\3\2\2\2\31\u009b")
        buf.write("\3\2\2\2\33\u009d\3\2\2\2\35\u009f\3\2\2\2\37\u00a1\3")
        buf.write("\2\2\2!\u00a3\3\2\2\2#\u00a5\3\2\2\2%\u00a7\3\2\2\2\'")
        buf.write("\u00a9\3\2\2\2)\u00ab\3\2\2\2+\u00ad\3\2\2\2-\u00af\3")
        buf.write("\2\2\2/\u00b1\3\2\2\2\61\u00b3\3\2\2\2\63\u00b6\3\2\2")
        buf.write("\2\65\u00b8\3\2\2\2\67\u00bb\3\2\2\29\u00bd\3\2\2\2;\u00bf")
        buf.write("\3\2\2\2=\u00c1\3\2\2\2?\u00c4\3\2\2\2A\u00c7\3\2\2\2")
        buf.write("C\u00c9\3\2\2\2E\u00cc\3\2\2\2G\u00cf\3\2\2\2I\u00d5\3")
        buf.write("\2\2\2K\u00d9\3\2\2\2M\u00de\3\2\2\2O\u00e5\3\2\2\2Q\u00eb")
        buf.write("\3\2\2\2S\u00f3\3\2\2\2U\u00f8\3\2\2\2W\u00fd\3\2\2\2")
        buf.write("Y\u0103\3\2\2\2[\u0106\3\2\2\2]\u0108\3\2\2\2_\u010a\3")
        buf.write("\2\2\2a\u011a\3\2\2\2c\u011f\3\2\2\2e\u0124\3\2\2\2g\u012f")
        buf.write("\3\2\2\2ij\7r\2\2jk\7t\2\2kl\7q\2\2lm\7i\2\2m\4\3\2\2")
        buf.write("\2no\7o\2\2op\7c\2\2pq\7k\2\2qr\7p\2\2r\6\3\2\2\2st\7")
        buf.write("h\2\2tu\7n\2\2uv\7q\2\2vw\7c\2\2wx\7v\2\2x\b\3\2\2\2y")
        buf.write("z\7k\2\2z{\7p\2\2{|\7v\2\2|\n\3\2\2\2}~\7u\2\2~\177\7")
        buf.write("v\2\2\177\u0080\7t\2\2\u0080\u0081\7k\2\2\u0081\u0082")
        buf.write("\7p\2\2\u0082\u0083\7i\2\2\u0083\f\3\2\2\2\u0084\u0085")
        buf.write("\7r\2\2\u0085\u0086\7t\2\2\u0086\u0087\7k\2\2\u0087\u0088")
        buf.write("\7p\2\2\u0088\u0089\7v\2\2\u0089\16\3\2\2\2\u008a\u008b")
        buf.write("\7x\2\2\u008b\u008c\7c\2\2\u008c\u008d\7t\2\2\u008d\u008e")
        buf.write("\7u\2\2\u008e\20\3\2\2\2\u008f\u0090\7k\2\2\u0090\u0091")
        buf.write("\7h\2\2\u0091\22\3\2\2\2\u0092\u0093\7g\2\2\u0093\u0094")
        buf.write("\7n\2\2\u0094\u0095\7u\2\2\u0095\u0096\7g\2\2\u0096\24")
        buf.write("\3\2\2\2\u0097\u0098\7\60\2\2\u0098\26\3\2\2\2\u0099\u009a")
        buf.write("\7.\2\2\u009a\30\3\2\2\2\u009b\u009c\7*\2\2\u009c\32\3")
        buf.write("\2\2\2\u009d\u009e\7+\2\2\u009e\34\3\2\2\2\u009f\u00a0")
        buf.write("\7}\2\2\u00a0\36\3\2\2\2\u00a1\u00a2\7\177\2\2\u00a2 ")
        buf.write("\3\2\2\2\u00a3\u00a4\7]\2\2\u00a4\"\3\2\2\2\u00a5\u00a6")
        buf.write("\7_\2\2\u00a6$\3\2\2\2\u00a7\u00a8\7=\2\2\u00a8&\3\2\2")
        buf.write("\2\u00a9\u00aa\7-\2\2\u00aa(\3\2\2\2\u00ab\u00ac\7/\2")
        buf.write("\2\u00ac*\3\2\2\2\u00ad\u00ae\7,\2\2\u00ae,\3\2\2\2\u00af")
        buf.write("\u00b0\7\61\2\2\u00b0.\3\2\2\2\u00b1\u00b2\7@\2\2\u00b2")
        buf.write("\60\3\2\2\2\u00b3\u00b4\7@\2\2\u00b4\u00b5\7?\2\2\u00b5")
        buf.write("\62\3\2\2\2\u00b6\u00b7\7>\2\2\u00b7\64\3\2\2\2\u00b8")
        buf.write("\u00b9\7>\2\2\u00b9\u00ba\7?\2\2\u00ba\66\3\2\2\2\u00bb")
        buf.write("\u00bc\7?\2\2\u00bc8\3\2\2\2\u00bd\u00be\7<\2\2\u00be")
        buf.write(":\3\2\2\2\u00bf\u00c0\7$\2\2\u00c0<\3\2\2\2\u00c1\u00c2")
        buf.write("\7(\2\2\u00c2\u00c3\7(\2\2\u00c3>\3\2\2\2\u00c4\u00c5")
        buf.write("\7~\2\2\u00c5\u00c6\7~\2\2\u00c6@\3\2\2\2\u00c7\u00c8")
        buf.write("\7#\2\2\u00c8B\3\2\2\2\u00c9\u00ca\7?\2\2\u00ca\u00cb")
        buf.write("\7?\2\2\u00cbD\3\2\2\2\u00cc\u00cd\7#\2\2\u00cd\u00ce")
        buf.write("\7?\2\2\u00ceF\3\2\2\2\u00cf\u00d0\7y\2\2\u00d0\u00d1")
        buf.write("\7j\2\2\u00d1\u00d2\7k\2\2\u00d2\u00d3\7n\2\2\u00d3\u00d4")
        buf.write("\7g\2\2\u00d4H\3\2\2\2\u00d5\u00d6\7h\2\2\u00d6\u00d7")
        buf.write("\7q\2\2\u00d7\u00d8\7t\2\2\u00d8J\3\2\2\2\u00d9\u00da")
        buf.write("\7u\2\2\u00da\u00db\7v\2\2\u00db\u00dc\7g\2\2\u00dc\u00dd")
        buf.write("\7r\2\2\u00ddL\3\2\2\2\u00de\u00df\7t\2\2\u00df\u00e0")
        buf.write("\7g\2\2\u00e0\u00e1\7v\2\2\u00e1\u00e2\7w\2\2\u00e2\u00e3")
        buf.write("\7t\2\2\u00e3\u00e4\7p\2\2\u00e4N\3\2\2\2\u00e5\u00e6")
        buf.write("\7e\2\2\u00e6\u00e7\7n\2\2\u00e7\u00e8\7c\2\2\u00e8\u00e9")
        buf.write("\7u\2\2\u00e9\u00ea\7u\2\2\u00eaP\3\2\2\2\u00eb\u00ec")
        buf.write("\7g\2\2\u00ec\u00ed\7z\2\2\u00ed\u00ee\7v\2\2\u00ee\u00ef")
        buf.write("\7g\2\2\u00ef\u00f0\7p\2\2\u00f0\u00f1\7f\2\2\u00f1\u00f2")
        buf.write("\7u\2\2\u00f2R\3\2\2\2\u00f3\u00f4\7h\2\2\u00f4\u00f5")
        buf.write("\7w\2\2\u00f5\u00f6\7p\2\2\u00f6\u00f7\7e\2\2\u00f7T\3")
        buf.write("\2\2\2\u00f8\u00f9\7x\2\2\u00f9\u00fa\7q\2\2\u00fa\u00fb")
        buf.write("\7k\2\2\u00fb\u00fc\7f\2\2\u00fcV\3\2\2\2\u00fd\u00fe")
        buf.write("\7k\2\2\u00fe\u00ff\7p\2\2\u00ff\u0100\7r\2\2\u0100\u0101")
        buf.write("\7w\2\2\u0101\u0102\7v\2\2\u0102X\3\2\2\2\u0103\u0104")
        buf.write("\7v\2\2\u0104\u0105\7q\2\2\u0105Z\3\2\2\2\u0106\u0107")
        buf.write("\t\2\2\2\u0107\\\3\2\2\2\u0108\u0109\t\3\2\2\u0109^\3")
        buf.write("\2\2\2\u010a\u010e\5;\36\2\u010b\u010d\t\4\2\2\u010c\u010b")
        buf.write("\3\2\2\2\u010d\u0110\3\2\2\2\u010e\u010c\3\2\2\2\u010e")
        buf.write("\u010f\3\2\2\2\u010f\u0111\3\2\2\2\u0110\u010e\3\2\2\2")
        buf.write("\u0111\u0112\5;\36\2\u0112`\3\2\2\2\u0113\u0117\5]/\2")
        buf.write("\u0114\u0116\5[.\2\u0115\u0114\3\2\2\2\u0116\u0119\3\2")
        buf.write("\2\2\u0117\u0115\3\2\2\2\u0117\u0118\3\2\2\2\u0118\u011b")
        buf.write("\3\2\2\2\u0119\u0117\3\2\2\2\u011a\u0113\3\2\2\2\u011b")
        buf.write("\u011c\3\2\2\2\u011c\u011a\3\2\2\2\u011c\u011d\3\2\2\2")
        buf.write("\u011db\3\2\2\2\u011e\u0120\5[.\2\u011f\u011e\3\2\2\2")
        buf.write("\u0120\u0121\3\2\2\2\u0121\u011f\3\2\2\2\u0121\u0122\3")
        buf.write("\2\2\2\u0122d\3\2\2\2\u0123\u0125\5[.\2\u0124\u0123\3")
        buf.write("\2\2\2\u0125\u0126\3\2\2\2\u0126\u0124\3\2\2\2\u0126\u0127")
        buf.write("\3\2\2\2\u0127\u0128\3\2\2\2\u0128\u012a\5\25\13\2\u0129")
        buf.write("\u012b\5[.\2\u012a\u0129\3\2\2\2\u012b\u012c\3\2\2\2\u012c")
        buf.write("\u012a\3\2\2\2\u012c\u012d\3\2\2\2\u012df\3\2\2\2\u012e")
        buf.write("\u0130\t\5\2\2\u012f\u012e\3\2\2\2\u0130\u0131\3\2\2\2")
        buf.write("\u0131\u012f\3\2\2\2\u0131\u0132\3\2\2\2\u0132\u0133\3")
        buf.write("\2\2\2\u0133\u0134\b\64\2\2\u0134h\3\2\2\2\n\2\u010e\u0117")
        buf.write("\u011c\u0121\u0126\u012c\u0131\3\b\2\2")
        return buf.getvalue()


class bubbaGrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PROG = 1
    MAIN = 2
    FLOAT = 3
    INT = 4
    STRING = 5
    PRINT = 6
    VARS = 7
    IF = 8
    ELSE = 9
    DOT = 10
    COMMA = 11
    LPARENTHESIS = 12
    RPARENTHESIS = 13
    LBRACE = 14
    RBRACE = 15
    LBRACKET = 16
    RBRACKET = 17
    SEMICOLON = 18
    ADD = 19
    MINUS = 20
    STAR = 21
    SLASH = 22
    GREATER = 23
    GREATEREQ = 24
    LESS = 25
    LESSEQ = 26
    EQUAL = 27
    COLON = 28
    QUOTE = 29
    AND = 30
    OR = 31
    NOT = 32
    EQEQUAL = 33
    NOTEQUAL = 34
    WHILE = 35
    FOR = 36
    STEP = 37
    RETURN = 38
    CLASS = 39
    EXTENDS = 40
    FUNC = 41
    VOID = 42
    INPUT = 43
    TO = 44
    V_STRING = 45
    ID = 46
    V_INT = 47
    V_FLOAT = 48
    WS = 49

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'prog'", "'main'", "'float'", "'int'", "'string'", "'print'", 
            "'vars'", "'if'", "'else'", "'.'", "','", "'('", "')'", "'{'", 
            "'}'", "'['", "']'", "';'", "'+'", "'-'", "'*'", "'/'", "'>'", 
            "'>='", "'<'", "'<='", "'='", "':'", "'\"'", "'&&'", "'||'", 
            "'!'", "'=='", "'!='", "'while'", "'for'", "'step'", "'return'", 
            "'class'", "'extends'", "'func'", "'void'", "'input'", "'to'" ]

    symbolicNames = [ "<INVALID>",
            "PROG", "MAIN", "FLOAT", "INT", "STRING", "PRINT", "VARS", "IF", 
            "ELSE", "DOT", "COMMA", "LPARENTHESIS", "RPARENTHESIS", "LBRACE", 
            "RBRACE", "LBRACKET", "RBRACKET", "SEMICOLON", "ADD", "MINUS", 
            "STAR", "SLASH", "GREATER", "GREATEREQ", "LESS", "LESSEQ", "EQUAL", 
            "COLON", "QUOTE", "AND", "OR", "NOT", "EQEQUAL", "NOTEQUAL", 
            "WHILE", "FOR", "STEP", "RETURN", "CLASS", "EXTENDS", "FUNC", 
            "VOID", "INPUT", "TO", "V_STRING", "ID", "V_INT", "V_FLOAT", 
            "WS" ]

    ruleNames = [ "PROG", "MAIN", "FLOAT", "INT", "STRING", "PRINT", "VARS", 
                  "IF", "ELSE", "DOT", "COMMA", "LPARENTHESIS", "RPARENTHESIS", 
                  "LBRACE", "RBRACE", "LBRACKET", "RBRACKET", "SEMICOLON", 
                  "ADD", "MINUS", "STAR", "SLASH", "GREATER", "GREATEREQ", 
                  "LESS", "LESSEQ", "EQUAL", "COLON", "QUOTE", "AND", "OR", 
                  "NOT", "EQEQUAL", "NOTEQUAL", "WHILE", "FOR", "STEP", 
                  "RETURN", "CLASS", "EXTENDS", "FUNC", "VOID", "INPUT", 
                  "TO", "DIGIT", "LETTER", "V_STRING", "ID", "V_INT", "V_FLOAT", 
                  "WS" ]

    grammarFileName = "bubbaGrammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


