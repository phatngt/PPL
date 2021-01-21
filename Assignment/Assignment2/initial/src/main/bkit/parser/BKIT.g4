grammar BKIT;

@lexer::header {
from lexererr import *
}

@lexer::members {
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
}

options{
	language=Python3;
}



//-------------- Fragment ------------------//

fragment Lowercase: [a-z];
fragment Uppercase: [A-Z];
fragment Digit: [0-9];
fragment Underscore: '_';
fragment Expoment: [eE] '-'? Digit+;
fragment Dot: '.';
fragment Character: ~[\r\n\b\f\t'"\\] | Escape|'\'"';
fragment Escape: '\\' [bfrnt'\\];
fragment IllegalEscape: '\\' ~[bfrnt'\\]|'\'' ;
fragment UnternimatedStringLitter: '"' Character* ;
fragment UnterminatedComment: .*? ~('*');

program: exp EOF;

exp: (term ASSIGN)* term;

term: factor COMPARE factor | factor;

factor: operand (ANDOR operand)*; 

operand: ID | INTLIT | BOOLIT | '(' exp ')';

INTLIT: [0-9]+ ;

BOOLIT: 'True' | 'False' ;

ANDOR: 'and' | 'or' ;

ASSIGN: '+=' | '-=' | '&=' | '|=' | ':=' ;

COMPARE: '=' | '<>' | '>=' | '<=' | '<' | '>' ;

ID: [a-z]+ ;

COMMENTLINE: '**' .*? '**'->skip;

WS : [ \t\r\n]+ -> skip ; 

ERROR_CHAR: .{
    raise ErrorToken(self.text)
};
UNCLOSE_STRING: '"' Character* ([\b\f\r\n\t\\] | EOF) {
    esc = ['\b', '\t', '\n', '\f', '\r', '\\']
    temp = str(self.text)
    if temp[-1] in esc:
        raise UncloseString(temp[1:-1])
    else :
        raise UncloseString(temp[1:])
};
ILLEGAL_ESCAPE: '"' Character* IllegalEscape {
    temp = str(self.text)
    raise IllegalEscape(temp[1:])
};
UNTERMINATED_COMMENT: '**' .*? {
    temp = str(self.text)
    if '**' not in temp[2:]:
        raise UnterminatedComment()
};