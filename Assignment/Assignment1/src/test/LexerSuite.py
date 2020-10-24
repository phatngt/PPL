import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    def test_comment(self):
        self.assertTrue(TestLexer.checkLexeme(""" **This is a comment** ""","""<EOF>""",100))
    def test_id(self):
        self.assertTrue(TestLexer.checkLexeme(""" a aABC a123 abcABC123 ""","""a,aABC,a123,abcABC123,<EOF>""",101))
    def test_keyword(self):
        self.assertTrue(TestLexer.checkLexeme(""" Body Else EndFor If Var EndDo Break ElseIf EndWhile Parameter While Continue EndBody For Return True Do EndIf Function Then False""",
        """Body,Else,EndFor,If,Var,EndDo,Break,ElseIf,EndWhile,Parameter,While,Continue,EndBody,For,Return,True,Do,EndIf,Function,Then,False,<EOF>""",102))
    def test_operator(self):
        self.assertTrue(TestLexer.checkLexeme("""+ +. - -. * *. \\ \\. % ! == != < > <= >= =/= <. >. <=. >=.""",
        """+,+.,-,-.,*,*.,\\,\\.,%,!,==,!=,<,>,<=,>=,=/=,<.,>.,<=.,>=.,<EOF>""",103))
    def test_bracket(self):
        self.assertTrue(TestLexer.checkLexeme(""" [ ] ; : , { } ( ) ""","""[,],;,:,,,{,},(,),<EOF>""",104))
    def test_int(self):
        self.assertTrue(TestLexer.checkLexeme(""" 0 1 2 3 4 12 123 0x123ABC 0X1234 0o1234 0O1234 ""","""0,1,2,3,4,12,123,0x123ABC,0X1234,0o1234,0O1234,<EOF>""",105))
    def test_float(self):
        self.assertTrue(TestLexer.checkLexeme(""" 12.0 12. 12.0e5 12.0E5 12.e3 12.E3 12.e5 12.E5 1200e-1 1200E-1 0.""","""12.0,12.,12.0e5,12.0E5,12.e3,12.E3,12.e5,12.E5,1200e-1,1200E-1,0.,<EOF>""",106))
    def test_string(self):
        self.assertTrue(TestLexer.checkLexeme('"abcdxyz" "123abcd"',"""abcdxyz,123abcd,<EOF>""",107))
    def test_boolean(self):
        self.assertTrue(TestLexer.checkLexeme("""True False""","""True,False,<EOF>""",108))
    def test_array(self):
        self.assertTrue(TestLexer.checkLexeme("""{} {12} {12,12} {12.1,12.2} {"abc","dcf"} {True,False,True} {{12,13},{12,13}} """,
        """{,},{,12,},{,12,,,12,},{,12.1,,,12.2,},{,abc,,,dcf,},{,True,,,False,,,True,},{,{,12,,,13,},,,{,12,,,13,},},<EOF>""",109))
    def test_array1(self):
        self.assertTrue(TestLexer.checkLexeme("""{1,"12"} {"abc" ,True} {12.1,True} {11.1,11}""",
        """{,1,,,12,},{,abc,,,True,},{,12.1,,,True,},{,11.1,,,11,},<EOF>""",110 ))
    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("ab?svn","ab,Error Token ?",111))
    def test_unclosed_string(self):
        self.assertTrue(TestLexer.checkLexeme(""" "this is""","""Unclosed String: this is""",112))
    
    #normal test
    def test_integer_literal(self):
        self.assertTrue(TestLexer.checkLexeme(r'''00001 00123 ''',r'''0,0,0,0,1,0,0,123,<EOF>''',113))
    def test_integer_literal16(self):
        self.assertTrue(TestLexer.checkLexeme(r'''00x123A 00XAAA 0xAGH''',r'''0,0x123A,0,0XAAA,0xA,Error Token G''',114))
    def test_integer_literal8(self):
        self.assertTrue(TestLexer.checkLexeme(r''' 00o123 00O123 0o789 ''', r'''0,0o123,0,0O123,0o7,89,<EOF>''', 115))
    def test_float_literal(self):
        self.assertTrue(TestLexer.checkLexeme(r''' . .0 a.1 1.a 1e ''',r'''.,.,0,a,.,1,1.,a,1,e,<EOF>''',116))
    def test_float_literal1(self):
        self.assertTrue(TestLexer.checkLexeme(r''' 000.000 12ea 12.e1a 12.00a ''',r'''000.000,12,ea,12.e1,a,12.00,a,<EOF>''',117))
    def test_string_literal(self):
        self.assertTrue(TestLexer.checkLexeme(r''' "abc '""''',r'''abc '",<EOF>''',118))
    def test_string_literal1(self):
        self.assertTrue(TestLexer.checkLexeme(r''' "abc     
        "''',r'''Unclosed String: abc     ''',119)) 
    def test_string_literal2(self):
        self.assertTrue(TestLexer.checkLexeme(r''' "abc '" ''',r'''Unclosed String: abc '" ''',120))
    def test_string_literal3(self):
        self.assertTrue(TestLexer.checkLexeme(r''' "abc \'\' cdf " ''',r'''abc \'\' cdf ,<EOF>''',121))
    def test_array_literal(self):
        self.assertTrue(TestLexer.checkLexeme(r''' {{{{{{{"a"}}}}}}} ''',r'''{,{,{,{,{,{,{,a,},},},},},},},<EOF>''',122))
    def test_array_literal1(self):
        self.assertTrue(TestLexer.checkLexeme(r''' {{{{{{{{{{{1,2}} ''',r'''{,{,{,{,{,{,{,{,{,{,{,1,,,2,},},<EOF>''',123))
    def test_var_decl(self):
        self.assertTrue(TestLexer.checkLexeme(r''' Var: x; Var: x,y,z; ''' , r'''Var,:,x,;,Var,:,x,,,y,,,z,;,<EOF>''', 124))
    def test_var_decl1(self):
        self.assertTrue(TestLexer.checkLexeme(r''' Var: x = 10; Var: r = 10,x;''',r'''Var,:,x,=,10,;,Var,:,r,=,10,,,x,;,<EOF>''',125))
    def test_var_decl2(self):
        self.assertTrue(TestLexer.checkLexeme(r''' Var: x[1]; Var: a[1][2];''',r'''Var,:,x,[,1,],;,Var,:,a,[,1,],[,2,],;,<EOF>''',126))
    def test_var_decl3(self):
        self.assertTrue(TestLexer.checkLexeme(r''' Var: x[1][2] = 1;''',r'''Var,:,x,[,1,],[,2,],=,1,;,<EOF>''',127 ))
    def test_func_decl(self):
        self.assertTrue(TestLexer.checkLexeme(r''' Function: fact Parameter: a,b,c Body: EndBody.''',r'''Function,:,fact,Parameter,:,a,,,b,,,c,Body,:,EndBody,.,<EOF>''',128))
    def test_func_decl1(self):
        self.assertTrue(TestLexer.checkLexeme(r''' Functio1: fact Parameter: a,b,c Body: EndBody.''', r'''Error Token F''',129))
    def test_func_decl2(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''Function: Foo
                    Parameter: x
                    Body:
                    EndBody. ''',
            r'''Function,:,Error Token F''',
            130
        ))
    def test_func_decl3(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''Function: foo
                    Parameter: X,y
                    Body:
                    EndBody. ''',
            r'''Function,:,foo,Parameter,:,Error Token X''',
            131
        ))
    #Test stm
    def test_if_stm(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''If n == 0 Then
                    Return 1;
                EndIf.''',
            r'''If,n,==,0,Then,Return,1,;,EndIf,.,<EOF>''',132))
    def test_if_stm1(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''If 1 >. 2 Then
                    Return 1;
                Else 
                    Return 2;
                EndIf.''',
            r'''If,1,>.,2,Then,Return,1,;,Else,Return,2,;,EndIf,.,<EOF>''',133))
    def test_if_stm2(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''If 1 < 2 Then
                    Return 1;
                ElseIf 1>3 Then
                    Return 3;
                Else
                    Return 5;
                EndIf.''',
            r'''If,1,<,2,Then,Return,1,;,ElseIf,1,>,3,Then,Return,3,;,Else,Return,5,;,EndIf,.,<EOF>''',134))
    def test_for_stm(self):
        self.assertTrue(TestLexer.checkLexeme(
            r''' For (i = 2, i < 10, 2) Do
                    writeln(i);
                EndFor.''',
            r'''For,(,i,=,2,,,i,<,10,,,2,),Do,writeln,(,i,),;,EndFor,.,<EOF>''',135))
    def test_for_stm1(self):
        self.assertTrue(TestLexer.checkLexeme(
            r''' FoR ( i = 2, i > 10, 4) Do:
                    writeln(i);
                EndFor. ''',
            r'''Error Token F''',
            136
        ))
    def test_while_smt(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''While i > 0 Do Return 1; EndWhile. ''',
            r'''While,i,>,0,Do,Return,1,;,EndWhile,.,<EOF>''',
            137
        ))
    def test_while_stm(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''WhIle i > 0 Do Return 1; EndWhile. ''',
            r'''Error Token W''',
            138
        ))
    def test_do_while_stm(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''Do a = 1; b = 2; i= i + 1; While i < 10 EndDo.''',
            r'''Do,a,=,1,;,b,=,2,;,i,=,i,+,1,;,While,i,<,10,EndDo,.,<EOF>''',
            139
        ))
    def test_do_while_stm(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''DO a = 1; b = 2; i= i + 1; While i < 10 EndDo.''',
            r'''Error Token D''',
            140
        ))
    def test_some_stm(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''For( i = 0, i < 10, 2) Do:
                    If i == 5 Then
                        Break;
                    ElseIf i < 5
                        Continue;
                    Else
                        Return 1;
                    EndIf.
                EndFor.  ''',
            r'''For,(,i,=,0,,,i,<,10,,,2,),Do,:,If,i,==,5,Then,Break,;,ElseIf,i,<,5,Continue,;,Else,Return,1,;,EndIf,.,EndFor,.,<EOF>''',
            141))
    def test_some_stm1(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''For( i = 0, i < 10, 2) Do:
                    If i == 5 Then
                        BreaK;
                    ElseIf i < 5
                        Continue;
                    Else
                        Return 1;
                    EndIf.
                EndFor.  ''',
            r'''For,(,i,=,0,,,i,<,10,,,2,),Do,:,If,i,==,5,Then,Error Token B''',
            142))
    def test_some_stm2(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''For( i = 0, i < 10, 2) Do:
                    If i == 5 Then
                        Break;
                    ElseIf i < 5
                        ContinuE;
                    Else
                        Return 1;
                    EndIf.
                EndFor.  ''',
            r'''For,(,i,=,0,,,i,<,10,,,2,),Do,:,If,i,==,5,Then,Break,;,ElseIf,i,<,5,Error Token C''',
            143))
    def test_some_stm3(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''For( i = 0, i < 10, 2) Do:
                    If i == 5 Then
                        Break;
                    ElseIf i < 5
                        Continue;
                    Else
                        ReturN 1;
                    EndIf.
                EndFor.  ''',
            r'''For,(,i,=,0,,,i,<,10,,,2,),Do,:,If,i,==,5,Then,Break,;,ElseIf,i,<,5,Continue,;,Else,Error Token R''',
            144))
    def test_call_func(self):
        self.assertTrue(TestLexer.checkLexeme(
            r''' Function: foo
                    Parameter:
                    Body:
                        foo(x,y,z);
                    EndBody. ''',
            r'''Function,:,foo,Parameter,:,Body,:,foo,(,x,,,y,,,z,),;,EndBody,.,<EOF>''',
            145
        ))
    def test_call_func1(self):
        self.assertTrue(TestLexer.checkLexeme(
            r''' Function: foo
                    Parameter:
                    Body:
                        Foo(x,y,z);
                    EndBody. ''',
            r'''Function,:,foo,Parameter,:,Body,:,Error Token F''',
            146
        ))
    def test_call_func2(self):
        self.assertTrue(TestLexer.checkLexeme(
            r''' Function: foo
                    Parameter:
                    Body:
                        foo(X,y,z);
                    EndBody. ''',
            r'''Function,:,foo,Parameter,:,Body,:,foo,(,Error Token X''',
            147
        ))
    #mix test
    def test_mix(self):
        self.assertTrue(TestLexer.checkLexeme(
        r''' Function: fact
                Parameter: a,b,c
                Body:
                    If n == 0 Then
                        Return 1;
                EndBody. ''',
        r'''Function,:,fact,Parameter,:,a,,,b,,,c,Body,:,If,n,==,0,Then,Return,1,;,EndBody,.,<EOF>''',148))
    def test_mix1(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''Var: x = 10;
                If x == 10 Then 
                    printLn("Goodbye world");
                EndIf. ''',
            r'''Var,:,x,=,10,;,If,x,==,10,Then,printLn,(,Goodbye world,),;,EndIf,.,<EOF>''',
            149
        ))
    def test_mix2(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''Var: x,y[1][2] = 10,{{1,"abc"},{2.0,True}};
                For(i = 0, i < x, i=i+1) Do
                    y[1][1] = 2;
                EndFor. ''',
            r'''Var,:,x,,,y,[,1,],[,2,],=,10,,,{,{,1,,,abc,},,,{,2.0,,,True,},},;,For,(,i,=,0,,,i,<,x,,,i,=,i,+,1,),Do,y,[,1,],[,1,],=,2,;,EndFor,.,<EOF>''',
            150
        ))
    def test_mix3(self):
        self.assertTrue(TestLexer.checkLexeme(
            r''' ** Computer balble **
                Var: x[1][1][1][1] = {{{{2}}}}};
                Function: foo
                    Parameter: x,y,z
                    Body:
                        printLn(x[1][1][1][1]);
                    EndBody. ''',
            r'''Var,:,x,[,1,],[,1,],[,1,],[,1,],=,{,{,{,{,2,},},},},},;,Function,:,foo,Parameter,:,x,,,y,,,z,Body,:,printLn,(,x,[,1,],[,1,],[,1,],[,1,],),;,EndBody,.,<EOF>''',
            151
        ))
    def test_mix4(self):
        self.assertTrue(TestLexer.checkLexeme(
        r''' Function: fact
                Parameter: a,b,c
                Body:
                    func(True);
                EndBody. ''',
        r'''Function,:,fact,Parameter,:,a,,,b,,,c,Body,:,func,(,True,),;,EndBody,.,<EOF>''',152))
    def test_mix5(self):
        self.assertTrue(TestLexer.checkLexeme(
        r''' Function: fact
                Parameter: a,b,c
                Body:
                    func(True);
                    print((((((()))))));
                EndBody. ''',
        r'''Function,:,fact,Parameter,:,a,,,b,,,c,Body,:,func,(,True,),;,print,(,(,(,(,(,(,(,),),),),),),),;,EndBody,.,<EOF>''',153))
    def test_mix6(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''Var: x = 1;
                Var: y,z = 2,3;
                Function: foo 
                    Parameter:a[1],a,b,c
                    Body:
                        Var: x,y;
                        Var:z;
                        For (i = 0, i < 10,i+1) Do
                            Var: x = 1;
                            printLn();
                            Var: a,b;
                        EndFor.
                    EndBody. ''',
            r'''Var,:,x,=,1,;,Var,:,y,,,z,=,2,,,3,;,Function,:,foo,Parameter,:,a,[,1,],,,a,,,b,,,c,Body,:,Var,:,x,,,y,;,Var,:,z,;,For,(,i,=,0,,,i,<,10,,,i,+,1,),Do,Var,:,x,=,1,;,printLn,(,),;,Var,:,a,,,b,;,EndFor,.,EndBody,.,<EOF>''',154))
    def test_mix7(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''Var: x = -1;
                    Function: foo 
                        Parameter:a[1]
                        Body:
                        EndBody. ''',
            r'''Var,:,x,=,-,1,;,Function,:,foo,Parameter,:,a,[,1,],Body,:,EndBody,.,<EOF>''',
            155
        ))
    def test_mix8(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''Var: x = 1;
                    Function: foo 
                        Parameter:a[1]
                        Body:
                        EndBody.
                    Var: y = 2; ''',
            r'''Var,:,x,=,1,;,Function,:,foo,Parameter,:,a,[,1,],Body,:,EndBody,.,Var,:,y,=,2,;,<EOF>''',
            156
        ))
    def test_mix9(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''Var: x = 1;
                    Function: foo 
                        Parameter:a[1]
                        Body:
                            Var: x,y;
                            Var:z;
                            If n == 0 Then
                                Var:Z;
                            ElseIf n == 0 Then
                                Var:a;
                            Else
                                Var:b;
                            EndIf.
                        EndBody. ''',
            r'''Var,:,x,=,1,;,Function,:,foo,Parameter,:,a,[,1,],Body,:,Var,:,x,,,y,;,Var,:,z,;,If,n,==,0,Then,Var,:,Error Token Z''',
            157
        ))
    def test_mix10(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''Var: x = 1;
                    Var: y,z = 2,3;
                    Function: foo 
                        Parameter:a[1]
                        Body:
                            Var: x,y;
                            Var:z;
                            If n == 0 Then
                                Var:z;
                            ElseIf n == 0 Then
                                Var:_aA;
                            Else
                                Var:b;
                            EndIf.
                        EndBody. ''',
            r'''Var,:,x,=,1,;,Var,:,y,,,z,=,2,,,3,;,Function,:,foo,Parameter,:,a,[,1,],Body,:,Var,:,x,,,y,;,Var,:,z,;,If,n,==,0,Then,Var,:,z,;,ElseIf,n,==,0,Then,Var,:,Error Token _''',
            158
        ))
    def test_mix11(self):
        self.assertTrue(TestLexer.checkLexeme(
            r''' Var: x = 1;
                 Var: y,z = 2,"3; ''',
            r'''Var,:,x,=,1,;,Var,:,y,,,z,=,2,,,Unclosed String: 3; ''',
            159
        ))
    def test_mix12(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''Var: x = 0x1234ABC;
                    Var: y,z = 2,0o12AB;
                    Function: foo 
                        Parameter:a[1],a,b,c
                        Body:
                            Var: x,y;
                            Var:z;
                            If n == 0 Then
                                Var:z;
                            ElseIf n == 0 Then
                                Var:a;
                            Else
                                Var:b;
                            EndIf.
                            Var: d,f;
                        EndBody. ''',
            r'''Var,:,x,=,0x1234ABC,;,Var,:,y,,,z,=,2,,,0o12,Error Token A''',
            160
        ))
    def test_mix13(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''Var: x = 1;
                    Var: y,z = 2,{{{{{{{{{3}}}}}}}}};
                    Function: foo 
                        Parameter:a[1],a,b,c
                        Body:
                            Var: x,y;
                            Var:z;
                            If n == 0 Then
                                Var:z;
                                Var:b;
                            ElseIf n == 0 Then
                                Var:a;
                                a = 1;
                                Var: x = 9;
                            Else
                                Var:b;
                            EndIf.
                        EndBody. ''',
            r'''Var,:,x,=,1,;,Var,:,y,,,z,=,2,,,{,{,{,{,{,{,{,{,{,3,},},},},},},},},},;,Function,:,foo,Parameter,:,a,[,1,],,,a,,,b,,,c,Body,:,Var,:,x,,,y,;,Var,:,z,;,If,n,==,0,Then,Var,:,z,;,Var,:,b,;,ElseIf,n,==,0,Then,Var,:,a,;,a,=,1,;,Var,:,x,=,9,;,Else,Var,:,b,;,EndIf,.,EndBody,.,<EOF>''',
            161
        ))
    def test_mix14(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''Var: x = 1;
                    Var: y,z = 2,3;
                    Function: foo 
                        Parameter:a[1],a,b,c
                        Body:
                            Var: x,y;
                            Var:z;
                            For (i = 0, i < 10,i+1) Do
                                Var: x = 1;
                                printLn();
                                Var: a,b;
                            EndFor.
                        EndBody. ''',
            r'''Var,:,x,=,1,;,Var,:,y,,,z,=,2,,,3,;,Function,:,foo,Parameter,:,a,[,1,],,,a,,,b,,,c,Body,:,Var,:,x,,,y,;,Var,:,z,;,For,(,i,=,0,,,i,<,10,,,i,+,1,),Do,Var,:,x,=,1,;,printLn,(,),;,Var,:,a,,,b,;,EndFor,.,EndBody,.,<EOF>''',
            162
        ))
    def test_mix15(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''Var: x = 1;
                    Var: y,z = 2,3;
                    Function: foo 
                        Parameter:a[1],a,b,c
                        Body:
                            Var: x,y;
                            Var:z;
                            Do 
                                Var: x,y;
                                x = x+.+1;
                                y = y+1;
                            While (x < 10)&(y<5)
                            EndDo.
                        EndBody. ''',
            r'''Var,:,x,=,1,;,Var,:,y,,,z,=,2,,,3,;,Function,:,foo,Parameter,:,a,[,1,],,,a,,,b,,,c,Body,:,Var,:,x,,,y,;,Var,:,z,;,Do,Var,:,x,,,y,;,x,=,x,+.,+,1,;,y,=,y,+,1,;,While,(,x,<,10,),Error Token &''',
            163
        ))
    def test_mix16(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''Var: x = 1;
                    Var: y,z = 2,3;
                    Function: foo 
                        Parameter:a[1],a,b,c
                        Body:
                            Var: x,y;
                            Var:z;
                            Do 
                                Var: x,y;
                                x = x+1+"abc"+True+12.0+{"a","b"};
                                y = y+1+"True \n\f\g\h;
                            While (x < 10)&&(y<5)
                            EndDo.
                        EndBody.''',
            r'''Var,:,x,=,1,;,Var,:,y,,,z,=,2,,,3,;,Function,:,foo,Parameter,:,a,[,1,],,,a,,,b,,,c,Body,:,Var,:,x,,,y,;,Var,:,z,;,Do,Var,:,x,,,y,;,x,=,x,+,1,+,abc,+,True,+,12.0,+,{,a,,,b,},;,y,=,y,+,1,+,Illegal Escape In String: True \n\f\g''',
            164
        ))
    def test_mix18(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''Var: x = 1;
                    Var: y,z = 2,3;
                    Function: foo 
                        Parameter:a[1],             a           ,           b           ,           c
                        Body:
                            Var: x,y;
                            Var:z;
                            While i < 10 Do
                                Var: x,y;
                                x = x+1 + "                     123";
                                y = y+1 + "1234'";
                            EndWhile.
                        EndBody.''',
            r'''Var,:,x,=,1,;,Var,:,y,,,z,=,2,,,3,;,Function,:,foo,Parameter,:,a,[,1,],,,a,,,b,,,c,Body,:,Var,:,x,,,y,;,Var,:,z,;,While,i,<,10,Do,Var,:,x,,,y,;,x,=,x,+,1,+,                     123,;,y,=,y,+,1,+,Unclosed String: 1234'";''',
            165
        ))
    def test_mix19(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''Var: x = 1;
                    Var: y,z = 2,3;
                    Function: foo 
                        Parameter:a[0x123ABC][0o12345],a,b,c
                        Body:
                            Var: x,y;
                            Var:z;
                            Do
                                Var: x,y;
                                x = x+1 + ** Error here?? \b\r\n\f\t\'\\**;
                                y = y+1 + **This is cmnt? Right,hihi ;
                                Var:a;
                            While x < 0x123A
                            EndDo.
                        EndBody. ''',
            r'''Var,:,x,=,1,;,Var,:,y,,,z,=,2,,,3,;,Function,:,foo,Parameter,:,a,[,0x123ABC,],[,0o12345,],,,a,,,b,,,c,Body,:,Var,:,x,,,y,;,Var,:,z,;,Do,Var,:,x,,,y,;,x,=,x,+,1,+,;,y,=,y,+,1,+,Unterminated Comment''',
            166
        ))
    def test_mix20(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''Var: x = 1;
                    Var: y,z = 2,3;
                    Function: foo 
                        Parameter:a[1],a,b,c
                        Body:
                            Var: x,y;
                            Var:z;
                            For( i = a(),i < b(),c()) Do
                                Return d();
                            EndFor.
                        EndBody.
                    Function: facb1234__
                        Parameter: a,b,c
                        BOdy:
                            Var: x,y;
                            foo(c,b,a);
                            Return 1;
                        EndBody. ''',
            r'''Var,:,x,=,1,;,Var,:,y,,,z,=,2,,,3,;,Function,:,foo,Parameter,:,a,[,1,],,,a,,,b,,,c,Body,:,Var,:,x,,,y,;,Var,:,z,;,For,(,i,=,a,(,),,,i,<,b,(,),,,c,(,),),Do,Return,d,(,),;,EndFor,.,EndBody,.,Function,:,facb1234__,Parameter,:,a,,,b,,,c,Error Token B''',
            167
        ))
    def test_mix21(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''Function: foo 
                        Parameter:a = c(),b
                        Body:
                            a = c()+d()+f();
                            For( i = a(),i < b(),c()) Do
                                Return d(**This is cmt \t\n\f\r**"abc""aaa'");
                            EndFor.
                            Return a;
                        EndBody. ''',
            r'''Function,:,foo,Parameter,:,a,=,c,(,),,,b,Body,:,a,=,c,(,),+,d,(,),+,f,(,),;,For,(,i,=,a,(,),,,i,<,b,(,),,,c,(,),),Do,Return,d,(,abc,Unclosed String: aaa'");''',
            168
        ))
    ######
    def test_mix22(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''Function: main
                        Parameter:
                        Body:
                            foo((1+2*(3-0x1\\(12.0 -. 0o1236*(True+"abc"\\.(**This is cmt***.12e1))))),2,3);
                        EndBody. ''',
            r'''Function,:,main,Parameter,:,Body,:,foo,(,(,1,+,2,*,(,3,-,0x1,\,\,(,12.0,-.,0o1236,*,(,True,+,abc,\,\.,(,*.,12e1,),),),),),,,2,,,3,),;,EndBody,.,<EOF>''',
            169
        ))
    def test_mix23(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''Function: foo 
                        Parameter:a,b
                        Body:
                            a = c()+d()+.f();
                            b = (c(d(e(f(g(1))))));
                            For( i = a(),i < b(),c()) Do
                                Return d();
                            EndFor.
                            Return a;
                        EndBody. ''',
            r'''Function,:,foo,Parameter,:,a,,,b,Body,:,a,=,c,(,),+,d,(,),+.,f,(,),;,b,=,(,c,(,d,(,e,(,f,(,g,(,1,),),),),),),;,For,(,i,=,a,(,),,,i,<,b,(,),,,c,(,),),Do,Return,d,(,),;,EndFor,.,Return,a,;,EndBody,.,<EOF>''',
            170
        ))
    def test_mix24(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''Function: foo 
                        Parameter:a,b
                        Body:
                            a = c()+d()+f();
                            ** Cmt ** 
                            b = (c(d(e(f(g(1-2)*3)\\4)%5)+6));
                            For( i = a(),i < b(),c()) Do
                                Return d();
                            EndFor.
                            Return a;
                        EndBody. ''',
            r'''Function,:,foo,Parameter,:,a,,,b,Body,:,a,=,c,(,),+,d,(,),+,f,(,),;,b,=,(,c,(,d,(,e,(,f,(,g,(,1,-,2,),*,3,),\,\,4,),%,5,),+,6,),),;,For,(,i,=,a,(,),,,i,<,b,(,),,,c,(,),),Do,Return,d,(,),;,EndFor,.,Return,a,;,EndBody,.,<EOF>''',
            171
        ))
    def test_mix25(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''Function: foo 
                        Parameter:a,b
                        Body:
                            a = c()+d()+f();
                            ** Cmt \r\b\t\f\n** 
                            b = (c(d(e(f(g(1-2)*3)\\4)%5)+6));
                            For( i = a(****),i < b(**Cmt \r\b\t\f\n**),c()) Do
                                Return d();
                            EndFor.
                            Return a;
                        EndBody.''',
            r'''Function,:,foo,Parameter,:,a,,,b,Body,:,a,=,c,(,),+,d,(,),+,f,(,),;,b,=,(,c,(,d,(,e,(,f,(,g,(,1,-,2,),*,3,),\,\,4,),%,5,),+,6,),),;,For,(,i,=,a,(,),,,i,<,b,(,),,,c,(,),),Do,Return,d,(,),;,EndFor,.,Return,a,;,EndBody,.,<EOF>''',
            172
        ))
    def test_mix26(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''Var: x = 1;
                    Var: y,z = 2,3;
                    Function: foo 
                        Parameter:a,b
                        Body:
                            a = c()+d()+f();
                            ** Cmt \r\b\t\f\n** 
                            b = (c(d(e(f(g(1-2)*3)\\4)%5)+6));
                            For( i = a(****),i < b(**Cmt \r\b\t\f\n**),c("'"'"")) Do
                                Return d();
                            EndFor.
                            Return a;
                        EndBody.''',
            r'''Var,:,x,=,1,;,Var,:,y,,,z,=,2,,,3,;,Function,:,foo,Parameter,:,a,,,b,Body,:,a,=,c,(,),+,d,(,),+,f,(,),;,b,=,(,c,(,d,(,e,(,f,(,g,(,1,-,2,),*,3,),\,\,4,),%,5,),+,6,),),;,For,(,i,=,a,(,),,,i,<,b,(,),,,c,(,'"'",),),Do,Return,d,(,),;,EndFor,.,Return,a,;,EndBody,.,<EOF>''',
            173
        ))
    def test_mix27(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''Function: foo 
                        Parameter:a,b
                        Body:
                            a = c()+d()+f();
                            ** Cmt \r\b\t\f\n** 
                            b = (c(d(e(f(g(1-2)*3)\\4)%5)+6));
                            For( i = a(****),i < b(**Cmt \r\b\t\f\n**),c("'"'")) Do
                                Return d();
                            EndFor.
                            Return a;
                        EndBody. ''',
            r'''Function,:,foo,Parameter,:,a,,,b,Body,:,a,=,c,(,),+,d,(,),+,f,(,),;,b,=,(,c,(,d,(,e,(,f,(,g,(,1,-,2,),*,3,),\,\,4,),%,5,),+,6,),),;,For,(,i,=,a,(,),,,i,<,b,(,),,,c,(,Unclosed String: '"'")) Do''',
            174
        ))
    def test_mix28(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''Function: foo 
                        Parameter:a,b
                        Body:
                            a = c()+d()+f();
                            ** Cmt \r\b\t\f\n** 
                            b = (c(d(e(f(g(1-2)*3)\\4)%5)+6));
                            While ((i + 5) >=. 7)&&(9-(8*9\\.9) +. 6)||(7-.4%5+9*.6) Do
                                printLn("Goodbye world");
                            EndWhile.
                            Return a;
                        EndBody. ''',
            r'''Function,:,foo,Parameter,:,a,,,b,Body,:,a,=,c,(,),+,d,(,),+,f,(,),;,b,=,(,c,(,d,(,e,(,f,(,g,(,1,-,2,),*,3,),\,\,4,),%,5,),+,6,),),;,While,(,(,i,+,5,),>=.,7,),&&,(,9,-,(,8,*,9,\,\.,9,),+.,6,),||,(,7,-.,4,%,5,+,9,*.,6,),Do,printLn,(,Goodbye world,),;,EndWhile,.,Return,a,;,EndBody,.,<EOF>''',
            175
        ))
    def test_mix29(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''Var: x = 1;
                    Var: y,z[12.0] = 2,3;
                    Function: main
                        Parameter:
                        Body:
                            foo(1,2,3,print("abc"));
                        EndBody.''',
            r'''Var,:,x,=,1,;,Var,:,y,,,z,[,12.0,],=,2,,,3,;,Function,:,main,Parameter,:,Body,:,foo,(,1,,,2,,,3,,,print,(,abc,),),;,EndBody,.,<EOF>''',
            176
        ))
    def test_mix30(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''Var: x = 1;
                    Var: y,z = 2,3;
                    Function: foo 
                        Parameter:a,b
                        Body:
                            a = c()+d()+f();
                            ** Cmt \r\b\t\f\n** 
                            b = (c(d(e(f(g(1-2)*3)\\4)%5)+6));
                            While ((i + 5) >=. 7)&&(9-(8*9\\.9) +. 6)||(7-.4%5+9*.6) Do
                                printLn("Goodbye world");
                            EndWhile.
                            Return a;
                        EndBody.
                    Function: main
                        Parameter:
                        Body:
                            foo(1,2,3);
                        EndBody.''',
            r'''Var,:,x,=,1,;,Var,:,y,,,z,=,2,,,3,;,Function,:,foo,Parameter,:,a,,,b,Body,:,a,=,c,(,),+,d,(,),+,f,(,),;,b,=,(,c,(,d,(,e,(,f,(,g,(,1,-,2,),*,3,),\,\,4,),%,5,),+,6,),),;,While,(,(,i,+,5,),>=.,7,),&&,(,9,-,(,8,*,9,\,\.,9,),+.,6,),||,(,7,-.,4,%,5,+,9,*.,6,),Do,printLn,(,Goodbye world,),;,EndWhile,.,Return,a,;,EndBody,.,Function,:,main,Parameter,:,Body,:,foo,(,1,,,2,,,3,),;,EndBody,.,<EOF>''',
            177
        ))
    def test_mix31(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''Var: x = 1;
                    Var: y,z[12][1][1234567890000] = 2,3;
                    Function: main
                        Parameter:
                        Body:
                            foo(1[0x1245ABCDF],a(0o1234567),True);
                        EndBody.''',
            r'''Var,:,x,=,1,;,Var,:,y,,,z,[,12,],[,1,],[,1234567890000,],=,2,,,3,;,Function,:,main,Parameter,:,Body,:,foo,(,1,[,0x1245ABCDF,],,,a,(,0o1234567,),,,True,),;,EndBody,.,<EOF>''',
            178
        ))
    def test_mix32(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''Var: x = 1;
                    Var: y,z[12][1][1234567890000] = 2,3;
                    Function: main
                        Parameter:
                        Body:
                            Var: x,a = 1,"a";
                            a = !!!!!!!!!x;
                            a = x!!!!!!!!;
                            foo(a,a(0o1234567),True);
                        EndBody.''',
            r'''Var,:,x,=,1,;,Var,:,y,,,z,[,12,],[,1,],[,1234567890000,],=,2,,,3,;,Function,:,main,Parameter,:,Body,:,Var,:,x,,,a,=,1,,,a,;,a,=,!,!,!,!,!,!,!,!,!,x,;,a,=,x,!,!,!,!,!,!,!,!,;,foo,(,a,,,a,(,0o1234567,),,,True,),;,EndBody,.,<EOF>''',
            179
        ))
    def test_mix33(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''Var: x = 1;
                    Var: y,z[12][1][1234567890000] = 2,3;
                    Function: main
                        Parameter:
                        Body:
                            Var: x,a = 1,"a";
                            a = !!!!!!!!!x;
                            a = (a&&(&&b));
                            foo(a,a(0o1234567),True);
                        EndBody.''',
            r'''Var,:,x,=,1,;,Var,:,y,,,z,[,12,],[,1,],[,1234567890000,],=,2,,,3,;,Function,:,main,Parameter,:,Body,:,Var,:,x,,,a,=,1,,,a,;,a,=,!,!,!,!,!,!,!,!,!,x,;,a,=,(,a,&&,(,&&,b,),),;,foo,(,a,,,a,(,0o1234567,),,,True,),;,EndBody,.,<EOF>''',
            180
        ))
    def test_mix34(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''Var: x = 1;
                    Var: y,z[12][1][1234567890000] = 2,3;
                    Function: main
                        Parameter:
                        Body:
                            While (i-.(1&&(4||2)))=/=5>=.7 Do
                                printLn(1);
                                Continue;
                            EndWhile.
                        EndBody.''',
            r'''Var,:,x,=,1,;,Var,:,y,,,z,[,12,],[,1,],[,1234567890000,],=,2,,,3,;,Function,:,main,Parameter,:,Body,:,While,(,i,-.,(,1,&&,(,4,||,2,),),),=/=,5,>=.,7,Do,printLn,(,1,),;,Continue,;,EndWhile,.,EndBody,.,<EOF>''',
            181
        ))
    def test_mix35(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''Var: x = 1;
                    Var: y,z[12][1][1234567890000] = 2,3;
                    Function: main
                        Parameter:
                        Body:
                            While ((i-.(1&&(4||2)))=/=5)>=.7-. Do
                                printLn(1);
                                Continue;
                            EndWhile.
                        EndBody.''',
            r'''Var,:,x,=,1,;,Var,:,y,,,z,[,12,],[,1,],[,1234567890000,],=,2,,,3,;,Function,:,main,Parameter,:,Body,:,While,(,(,i,-.,(,1,&&,(,4,||,2,),),),=/=,5,),>=.,7,-.,Do,printLn,(,1,),;,Continue,;,EndWhile,.,EndBody,.,<EOF>''',
            182
        ))
    def test_mix36(self):
        self.assertTrue(TestLexer.checkLexeme(
            r''' Var: x = 1;
                    Var: y,z[12][1][1234567890000] = 2,3;
                    Function: main
                        Parameter:
                        Body:
                            While ((i-.(1&&(4||2)))=/=5)>=.7&& foo() Do
                                printLn(1);
                                Continue;
                            EndWhile.
                        EndBody.''',
            r'''Var,:,x,=,1,;,Var,:,y,,,z,[,12,],[,1,],[,1234567890000,],=,2,,,3,;,Function,:,main,Parameter,:,Body,:,While,(,(,i,-.,(,1,&&,(,4,||,2,),),),=/=,5,),>=.,7,&&,foo,(,),Do,printLn,(,1,),;,Continue,;,EndWhile,.,EndBody,.,<EOF>''',
            183
        ))
    def test_mix37(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''Var: x = 1;
                    Var: y,z[12][1][1234567890000] = 2,3;
                    Function: main
                        Parameter:
                        Body:
                            While ((i-.(1&&(4||2)))=/=5)>=.7&& foo() Do
                                printLn(1);
                                Continue;
                                If (n_123_ACV____ == 1e12123) || a[[[[[[["a"]]]]]]] Then
                                EndIf.
                            EndWhile.
                        EndBody.''',
            r'''Var,:,x,=,1,;,Var,:,y,,,z,[,12,],[,1,],[,1234567890000,],=,2,,,3,;,Function,:,main,Parameter,:,Body,:,While,(,(,i,-.,(,1,&&,(,4,||,2,),),),=/=,5,),>=.,7,&&,foo,(,),Do,printLn,(,1,),;,Continue,;,If,(,n_123_ACV____,==,1e12123,),||,a,[,[,[,[,[,[,[,a,],],],],],],],Then,EndIf,.,EndWhile,.,EndBody,.,<EOF>''',
            184
        ))
    def test_mix38(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''Function: foo 
                        Parameter:a[0x123ABC][0o12345],a,b,c
                        Body:
                            Var:a;
                            Var:a_;
                            Var:aB;
                            Var:a_B**This is cmt**;
                            Var:a123a_123A;
                            Var:a_b_123_B[123][0x123];
                        EndBody. ''',
            r'''Function,:,foo,Parameter,:,a,[,0x123ABC,],[,0o12345,],,,a,,,b,,,c,Body,:,Var,:,a,;,Var,:,a_,;,Var,:,aB,;,Var,:,a_B,;,Var,:,a123a_123A,;,Var,:,a_b_123_B,[,123,],[,0x123,],;,EndBody,.,<EOF>''',
            185
        ))
    def test_mix39(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''Var: x = 1;
                    Var: y,z = 2,3;
                    Function: foo 
                        Parameter:a[0x123ABC][0o12345],a,b,c
                        Body:
                            Var: x,y;
                            Var:z;
                            Do
                                Var: x,y;
                                x = x+1 + ** Error here?? \b\r\f\n\t\'\\** 1;
                                y = y+1 + **This is cmnt? Right,hihi**"abc"+True ;
                            While a[!!(x < 0x123A)][!!(1-1.0)b[15]] 
                            EndDo.
                        EndBody.''',
            r'''Var,:,x,=,1,;,Var,:,y,,,z,=,2,,,3,;,Function,:,foo,Parameter,:,a,[,0x123ABC,],[,0o12345,],,,a,,,b,,,c,Body,:,Var,:,x,,,y,;,Var,:,z,;,Do,Var,:,x,,,y,;,x,=,x,+,1,+,1,;,y,=,y,+,1,+,abc,+,True,;,While,a,[,!,!,(,x,<,0x123A,),],[,!,!,(,1,-,1.0,),b,[,15,],],EndDo,.,EndBody,.,<EOF>''',
            186
        ))
    def test_mix40(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''Function: foo 
                        PaRameter:a[0x123ABC][0o12345],a,b,c
                        Body:
                            While True Do 
                            EndWhile.
                            Do
                            While True 
                            EndDo.
                            If True Then
                            ElseIf True Then
                            Else
                            EndIf.
                            For(i=True,i<True,True) Do
                            EndFor.
                        EndBody.''',
            r'''Function,:,foo,Error Token P''',
            187
        ))
    def test_mix41(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''Function: foo 
                        Parameter:a[1]
                        Body:
                            b = a[1+2];
                            a[i+2] = (1+3)+4;
                            a = foo(30;
                            a = 0[10];
                        EndBody.''',
            r'''Function,:,foo,Parameter,:,a,[,1,],Body,:,b,=,a,[,1,+,2,],;,a,[,i,+,2,],=,(,1,+,3,),+,4,;,a,=,foo,(,30,;,a,=,0,[,10,],;,EndBody,.,<EOF>''',
            188
        ))
    def test_mix42(self):
        self.assertTrue(TestLexer.checkLexeme(
            r''' Function: foo 
                        Parameter:a[1]
                        Body:
                            b = a[1+2];
                            a[i+2] = (1+3)+4;
                            a = foo(,,,,);
                            a = 0[10]`
                        EndBody.''',
            r'''Function,:,foo,Parameter,:,a,[,1,],Body,:,b,=,a,[,1,+,2,],;,a,[,i,+,2,],=,(,1,+,3,),+,4,;,a,=,foo,(,,,,,,,,,),;,a,=,0,[,10,],Error Token `''',
            189
        ))
    


    #Test unterminated
    def test_unterminated_cmt(self):
        self.assertTrue(TestLexer.checkLexeme(r''' ** This is ''',r'''Unterminated Comment''',190))
    def test_illegal_string(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''"hello [] \n \m"''',
            r'''Illegal Escape In String: hello [] \n \m''',
            191))
    def test_unterminated_cmt1(self):
        self.assertTrue(TestLexer.checkLexeme(
            r''' **This is \b\n\r\f\t '" \ ''' ,
            r'''Unterminated Comment''',
            192))
    def test_unclosed_string1(self):
        self.assertTrue(TestLexer.checkLexeme(
            r''' "**This is '" ''' ,
            r'''Unclosed String: **This is '" ''',
            193))
    def test_unclosed_string2(self):
        self.assertTrue(TestLexer.checkLexeme(
            r''' "**This is '""" ''' ,
            r'''**This is '",Unclosed String:  ''',
            194))
    def test_unclosed_string3(self):
        self.assertTrue(TestLexer.checkLexeme(
            r''' "**This is '"""abc""dcf'" ''' ,
            r'''**This is '",abc,Unclosed String: dcf'" ''',
            195))
    def test_illegal_string1(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''"abc\mabc''' ,
            r'''Illegal Escape In String: abc\m''',
            196))
    def test_comment1(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''**inline and /* block // and inline /* and block **''' ,
            r'''<EOF>''',
            197))
    def test_comment2(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''** first block co
            
            
            
            
            mment------ /*and another*/ **''' ,
            r'''<EOF>''',
            198))
    def test_literal(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''123 000012 00001.00000 000.000 1234. 000e0 000. 0000.0e-0000 0x1230000 0o00000 "abc" "!@\#$%@%$%$%^%"''' ,
            r'''123,0,0,0,0,12,00001.00000,000.000,1234.,000e0,000.,0000.0e-0000,0x1230000,0o00000,abc,Illegal Escape In String: !@\#''',
            199))
    def test_error_token(self):
        self.assertTrue(TestLexer.checkLexeme(
            r''' "!@#$%^&*()" ''',
            r'''!@#$%^&*(),<EOF>''',
            200
        ))
    
    
    
    