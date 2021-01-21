# Generated from e:\PPL\Assignment\Assignment2\initial\src\main\bkit\parser\BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\7")
        buf.write("f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3\3\3\3\3")
        buf.write("\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\5\b\62\n\b\3\b")
        buf.write("\6\b\65\n\b\r\b\16\b\66\3\t\3\t\3\n\3\n\3\n\3\n\5\n?\n")
        buf.write("\n\3\13\3\13\3\13\3\f\3\f\3\f\5\fG\n\f\3\r\3\r\7\rK\n")
        buf.write("\r\f\r\16\rN\13\r\3\16\7\16Q\n\16\f\16\16\16T\13\16\3")
        buf.write("\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\21\6\21c\n\21\r\21\16\21d\3R\2\22\3\3\5\4\7\2")
        buf.write("\t\2\13\2\r\2\17\2\21\2\23\2\25\2\27\2\31\2\33\2\35\5")
        buf.write("\37\6!\7\3\2\t\3\2c|\3\2C\\\3\2\62;\4\2GGgg\7\2\n\f\16")
        buf.write("\17$$))^^\t\2))^^ddhhppttvv\3\2,,\2b\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\3#\3\2\2\2")
        buf.write("\5%\3\2\2\2\7\'\3\2\2\2\t)\3\2\2\2\13+\3\2\2\2\r-\3\2")
        buf.write("\2\2\17/\3\2\2\2\218\3\2\2\2\23>\3\2\2\2\25@\3\2\2\2\27")
        buf.write("F\3\2\2\2\31H\3\2\2\2\33R\3\2\2\2\35W\3\2\2\2\37[\3\2")
        buf.write("\2\2!b\3\2\2\2#$\7=\2\2$\4\3\2\2\2%&\7.\2\2&\6\3\2\2\2")
        buf.write("\'(\t\2\2\2(\b\3\2\2\2)*\t\3\2\2*\n\3\2\2\2+,\t\4\2\2")
        buf.write(",\f\3\2\2\2-.\7a\2\2.\16\3\2\2\2/\61\t\5\2\2\60\62\7/")
        buf.write("\2\2\61\60\3\2\2\2\61\62\3\2\2\2\62\64\3\2\2\2\63\65\5")
        buf.write("\13\6\2\64\63\3\2\2\2\65\66\3\2\2\2\66\64\3\2\2\2\66\67")
        buf.write("\3\2\2\2\67\20\3\2\2\289\7\60\2\29\22\3\2\2\2:?\n\6\2")
        buf.write("\2;?\5\25\13\2<=\7)\2\2=?\7$\2\2>:\3\2\2\2>;\3\2\2\2>")
        buf.write("<\3\2\2\2?\24\3\2\2\2@A\7^\2\2AB\t\7\2\2B\26\3\2\2\2C")
        buf.write("D\7^\2\2DG\n\7\2\2EG\7)\2\2FC\3\2\2\2FE\3\2\2\2G\30\3")
        buf.write("\2\2\2HL\7$\2\2IK\5\23\n\2JI\3\2\2\2KN\3\2\2\2LJ\3\2\2")
        buf.write("\2LM\3\2\2\2M\32\3\2\2\2NL\3\2\2\2OQ\13\2\2\2PO\3\2\2")
        buf.write("\2QT\3\2\2\2RS\3\2\2\2RP\3\2\2\2SU\3\2\2\2TR\3\2\2\2U")
        buf.write("V\n\b\2\2V\34\3\2\2\2WX\7k\2\2XY\7p\2\2YZ\7v\2\2Z\36\3")
        buf.write("\2\2\2[\\\7h\2\2\\]\7n\2\2]^\7q\2\2^_\7c\2\2_`\7v\2\2")
        buf.write("` \3\2\2\2ac\t\2\2\2ba\3\2\2\2cd\3\2\2\2db\3\2\2\2de\3")
        buf.write("\2\2\2e\"\3\2\2\2\n\2\61\66>FLRd\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    INTTYPE = 3
    FLOATTYPE = 4
    ID = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "','", "'int'", "'float'" ]

    symbolicNames = [ "<INVALID>",
            "INTTYPE", "FLOATTYPE", "ID" ]

    ruleNames = [ "T__0", "T__1", "Lowercase", "Uppercase", "Digit", "Underscore", 
                  "Expoment", "Dot", "Character", "Escape", "IllegalEscape", 
                  "UnternimatedStringLitter", "UnterminatedComment", "INTTYPE", 
                  "FLOATTYPE", "ID" ]

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


