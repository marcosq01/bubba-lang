# Generated from bubbaGrammar.g4 by ANTLR 4.9
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\65")
        buf.write("\u01f9\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3")
        buf.write("\3\5\3\u0097\n\3\3\4\3\4\5\4\u009b\n\4\3\5\3\5\3\5\3\5")
        buf.write("\5\5\u00a1\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\5\t\u00b7\n\t")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\f\3\f")
        buf.write("\3\f\5\f\u00c7\n\f\3\r\3\r\3\r\3\16\3\16\5\16\u00ce\n")
        buf.write("\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00d7\n\17")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\5\22\u00e4\n\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5")
        buf.write("\23\u00ed\n\23\3\24\3\24\3\24\5\24\u00f2\n\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\27")
        buf.write("\3\27\5\27\u0102\n\27\3\30\3\30\3\30\3\30\3\30\3\31\3")
        buf.write("\31\3\31\3\31\3\32\3\32\3\32\3\32\5\32\u0111\n\32\3\33")
        buf.write("\3\33\3\33\3\34\3\34\3\34\5\34\u0119\n\34\3\35\3\35\3")
        buf.write("\35\3\35\3\35\3\35\3\35\3\35\5\35\u0123\n\35\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u012d\n\36\3\37\3")
        buf.write("\37\3\37\5\37\u0132\n\37\3 \3 \3 \3!\3!\3!\3!\3!\5!\u013c")
        buf.write("\n!\3\"\3\"\3\"\3#\3#\3#\3#\3#\5#\u0146\n#\3$\3$\3$\3")
        buf.write("%\3%\3%\3%\5%\u014f\n%\3&\3&\3\'\3\'\3\'\3(\3(\3(\5(\u0159")
        buf.write("\n(\3)\3)\3)\3*\3*\3*\5*\u0161\n*\3+\3+\3+\3+\3+\3+\3")
        buf.write("+\3+\3+\3+\3+\3+\3+\3,\3,\5,\u0172\n,\3-\3-\3-\3-\3-\3")
        buf.write("-\3-\3-\3-\3.\3.\3.\5.\u0180\n.\3/\3/\5/\u0184\n/\3\60")
        buf.write("\3\60\3\60\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61")
        buf.write("\5\61\u0192\n\61\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3")
        buf.write("\63\3\63\3\63\3\63\5\63\u019f\n\63\3\64\3\64\3\64\3\64")
        buf.write("\3\65\3\65\5\65\u01a7\n\65\3\66\3\66\3\66\3\66\5\66\u01ad")
        buf.write("\n\66\3\67\3\67\3\67\3\67\3\67\3\67\38\38\58\u01b7\n8")
        buf.write("\39\39\59\u01bb\n9\3:\3:\3:\3:\3:\3;\3;\3;\5;\u01c5\n")
        buf.write(";\3<\3<\3=\3=\3=\3=\3=\3=\3=\3>\3>\3>\5>\u01d3\n>\3?\3")
        buf.write("?\5?\u01d7\n?\3@\3@\3@\3A\3A\3A\5A\u01df\nA\3B\3B\3C\3")
        buf.write("C\3C\3C\3C\3C\3C\3C\3C\3C\3D\3D\5D\u01ef\nD\3E\3E\3E\3")
        buf.write("E\3E\3E\5E\u01f7\nE\3E\2\2F\2\4\6\b\n\f\16\20\22\24\26")
        buf.write("\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\")
        buf.write("^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086\u0088\2\6\3")
        buf.write("\2\60\61\4\2\31\34#$\3\2\5\7\4\2//\61\62\2\u01e3\2\u008a")
        buf.write("\3\2\2\2\4\u0096\3\2\2\2\6\u009a\3\2\2\2\b\u00a0\3\2\2")
        buf.write("\2\n\u00a2\3\2\2\2\f\u00a9\3\2\2\2\16\u00b1\3\2\2\2\20")
        buf.write("\u00b6\3\2\2\2\22\u00b8\3\2\2\2\24\u00c1\3\2\2\2\26\u00c6")
        buf.write("\3\2\2\2\30\u00c8\3\2\2\2\32\u00cd\3\2\2\2\34\u00d6\3")
        buf.write("\2\2\2\36\u00d8\3\2\2\2 \u00dc\3\2\2\2\"\u00e3\3\2\2\2")
        buf.write("$\u00ec\3\2\2\2&\u00f1\3\2\2\2(\u00f3\3\2\2\2*\u00fc\3")
        buf.write("\2\2\2,\u0101\3\2\2\2.\u0103\3\2\2\2\60\u0108\3\2\2\2")
        buf.write("\62\u0110\3\2\2\2\64\u0112\3\2\2\2\66\u0118\3\2\2\28\u0122")
        buf.write("\3\2\2\2:\u012c\3\2\2\2<\u0131\3\2\2\2>\u0133\3\2\2\2")
        buf.write("@\u013b\3\2\2\2B\u013d\3\2\2\2D\u0145\3\2\2\2F\u0147\3")
        buf.write("\2\2\2H\u014e\3\2\2\2J\u0150\3\2\2\2L\u0152\3\2\2\2N\u0158")
        buf.write("\3\2\2\2P\u015a\3\2\2\2R\u0160\3\2\2\2T\u0162\3\2\2\2")
        buf.write("V\u0171\3\2\2\2X\u0173\3\2\2\2Z\u017f\3\2\2\2\\\u0183")
        buf.write("\3\2\2\2^\u0185\3\2\2\2`\u0191\3\2\2\2b\u0193\3\2\2\2")
        buf.write("d\u019e\3\2\2\2f\u01a0\3\2\2\2h\u01a6\3\2\2\2j\u01ac\3")
        buf.write("\2\2\2l\u01ae\3\2\2\2n\u01b6\3\2\2\2p\u01ba\3\2\2\2r\u01bc")
        buf.write("\3\2\2\2t\u01c4\3\2\2\2v\u01c6\3\2\2\2x\u01c8\3\2\2\2")
        buf.write("z\u01d2\3\2\2\2|\u01d6\3\2\2\2~\u01d8\3\2\2\2\u0080\u01de")
        buf.write("\3\2\2\2\u0082\u01e0\3\2\2\2\u0084\u01e2\3\2\2\2\u0086")
        buf.write("\u01ee\3\2\2\2\u0088\u01f6\3\2\2\2\u008a\u008b\7\3\2\2")
        buf.write("\u008b\u008c\7\60\2\2\u008c\u008d\7\36\2\2\u008d\u008e")
        buf.write("\5\4\3\2\u008e\u008f\5\6\4\2\u008f\u0090\5\b\5\2\u0090")
        buf.write("\u0091\5\n\6\2\u0091\3\3\2\2\2\u0092\u0093\5X-\2\u0093")
        buf.write("\u0094\5\4\3\2\u0094\u0097\3\2\2\2\u0095\u0097\3\2\2\2")
        buf.write("\u0096\u0092\3\2\2\2\u0096\u0095\3\2\2\2\u0097\5\3\2\2")
        buf.write("\2\u0098\u009b\5l\67\2\u0099\u009b\3\2\2\2\u009a\u0098")
        buf.write("\3\2\2\2\u009a\u0099\3\2\2\2\u009b\7\3\2\2\2\u009c\u009d")
        buf.write("\5\u0088E\2\u009d\u009e\5\b\5\2\u009e\u00a1\3\2\2\2\u009f")
        buf.write("\u00a1\3\2\2\2\u00a0\u009c\3\2\2\2\u00a0\u009f\3\2\2\2")
        buf.write("\u00a1\t\3\2\2\2\u00a2\u00a3\7\4\2\2\u00a3\u00a4\7\16")
        buf.write("\2\2\u00a4\u00a5\7\17\2\2\u00a5\u00a6\7\20\2\2\u00a6\u00a7")
        buf.write("\5f\64\2\u00a7\u00a8\7\21\2\2\u00a8\13\3\2\2\2\u00a9\u00aa")
        buf.write("\7%\2\2\u00aa\u00ab\7\16\2\2\u00ab\u00ac\5P)\2\u00ac\u00ad")
        buf.write("\7\17\2\2\u00ad\u00ae\7\20\2\2\u00ae\u00af\5\16\b\2\u00af")
        buf.write("\u00b0\7\21\2\2\u00b0\r\3\2\2\2\u00b1\u00b2\5\34\17\2")
        buf.write("\u00b2\u00b3\5\20\t\2\u00b3\17\3\2\2\2\u00b4\u00b7\5\16")
        buf.write("\b\2\u00b5\u00b7\3\2\2\2\u00b6\u00b4\3\2\2\2\u00b6\u00b5")
        buf.write("\3\2\2\2\u00b7\21\3\2\2\2\u00b8\u00b9\7&\2\2\u00b9\u00ba")
        buf.write("\5\24\13\2\u00ba\u00bb\7.\2\2\u00bb\u00bc\5\24\13\2\u00bc")
        buf.write("\u00bd\5\26\f\2\u00bd\u00be\7\20\2\2\u00be\u00bf\5\30")
        buf.write("\r\2\u00bf\u00c0\7\21\2\2\u00c0\23\3\2\2\2\u00c1\u00c2")
        buf.write("\t\2\2\2\u00c2\25\3\2\2\2\u00c3\u00c4\7\'\2\2\u00c4\u00c7")
        buf.write("\5\24\13\2\u00c5\u00c7\3\2\2\2\u00c6\u00c3\3\2\2\2\u00c6")
        buf.write("\u00c5\3\2\2\2\u00c7\27\3\2\2\2\u00c8\u00c9\5\34\17\2")
        buf.write("\u00c9\u00ca\5\32\16\2\u00ca\31\3\2\2\2\u00cb\u00ce\5")
        buf.write("\30\r\2\u00cc\u00ce\3\2\2\2\u00cd\u00cb\3\2\2\2\u00cd")
        buf.write("\u00cc\3\2\2\2\u00ce\33\3\2\2\2\u00cf\u00d7\5\60\31\2")
        buf.write("\u00d0\u00d7\5x=\2\u00d1\u00d7\5(\25\2\u00d2\u00d7\5\22")
        buf.write("\n\2\u00d3\u00d7\5\f\7\2\u00d4\u00d7\5^\60\2\u00d5\u00d7")
        buf.write("\5b\62\2\u00d6\u00cf\3\2\2\2\u00d6\u00d0\3\2\2\2\u00d6")
        buf.write("\u00d1\3\2\2\2\u00d6\u00d2\3\2\2\2\u00d6\u00d3\3\2\2\2")
        buf.write("\u00d6\u00d4\3\2\2\2\u00d6\u00d5\3\2\2\2\u00d7\35\3\2")
        buf.write("\2\2\u00d8\u00d9\7\60\2\2\u00d9\u00da\5 \21\2\u00da\u00db")
        buf.write("\7\24\2\2\u00db\37\3\2\2\2\u00dc\u00dd\5\"\22\2\u00dd")
        buf.write("\u00de\5$\23\2\u00de!\3\2\2\2\u00df\u00e0\7\r\2\2\u00e0")
        buf.write("\u00e1\7\60\2\2\u00e1\u00e4\5\"\22\2\u00e2\u00e4\3\2\2")
        buf.write("\2\u00e3\u00df\3\2\2\2\u00e3\u00e2\3\2\2\2\u00e4#\3\2")
        buf.write("\2\2\u00e5\u00e6\7\22\2\2\u00e6\u00e7\7\61\2\2\u00e7\u00e8")
        buf.write("\5&\24\2\u00e8\u00e9\7\23\2\2\u00e9\u00ea\5\"\22\2\u00ea")
        buf.write("\u00ed\3\2\2\2\u00eb\u00ed\3\2\2\2\u00ec\u00e5\3\2\2\2")
        buf.write("\u00ec\u00eb\3\2\2\2\u00ed%\3\2\2\2\u00ee\u00ef\7\r\2")
        buf.write("\2\u00ef\u00f2\7\61\2\2\u00f0\u00f2\3\2\2\2\u00f1\u00ee")
        buf.write("\3\2\2\2\u00f1\u00f0\3\2\2\2\u00f2\'\3\2\2\2\u00f3\u00f4")
        buf.write("\7\n\2\2\u00f4\u00f5\7\16\2\2\u00f5\u00f6\5P)\2\u00f6")
        buf.write("\u00f7\7\17\2\2\u00f7\u00f8\7\20\2\2\u00f8\u00f9\5*\26")
        buf.write("\2\u00f9\u00fa\7\21\2\2\u00fa\u00fb\5.\30\2\u00fb)\3\2")
        buf.write("\2\2\u00fc\u00fd\5\34\17\2\u00fd\u00fe\5,\27\2\u00fe+")
        buf.write("\3\2\2\2\u00ff\u0102\5*\26\2\u0100\u0102\3\2\2\2\u0101")
        buf.write("\u00ff\3\2\2\2\u0101\u0100\3\2\2\2\u0102-\3\2\2\2\u0103")
        buf.write("\u0104\7\13\2\2\u0104\u0105\7\20\2\2\u0105\u0106\5*\26")
        buf.write("\2\u0106\u0107\7\21\2\2\u0107/\3\2\2\2\u0108\u0109\5\62")
        buf.write("\32\2\u0109\u010a\7\35\2\2\u010a\u010b\5P)\2\u010b\61")
        buf.write("\3\2\2\2\u010c\u010d\7\60\2\2\u010d\u010e\7\f\2\2\u010e")
        buf.write("\u0111\7\60\2\2\u010f\u0111\7\60\2\2\u0110\u010c\3\2\2")
        buf.write("\2\u0110\u010f\3\2\2\2\u0111\63\3\2\2\2\u0112\u0113\5")
        buf.write("\66\34\2\u0113\u0114\58\35\2\u0114\65\3\2\2\2\u0115\u0119")
        buf.write("\7\25\2\2\u0116\u0119\7\26\2\2\u0117\u0119\3\2\2\2\u0118")
        buf.write("\u0115\3\2\2\2\u0118\u0116\3\2\2\2\u0118\u0117\3\2\2\2")
        buf.write("\u0119\67\3\2\2\2\u011a\u0123\5\u0082B\2\u011b\u0123\5")
        buf.write("x=\2\u011c\u011d\7\16\2\2\u011d\u011e\5P)\2\u011e\u011f")
        buf.write("\7\17\2\2\u011f\u0123\3\2\2\2\u0120\u0121\7\60\2\2\u0121")
        buf.write("\u0123\5:\36\2\u0122\u011a\3\2\2\2\u0122\u011b\3\2\2\2")
        buf.write("\u0122\u011c\3\2\2\2\u0122\u0120\3\2\2\2\u01239\3\2\2")
        buf.write("\2\u0124\u0125\7\22\2\2\u0125\u0126\5P)\2\u0126\u0127")
        buf.write("\5<\37\2\u0127\u0128\7\23\2\2\u0128\u012d\3\2\2\2\u0129")
        buf.write("\u012a\7\f\2\2\u012a\u012d\7\60\2\2\u012b\u012d\3\2\2")
        buf.write("\2\u012c\u0124\3\2\2\2\u012c\u0129\3\2\2\2\u012c\u012b")
        buf.write("\3\2\2\2\u012d;\3\2\2\2\u012e\u012f\7\r\2\2\u012f\u0132")
        buf.write("\5P)\2\u0130\u0132\3\2\2\2\u0131\u012e\3\2\2\2\u0131\u0130")
        buf.write("\3\2\2\2\u0132=\3\2\2\2\u0133\u0134\5\64\33\2\u0134\u0135")
        buf.write("\5@!\2\u0135?\3\2\2\2\u0136\u0137\7\27\2\2\u0137\u013c")
        buf.write("\5> \2\u0138\u0139\7\30\2\2\u0139\u013c\5> \2\u013a\u013c")
        buf.write("\3\2\2\2\u013b\u0136\3\2\2\2\u013b\u0138\3\2\2\2\u013b")
        buf.write("\u013a\3\2\2\2\u013cA\3\2\2\2\u013d\u013e\5> \2\u013e")
        buf.write("\u013f\5D#\2\u013fC\3\2\2\2\u0140\u0141\7\25\2\2\u0141")
        buf.write("\u0146\5B\"\2\u0142\u0143\7\26\2\2\u0143\u0146\5B\"\2")
        buf.write("\u0144\u0146\3\2\2\2\u0145\u0140\3\2\2\2\u0145\u0142\3")
        buf.write("\2\2\2\u0145\u0144\3\2\2\2\u0146E\3\2\2\2\u0147\u0148")
        buf.write("\5B\"\2\u0148\u0149\5H%\2\u0149G\3\2\2\2\u014a\u014b\5")
        buf.write("J&\2\u014b\u014c\5B\"\2\u014c\u014f\3\2\2\2\u014d\u014f")
        buf.write("\3\2\2\2\u014e\u014a\3\2\2\2\u014e\u014d\3\2\2\2\u014f")
        buf.write("I\3\2\2\2\u0150\u0151\t\3\2\2\u0151K\3\2\2\2\u0152\u0153")
        buf.write("\5F$\2\u0153\u0154\5N(\2\u0154M\3\2\2\2\u0155\u0156\7")
        buf.write(" \2\2\u0156\u0159\5L\'\2\u0157\u0159\3\2\2\2\u0158\u0155")
        buf.write("\3\2\2\2\u0158\u0157\3\2\2\2\u0159O\3\2\2\2\u015a\u015b")
        buf.write("\5L\'\2\u015b\u015c\5R*\2\u015cQ\3\2\2\2\u015d\u015e\7")
        buf.write("!\2\2\u015e\u0161\5P)\2\u015f\u0161\3\2\2\2\u0160\u015d")
        buf.write("\3\2\2\2\u0160\u015f\3\2\2\2\u0161S\3\2\2\2\u0162\u0163")
        buf.write("\7+\2\2\u0163\u0164\5v<\2\u0164\u0165\7\60\2\2\u0165\u0166")
        buf.write("\7\16\2\2\u0166\u0167\5V,\2\u0167\u0168\7\17\2\2\u0168")
        buf.write("\u0169\7\20\2\2\u0169\u016a\5f\64\2\u016a\u016b\7(\2\2")
        buf.write("\u016b\u016c\5P)\2\u016c\u016d\7\24\2\2\u016d\u016e\7")
        buf.write("\21\2\2\u016eU\3\2\2\2\u016f\u0172\5r:\2\u0170\u0172\3")
        buf.write("\2\2\2\u0171\u016f\3\2\2\2\u0171\u0170\3\2\2\2\u0172W")
        buf.write("\3\2\2\2\u0173\u0174\7)\2\2\u0174\u0175\7\60\2\2\u0175")
        buf.write("\u0176\5Z.\2\u0176\u0177\7\20\2\2\u0177\u0178\5l\67\2")
        buf.write("\u0178\u0179\5\\/\2\u0179\u017a\7\21\2\2\u017a\u017b\7")
        buf.write("\24\2\2\u017bY\3\2\2\2\u017c\u017d\7*\2\2\u017d\u0180")
        buf.write("\7\60\2\2\u017e\u0180\3\2\2\2\u017f\u017c\3\2\2\2\u017f")
        buf.write("\u017e\3\2\2\2\u0180[\3\2\2\2\u0181\u0184\5\u0088E\2\u0182")
        buf.write("\u0184\3\2\2\2\u0183\u0181\3\2\2\2\u0183\u0182\3\2\2\2")
        buf.write("\u0184]\3\2\2\2\u0185\u0186\7\b\2\2\u0186\u0187\7\16\2")
        buf.write("\2\u0187\u0188\5P)\2\u0188\u0189\5`\61\2\u0189\u018a\7")
        buf.write("\17\2\2\u018a\u018b\7\24\2\2\u018b_\3\2\2\2\u018c\u018d")
        buf.write("\7\r\2\2\u018d\u018e\5P)\2\u018e\u018f\5`\61\2\u018f\u0192")
        buf.write("\3\2\2\2\u0190\u0192\3\2\2\2\u0191\u018c\3\2\2\2\u0191")
        buf.write("\u0190\3\2\2\2\u0192a\3\2\2\2\u0193\u0194\7-\2\2\u0194")
        buf.write("\u0195\7\16\2\2\u0195\u0196\7\60\2\2\u0196\u0197\5d\63")
        buf.write("\2\u0197\u0198\7\17\2\2\u0198\u0199\7\24\2\2\u0199c\3")
        buf.write("\2\2\2\u019a\u019b\7\r\2\2\u019b\u019c\7\60\2\2\u019c")
        buf.write("\u019f\5d\63\2\u019d\u019f\3\2\2\2\u019e\u019a\3\2\2\2")
        buf.write("\u019e\u019d\3\2\2\2\u019fe\3\2\2\2\u01a0\u01a1\5h\65")
        buf.write("\2\u01a1\u01a2\5\34\17\2\u01a2\u01a3\5j\66\2\u01a3g\3")
        buf.write("\2\2\2\u01a4\u01a7\5l\67\2\u01a5\u01a7\3\2\2\2\u01a6\u01a4")
        buf.write("\3\2\2\2\u01a6\u01a5\3\2\2\2\u01a7i\3\2\2\2\u01a8\u01a9")
        buf.write("\5\34\17\2\u01a9\u01aa\5j\66\2\u01aa\u01ad\3\2\2\2\u01ab")
        buf.write("\u01ad\3\2\2\2\u01ac\u01a8\3\2\2\2\u01ac\u01ab\3\2\2\2")
        buf.write("\u01adk\3\2\2\2\u01ae\u01af\7\t\2\2\u01af\u01b0\5n8\2")
        buf.write("\u01b0\u01b1\7\36\2\2\u01b1\u01b2\5\36\20\2\u01b2\u01b3")
        buf.write("\5p9\2\u01b3m\3\2\2\2\u01b4\u01b7\7\60\2\2\u01b5\u01b7")
        buf.write("\5v<\2\u01b6\u01b4\3\2\2\2\u01b6\u01b5\3\2\2\2\u01b7o")
        buf.write("\3\2\2\2\u01b8\u01bb\5l\67\2\u01b9\u01bb\3\2\2\2\u01ba")
        buf.write("\u01b8\3\2\2\2\u01ba\u01b9\3\2\2\2\u01bbq\3\2\2\2\u01bc")
        buf.write("\u01bd\5v<\2\u01bd\u01be\7\36\2\2\u01be\u01bf\7\60\2\2")
        buf.write("\u01bf\u01c0\5t;\2\u01c0s\3\2\2\2\u01c1\u01c2\7\r\2\2")
        buf.write("\u01c2\u01c5\5r:\2\u01c3\u01c5\3\2\2\2\u01c4\u01c1\3\2")
        buf.write("\2\2\u01c4\u01c3\3\2\2\2\u01c5u\3\2\2\2\u01c6\u01c7\t")
        buf.write("\4\2\2\u01c7w\3\2\2\2\u01c8\u01c9\7\60\2\2\u01c9\u01ca")
        buf.write("\5z>\2\u01ca\u01cb\7\16\2\2\u01cb\u01cc\5|?\2\u01cc\u01cd")
        buf.write("\7\17\2\2\u01cd\u01ce\7\24\2\2\u01cey\3\2\2\2\u01cf\u01d0")
        buf.write("\7\f\2\2\u01d0\u01d3\7\60\2\2\u01d1\u01d3\3\2\2\2\u01d2")
        buf.write("\u01cf\3\2\2\2\u01d2\u01d1\3\2\2\2\u01d3{\3\2\2\2\u01d4")
        buf.write("\u01d7\5~@\2\u01d5\u01d7\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d6")
        buf.write("\u01d5\3\2\2\2\u01d7}\3\2\2\2\u01d8\u01d9\5P)\2\u01d9")
        buf.write("\u01da\5\u0080A\2\u01da\177\3\2\2\2\u01db\u01dc\7\r\2")
        buf.write("\2\u01dc\u01df\5~@\2\u01dd\u01df\3\2\2\2\u01de\u01db\3")
        buf.write("\2\2\2\u01de\u01dd\3\2\2\2\u01df\u0081\3\2\2\2\u01e0\u01e1")
        buf.write("\t\5\2\2\u01e1\u0083\3\2\2\2\u01e2\u01e3\7+\2\2\u01e3")
        buf.write("\u01e4\7,\2\2\u01e4\u01e5\7\60\2\2\u01e5\u01e6\7\16\2")
        buf.write("\2\u01e6\u01e7\5\u0086D\2\u01e7\u01e8\7\17\2\2\u01e8\u01e9")
        buf.write("\7\20\2\2\u01e9\u01ea\5f\64\2\u01ea\u01eb\7\21\2\2\u01eb")
        buf.write("\u0085\3\2\2\2\u01ec\u01ef\5r:\2\u01ed\u01ef\3\2\2\2\u01ee")
        buf.write("\u01ec\3\2\2\2\u01ee\u01ed\3\2\2\2\u01ef\u0087\3\2\2\2")
        buf.write("\u01f0\u01f1\5\u0084C\2\u01f1\u01f2\5\u0088E\2\u01f2\u01f7")
        buf.write("\3\2\2\2\u01f3\u01f4\5T+\2\u01f4\u01f5\5\u0088E\2\u01f5")
        buf.write("\u01f7\3\2\2\2\u01f6\u01f0\3\2\2\2\u01f6\u01f3\3\2\2\2")
        buf.write("\u01f7\u0089\3\2\2\2&\u0096\u009a\u00a0\u00b6\u00c6\u00cd")
        buf.write("\u00d6\u00e3\u00ec\u00f1\u0101\u0110\u0118\u0122\u012c")
        buf.write("\u0131\u013b\u0145\u014e\u0158\u0160\u0171\u017f\u0183")
        buf.write("\u0191\u019e\u01a6\u01ac\u01b6\u01ba\u01c4\u01d2\u01d6")
        buf.write("\u01de\u01ee\u01f6")
        return buf.getvalue()


class bubbaGrammarParser ( Parser ):

    grammarFileName = "bubbaGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'prog'", "'main'", "'float'", "'int'", 
                     "'string'", "'print'", "'vars'", "'if'", "'else'", 
                     "'.'", "','", "'('", "')'", "'{'", "'}'", "'['", "']'", 
                     "';'", "'+'", "'-'", "'*'", "'/'", "'>'", "'>='", "'<'", 
                     "'<='", "'='", "':'", "'\"'", "'&&'", "'||'", "'!'", 
                     "'=='", "'!='", "'while'", "'for'", "'step'", "'return'", 
                     "'class'", "'extends'", "'func'", "'void'", "'input'", 
                     "'to'" ]

    symbolicNames = [ "<INVALID>", "PROG", "MAIN", "FLOAT", "INT", "STRING", 
                      "PRINT", "VARS", "IF", "ELSE", "DOT", "COMMA", "LPARENTHESIS", 
                      "RPARENTHESIS", "LBRACE", "RBRACE", "LBRACKET", "RBRACKET", 
                      "SEMICOLON", "ADD", "MINUS", "STAR", "SLASH", "GREATER", 
                      "GREATEREQ", "LESS", "LESSEQ", "EQUAL", "COLON", "QUOTE", 
                      "AND", "OR", "NOT", "EQEQUAL", "NOTEQUAL", "WHILE", 
                      "FOR", "STEP", "RETURN", "CLASS", "EXTENDS", "FUNC", 
                      "VOID", "INPUT", "TO", "V_STRING", "ID", "V_INT", 
                      "V_FLOAT", "WS", "COMMENT", "LINE_COMMENT" ]

    RULE_program = 0
    RULE_paux = 1
    RULE_paux2 = 2
    RULE_paux3 = 3
    RULE_main = 4
    RULE_whiler = 5
    RULE_whileaux = 6
    RULE_whileaux2 = 7
    RULE_forr = 8
    RULE_foraux = 9
    RULE_foraux2 = 10
    RULE_foraux3 = 11
    RULE_foraux4 = 12
    RULE_statement = 13
    RULE_lid = 14
    RULE_lidaux = 15
    RULE_laux = 16
    RULE_laux2 = 17
    RULE_maux = 18
    RULE_cond = 19
    RULE_condaux = 20
    RULE_condaux2 = 21
    RULE_condaux3 = 22
    RULE_assign = 23
    RULE_assignaux = 24
    RULE_factor = 25
    RULE_faux = 26
    RULE_faux2 = 27
    RULE_faux3 = 28
    RULE_faux4 = 29
    RULE_term = 30
    RULE_termaux = 31
    RULE_exp = 32
    RULE_expaux = 33
    RULE_aexp = 34
    RULE_aexpaux = 35
    RULE_aexps = 36
    RULE_bexp = 37
    RULE_bexpaux = 38
    RULE_expression = 39
    RULE_expressionaux = 40
    RULE_func = 41
    RULE_funcaux = 42
    RULE_classr = 43
    RULE_class_a = 44
    RULE_class_b = 45
    RULE_output = 46
    RULE_output_a = 47
    RULE_inputr = 48
    RULE_input_a = 49
    RULE_body = 50
    RULE_body_a = 51
    RULE_body_b = 52
    RULE_varsr = 53
    RULE_vars_a = 54
    RULE_vars_b = 55
    RULE_args = 56
    RULE_args_a = 57
    RULE_type_simple = 58
    RULE_call = 59
    RULE_call_a = 60
    RULE_call_b = 61
    RULE_params = 62
    RULE_params_a = 63
    RULE_var_cte = 64
    RULE_void = 65
    RULE_void_a = 66
    RULE_methods = 67

    ruleNames =  [ "program", "paux", "paux2", "paux3", "main", "whiler", 
                   "whileaux", "whileaux2", "forr", "foraux", "foraux2", 
                   "foraux3", "foraux4", "statement", "lid", "lidaux", "laux", 
                   "laux2", "maux", "cond", "condaux", "condaux2", "condaux3", 
                   "assign", "assignaux", "factor", "faux", "faux2", "faux3", 
                   "faux4", "term", "termaux", "exp", "expaux", "aexp", 
                   "aexpaux", "aexps", "bexp", "bexpaux", "expression", 
                   "expressionaux", "func", "funcaux", "classr", "class_a", 
                   "class_b", "output", "output_a", "inputr", "input_a", 
                   "body", "body_a", "body_b", "varsr", "vars_a", "vars_b", 
                   "args", "args_a", "type_simple", "call", "call_a", "call_b", 
                   "params", "params_a", "var_cte", "void", "void_a", "methods" ]

    EOF = Token.EOF
    PROG=1
    MAIN=2
    FLOAT=3
    INT=4
    STRING=5
    PRINT=6
    VARS=7
    IF=8
    ELSE=9
    DOT=10
    COMMA=11
    LPARENTHESIS=12
    RPARENTHESIS=13
    LBRACE=14
    RBRACE=15
    LBRACKET=16
    RBRACKET=17
    SEMICOLON=18
    ADD=19
    MINUS=20
    STAR=21
    SLASH=22
    GREATER=23
    GREATEREQ=24
    LESS=25
    LESSEQ=26
    EQUAL=27
    COLON=28
    QUOTE=29
    AND=30
    OR=31
    NOT=32
    EQEQUAL=33
    NOTEQUAL=34
    WHILE=35
    FOR=36
    STEP=37
    RETURN=38
    CLASS=39
    EXTENDS=40
    FUNC=41
    VOID=42
    INPUT=43
    TO=44
    V_STRING=45
    ID=46
    V_INT=47
    V_FLOAT=48
    WS=49
    COMMENT=50
    LINE_COMMENT=51

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROG(self):
            return self.getToken(bubbaGrammarParser.PROG, 0)

        def ID(self):
            return self.getToken(bubbaGrammarParser.ID, 0)

        def COLON(self):
            return self.getToken(bubbaGrammarParser.COLON, 0)

        def paux(self):
            return self.getTypedRuleContext(bubbaGrammarParser.PauxContext,0)


        def paux2(self):
            return self.getTypedRuleContext(bubbaGrammarParser.Paux2Context,0)


        def paux3(self):
            return self.getTypedRuleContext(bubbaGrammarParser.Paux3Context,0)


        def main(self):
            return self.getTypedRuleContext(bubbaGrammarParser.MainContext,0)


        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = bubbaGrammarParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(bubbaGrammarParser.PROG)
            self.state = 137
            self.match(bubbaGrammarParser.ID)
            self.state = 138
            self.match(bubbaGrammarParser.COLON)
            self.state = 139
            self.paux()
            self.state = 140
            self.paux2()
            self.state = 141
            self.paux3()
            self.state = 142
            self.main()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PauxContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classr(self):
            return self.getTypedRuleContext(bubbaGrammarParser.ClassrContext,0)


        def paux(self):
            return self.getTypedRuleContext(bubbaGrammarParser.PauxContext,0)


        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_paux

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPaux" ):
                listener.enterPaux(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPaux" ):
                listener.exitPaux(self)




    def paux(self):

        localctx = bubbaGrammarParser.PauxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_paux)
        try:
            self.state = 148
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [bubbaGrammarParser.CLASS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 144
                self.classr()
                self.state = 145
                self.paux()
                pass
            elif token in [bubbaGrammarParser.MAIN, bubbaGrammarParser.VARS, bubbaGrammarParser.FUNC]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Paux2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varsr(self):
            return self.getTypedRuleContext(bubbaGrammarParser.VarsrContext,0)


        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_paux2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPaux2" ):
                listener.enterPaux2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPaux2" ):
                listener.exitPaux2(self)




    def paux2(self):

        localctx = bubbaGrammarParser.Paux2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_paux2)
        try:
            self.state = 152
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [bubbaGrammarParser.VARS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 150
                self.varsr()
                pass
            elif token in [bubbaGrammarParser.MAIN, bubbaGrammarParser.FUNC]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Paux3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def methods(self):
            return self.getTypedRuleContext(bubbaGrammarParser.MethodsContext,0)


        def paux3(self):
            return self.getTypedRuleContext(bubbaGrammarParser.Paux3Context,0)


        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_paux3

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPaux3" ):
                listener.enterPaux3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPaux3" ):
                listener.exitPaux3(self)




    def paux3(self):

        localctx = bubbaGrammarParser.Paux3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_paux3)
        try:
            self.state = 158
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [bubbaGrammarParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                self.methods()
                self.state = 155
                self.paux3()
                pass
            elif token in [bubbaGrammarParser.MAIN]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAIN(self):
            return self.getToken(bubbaGrammarParser.MAIN, 0)

        def LPARENTHESIS(self):
            return self.getToken(bubbaGrammarParser.LPARENTHESIS, 0)

        def RPARENTHESIS(self):
            return self.getToken(bubbaGrammarParser.RPARENTHESIS, 0)

        def LBRACE(self):
            return self.getToken(bubbaGrammarParser.LBRACE, 0)

        def body(self):
            return self.getTypedRuleContext(bubbaGrammarParser.BodyContext,0)


        def RBRACE(self):
            return self.getToken(bubbaGrammarParser.RBRACE, 0)

        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_main

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMain" ):
                listener.enterMain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMain" ):
                listener.exitMain(self)




    def main(self):

        localctx = bubbaGrammarParser.MainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_main)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(bubbaGrammarParser.MAIN)
            self.state = 161
            self.match(bubbaGrammarParser.LPARENTHESIS)
            self.state = 162
            self.match(bubbaGrammarParser.RPARENTHESIS)
            self.state = 163
            self.match(bubbaGrammarParser.LBRACE)
            self.state = 164
            self.body()
            self.state = 165
            self.match(bubbaGrammarParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhilerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(bubbaGrammarParser.WHILE, 0)

        def LPARENTHESIS(self):
            return self.getToken(bubbaGrammarParser.LPARENTHESIS, 0)

        def expression(self):
            return self.getTypedRuleContext(bubbaGrammarParser.ExpressionContext,0)


        def RPARENTHESIS(self):
            return self.getToken(bubbaGrammarParser.RPARENTHESIS, 0)

        def LBRACE(self):
            return self.getToken(bubbaGrammarParser.LBRACE, 0)

        def whileaux(self):
            return self.getTypedRuleContext(bubbaGrammarParser.WhileauxContext,0)


        def RBRACE(self):
            return self.getToken(bubbaGrammarParser.RBRACE, 0)

        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_whiler

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhiler" ):
                listener.enterWhiler(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhiler" ):
                listener.exitWhiler(self)




    def whiler(self):

        localctx = bubbaGrammarParser.WhilerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_whiler)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(bubbaGrammarParser.WHILE)
            self.state = 168
            self.match(bubbaGrammarParser.LPARENTHESIS)
            self.state = 169
            self.expression()
            self.state = 170
            self.match(bubbaGrammarParser.RPARENTHESIS)
            self.state = 171
            self.match(bubbaGrammarParser.LBRACE)
            self.state = 172
            self.whileaux()
            self.state = 173
            self.match(bubbaGrammarParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileauxContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(bubbaGrammarParser.StatementContext,0)


        def whileaux2(self):
            return self.getTypedRuleContext(bubbaGrammarParser.Whileaux2Context,0)


        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_whileaux

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileaux" ):
                listener.enterWhileaux(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileaux" ):
                listener.exitWhileaux(self)




    def whileaux(self):

        localctx = bubbaGrammarParser.WhileauxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_whileaux)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.statement()
            self.state = 176
            self.whileaux2()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Whileaux2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def whileaux(self):
            return self.getTypedRuleContext(bubbaGrammarParser.WhileauxContext,0)


        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_whileaux2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileaux2" ):
                listener.enterWhileaux2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileaux2" ):
                listener.exitWhileaux2(self)




    def whileaux2(self):

        localctx = bubbaGrammarParser.Whileaux2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_whileaux2)
        try:
            self.state = 180
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [bubbaGrammarParser.PRINT, bubbaGrammarParser.IF, bubbaGrammarParser.WHILE, bubbaGrammarParser.FOR, bubbaGrammarParser.INPUT, bubbaGrammarParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                self.whileaux()
                pass
            elif token in [bubbaGrammarParser.RBRACE]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(bubbaGrammarParser.FOR, 0)

        def foraux(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(bubbaGrammarParser.ForauxContext)
            else:
                return self.getTypedRuleContext(bubbaGrammarParser.ForauxContext,i)


        def TO(self):
            return self.getToken(bubbaGrammarParser.TO, 0)

        def foraux2(self):
            return self.getTypedRuleContext(bubbaGrammarParser.Foraux2Context,0)


        def LBRACE(self):
            return self.getToken(bubbaGrammarParser.LBRACE, 0)

        def foraux3(self):
            return self.getTypedRuleContext(bubbaGrammarParser.Foraux3Context,0)


        def RBRACE(self):
            return self.getToken(bubbaGrammarParser.RBRACE, 0)

        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_forr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForr" ):
                listener.enterForr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForr" ):
                listener.exitForr(self)




    def forr(self):

        localctx = bubbaGrammarParser.ForrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_forr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(bubbaGrammarParser.FOR)
            self.state = 183
            self.foraux()
            self.state = 184
            self.match(bubbaGrammarParser.TO)
            self.state = 185
            self.foraux()
            self.state = 186
            self.foraux2()
            self.state = 187
            self.match(bubbaGrammarParser.LBRACE)
            self.state = 188
            self.foraux3()
            self.state = 189
            self.match(bubbaGrammarParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForauxContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def V_INT(self):
            return self.getToken(bubbaGrammarParser.V_INT, 0)

        def ID(self):
            return self.getToken(bubbaGrammarParser.ID, 0)

        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_foraux

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForaux" ):
                listener.enterForaux(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForaux" ):
                listener.exitForaux(self)




    def foraux(self):

        localctx = bubbaGrammarParser.ForauxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_foraux)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            _la = self._input.LA(1)
            if not(_la==bubbaGrammarParser.ID or _la==bubbaGrammarParser.V_INT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Foraux2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STEP(self):
            return self.getToken(bubbaGrammarParser.STEP, 0)

        def foraux(self):
            return self.getTypedRuleContext(bubbaGrammarParser.ForauxContext,0)


        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_foraux2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForaux2" ):
                listener.enterForaux2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForaux2" ):
                listener.exitForaux2(self)




    def foraux2(self):

        localctx = bubbaGrammarParser.Foraux2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_foraux2)
        try:
            self.state = 196
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [bubbaGrammarParser.STEP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self.match(bubbaGrammarParser.STEP)
                self.state = 194
                self.foraux()
                pass
            elif token in [bubbaGrammarParser.LBRACE]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Foraux3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(bubbaGrammarParser.StatementContext,0)


        def foraux4(self):
            return self.getTypedRuleContext(bubbaGrammarParser.Foraux4Context,0)


        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_foraux3

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForaux3" ):
                listener.enterForaux3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForaux3" ):
                listener.exitForaux3(self)




    def foraux3(self):

        localctx = bubbaGrammarParser.Foraux3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_foraux3)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.statement()
            self.state = 199
            self.foraux4()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Foraux4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def foraux3(self):
            return self.getTypedRuleContext(bubbaGrammarParser.Foraux3Context,0)


        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_foraux4

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForaux4" ):
                listener.enterForaux4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForaux4" ):
                listener.exitForaux4(self)




    def foraux4(self):

        localctx = bubbaGrammarParser.Foraux4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_foraux4)
        try:
            self.state = 203
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [bubbaGrammarParser.PRINT, bubbaGrammarParser.IF, bubbaGrammarParser.WHILE, bubbaGrammarParser.FOR, bubbaGrammarParser.INPUT, bubbaGrammarParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 201
                self.foraux3()
                pass
            elif token in [bubbaGrammarParser.RBRACE]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign(self):
            return self.getTypedRuleContext(bubbaGrammarParser.AssignContext,0)


        def call(self):
            return self.getTypedRuleContext(bubbaGrammarParser.CallContext,0)


        def cond(self):
            return self.getTypedRuleContext(bubbaGrammarParser.CondContext,0)


        def forr(self):
            return self.getTypedRuleContext(bubbaGrammarParser.ForrContext,0)


        def whiler(self):
            return self.getTypedRuleContext(bubbaGrammarParser.WhilerContext,0)


        def output(self):
            return self.getTypedRuleContext(bubbaGrammarParser.OutputContext,0)


        def inputr(self):
            return self.getTypedRuleContext(bubbaGrammarParser.InputrContext,0)


        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = bubbaGrammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_statement)
        try:
            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 205
                self.assign()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 206
                self.call()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 207
                self.cond()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 208
                self.forr()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 209
                self.whiler()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 210
                self.output()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 211
                self.inputr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LidContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(bubbaGrammarParser.ID, 0)

        def lidaux(self):
            return self.getTypedRuleContext(bubbaGrammarParser.LidauxContext,0)


        def SEMICOLON(self):
            return self.getToken(bubbaGrammarParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_lid

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLid" ):
                listener.enterLid(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLid" ):
                listener.exitLid(self)




    def lid(self):

        localctx = bubbaGrammarParser.LidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_lid)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(bubbaGrammarParser.ID)
            self.state = 215
            self.lidaux()
            self.state = 216
            self.match(bubbaGrammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LidauxContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def laux(self):
            return self.getTypedRuleContext(bubbaGrammarParser.LauxContext,0)


        def laux2(self):
            return self.getTypedRuleContext(bubbaGrammarParser.Laux2Context,0)


        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_lidaux

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLidaux" ):
                listener.enterLidaux(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLidaux" ):
                listener.exitLidaux(self)




    def lidaux(self):

        localctx = bubbaGrammarParser.LidauxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_lidaux)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.laux()
            self.state = 219
            self.laux2()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LauxContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(bubbaGrammarParser.COMMA, 0)

        def ID(self):
            return self.getToken(bubbaGrammarParser.ID, 0)

        def laux(self):
            return self.getTypedRuleContext(bubbaGrammarParser.LauxContext,0)


        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_laux

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLaux" ):
                listener.enterLaux(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLaux" ):
                listener.exitLaux(self)




    def laux(self):

        localctx = bubbaGrammarParser.LauxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_laux)
        try:
            self.state = 225
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [bubbaGrammarParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.match(bubbaGrammarParser.COMMA)
                self.state = 222
                self.match(bubbaGrammarParser.ID)
                self.state = 223
                self.laux()
                pass
            elif token in [bubbaGrammarParser.LBRACKET, bubbaGrammarParser.SEMICOLON]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Laux2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(bubbaGrammarParser.LBRACKET, 0)

        def V_INT(self):
            return self.getToken(bubbaGrammarParser.V_INT, 0)

        def maux(self):
            return self.getTypedRuleContext(bubbaGrammarParser.MauxContext,0)


        def RBRACKET(self):
            return self.getToken(bubbaGrammarParser.RBRACKET, 0)

        def laux(self):
            return self.getTypedRuleContext(bubbaGrammarParser.LauxContext,0)


        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_laux2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLaux2" ):
                listener.enterLaux2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLaux2" ):
                listener.exitLaux2(self)




    def laux2(self):

        localctx = bubbaGrammarParser.Laux2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_laux2)
        try:
            self.state = 234
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [bubbaGrammarParser.LBRACKET]:
                self.enterOuterAlt(localctx, 1)
                self.state = 227
                self.match(bubbaGrammarParser.LBRACKET)
                self.state = 228
                self.match(bubbaGrammarParser.V_INT)
                self.state = 229
                self.maux()
                self.state = 230
                self.match(bubbaGrammarParser.RBRACKET)
                self.state = 231
                self.laux()
                pass
            elif token in [bubbaGrammarParser.SEMICOLON]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MauxContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(bubbaGrammarParser.COMMA, 0)

        def V_INT(self):
            return self.getToken(bubbaGrammarParser.V_INT, 0)

        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_maux

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMaux" ):
                listener.enterMaux(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMaux" ):
                listener.exitMaux(self)




    def maux(self):

        localctx = bubbaGrammarParser.MauxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_maux)
        try:
            self.state = 239
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [bubbaGrammarParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 236
                self.match(bubbaGrammarParser.COMMA)
                self.state = 237
                self.match(bubbaGrammarParser.V_INT)
                pass
            elif token in [bubbaGrammarParser.RBRACKET]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(bubbaGrammarParser.IF, 0)

        def LPARENTHESIS(self):
            return self.getToken(bubbaGrammarParser.LPARENTHESIS, 0)

        def expression(self):
            return self.getTypedRuleContext(bubbaGrammarParser.ExpressionContext,0)


        def RPARENTHESIS(self):
            return self.getToken(bubbaGrammarParser.RPARENTHESIS, 0)

        def LBRACE(self):
            return self.getToken(bubbaGrammarParser.LBRACE, 0)

        def condaux(self):
            return self.getTypedRuleContext(bubbaGrammarParser.CondauxContext,0)


        def RBRACE(self):
            return self.getToken(bubbaGrammarParser.RBRACE, 0)

        def condaux3(self):
            return self.getTypedRuleContext(bubbaGrammarParser.Condaux3Context,0)


        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_cond

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCond" ):
                listener.enterCond(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCond" ):
                listener.exitCond(self)




    def cond(self):

        localctx = bubbaGrammarParser.CondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_cond)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.match(bubbaGrammarParser.IF)
            self.state = 242
            self.match(bubbaGrammarParser.LPARENTHESIS)
            self.state = 243
            self.expression()
            self.state = 244
            self.match(bubbaGrammarParser.RPARENTHESIS)
            self.state = 245
            self.match(bubbaGrammarParser.LBRACE)
            self.state = 246
            self.condaux()
            self.state = 247
            self.match(bubbaGrammarParser.RBRACE)
            self.state = 248
            self.condaux3()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondauxContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(bubbaGrammarParser.StatementContext,0)


        def condaux2(self):
            return self.getTypedRuleContext(bubbaGrammarParser.Condaux2Context,0)


        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_condaux

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondaux" ):
                listener.enterCondaux(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondaux" ):
                listener.exitCondaux(self)




    def condaux(self):

        localctx = bubbaGrammarParser.CondauxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_condaux)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.statement()
            self.state = 251
            self.condaux2()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Condaux2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condaux(self):
            return self.getTypedRuleContext(bubbaGrammarParser.CondauxContext,0)


        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_condaux2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondaux2" ):
                listener.enterCondaux2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondaux2" ):
                listener.exitCondaux2(self)




    def condaux2(self):

        localctx = bubbaGrammarParser.Condaux2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_condaux2)
        try:
            self.state = 255
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [bubbaGrammarParser.PRINT, bubbaGrammarParser.IF, bubbaGrammarParser.WHILE, bubbaGrammarParser.FOR, bubbaGrammarParser.INPUT, bubbaGrammarParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 253
                self.condaux()
                pass
            elif token in [bubbaGrammarParser.RBRACE]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Condaux3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(bubbaGrammarParser.ELSE, 0)

        def LBRACE(self):
            return self.getToken(bubbaGrammarParser.LBRACE, 0)

        def condaux(self):
            return self.getTypedRuleContext(bubbaGrammarParser.CondauxContext,0)


        def RBRACE(self):
            return self.getToken(bubbaGrammarParser.RBRACE, 0)

        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_condaux3

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondaux3" ):
                listener.enterCondaux3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondaux3" ):
                listener.exitCondaux3(self)




    def condaux3(self):

        localctx = bubbaGrammarParser.Condaux3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_condaux3)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.match(bubbaGrammarParser.ELSE)
            self.state = 258
            self.match(bubbaGrammarParser.LBRACE)
            self.state = 259
            self.condaux()
            self.state = 260
            self.match(bubbaGrammarParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignaux(self):
            return self.getTypedRuleContext(bubbaGrammarParser.AssignauxContext,0)


        def EQUAL(self):
            return self.getToken(bubbaGrammarParser.EQUAL, 0)

        def expression(self):
            return self.getTypedRuleContext(bubbaGrammarParser.ExpressionContext,0)


        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)




    def assign(self):

        localctx = bubbaGrammarParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.assignaux()
            self.state = 263
            self.match(bubbaGrammarParser.EQUAL)
            self.state = 264
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignauxContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(bubbaGrammarParser.ID)
            else:
                return self.getToken(bubbaGrammarParser.ID, i)

        def DOT(self):
            return self.getToken(bubbaGrammarParser.DOT, 0)

        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_assignaux

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignaux" ):
                listener.enterAssignaux(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignaux" ):
                listener.exitAssignaux(self)




    def assignaux(self):

        localctx = bubbaGrammarParser.AssignauxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_assignaux)
        try:
            self.state = 270
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 266
                self.match(bubbaGrammarParser.ID)
                self.state = 267
                self.match(bubbaGrammarParser.DOT)
                self.state = 268
                self.match(bubbaGrammarParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 269
                self.match(bubbaGrammarParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def faux(self):
            return self.getTypedRuleContext(bubbaGrammarParser.FauxContext,0)


        def faux2(self):
            return self.getTypedRuleContext(bubbaGrammarParser.Faux2Context,0)


        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = bubbaGrammarParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_factor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.faux()
            self.state = 273
            self.faux2()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FauxContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(bubbaGrammarParser.ADD, 0)

        def MINUS(self):
            return self.getToken(bubbaGrammarParser.MINUS, 0)

        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_faux

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFaux" ):
                listener.enterFaux(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFaux" ):
                listener.exitFaux(self)




    def faux(self):

        localctx = bubbaGrammarParser.FauxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_faux)
        try:
            self.state = 278
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [bubbaGrammarParser.ADD]:
                self.enterOuterAlt(localctx, 1)
                self.state = 275
                self.match(bubbaGrammarParser.ADD)
                pass
            elif token in [bubbaGrammarParser.MINUS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 276
                self.match(bubbaGrammarParser.MINUS)
                pass
            elif token in [bubbaGrammarParser.LPARENTHESIS, bubbaGrammarParser.V_STRING, bubbaGrammarParser.ID, bubbaGrammarParser.V_INT, bubbaGrammarParser.V_FLOAT]:
                self.enterOuterAlt(localctx, 3)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Faux2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_cte(self):
            return self.getTypedRuleContext(bubbaGrammarParser.Var_cteContext,0)


        def call(self):
            return self.getTypedRuleContext(bubbaGrammarParser.CallContext,0)


        def LPARENTHESIS(self):
            return self.getToken(bubbaGrammarParser.LPARENTHESIS, 0)

        def expression(self):
            return self.getTypedRuleContext(bubbaGrammarParser.ExpressionContext,0)


        def RPARENTHESIS(self):
            return self.getToken(bubbaGrammarParser.RPARENTHESIS, 0)

        def ID(self):
            return self.getToken(bubbaGrammarParser.ID, 0)

        def faux3(self):
            return self.getTypedRuleContext(bubbaGrammarParser.Faux3Context,0)


        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_faux2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFaux2" ):
                listener.enterFaux2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFaux2" ):
                listener.exitFaux2(self)




    def faux2(self):

        localctx = bubbaGrammarParser.Faux2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_faux2)
        try:
            self.state = 288
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 280
                self.var_cte()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 281
                self.call()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 282
                self.match(bubbaGrammarParser.LPARENTHESIS)
                self.state = 283
                self.expression()
                self.state = 284
                self.match(bubbaGrammarParser.RPARENTHESIS)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 286
                self.match(bubbaGrammarParser.ID)
                self.state = 287
                self.faux3()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Faux3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(bubbaGrammarParser.LBRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(bubbaGrammarParser.ExpressionContext,0)


        def faux4(self):
            return self.getTypedRuleContext(bubbaGrammarParser.Faux4Context,0)


        def RBRACKET(self):
            return self.getToken(bubbaGrammarParser.RBRACKET, 0)

        def DOT(self):
            return self.getToken(bubbaGrammarParser.DOT, 0)

        def ID(self):
            return self.getToken(bubbaGrammarParser.ID, 0)

        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_faux3

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFaux3" ):
                listener.enterFaux3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFaux3" ):
                listener.exitFaux3(self)




    def faux3(self):

        localctx = bubbaGrammarParser.Faux3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_faux3)
        try:
            self.state = 298
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [bubbaGrammarParser.LBRACKET]:
                self.enterOuterAlt(localctx, 1)
                self.state = 290
                self.match(bubbaGrammarParser.LBRACKET)
                self.state = 291
                self.expression()
                self.state = 292
                self.faux4()
                self.state = 293
                self.match(bubbaGrammarParser.RBRACKET)
                pass
            elif token in [bubbaGrammarParser.DOT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 295
                self.match(bubbaGrammarParser.DOT)
                self.state = 296
                self.match(bubbaGrammarParser.ID)
                pass
            elif token in [bubbaGrammarParser.PRINT, bubbaGrammarParser.IF, bubbaGrammarParser.COMMA, bubbaGrammarParser.RPARENTHESIS, bubbaGrammarParser.RBRACE, bubbaGrammarParser.RBRACKET, bubbaGrammarParser.SEMICOLON, bubbaGrammarParser.ADD, bubbaGrammarParser.MINUS, bubbaGrammarParser.STAR, bubbaGrammarParser.SLASH, bubbaGrammarParser.GREATER, bubbaGrammarParser.GREATEREQ, bubbaGrammarParser.LESS, bubbaGrammarParser.LESSEQ, bubbaGrammarParser.AND, bubbaGrammarParser.OR, bubbaGrammarParser.EQEQUAL, bubbaGrammarParser.NOTEQUAL, bubbaGrammarParser.WHILE, bubbaGrammarParser.FOR, bubbaGrammarParser.RETURN, bubbaGrammarParser.INPUT, bubbaGrammarParser.ID]:
                self.enterOuterAlt(localctx, 3)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Faux4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(bubbaGrammarParser.COMMA, 0)

        def expression(self):
            return self.getTypedRuleContext(bubbaGrammarParser.ExpressionContext,0)


        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_faux4

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFaux4" ):
                listener.enterFaux4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFaux4" ):
                listener.exitFaux4(self)




    def faux4(self):

        localctx = bubbaGrammarParser.Faux4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_faux4)
        try:
            self.state = 303
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [bubbaGrammarParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 300
                self.match(bubbaGrammarParser.COMMA)
                self.state = 301
                self.expression()
                pass
            elif token in [bubbaGrammarParser.RBRACKET]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(bubbaGrammarParser.FactorContext,0)


        def termaux(self):
            return self.getTypedRuleContext(bubbaGrammarParser.TermauxContext,0)


        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = bubbaGrammarParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_term)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.factor()
            self.state = 306
            self.termaux()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermauxContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(bubbaGrammarParser.STAR, 0)

        def term(self):
            return self.getTypedRuleContext(bubbaGrammarParser.TermContext,0)


        def SLASH(self):
            return self.getToken(bubbaGrammarParser.SLASH, 0)

        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_termaux

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermaux" ):
                listener.enterTermaux(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermaux" ):
                listener.exitTermaux(self)




    def termaux(self):

        localctx = bubbaGrammarParser.TermauxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_termaux)
        try:
            self.state = 313
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [bubbaGrammarParser.STAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 308
                self.match(bubbaGrammarParser.STAR)
                self.state = 309
                self.term()
                pass
            elif token in [bubbaGrammarParser.SLASH]:
                self.enterOuterAlt(localctx, 2)
                self.state = 310
                self.match(bubbaGrammarParser.SLASH)
                self.state = 311
                self.term()
                pass
            elif token in [bubbaGrammarParser.PRINT, bubbaGrammarParser.IF, bubbaGrammarParser.COMMA, bubbaGrammarParser.RPARENTHESIS, bubbaGrammarParser.RBRACE, bubbaGrammarParser.RBRACKET, bubbaGrammarParser.SEMICOLON, bubbaGrammarParser.ADD, bubbaGrammarParser.MINUS, bubbaGrammarParser.GREATER, bubbaGrammarParser.GREATEREQ, bubbaGrammarParser.LESS, bubbaGrammarParser.LESSEQ, bubbaGrammarParser.AND, bubbaGrammarParser.OR, bubbaGrammarParser.EQEQUAL, bubbaGrammarParser.NOTEQUAL, bubbaGrammarParser.WHILE, bubbaGrammarParser.FOR, bubbaGrammarParser.RETURN, bubbaGrammarParser.INPUT, bubbaGrammarParser.ID]:
                self.enterOuterAlt(localctx, 3)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(bubbaGrammarParser.TermContext,0)


        def expaux(self):
            return self.getTypedRuleContext(bubbaGrammarParser.ExpauxContext,0)


        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)




    def exp(self):

        localctx = bubbaGrammarParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.term()
            self.state = 316
            self.expaux()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpauxContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(bubbaGrammarParser.ADD, 0)

        def exp(self):
            return self.getTypedRuleContext(bubbaGrammarParser.ExpContext,0)


        def MINUS(self):
            return self.getToken(bubbaGrammarParser.MINUS, 0)

        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_expaux

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpaux" ):
                listener.enterExpaux(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpaux" ):
                listener.exitExpaux(self)




    def expaux(self):

        localctx = bubbaGrammarParser.ExpauxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_expaux)
        try:
            self.state = 323
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [bubbaGrammarParser.ADD]:
                self.enterOuterAlt(localctx, 1)
                self.state = 318
                self.match(bubbaGrammarParser.ADD)
                self.state = 319
                self.exp()
                pass
            elif token in [bubbaGrammarParser.MINUS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 320
                self.match(bubbaGrammarParser.MINUS)
                self.state = 321
                self.exp()
                pass
            elif token in [bubbaGrammarParser.PRINT, bubbaGrammarParser.IF, bubbaGrammarParser.COMMA, bubbaGrammarParser.RPARENTHESIS, bubbaGrammarParser.RBRACE, bubbaGrammarParser.RBRACKET, bubbaGrammarParser.SEMICOLON, bubbaGrammarParser.GREATER, bubbaGrammarParser.GREATEREQ, bubbaGrammarParser.LESS, bubbaGrammarParser.LESSEQ, bubbaGrammarParser.AND, bubbaGrammarParser.OR, bubbaGrammarParser.EQEQUAL, bubbaGrammarParser.NOTEQUAL, bubbaGrammarParser.WHILE, bubbaGrammarParser.FOR, bubbaGrammarParser.RETURN, bubbaGrammarParser.INPUT, bubbaGrammarParser.ID]:
                self.enterOuterAlt(localctx, 3)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AexpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(bubbaGrammarParser.ExpContext,0)


        def aexpaux(self):
            return self.getTypedRuleContext(bubbaGrammarParser.AexpauxContext,0)


        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_aexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAexp" ):
                listener.enterAexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAexp" ):
                listener.exitAexp(self)




    def aexp(self):

        localctx = bubbaGrammarParser.AexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_aexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.exp()
            self.state = 326
            self.aexpaux()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AexpauxContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def aexps(self):
            return self.getTypedRuleContext(bubbaGrammarParser.AexpsContext,0)


        def exp(self):
            return self.getTypedRuleContext(bubbaGrammarParser.ExpContext,0)


        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_aexpaux

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAexpaux" ):
                listener.enterAexpaux(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAexpaux" ):
                listener.exitAexpaux(self)




    def aexpaux(self):

        localctx = bubbaGrammarParser.AexpauxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_aexpaux)
        try:
            self.state = 332
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [bubbaGrammarParser.GREATER, bubbaGrammarParser.GREATEREQ, bubbaGrammarParser.LESS, bubbaGrammarParser.LESSEQ, bubbaGrammarParser.EQEQUAL, bubbaGrammarParser.NOTEQUAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 328
                self.aexps()
                self.state = 329
                self.exp()
                pass
            elif token in [bubbaGrammarParser.PRINT, bubbaGrammarParser.IF, bubbaGrammarParser.COMMA, bubbaGrammarParser.RPARENTHESIS, bubbaGrammarParser.RBRACE, bubbaGrammarParser.RBRACKET, bubbaGrammarParser.SEMICOLON, bubbaGrammarParser.AND, bubbaGrammarParser.OR, bubbaGrammarParser.WHILE, bubbaGrammarParser.FOR, bubbaGrammarParser.RETURN, bubbaGrammarParser.INPUT, bubbaGrammarParser.ID]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AexpsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GREATER(self):
            return self.getToken(bubbaGrammarParser.GREATER, 0)

        def LESS(self):
            return self.getToken(bubbaGrammarParser.LESS, 0)

        def EQEQUAL(self):
            return self.getToken(bubbaGrammarParser.EQEQUAL, 0)

        def NOTEQUAL(self):
            return self.getToken(bubbaGrammarParser.NOTEQUAL, 0)

        def GREATEREQ(self):
            return self.getToken(bubbaGrammarParser.GREATEREQ, 0)

        def LESSEQ(self):
            return self.getToken(bubbaGrammarParser.LESSEQ, 0)

        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_aexps

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAexps" ):
                listener.enterAexps(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAexps" ):
                listener.exitAexps(self)




    def aexps(self):

        localctx = bubbaGrammarParser.AexpsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_aexps)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << bubbaGrammarParser.GREATER) | (1 << bubbaGrammarParser.GREATEREQ) | (1 << bubbaGrammarParser.LESS) | (1 << bubbaGrammarParser.LESSEQ) | (1 << bubbaGrammarParser.EQEQUAL) | (1 << bubbaGrammarParser.NOTEQUAL))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BexpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def aexp(self):
            return self.getTypedRuleContext(bubbaGrammarParser.AexpContext,0)


        def bexpaux(self):
            return self.getTypedRuleContext(bubbaGrammarParser.BexpauxContext,0)


        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_bexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBexp" ):
                listener.enterBexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBexp" ):
                listener.exitBexp(self)




    def bexp(self):

        localctx = bubbaGrammarParser.BexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_bexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.aexp()
            self.state = 337
            self.bexpaux()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BexpauxContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(bubbaGrammarParser.AND, 0)

        def bexp(self):
            return self.getTypedRuleContext(bubbaGrammarParser.BexpContext,0)


        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_bexpaux

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBexpaux" ):
                listener.enterBexpaux(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBexpaux" ):
                listener.exitBexpaux(self)




    def bexpaux(self):

        localctx = bubbaGrammarParser.BexpauxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_bexpaux)
        try:
            self.state = 342
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [bubbaGrammarParser.AND]:
                self.enterOuterAlt(localctx, 1)
                self.state = 339
                self.match(bubbaGrammarParser.AND)
                self.state = 340
                self.bexp()
                pass
            elif token in [bubbaGrammarParser.PRINT, bubbaGrammarParser.IF, bubbaGrammarParser.COMMA, bubbaGrammarParser.RPARENTHESIS, bubbaGrammarParser.RBRACE, bubbaGrammarParser.RBRACKET, bubbaGrammarParser.SEMICOLON, bubbaGrammarParser.OR, bubbaGrammarParser.WHILE, bubbaGrammarParser.FOR, bubbaGrammarParser.RETURN, bubbaGrammarParser.INPUT, bubbaGrammarParser.ID]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bexp(self):
            return self.getTypedRuleContext(bubbaGrammarParser.BexpContext,0)


        def expressionaux(self):
            return self.getTypedRuleContext(bubbaGrammarParser.ExpressionauxContext,0)


        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = bubbaGrammarParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344
            self.bexp()
            self.state = 345
            self.expressionaux()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionauxContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OR(self):
            return self.getToken(bubbaGrammarParser.OR, 0)

        def expression(self):
            return self.getTypedRuleContext(bubbaGrammarParser.ExpressionContext,0)


        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_expressionaux

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionaux" ):
                listener.enterExpressionaux(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionaux" ):
                listener.exitExpressionaux(self)




    def expressionaux(self):

        localctx = bubbaGrammarParser.ExpressionauxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_expressionaux)
        try:
            self.state = 350
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [bubbaGrammarParser.OR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 347
                self.match(bubbaGrammarParser.OR)
                self.state = 348
                self.expression()
                pass
            elif token in [bubbaGrammarParser.PRINT, bubbaGrammarParser.IF, bubbaGrammarParser.COMMA, bubbaGrammarParser.RPARENTHESIS, bubbaGrammarParser.RBRACE, bubbaGrammarParser.RBRACKET, bubbaGrammarParser.SEMICOLON, bubbaGrammarParser.WHILE, bubbaGrammarParser.FOR, bubbaGrammarParser.RETURN, bubbaGrammarParser.INPUT, bubbaGrammarParser.ID]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(bubbaGrammarParser.FUNC, 0)

        def type_simple(self):
            return self.getTypedRuleContext(bubbaGrammarParser.Type_simpleContext,0)


        def ID(self):
            return self.getToken(bubbaGrammarParser.ID, 0)

        def LPARENTHESIS(self):
            return self.getToken(bubbaGrammarParser.LPARENTHESIS, 0)

        def funcaux(self):
            return self.getTypedRuleContext(bubbaGrammarParser.FuncauxContext,0)


        def RPARENTHESIS(self):
            return self.getToken(bubbaGrammarParser.RPARENTHESIS, 0)

        def LBRACE(self):
            return self.getToken(bubbaGrammarParser.LBRACE, 0)

        def body(self):
            return self.getTypedRuleContext(bubbaGrammarParser.BodyContext,0)


        def RETURN(self):
            return self.getToken(bubbaGrammarParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(bubbaGrammarParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(bubbaGrammarParser.SEMICOLON, 0)

        def RBRACE(self):
            return self.getToken(bubbaGrammarParser.RBRACE, 0)

        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc" ):
                listener.enterFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc" ):
                listener.exitFunc(self)




    def func(self):

        localctx = bubbaGrammarParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            self.match(bubbaGrammarParser.FUNC)
            self.state = 353
            self.type_simple()
            self.state = 354
            self.match(bubbaGrammarParser.ID)
            self.state = 355
            self.match(bubbaGrammarParser.LPARENTHESIS)
            self.state = 356
            self.funcaux()
            self.state = 357
            self.match(bubbaGrammarParser.RPARENTHESIS)
            self.state = 358
            self.match(bubbaGrammarParser.LBRACE)
            self.state = 359
            self.body()
            self.state = 360
            self.match(bubbaGrammarParser.RETURN)
            self.state = 361
            self.expression()
            self.state = 362
            self.match(bubbaGrammarParser.SEMICOLON)
            self.state = 363
            self.match(bubbaGrammarParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncauxContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def args(self):
            return self.getTypedRuleContext(bubbaGrammarParser.ArgsContext,0)


        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_funcaux

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncaux" ):
                listener.enterFuncaux(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncaux" ):
                listener.exitFuncaux(self)




    def funcaux(self):

        localctx = bubbaGrammarParser.FuncauxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_funcaux)
        try:
            self.state = 367
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [bubbaGrammarParser.FLOAT, bubbaGrammarParser.INT, bubbaGrammarParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 365
                self.args()
                pass
            elif token in [bubbaGrammarParser.RPARENTHESIS]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(bubbaGrammarParser.CLASS, 0)

        def ID(self):
            return self.getToken(bubbaGrammarParser.ID, 0)

        def class_a(self):
            return self.getTypedRuleContext(bubbaGrammarParser.Class_aContext,0)


        def LBRACE(self):
            return self.getToken(bubbaGrammarParser.LBRACE, 0)

        def varsr(self):
            return self.getTypedRuleContext(bubbaGrammarParser.VarsrContext,0)


        def class_b(self):
            return self.getTypedRuleContext(bubbaGrammarParser.Class_bContext,0)


        def RBRACE(self):
            return self.getToken(bubbaGrammarParser.RBRACE, 0)

        def SEMICOLON(self):
            return self.getToken(bubbaGrammarParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_classr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassr" ):
                listener.enterClassr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassr" ):
                listener.exitClassr(self)




    def classr(self):

        localctx = bubbaGrammarParser.ClassrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_classr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self.match(bubbaGrammarParser.CLASS)
            self.state = 370
            self.match(bubbaGrammarParser.ID)
            self.state = 371
            self.class_a()
            self.state = 372
            self.match(bubbaGrammarParser.LBRACE)
            self.state = 373
            self.varsr()
            self.state = 374
            self.class_b()
            self.state = 375
            self.match(bubbaGrammarParser.RBRACE)
            self.state = 376
            self.match(bubbaGrammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_aContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXTENDS(self):
            return self.getToken(bubbaGrammarParser.EXTENDS, 0)

        def ID(self):
            return self.getToken(bubbaGrammarParser.ID, 0)

        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_class_a

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClass_a" ):
                listener.enterClass_a(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClass_a" ):
                listener.exitClass_a(self)




    def class_a(self):

        localctx = bubbaGrammarParser.Class_aContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_class_a)
        try:
            self.state = 381
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [bubbaGrammarParser.EXTENDS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 378
                self.match(bubbaGrammarParser.EXTENDS)
                self.state = 379
                self.match(bubbaGrammarParser.ID)
                pass
            elif token in [bubbaGrammarParser.LBRACE]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_bContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def methods(self):
            return self.getTypedRuleContext(bubbaGrammarParser.MethodsContext,0)


        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_class_b

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClass_b" ):
                listener.enterClass_b(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClass_b" ):
                listener.exitClass_b(self)




    def class_b(self):

        localctx = bubbaGrammarParser.Class_bContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_class_b)
        try:
            self.state = 385
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [bubbaGrammarParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 383
                self.methods()
                pass
            elif token in [bubbaGrammarParser.RBRACE]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OutputContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(bubbaGrammarParser.PRINT, 0)

        def LPARENTHESIS(self):
            return self.getToken(bubbaGrammarParser.LPARENTHESIS, 0)

        def expression(self):
            return self.getTypedRuleContext(bubbaGrammarParser.ExpressionContext,0)


        def output_a(self):
            return self.getTypedRuleContext(bubbaGrammarParser.Output_aContext,0)


        def RPARENTHESIS(self):
            return self.getToken(bubbaGrammarParser.RPARENTHESIS, 0)

        def SEMICOLON(self):
            return self.getToken(bubbaGrammarParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_output

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOutput" ):
                listener.enterOutput(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOutput" ):
                listener.exitOutput(self)




    def output(self):

        localctx = bubbaGrammarParser.OutputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_output)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.match(bubbaGrammarParser.PRINT)
            self.state = 388
            self.match(bubbaGrammarParser.LPARENTHESIS)
            self.state = 389
            self.expression()
            self.state = 390
            self.output_a()
            self.state = 391
            self.match(bubbaGrammarParser.RPARENTHESIS)
            self.state = 392
            self.match(bubbaGrammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Output_aContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(bubbaGrammarParser.COMMA, 0)

        def expression(self):
            return self.getTypedRuleContext(bubbaGrammarParser.ExpressionContext,0)


        def output_a(self):
            return self.getTypedRuleContext(bubbaGrammarParser.Output_aContext,0)


        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_output_a

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOutput_a" ):
                listener.enterOutput_a(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOutput_a" ):
                listener.exitOutput_a(self)




    def output_a(self):

        localctx = bubbaGrammarParser.Output_aContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_output_a)
        try:
            self.state = 399
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [bubbaGrammarParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 394
                self.match(bubbaGrammarParser.COMMA)
                self.state = 395
                self.expression()
                self.state = 396
                self.output_a()
                pass
            elif token in [bubbaGrammarParser.RPARENTHESIS]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InputrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INPUT(self):
            return self.getToken(bubbaGrammarParser.INPUT, 0)

        def LPARENTHESIS(self):
            return self.getToken(bubbaGrammarParser.LPARENTHESIS, 0)

        def ID(self):
            return self.getToken(bubbaGrammarParser.ID, 0)

        def input_a(self):
            return self.getTypedRuleContext(bubbaGrammarParser.Input_aContext,0)


        def RPARENTHESIS(self):
            return self.getToken(bubbaGrammarParser.RPARENTHESIS, 0)

        def SEMICOLON(self):
            return self.getToken(bubbaGrammarParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_inputr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInputr" ):
                listener.enterInputr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInputr" ):
                listener.exitInputr(self)




    def inputr(self):

        localctx = bubbaGrammarParser.InputrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_inputr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            self.match(bubbaGrammarParser.INPUT)
            self.state = 402
            self.match(bubbaGrammarParser.LPARENTHESIS)
            self.state = 403
            self.match(bubbaGrammarParser.ID)
            self.state = 404
            self.input_a()
            self.state = 405
            self.match(bubbaGrammarParser.RPARENTHESIS)
            self.state = 406
            self.match(bubbaGrammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Input_aContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(bubbaGrammarParser.COMMA, 0)

        def ID(self):
            return self.getToken(bubbaGrammarParser.ID, 0)

        def input_a(self):
            return self.getTypedRuleContext(bubbaGrammarParser.Input_aContext,0)


        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_input_a

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInput_a" ):
                listener.enterInput_a(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInput_a" ):
                listener.exitInput_a(self)




    def input_a(self):

        localctx = bubbaGrammarParser.Input_aContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_input_a)
        try:
            self.state = 412
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [bubbaGrammarParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 408
                self.match(bubbaGrammarParser.COMMA)
                self.state = 409
                self.match(bubbaGrammarParser.ID)
                self.state = 410
                self.input_a()
                pass
            elif token in [bubbaGrammarParser.RPARENTHESIS]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def body_a(self):
            return self.getTypedRuleContext(bubbaGrammarParser.Body_aContext,0)


        def statement(self):
            return self.getTypedRuleContext(bubbaGrammarParser.StatementContext,0)


        def body_b(self):
            return self.getTypedRuleContext(bubbaGrammarParser.Body_bContext,0)


        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody" ):
                listener.enterBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody" ):
                listener.exitBody(self)




    def body(self):

        localctx = bubbaGrammarParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
            self.body_a()
            self.state = 415
            self.statement()
            self.state = 416
            self.body_b()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Body_aContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varsr(self):
            return self.getTypedRuleContext(bubbaGrammarParser.VarsrContext,0)


        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_body_a

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody_a" ):
                listener.enterBody_a(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody_a" ):
                listener.exitBody_a(self)




    def body_a(self):

        localctx = bubbaGrammarParser.Body_aContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_body_a)
        try:
            self.state = 420
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [bubbaGrammarParser.VARS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 418
                self.varsr()
                pass
            elif token in [bubbaGrammarParser.PRINT, bubbaGrammarParser.IF, bubbaGrammarParser.WHILE, bubbaGrammarParser.FOR, bubbaGrammarParser.INPUT, bubbaGrammarParser.ID]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Body_bContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(bubbaGrammarParser.StatementContext,0)


        def body_b(self):
            return self.getTypedRuleContext(bubbaGrammarParser.Body_bContext,0)


        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_body_b

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody_b" ):
                listener.enterBody_b(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody_b" ):
                listener.exitBody_b(self)




    def body_b(self):

        localctx = bubbaGrammarParser.Body_bContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_body_b)
        try:
            self.state = 426
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [bubbaGrammarParser.PRINT, bubbaGrammarParser.IF, bubbaGrammarParser.WHILE, bubbaGrammarParser.FOR, bubbaGrammarParser.INPUT, bubbaGrammarParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 422
                self.statement()
                self.state = 423
                self.body_b()
                pass
            elif token in [bubbaGrammarParser.RBRACE, bubbaGrammarParser.RETURN]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarsrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARS(self):
            return self.getToken(bubbaGrammarParser.VARS, 0)

        def vars_a(self):
            return self.getTypedRuleContext(bubbaGrammarParser.Vars_aContext,0)


        def COLON(self):
            return self.getToken(bubbaGrammarParser.COLON, 0)

        def lid(self):
            return self.getTypedRuleContext(bubbaGrammarParser.LidContext,0)


        def vars_b(self):
            return self.getTypedRuleContext(bubbaGrammarParser.Vars_bContext,0)


        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_varsr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarsr" ):
                listener.enterVarsr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarsr" ):
                listener.exitVarsr(self)




    def varsr(self):

        localctx = bubbaGrammarParser.VarsrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_varsr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 428
            self.match(bubbaGrammarParser.VARS)
            self.state = 429
            self.vars_a()
            self.state = 430
            self.match(bubbaGrammarParser.COLON)
            self.state = 431
            self.lid()
            self.state = 432
            self.vars_b()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vars_aContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(bubbaGrammarParser.ID, 0)

        def type_simple(self):
            return self.getTypedRuleContext(bubbaGrammarParser.Type_simpleContext,0)


        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_vars_a

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVars_a" ):
                listener.enterVars_a(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVars_a" ):
                listener.exitVars_a(self)




    def vars_a(self):

        localctx = bubbaGrammarParser.Vars_aContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_vars_a)
        try:
            self.state = 436
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [bubbaGrammarParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 434
                self.match(bubbaGrammarParser.ID)
                pass
            elif token in [bubbaGrammarParser.FLOAT, bubbaGrammarParser.INT, bubbaGrammarParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 435
                self.type_simple()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vars_bContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varsr(self):
            return self.getTypedRuleContext(bubbaGrammarParser.VarsrContext,0)


        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_vars_b

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVars_b" ):
                listener.enterVars_b(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVars_b" ):
                listener.exitVars_b(self)




    def vars_b(self):

        localctx = bubbaGrammarParser.Vars_bContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_vars_b)
        try:
            self.state = 440
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [bubbaGrammarParser.VARS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 438
                self.varsr()
                pass
            elif token in [bubbaGrammarParser.MAIN, bubbaGrammarParser.PRINT, bubbaGrammarParser.IF, bubbaGrammarParser.RBRACE, bubbaGrammarParser.WHILE, bubbaGrammarParser.FOR, bubbaGrammarParser.FUNC, bubbaGrammarParser.INPUT, bubbaGrammarParser.ID]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_simple(self):
            return self.getTypedRuleContext(bubbaGrammarParser.Type_simpleContext,0)


        def COLON(self):
            return self.getToken(bubbaGrammarParser.COLON, 0)

        def ID(self):
            return self.getToken(bubbaGrammarParser.ID, 0)

        def args_a(self):
            return self.getTypedRuleContext(bubbaGrammarParser.Args_aContext,0)


        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_args

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgs" ):
                listener.enterArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgs" ):
                listener.exitArgs(self)




    def args(self):

        localctx = bubbaGrammarParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_args)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 442
            self.type_simple()
            self.state = 443
            self.match(bubbaGrammarParser.COLON)
            self.state = 444
            self.match(bubbaGrammarParser.ID)
            self.state = 445
            self.args_a()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Args_aContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(bubbaGrammarParser.COMMA, 0)

        def args(self):
            return self.getTypedRuleContext(bubbaGrammarParser.ArgsContext,0)


        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_args_a

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgs_a" ):
                listener.enterArgs_a(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgs_a" ):
                listener.exitArgs_a(self)




    def args_a(self):

        localctx = bubbaGrammarParser.Args_aContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_args_a)
        try:
            self.state = 450
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [bubbaGrammarParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 447
                self.match(bubbaGrammarParser.COMMA)
                self.state = 448
                self.args()
                pass
            elif token in [bubbaGrammarParser.RPARENTHESIS]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_simpleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(bubbaGrammarParser.INT, 0)

        def FLOAT(self):
            return self.getToken(bubbaGrammarParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(bubbaGrammarParser.STRING, 0)

        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_type_simple

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_simple" ):
                listener.enterType_simple(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_simple" ):
                listener.exitType_simple(self)




    def type_simple(self):

        localctx = bubbaGrammarParser.Type_simpleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_type_simple)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 452
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << bubbaGrammarParser.FLOAT) | (1 << bubbaGrammarParser.INT) | (1 << bubbaGrammarParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(bubbaGrammarParser.ID, 0)

        def call_a(self):
            return self.getTypedRuleContext(bubbaGrammarParser.Call_aContext,0)


        def LPARENTHESIS(self):
            return self.getToken(bubbaGrammarParser.LPARENTHESIS, 0)

        def call_b(self):
            return self.getTypedRuleContext(bubbaGrammarParser.Call_bContext,0)


        def RPARENTHESIS(self):
            return self.getToken(bubbaGrammarParser.RPARENTHESIS, 0)

        def SEMICOLON(self):
            return self.getToken(bubbaGrammarParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall" ):
                listener.enterCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall" ):
                listener.exitCall(self)




    def call(self):

        localctx = bubbaGrammarParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 454
            self.match(bubbaGrammarParser.ID)
            self.state = 455
            self.call_a()
            self.state = 456
            self.match(bubbaGrammarParser.LPARENTHESIS)
            self.state = 457
            self.call_b()
            self.state = 458
            self.match(bubbaGrammarParser.RPARENTHESIS)
            self.state = 459
            self.match(bubbaGrammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_aContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(bubbaGrammarParser.DOT, 0)

        def ID(self):
            return self.getToken(bubbaGrammarParser.ID, 0)

        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_call_a

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall_a" ):
                listener.enterCall_a(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall_a" ):
                listener.exitCall_a(self)




    def call_a(self):

        localctx = bubbaGrammarParser.Call_aContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_call_a)
        try:
            self.state = 464
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [bubbaGrammarParser.DOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 461
                self.match(bubbaGrammarParser.DOT)
                self.state = 462
                self.match(bubbaGrammarParser.ID)
                pass
            elif token in [bubbaGrammarParser.LPARENTHESIS]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_bContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def params(self):
            return self.getTypedRuleContext(bubbaGrammarParser.ParamsContext,0)


        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_call_b

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall_b" ):
                listener.enterCall_b(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall_b" ):
                listener.exitCall_b(self)




    def call_b(self):

        localctx = bubbaGrammarParser.Call_bContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_call_b)
        try:
            self.state = 468
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [bubbaGrammarParser.LPARENTHESIS, bubbaGrammarParser.ADD, bubbaGrammarParser.MINUS, bubbaGrammarParser.V_STRING, bubbaGrammarParser.ID, bubbaGrammarParser.V_INT, bubbaGrammarParser.V_FLOAT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 466
                self.params()
                pass
            elif token in [bubbaGrammarParser.RPARENTHESIS]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(bubbaGrammarParser.ExpressionContext,0)


        def params_a(self):
            return self.getTypedRuleContext(bubbaGrammarParser.Params_aContext,0)


        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParams" ):
                listener.enterParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParams" ):
                listener.exitParams(self)




    def params(self):

        localctx = bubbaGrammarParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_params)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 470
            self.expression()
            self.state = 471
            self.params_a()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Params_aContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(bubbaGrammarParser.COMMA, 0)

        def params(self):
            return self.getTypedRuleContext(bubbaGrammarParser.ParamsContext,0)


        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_params_a

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParams_a" ):
                listener.enterParams_a(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParams_a" ):
                listener.exitParams_a(self)




    def params_a(self):

        localctx = bubbaGrammarParser.Params_aContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_params_a)
        try:
            self.state = 476
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [bubbaGrammarParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 473
                self.match(bubbaGrammarParser.COMMA)
                self.state = 474
                self.params()
                pass
            elif token in [bubbaGrammarParser.RPARENTHESIS]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_cteContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def V_INT(self):
            return self.getToken(bubbaGrammarParser.V_INT, 0)

        def V_FLOAT(self):
            return self.getToken(bubbaGrammarParser.V_FLOAT, 0)

        def V_STRING(self):
            return self.getToken(bubbaGrammarParser.V_STRING, 0)

        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_var_cte

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_cte" ):
                listener.enterVar_cte(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_cte" ):
                listener.exitVar_cte(self)




    def var_cte(self):

        localctx = bubbaGrammarParser.Var_cteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_var_cte)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 478
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << bubbaGrammarParser.V_STRING) | (1 << bubbaGrammarParser.V_INT) | (1 << bubbaGrammarParser.V_FLOAT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VoidContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(bubbaGrammarParser.FUNC, 0)

        def VOID(self):
            return self.getToken(bubbaGrammarParser.VOID, 0)

        def ID(self):
            return self.getToken(bubbaGrammarParser.ID, 0)

        def LPARENTHESIS(self):
            return self.getToken(bubbaGrammarParser.LPARENTHESIS, 0)

        def void_a(self):
            return self.getTypedRuleContext(bubbaGrammarParser.Void_aContext,0)


        def RPARENTHESIS(self):
            return self.getToken(bubbaGrammarParser.RPARENTHESIS, 0)

        def LBRACE(self):
            return self.getToken(bubbaGrammarParser.LBRACE, 0)

        def body(self):
            return self.getTypedRuleContext(bubbaGrammarParser.BodyContext,0)


        def RBRACE(self):
            return self.getToken(bubbaGrammarParser.RBRACE, 0)

        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_void

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVoid" ):
                listener.enterVoid(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVoid" ):
                listener.exitVoid(self)




    def void(self):

        localctx = bubbaGrammarParser.VoidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_void)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 480
            self.match(bubbaGrammarParser.FUNC)
            self.state = 481
            self.match(bubbaGrammarParser.VOID)
            self.state = 482
            self.match(bubbaGrammarParser.ID)
            self.state = 483
            self.match(bubbaGrammarParser.LPARENTHESIS)
            self.state = 484
            self.void_a()
            self.state = 485
            self.match(bubbaGrammarParser.RPARENTHESIS)
            self.state = 486
            self.match(bubbaGrammarParser.LBRACE)
            self.state = 487
            self.body()
            self.state = 488
            self.match(bubbaGrammarParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Void_aContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def args(self):
            return self.getTypedRuleContext(bubbaGrammarParser.ArgsContext,0)


        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_void_a

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVoid_a" ):
                listener.enterVoid_a(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVoid_a" ):
                listener.exitVoid_a(self)




    def void_a(self):

        localctx = bubbaGrammarParser.Void_aContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_void_a)
        try:
            self.state = 492
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [bubbaGrammarParser.FLOAT, bubbaGrammarParser.INT, bubbaGrammarParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 490
                self.args()
                pass
            elif token in [bubbaGrammarParser.RPARENTHESIS]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def void(self):
            return self.getTypedRuleContext(bubbaGrammarParser.VoidContext,0)


        def methods(self):
            return self.getTypedRuleContext(bubbaGrammarParser.MethodsContext,0)


        def func(self):
            return self.getTypedRuleContext(bubbaGrammarParser.FuncContext,0)


        def getRuleIndex(self):
            return bubbaGrammarParser.RULE_methods

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethods" ):
                listener.enterMethods(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethods" ):
                listener.exitMethods(self)




    def methods(self):

        localctx = bubbaGrammarParser.MethodsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_methods)
        try:
            self.state = 500
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 494
                self.void()
                self.state = 495
                self.methods()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 497
                self.func()
                self.state = 498
                self.methods()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





