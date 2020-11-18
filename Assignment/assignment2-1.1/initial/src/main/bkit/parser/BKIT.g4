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

//----------------Parser-----------------//
program  : declaration+ EOF ;
// declaration: (var_declare+ func_declare*)| (var_declare* func_declare+);
declaration: vardeclare|funcdeclare;
//-----------Declare variable------------//
vardeclare: VAR COLON varlist SEMI ;
varlist: varinit (COMMA varinit)* ;
varinit: var (ASSIGN valuelist)*;
valuelist: litlist;
var: ID (LSB INTLIT RSB)*;

//-----------Declare function-------------//
funcdeclare: FUNCTION COLON ID paralist? blockstm ;
paralist: PARAMETER COLON var (COMMA var)*;
// blockstm: BODY COLON vardeclare* stm* ENDBODY DOT;
blockstm: BODY COLON var_decl_and_stm ENDBODY DOT;
call_func: ID LPAREN (exp (COMMA exp)*)? RPAREN;
//-----------Statements-----------------//
stm: if_stm|for_stm|while_stm|do_while_stm|return_stm|continue_stm|break_stm|assign_stm|callfunc_stm;
var_decl_and_stm: vardeclare* stm*;
if_stm: IF exp THEN var_decl_and_stm (ELSEIF exp THEN var_decl_and_stm)* (ELSE var_decl_and_stm)? ENDIF DOT;
for_stm: FOR LPAREN ID ASSIGN exp COMMA exp COMMA exp RPAREN DO var_decl_and_stm ENDFOR DOT;
while_stm: WHILE exp DO var_decl_and_stm ENDWHILE DOT;
do_while_stm:DO var_decl_and_stm WHILE exp ENDDO DOT ;
return_stm: RETURN exp? SEMI;
continue_stm: CONTINUE SEMI;
break_stm: BREAK SEMI;
// assign_stm: (paralist|varlist|arrayvar) ASSIGN exp SEMI;
assign_stm: ID|exp6 ASSIGN exp SEMI;
callfunc_stm: call_func SEMI;


//-----------Expression------------------//
exp: exp1 (EQ|INEQ|ILT|IGT|ILTOEQ|IGTOEQ|FNEQ|FLT|FGLT|FLTOEQ|FGTOEQ) exp1|exp1;
exp1: exp1 (AND|OR) exp2|exp2;
exp2: exp2 (INTADD|FLOATADD|INTSIGNNEG|FLOATSIGNNEG) exp3|exp3;
exp3: exp3 (INTMUL|FLOATMUL|INTDIV|FLOATDIV|INTREM) exp4|exp4;
exp4: (NEG) exp4|exp5;
exp5: (INTSIGNNEG|FLOATSIGNNEG) exp5|exp6;
exp6: exp6 (LSB exp RSB)+ |exp7;
exp7: ID LPAREN (exp (COMMA exp)*)? RPAREN|exp8;
exp8: LPAREN exp RPAREN|operand;
operand: litlist|ID;


    



//---------------- Lexer ----------------//
//-----------------Identifier------------//
ID: (Lowercase)(Lowercase|Uppercase|Digit|Underscore)* ;
//----------------Comment----------------//
COMMENTLINE: '**' .*? '**'->skip;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

//---------------- Keyword --------------//
BODY: 'Body';
ELSE: 'Else';
ENDFOR: 'EndFor';
IF: 'If';
VAR: 'Var';
ENDDO: 'EndDo';
BREAK: 'Break';
ELSEIF: 'ElseIf';
ENDWHILE: 'EndWhile';
PARAMETER: 'Parameter';
WHILE: 'While';
CONTINUE: 'Continue';
ENDBODY: 'EndBody';
FOR: 'For';
RETURN: 'Return';
TRUE: 'True';
DO: 'Do';
ENDIF: 'EndIf';
FUNCTION: 'Function';
THEN: 'Then';
FALSE: 'False';
//------------Operator------------------//

INTADD: '+';
FLOATADD: '+.';
INTSIGNNEG: '-';
FLOATSIGNNEG: '-.';
INTMUL: '*';
FLOATMUL: '*.';
INTDIV: '\\';
FLOATDIV: '\\.';
INTREM: '%';
ASSIGN: '=';

NEG: '!';
AND: '&&';
OR: '||';

EQ: '==';
INEQ: '!=';
ILT: '<';
IGT: '>';
ILTOEQ: '<=';
IGTOEQ: '>=';
FNEQ:'=/=';
FLT: '<.';
FGLT: '>.';
FLTOEQ: '<=.';
FGTOEQ: '>=.';



//--------------Separators--------------//
LSB: '[';
RSB: ']';
SEMI: ';' ;
COLON: ':' ;
COMMA: ',';
LBRACE: '{';
RBRACE: '}';
DOT: Dot;
LPAREN: '(';
RPAREN: ')'; 
//-------------Literals--------------------//
INTLIT: ('0'|[1-9]Digit*|'0'[xX](Digit|[A-F])+|'0'[oO][0-7]+);
FLOATLIT: (Digit+ Dot Digit* Expoment?|Digit+ Dot Digit+ Expoment?|Digit+ Expoment);

BOOLEANLIT: TRUE|FALSE;
STRINGLIT: UnternimatedStringLitter '"'{
    temp = str(self.text)
    self.text = temp[1:-1]
};
litlist: INTLIT|FLOATLIT|TRUE|FALSE|STRINGLIT|arraylist;
arraylist: LBRACE (litlist (COMMA litlist)*)? RBRACE;

//---------------Error Token---------------///

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