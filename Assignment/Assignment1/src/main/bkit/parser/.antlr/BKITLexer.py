# Generated from c:\Users\phatnt\Desktop\PPL\Assignment\Assignment1\src\main\bkit\parser\BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2D")
        buf.write("\u022f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6")
        buf.write("\5\6\u00a8\n\6\3\6\6\6\u00ab\n\6\r\6\16\6\u00ac\3\7\3")
        buf.write("\7\3\b\3\b\3\b\3\b\5\b\u00b5\n\b\3\t\3\t\3\t\3\n\3\n\3")
        buf.write("\n\5\n\u00bd\n\n\3\13\3\13\7\13\u00c1\n\13\f\13\16\13")
        buf.write("\u00c4\13\13\3\f\7\f\u00c7\n\f\f\f\16\f\u00ca\13\f\3\f")
        buf.write("\3\f\3\r\3\r\3\r\3\r\3\r\7\r\u00d3\n\r\f\r\16\r\u00d6")
        buf.write("\13\r\3\16\3\16\3\16\3\16\7\16\u00dc\n\16\f\16\16\16\u00df")
        buf.write("\13\16\3\16\3\16\3\16\3\16\3\16\3\17\6\17\u00e7\n\17\r")
        buf.write("\17\16\17\u00e8\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!")
        buf.write("\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3")
        buf.write("#\3#\3#\3$\3$\3$\3$\3$\3$\3%\3%\3&\3&\3&\3\'\3\'\3(\3")
        buf.write("(\3(\3)\3)\3*\3*\3*\3+\3+\3,\3,\3,\3-\3-\3.\3.\3/\3/\3")
        buf.write("\60\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3\62\3\63\3\63")
        buf.write("\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\66\3\67\3\67\3\67")
        buf.write("\38\38\38\38\39\39\39\3:\3:\3:\3;\3;\3;\3;\3<\3<\3<\3")
        buf.write("<\3=\3=\3>\3>\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3D\3D\3E\3")
        buf.write("E\3F\3F\3G\3G\3G\7G\u01c8\nG\fG\16G\u01cb\13G\3G\3G\3")
        buf.write("G\3G\6G\u01d1\nG\rG\16G\u01d2\3G\3G\3G\6G\u01d8\nG\rG")
        buf.write("\16G\u01d9\5G\u01dc\nG\3H\6H\u01df\nH\rH\16H\u01e0\3H")
        buf.write("\3H\7H\u01e5\nH\fH\16H\u01e8\13H\3H\5H\u01eb\nH\3H\6H")
        buf.write("\u01ee\nH\rH\16H\u01ef\3H\3H\6H\u01f4\nH\rH\16H\u01f5")
        buf.write("\3H\5H\u01f9\nH\3H\6H\u01fc\nH\rH\16H\u01fd\3H\3H\5H\u0202")
        buf.write("\nH\3I\3I\5I\u0206\nI\3J\3J\3J\3J\3K\3K\3K\3L\3L\7L\u0211")
        buf.write("\nL\fL\16L\u0214\13L\3L\5L\u0217\nL\3L\3L\3M\3M\7M\u021d")
        buf.write("\nM\fM\16M\u0220\13M\3M\3M\3M\3N\3N\3N\3N\7N\u0229\nN")
        buf.write("\fN\16N\u022c\13N\3N\3N\5\u00c8\u00dd\u022a\2O\3\2\5\2")
        buf.write("\7\2\t\2\13\2\r\2\17\2\21\2\23\2\25\2\27\2\31\3\33\4\35")
        buf.write("\5\37\6!\7#\b%\t\'\n)\13+\f-\r/\16\61\17\63\20\65\21\67")
        buf.write("\229\23;\24=\25?\26A\27C\30E\31G\32I\33K\34M\35O\36Q\37")
        buf.write("S U!W\"Y#[$]%_&a\'c(e)g*i+k,m-o.q/s\60u\61w\62y\63{\64")
        buf.write("}\65\177\66\u0081\67\u00838\u00859\u0087:\u0089;\u008b")
        buf.write("<\u008d=\u008f>\u0091?\u0093@\u0095A\u0097B\u0099C\u009b")
        buf.write("D\3\2\20\3\2c|\3\2C\\\3\2\62;\4\2GGgg\7\2\n\f\16\17$$")
        buf.write("))^^\t\2))^^ddhhppttvv\3\2,,\5\2\13\f\17\17\"\"\3\2\63")
        buf.write(";\4\2ZZzz\3\2CH\4\2QQqq\3\2\629\5\3\n\f\16\17^^\2\u0244")
        buf.write("\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2")
        buf.write("!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3")
        buf.write("\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c")
        buf.write("\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2")
        buf.write("m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2")
        buf.write("\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2")
        buf.write("\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2")
        buf.write("\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d")
        buf.write("\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2")
        buf.write("\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b")
        buf.write("\3\2\2\2\3\u009d\3\2\2\2\5\u009f\3\2\2\2\7\u00a1\3\2\2")
        buf.write("\2\t\u00a3\3\2\2\2\13\u00a5\3\2\2\2\r\u00ae\3\2\2\2\17")
        buf.write("\u00b4\3\2\2\2\21\u00b6\3\2\2\2\23\u00bc\3\2\2\2\25\u00be")
        buf.write("\3\2\2\2\27\u00c8\3\2\2\2\31\u00cd\3\2\2\2\33\u00d7\3")
        buf.write("\2\2\2\35\u00e6\3\2\2\2\37\u00ec\3\2\2\2!\u00f1\3\2\2")
        buf.write("\2#\u00f6\3\2\2\2%\u00fd\3\2\2\2\'\u0100\3\2\2\2)\u0104")
        buf.write("\3\2\2\2+\u010a\3\2\2\2-\u0110\3\2\2\2/\u0117\3\2\2\2")
        buf.write("\61\u0120\3\2\2\2\63\u012a\3\2\2\2\65\u0130\3\2\2\2\67")
        buf.write("\u0139\3\2\2\29\u0141\3\2\2\2;\u0145\3\2\2\2=\u014c\3")
        buf.write("\2\2\2?\u0151\3\2\2\2A\u0154\3\2\2\2C\u015a\3\2\2\2E\u0163")
        buf.write("\3\2\2\2G\u0168\3\2\2\2I\u016e\3\2\2\2K\u0170\3\2\2\2")
        buf.write("M\u0173\3\2\2\2O\u0175\3\2\2\2Q\u0178\3\2\2\2S\u017a\3")
        buf.write("\2\2\2U\u017d\3\2\2\2W\u017f\3\2\2\2Y\u0182\3\2\2\2[\u0184")
        buf.write("\3\2\2\2]\u0186\3\2\2\2_\u0188\3\2\2\2a\u018b\3\2\2\2")
        buf.write("c\u018e\3\2\2\2e\u0191\3\2\2\2g\u0194\3\2\2\2i\u0196\3")
        buf.write("\2\2\2k\u0198\3\2\2\2m\u019b\3\2\2\2o\u019e\3\2\2\2q\u01a2")
        buf.write("\3\2\2\2s\u01a5\3\2\2\2u\u01a8\3\2\2\2w\u01ac\3\2\2\2")
        buf.write("y\u01b0\3\2\2\2{\u01b2\3\2\2\2}\u01b4\3\2\2\2\177\u01b6")
        buf.write("\3\2\2\2\u0081\u01b8\3\2\2\2\u0083\u01ba\3\2\2\2\u0085")
        buf.write("\u01bc\3\2\2\2\u0087\u01be\3\2\2\2\u0089\u01c0\3\2\2\2")
        buf.write("\u008b\u01c2\3\2\2\2\u008d\u01db\3\2\2\2\u008f\u0201\3")
        buf.write("\2\2\2\u0091\u0205\3\2\2\2\u0093\u0207\3\2\2\2\u0095\u020b")
        buf.write("\3\2\2\2\u0097\u020e\3\2\2\2\u0099\u021a\3\2\2\2\u009b")
        buf.write("\u0224\3\2\2\2\u009d\u009e\t\2\2\2\u009e\4\3\2\2\2\u009f")
        buf.write("\u00a0\t\3\2\2\u00a0\6\3\2\2\2\u00a1\u00a2\t\4\2\2\u00a2")
        buf.write("\b\3\2\2\2\u00a3\u00a4\7a\2\2\u00a4\n\3\2\2\2\u00a5\u00a7")
        buf.write("\t\5\2\2\u00a6\u00a8\7/\2\2\u00a7\u00a6\3\2\2\2\u00a7")
        buf.write("\u00a8\3\2\2\2\u00a8\u00aa\3\2\2\2\u00a9\u00ab\5\7\4\2")
        buf.write("\u00aa\u00a9\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00aa\3")
        buf.write("\2\2\2\u00ac\u00ad\3\2\2\2\u00ad\f\3\2\2\2\u00ae\u00af")
        buf.write("\7\60\2\2\u00af\16\3\2\2\2\u00b0\u00b5\n\6\2\2\u00b1\u00b5")
        buf.write("\5\21\t\2\u00b2\u00b3\7)\2\2\u00b3\u00b5\7$\2\2\u00b4")
        buf.write("\u00b0\3\2\2\2\u00b4\u00b1\3\2\2\2\u00b4\u00b2\3\2\2\2")
        buf.write("\u00b5\20\3\2\2\2\u00b6\u00b7\7^\2\2\u00b7\u00b8\t\7\2")
        buf.write("\2\u00b8\22\3\2\2\2\u00b9\u00ba\7^\2\2\u00ba\u00bd\n\7")
        buf.write("\2\2\u00bb\u00bd\7)\2\2\u00bc\u00b9\3\2\2\2\u00bc\u00bb")
        buf.write("\3\2\2\2\u00bd\24\3\2\2\2\u00be\u00c2\7$\2\2\u00bf\u00c1")
        buf.write("\5\17\b\2\u00c0\u00bf\3\2\2\2\u00c1\u00c4\3\2\2\2\u00c2")
        buf.write("\u00c0\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\26\3\2\2\2\u00c4")
        buf.write("\u00c2\3\2\2\2\u00c5\u00c7\13\2\2\2\u00c6\u00c5\3\2\2")
        buf.write("\2\u00c7\u00ca\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c8\u00c6")
        buf.write("\3\2\2\2\u00c9\u00cb\3\2\2\2\u00ca\u00c8\3\2\2\2\u00cb")
        buf.write("\u00cc\n\b\2\2\u00cc\30\3\2\2\2\u00cd\u00d4\5\3\2\2\u00ce")
        buf.write("\u00d3\5\3\2\2\u00cf\u00d3\5\5\3\2\u00d0\u00d3\5\7\4\2")
        buf.write("\u00d1\u00d3\5\t\5\2\u00d2\u00ce\3\2\2\2\u00d2\u00cf\3")
        buf.write("\2\2\2\u00d2\u00d0\3\2\2\2\u00d2\u00d1\3\2\2\2\u00d3\u00d6")
        buf.write("\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d4\u00d5\3\2\2\2\u00d5")
        buf.write("\32\3\2\2\2\u00d6\u00d4\3\2\2\2\u00d7\u00d8\7,\2\2\u00d8")
        buf.write("\u00d9\7,\2\2\u00d9\u00dd\3\2\2\2\u00da\u00dc\13\2\2\2")
        buf.write("\u00db\u00da\3\2\2\2\u00dc\u00df\3\2\2\2\u00dd\u00de\3")
        buf.write("\2\2\2\u00dd\u00db\3\2\2\2\u00de\u00e0\3\2\2\2\u00df\u00dd")
        buf.write("\3\2\2\2\u00e0\u00e1\7,\2\2\u00e1\u00e2\7,\2\2\u00e2\u00e3")
        buf.write("\3\2\2\2\u00e3\u00e4\b\16\2\2\u00e4\34\3\2\2\2\u00e5\u00e7")
        buf.write("\t\t\2\2\u00e6\u00e5\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8")
        buf.write("\u00e6\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9\u00ea\3\2\2\2")
        buf.write("\u00ea\u00eb\b\17\2\2\u00eb\36\3\2\2\2\u00ec\u00ed\7D")
        buf.write("\2\2\u00ed\u00ee\7q\2\2\u00ee\u00ef\7f\2\2\u00ef\u00f0")
        buf.write("\7{\2\2\u00f0 \3\2\2\2\u00f1\u00f2\7G\2\2\u00f2\u00f3")
        buf.write("\7n\2\2\u00f3\u00f4\7u\2\2\u00f4\u00f5\7g\2\2\u00f5\"")
        buf.write("\3\2\2\2\u00f6\u00f7\7G\2\2\u00f7\u00f8\7p\2\2\u00f8\u00f9")
        buf.write("\7f\2\2\u00f9\u00fa\7H\2\2\u00fa\u00fb\7q\2\2\u00fb\u00fc")
        buf.write("\7t\2\2\u00fc$\3\2\2\2\u00fd\u00fe\7K\2\2\u00fe\u00ff")
        buf.write("\7h\2\2\u00ff&\3\2\2\2\u0100\u0101\7X\2\2\u0101\u0102")
        buf.write("\7c\2\2\u0102\u0103\7t\2\2\u0103(\3\2\2\2\u0104\u0105")
        buf.write("\7G\2\2\u0105\u0106\7p\2\2\u0106\u0107\7f\2\2\u0107\u0108")
        buf.write("\7F\2\2\u0108\u0109\7q\2\2\u0109*\3\2\2\2\u010a\u010b")
        buf.write("\7D\2\2\u010b\u010c\7t\2\2\u010c\u010d\7g\2\2\u010d\u010e")
        buf.write("\7c\2\2\u010e\u010f\7m\2\2\u010f,\3\2\2\2\u0110\u0111")
        buf.write("\7G\2\2\u0111\u0112\7n\2\2\u0112\u0113\7u\2\2\u0113\u0114")
        buf.write("\7g\2\2\u0114\u0115\7K\2\2\u0115\u0116\7h\2\2\u0116.\3")
        buf.write("\2\2\2\u0117\u0118\7G\2\2\u0118\u0119\7p\2\2\u0119\u011a")
        buf.write("\7f\2\2\u011a\u011b\7Y\2\2\u011b\u011c\7j\2\2\u011c\u011d")
        buf.write("\7k\2\2\u011d\u011e\7n\2\2\u011e\u011f\7g\2\2\u011f\60")
        buf.write("\3\2\2\2\u0120\u0121\7R\2\2\u0121\u0122\7c\2\2\u0122\u0123")
        buf.write("\7t\2\2\u0123\u0124\7c\2\2\u0124\u0125\7o\2\2\u0125\u0126")
        buf.write("\7g\2\2\u0126\u0127\7v\2\2\u0127\u0128\7g\2\2\u0128\u0129")
        buf.write("\7t\2\2\u0129\62\3\2\2\2\u012a\u012b\7Y\2\2\u012b\u012c")
        buf.write("\7j\2\2\u012c\u012d\7k\2\2\u012d\u012e\7n\2\2\u012e\u012f")
        buf.write("\7g\2\2\u012f\64\3\2\2\2\u0130\u0131\7E\2\2\u0131\u0132")
        buf.write("\7q\2\2\u0132\u0133\7p\2\2\u0133\u0134\7v\2\2\u0134\u0135")
        buf.write("\7k\2\2\u0135\u0136\7p\2\2\u0136\u0137\7w\2\2\u0137\u0138")
        buf.write("\7g\2\2\u0138\66\3\2\2\2\u0139\u013a\7G\2\2\u013a\u013b")
        buf.write("\7p\2\2\u013b\u013c\7f\2\2\u013c\u013d\7D\2\2\u013d\u013e")
        buf.write("\7q\2\2\u013e\u013f\7f\2\2\u013f\u0140\7{\2\2\u01408\3")
        buf.write("\2\2\2\u0141\u0142\7H\2\2\u0142\u0143\7q\2\2\u0143\u0144")
        buf.write("\7t\2\2\u0144:\3\2\2\2\u0145\u0146\7T\2\2\u0146\u0147")
        buf.write("\7g\2\2\u0147\u0148\7v\2\2\u0148\u0149\7w\2\2\u0149\u014a")
        buf.write("\7t\2\2\u014a\u014b\7p\2\2\u014b<\3\2\2\2\u014c\u014d")
        buf.write("\7V\2\2\u014d\u014e\7t\2\2\u014e\u014f\7w\2\2\u014f\u0150")
        buf.write("\7g\2\2\u0150>\3\2\2\2\u0151\u0152\7F\2\2\u0152\u0153")
        buf.write("\7q\2\2\u0153@\3\2\2\2\u0154\u0155\7G\2\2\u0155\u0156")
        buf.write("\7p\2\2\u0156\u0157\7f\2\2\u0157\u0158\7K\2\2\u0158\u0159")
        buf.write("\7h\2\2\u0159B\3\2\2\2\u015a\u015b\7H\2\2\u015b\u015c")
        buf.write("\7w\2\2\u015c\u015d\7p\2\2\u015d\u015e\7e\2\2\u015e\u015f")
        buf.write("\7v\2\2\u015f\u0160\7k\2\2\u0160\u0161\7q\2\2\u0161\u0162")
        buf.write("\7p\2\2\u0162D\3\2\2\2\u0163\u0164\7V\2\2\u0164\u0165")
        buf.write("\7j\2\2\u0165\u0166\7g\2\2\u0166\u0167\7p\2\2\u0167F\3")
        buf.write("\2\2\2\u0168\u0169\7H\2\2\u0169\u016a\7c\2\2\u016a\u016b")
        buf.write("\7n\2\2\u016b\u016c\7u\2\2\u016c\u016d\7g\2\2\u016dH\3")
        buf.write("\2\2\2\u016e\u016f\7-\2\2\u016fJ\3\2\2\2\u0170\u0171\7")
        buf.write("-\2\2\u0171\u0172\7\60\2\2\u0172L\3\2\2\2\u0173\u0174")
        buf.write("\7/\2\2\u0174N\3\2\2\2\u0175\u0176\7/\2\2\u0176\u0177")
        buf.write("\7\60\2\2\u0177P\3\2\2\2\u0178\u0179\7,\2\2\u0179R\3\2")
        buf.write("\2\2\u017a\u017b\7,\2\2\u017b\u017c\7\60\2\2\u017cT\3")
        buf.write("\2\2\2\u017d\u017e\7^\2\2\u017eV\3\2\2\2\u017f\u0180\7")
        buf.write("^\2\2\u0180\u0181\7\60\2\2\u0181X\3\2\2\2\u0182\u0183")
        buf.write("\7\'\2\2\u0183Z\3\2\2\2\u0184\u0185\7?\2\2\u0185\\\3\2")
        buf.write("\2\2\u0186\u0187\7#\2\2\u0187^\3\2\2\2\u0188\u0189\7(")
        buf.write("\2\2\u0189\u018a\7(\2\2\u018a`\3\2\2\2\u018b\u018c\7~")
        buf.write("\2\2\u018c\u018d\7~\2\2\u018db\3\2\2\2\u018e\u018f\7?")
        buf.write("\2\2\u018f\u0190\7?\2\2\u0190d\3\2\2\2\u0191\u0192\7#")
        buf.write("\2\2\u0192\u0193\7?\2\2\u0193f\3\2\2\2\u0194\u0195\7>")
        buf.write("\2\2\u0195h\3\2\2\2\u0196\u0197\7@\2\2\u0197j\3\2\2\2")
        buf.write("\u0198\u0199\7>\2\2\u0199\u019a\7?\2\2\u019al\3\2\2\2")
        buf.write("\u019b\u019c\7@\2\2\u019c\u019d\7?\2\2\u019dn\3\2\2\2")
        buf.write("\u019e\u019f\7?\2\2\u019f\u01a0\7\61\2\2\u01a0\u01a1\7")
        buf.write("?\2\2\u01a1p\3\2\2\2\u01a2\u01a3\7>\2\2\u01a3\u01a4\7")
        buf.write("\60\2\2\u01a4r\3\2\2\2\u01a5\u01a6\7@\2\2\u01a6\u01a7")
        buf.write("\7\60\2\2\u01a7t\3\2\2\2\u01a8\u01a9\7>\2\2\u01a9\u01aa")
        buf.write("\7?\2\2\u01aa\u01ab\7\60\2\2\u01abv\3\2\2\2\u01ac\u01ad")
        buf.write("\7@\2\2\u01ad\u01ae\7?\2\2\u01ae\u01af\7\60\2\2\u01af")
        buf.write("x\3\2\2\2\u01b0\u01b1\7]\2\2\u01b1z\3\2\2\2\u01b2\u01b3")
        buf.write("\7_\2\2\u01b3|\3\2\2\2\u01b4\u01b5\7=\2\2\u01b5~\3\2\2")
        buf.write("\2\u01b6\u01b7\7<\2\2\u01b7\u0080\3\2\2\2\u01b8\u01b9")
        buf.write("\7.\2\2\u01b9\u0082\3\2\2\2\u01ba\u01bb\7}\2\2\u01bb\u0084")
        buf.write("\3\2\2\2\u01bc\u01bd\7\177\2\2\u01bd\u0086\3\2\2\2\u01be")
        buf.write("\u01bf\5\r\7\2\u01bf\u0088\3\2\2\2\u01c0\u01c1\7*\2\2")
        buf.write("\u01c1\u008a\3\2\2\2\u01c2\u01c3\7+\2\2\u01c3\u008c\3")
        buf.write("\2\2\2\u01c4\u01dc\7\62\2\2\u01c5\u01c9\t\n\2\2\u01c6")
        buf.write("\u01c8\5\7\4\2\u01c7\u01c6\3\2\2\2\u01c8\u01cb\3\2\2\2")
        buf.write("\u01c9\u01c7\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca\u01dc\3")
        buf.write("\2\2\2\u01cb\u01c9\3\2\2\2\u01cc\u01cd\7\62\2\2\u01cd")
        buf.write("\u01d0\t\13\2\2\u01ce\u01d1\5\7\4\2\u01cf\u01d1\t\f\2")
        buf.write("\2\u01d0\u01ce\3\2\2\2\u01d0\u01cf\3\2\2\2\u01d1\u01d2")
        buf.write("\3\2\2\2\u01d2\u01d0\3\2\2\2\u01d2\u01d3\3\2\2\2\u01d3")
        buf.write("\u01dc\3\2\2\2\u01d4\u01d5\7\62\2\2\u01d5\u01d7\t\r\2")
        buf.write("\2\u01d6\u01d8\t\16\2\2\u01d7\u01d6\3\2\2\2\u01d8\u01d9")
        buf.write("\3\2\2\2\u01d9\u01d7\3\2\2\2\u01d9\u01da\3\2\2\2\u01da")
        buf.write("\u01dc\3\2\2\2\u01db\u01c4\3\2\2\2\u01db\u01c5\3\2\2\2")
        buf.write("\u01db\u01cc\3\2\2\2\u01db\u01d4\3\2\2\2\u01dc\u008e\3")
        buf.write("\2\2\2\u01dd\u01df\5\7\4\2\u01de\u01dd\3\2\2\2\u01df\u01e0")
        buf.write("\3\2\2\2\u01e0\u01de\3\2\2\2\u01e0\u01e1\3\2\2\2\u01e1")
        buf.write("\u01e2\3\2\2\2\u01e2\u01e6\5\r\7\2\u01e3\u01e5\5\7\4\2")
        buf.write("\u01e4\u01e3\3\2\2\2\u01e5\u01e8\3\2\2\2\u01e6\u01e4\3")
        buf.write("\2\2\2\u01e6\u01e7\3\2\2\2\u01e7\u01ea\3\2\2\2\u01e8\u01e6")
        buf.write("\3\2\2\2\u01e9\u01eb\5\13\6\2\u01ea\u01e9\3\2\2\2\u01ea")
        buf.write("\u01eb\3\2\2\2\u01eb\u0202\3\2\2\2\u01ec\u01ee\5\7\4\2")
        buf.write("\u01ed\u01ec\3\2\2\2\u01ee\u01ef\3\2\2\2\u01ef\u01ed\3")
        buf.write("\2\2\2\u01ef\u01f0\3\2\2\2\u01f0\u01f1\3\2\2\2\u01f1\u01f3")
        buf.write("\5\r\7\2\u01f2\u01f4\5\7\4\2\u01f3\u01f2\3\2\2\2\u01f4")
        buf.write("\u01f5\3\2\2\2\u01f5\u01f3\3\2\2\2\u01f5\u01f6\3\2\2\2")
        buf.write("\u01f6\u01f8\3\2\2\2\u01f7\u01f9\5\13\6\2\u01f8\u01f7")
        buf.write("\3\2\2\2\u01f8\u01f9\3\2\2\2\u01f9\u0202\3\2\2\2\u01fa")
        buf.write("\u01fc\5\7\4\2\u01fb\u01fa\3\2\2\2\u01fc\u01fd\3\2\2\2")
        buf.write("\u01fd\u01fb\3\2\2\2\u01fd\u01fe\3\2\2\2\u01fe\u01ff\3")
        buf.write("\2\2\2\u01ff\u0200\5\13\6\2\u0200\u0202\3\2\2\2\u0201")
        buf.write("\u01de\3\2\2\2\u0201\u01ed\3\2\2\2\u0201\u01fb\3\2\2\2")
        buf.write("\u0202\u0090\3\2\2\2\u0203\u0206\5=\37\2\u0204\u0206\5")
        buf.write("G$\2\u0205\u0203\3\2\2\2\u0205\u0204\3\2\2\2\u0206\u0092")
        buf.write("\3\2\2\2\u0207\u0208\5\25\13\2\u0208\u0209\7$\2\2\u0209")
        buf.write("\u020a\bJ\3\2\u020a\u0094\3\2\2\2\u020b\u020c\13\2\2\2")
        buf.write("\u020c\u020d\bK\4\2\u020d\u0096\3\2\2\2\u020e\u0212\7")
        buf.write("$\2\2\u020f\u0211\5\17\b\2\u0210\u020f\3\2\2\2\u0211\u0214")
        buf.write("\3\2\2\2\u0212\u0210\3\2\2\2\u0212\u0213\3\2\2\2\u0213")
        buf.write("\u0216\3\2\2\2\u0214\u0212\3\2\2\2\u0215\u0217\t\17\2")
        buf.write("\2\u0216\u0215\3\2\2\2\u0217\u0218\3\2\2\2\u0218\u0219")
        buf.write("\bL\5\2\u0219\u0098\3\2\2\2\u021a\u021e\7$\2\2\u021b\u021d")
        buf.write("\5\17\b\2\u021c\u021b\3\2\2\2\u021d\u0220\3\2\2\2\u021e")
        buf.write("\u021c\3\2\2\2\u021e\u021f\3\2\2\2\u021f\u0221\3\2\2\2")
        buf.write("\u0220\u021e\3\2\2\2\u0221\u0222\5\23\n\2\u0222\u0223")
        buf.write("\bM\6\2\u0223\u009a\3\2\2\2\u0224\u0225\7,\2\2\u0225\u0226")
        buf.write("\7,\2\2\u0226\u022a\3\2\2\2\u0227\u0229\13\2\2\2\u0228")
        buf.write("\u0227\3\2\2\2\u0229\u022c\3\2\2\2\u022a\u022b\3\2\2\2")
        buf.write("\u022a\u0228\3\2\2\2\u022b\u022d\3\2\2\2\u022c\u022a\3")
        buf.write("\2\2\2\u022d\u022e\bN\7\2\u022e\u009c\3\2\2\2\37\2\u00a7")
        buf.write("\u00ac\u00b4\u00bc\u00c2\u00c8\u00d2\u00d4\u00dd\u00e8")
        buf.write("\u01c9\u01d0\u01d2\u01d9\u01db\u01e0\u01e6\u01ea\u01ef")
        buf.write("\u01f5\u01f8\u01fd\u0201\u0205\u0212\u0216\u021e\u022a")
        buf.write("\b\b\2\2\3J\2\3K\3\3L\4\3M\5\3N\6")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ID = 1
    COMMENTLINE = 2
    WS = 3
    BODY = 4
    ELSE = 5
    ENDFOR = 6
    IF = 7
    VAR = 8
    ENDDO = 9
    BREAK = 10
    ELSEIF = 11
    ENDWHILE = 12
    PARAMETER = 13
    WHILE = 14
    CONTINUE = 15
    ENDBODY = 16
    FOR = 17
    RETURN = 18
    TRUE = 19
    DO = 20
    ENDIF = 21
    FUNCTION = 22
    THEN = 23
    FALSE = 24
    INTADD = 25
    FLOATADD = 26
    INTSIGNNEG = 27
    FLOATSIGNNEG = 28
    INTMUL = 29
    FLOATMUL = 30
    INTDIV = 31
    FLOATDIV = 32
    INTREM = 33
    ASSIGN = 34
    NEG = 35
    AND = 36
    OR = 37
    EQ = 38
    INEQ = 39
    ILT = 40
    IGT = 41
    ILTOEQ = 42
    IGTOEQ = 43
    FNEQ = 44
    FLT = 45
    FGLT = 46
    FLTOEQ = 47
    FGTOEQ = 48
    LSB = 49
    RSB = 50
    SEMI = 51
    COLON = 52
    COMMA = 53
    LBRACE = 54
    RBRACE = 55
    DOT = 56
    LPAREN = 57
    RPAREN = 58
    INTLIT = 59
    FLOATLIT = 60
    BOOLEANLIT = 61
    STRINGLIT = 62
    ERROR_CHAR = 63
    UNCLOSE_STRING = 64
    ILLEGAL_ESCAPE = 65
    UNTERMINATED_COMMENT = 66

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Body'", "'Else'", "'EndFor'", "'If'", "'Var'", "'EndDo'", 
            "'Break'", "'ElseIf'", "'EndWhile'", "'Parameter'", "'While'", 
            "'Continue'", "'EndBody'", "'For'", "'Return'", "'True'", "'Do'", 
            "'EndIf'", "'Function'", "'Then'", "'False'", "'+'", "'+.'", 
            "'-'", "'-.'", "'*'", "'*.'", "'\\'", "'\\.'", "'%'", "'='", 
            "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", "'>'", "'<='", 
            "'>='", "'=/='", "'<.'", "'>.'", "'<=.'", "'>=.'", "'['", "']'", 
            "';'", "':'", "','", "'{'", "'}'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "COMMENTLINE", "WS", "BODY", "ELSE", "ENDFOR", "IF", "VAR", 
            "ENDDO", "BREAK", "ELSEIF", "ENDWHILE", "PARAMETER", "WHILE", 
            "CONTINUE", "ENDBODY", "FOR", "RETURN", "TRUE", "DO", "ENDIF", 
            "FUNCTION", "THEN", "FALSE", "INTADD", "FLOATADD", "INTSIGNNEG", 
            "FLOATSIGNNEG", "INTMUL", "FLOATMUL", "INTDIV", "FLOATDIV", 
            "INTREM", "ASSIGN", "NEG", "AND", "OR", "EQ", "INEQ", "ILT", 
            "IGT", "ILTOEQ", "IGTOEQ", "FNEQ", "FLT", "FGLT", "FLTOEQ", 
            "FGTOEQ", "LSB", "RSB", "SEMI", "COLON", "COMMA", "LBRACE", 
            "RBRACE", "DOT", "LPAREN", "RPAREN", "INTLIT", "FLOATLIT", "BOOLEANLIT", 
            "STRINGLIT", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "UNTERMINATED_COMMENT" ]

    ruleNames = [ "Lowercase", "Uppercase", "Digit", "Underscore", "Expoment", 
                  "Dot", "Character", "Escape", "IllegalEscape", "UnternimatedStringLitter", 
                  "UnterminatedComment", "ID", "COMMENTLINE", "WS", "BODY", 
                  "ELSE", "ENDFOR", "IF", "VAR", "ENDDO", "BREAK", "ELSEIF", 
                  "ENDWHILE", "PARAMETER", "WHILE", "CONTINUE", "ENDBODY", 
                  "FOR", "RETURN", "TRUE", "DO", "ENDIF", "FUNCTION", "THEN", 
                  "FALSE", "INTADD", "FLOATADD", "INTSIGNNEG", "FLOATSIGNNEG", 
                  "INTMUL", "FLOATMUL", "INTDIV", "FLOATDIV", "INTREM", 
                  "ASSIGN", "NEG", "AND", "OR", "EQ", "INEQ", "ILT", "IGT", 
                  "ILTOEQ", "IGTOEQ", "FNEQ", "FLT", "FGLT", "FLTOEQ", "FGTOEQ", 
                  "LSB", "RSB", "SEMI", "COLON", "COMMA", "LBRACE", "RBRACE", 
                  "DOT", "LPAREN", "RPAREN", "INTLIT", "FLOATLIT", "BOOLEANLIT", 
                  "STRINGLIT", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "UNTERMINATED_COMMENT" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[72] = self.STRINGLIT_action 
            actions[73] = self.ERROR_CHAR_action 
            actions[74] = self.UNCLOSE_STRING_action 
            actions[75] = self.ILLEGAL_ESCAPE_action 
            actions[76] = self.UNTERMINATED_COMMENT_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                temp = str(self.text)
                self.text = temp[1:-1]

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                raise ErrorToken(self.text)

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                esc = ['\b', '\t', '\n', '\f', '\r', '\\']
                temp = str(self.text)
                if temp[-1] in esc:
                    raise UncloseString(temp[1:-1])
                else :
                    raise UncloseString(temp[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                temp = str(self.text)
                raise IllegalEscape(temp[1:])

     

    def UNTERMINATED_COMMENT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                temp = str(self.text)
                if '**' not in temp[2:]:
                    raise UnterminatedComment()

     


