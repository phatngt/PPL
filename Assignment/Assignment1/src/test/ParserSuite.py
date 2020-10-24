import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Var: x;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
    
    def test_wrong_miss_close(self):
        """Miss variable"""
        input = """Var: ;"""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    def test_simple_program1(self):
        input = """Function: foo Parameter:a,b,c Body: EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))
    def test_simple_program2(self):
        input = """Function: foo
                    Parameter:a,b,c
                        Body:
                            Var:x;
                            d = 1; 
                        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))
    def test_simple_program3(self):
        input = """ Function: foo
                        Parameter:
                        Body:
                            If n == 0 Then
                                Return 1;
                            Else 
                                c = a+b;
                            EndIf.
                        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))
    def test_simple_program4(self):
        input = """Function: main
                        Parameter:
                        Body:
                            If 1 == 0.0 Then
                                Return 1;
                            EndIf.
                        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))
    def test_simple_program5(self):
        input = """Function: foo
                    Parameter:a,b,c
                        Body:
                            Var:x;
                            If n == 0 Then
                                Return 1;
                            EndIf.
                        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))
    #Test statements
    def test_if_stm(self):
        input = """ Function: main
                        Parameter:
                        Body:
                            If e == 1 Then
                                a = 2;
                                Return a;
                            EndIf.
                        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))
    def test_wrong_if_stm(self):
        input = """ Function: main
                        Parameter:
                        Body:
                            If e = 1 Then
                                a = 2;
                                Return a;
                            EndIf.
                        EndBody."""
        expect = "Error on line 4 col 33: ="
        self.assertTrue(TestParser.checkParser(input,expect,209))
    def test_if_stm1(self):
        input = """ Function: main
                        Parameter:
                        Body:
                            If e == 1 Then
                                a = 2;
                                Return a;
                            Else
                                b = 2;
                                Return 1;
                            EndIf.
                        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,210))
    def test_wrong_if_stm1(self):
        input = """ Function: main
                        Parameter:
                        Body:    
                            If e == 1 Then
                                a = 2;
                                Return a;
                            Else
                                Return 1;
                        EndBody."""
        expect = "Error on line 9 col 24: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,211))
    def test_logical_if_stm(self):
        input = """ Function: main
                        Parameter:
                        Body:
                            If (e == 1) && f  Then
                                a = 2;
                                Return a;
                            ElseIf
                                Return 1;
                            EndIf.
                        EndBody."""
        expect = "Error on line 8 col 32: Return"
        self.assertTrue(TestParser.checkParser(input,expect,212))
    def test_logical_if_stm1(self):
        input = """ Function: main
                        Parameter:
                        Body:
                            If (e == 1) && f  Then
                                a = 2;
                                Return a;
                            ElseIf i < 2 Then
                                a = 2;
                                Return 1;
                            EndIf.
                        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,213))
    def test_for_stm(self):
        input = """Function: main
                        Parameter:
                        Body:
                            For(i = 1, i < 10,1) Do
                                printLn(i);
                            EndFor.
                        EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,214))
    def test_for_stm1(self):
        input = """Function: main
                        Parameter:
                        Body:
                            For(i = 1; i < 10,1) Do
                                printLn(i);
                            EndFor.
                        EndBody. """
        expect = "Error on line 4 col 37: ;"
        self.assertTrue(TestParser.checkParser(input,expect,215))
    def test_for_stm2(self):
        input = """Function: main
                        Parameter:
                        Body:
                            For(i = 1, i < 10,1 Do
                                printLn(i);
                            EndFor.
                        EndBody. """
        expect = "Error on line 4 col 48: Do"
        self.assertTrue(TestParser.checkParser(input,expect,216))
    def test_for_stm3(self):
        input = """Function: main
                        Parameter:
                        Body:
                            For(i = 1, i < 10,1)
                                printLn(i);
                            EndFor.
                        EndBody. """
        expect = "Error on line 5 col 32: printLn"
        self.assertTrue(TestParser.checkParser(input,expect,217))
    def test_for_stm4(self):
        input = """Function: main
                        Parameter:
                        Body:
                            For(i, i < 10,1)
                                printLn(i);
                            EndFor.
                        EndBody. """
        expect = "Error on line 4 col 33: ,"
        self.assertTrue(TestParser.checkParser(input,expect,218))
    def test_for_stm5(self):
        input = """Function: main
                        Parameter:
                        Body:
                            For()
                                printLn(i);
                            EndFor.
                        EndBody. """
        expect = "Error on line 4 col 32: )"
        self.assertTrue(TestParser.checkParser(input,expect,219))
    def test_while_stm(self):
        input = """Function: main
                        Parameter:
                        Body:
                            While i < 10 Do
                                i = i+1;
                                printLn(i);
                            EndWhile.
                        EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,220))
    def test_while_stm1(self):
        input = """Function: main
                        Parameter:
                        Body:
                            While  Do
                                i = i+1;
                                printLn(i);
                            EndWhile.
                        EndBody. """
        expect = "Error on line 4 col 35: Do"
        self.assertTrue(TestParser.checkParser(input,expect,221))
    def test_while_stm2(self):
        input = """Function: main
                        Parameter:
                        Body:
                            While i < 1
                                i = i+1;
                                printLn(i);
                            EndWhile.
                        EndBody. """
        expect = "Error on line 5 col 32: i"
        self.assertTrue(TestParser.checkParser(input,expect,222))
    def test_while_stm3(self):
        input = """Function: main
                        Parameter:
                        Body:
                            While i < 1 Do
                                i = i+1;
                                printLn(i);
                            EndWhile
                        EndBody. """
        expect = "Error on line 8 col 24: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,223))
    def test_do_while_stm(self):
        input = """Function: main
                        Parameter:
                        Body:
                            Do
                                i = i+1;
                            While i < 10
                            EndDo.
                        EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,224))
    def test_do_while_stm1(self):
        input = """Function: main
                        Parameter:
                        Body:
                            Do:
                                i = i+1;
                            While i < 10
                            EndDo.
                        EndBody. """
        expect = "Error on line 4 col 30: :"
        self.assertTrue(TestParser.checkParser(input,expect,225))
    def test_do_while_stm2(self):
        input = """Function: main
                        Parameter:
                        Body:
                            Do
                                i = i+1;
                            While
                            EndDo.
                        EndBody. """
        expect = "Error on line 7 col 28: EndDo"
        self.assertTrue(TestParser.checkParser(input,expect,226))
    def test_do_while_stm3(self):
        input = """Function: main
                        Parameter:
                        Body:
                            Do
                                i = i+1;
                            While i < 10
                            EndDo
                        EndBody. """
        expect = "Error on line 8 col 24: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,227))
    def test_break_stm(self):
        input = """Function: main
                        Parameter:
                        Body:
                            Break;
                        EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,228))
    def test_break_stm1(self):
        input = """Function: main
                        Parameter:
                        Body:
                            Break
                        EndBody. """
        expect = "Error on line 5 col 24: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,229))
    def test_continue_stm(self):
        input = """Function: main
                        Parameter:
                        Body:
                            Continue;
                        EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,230))
    def test_continue_stm1(self):
        input = """Function: main
                        Parameter:
                        Body:
                            Continue
                        EndBody. """
        expect = "Error on line 5 col 24: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,231))
    def test_call_func_stm(self):
        input = """ Function: foo 
                        Parameter:a[1]
                        Body:
                            b = a[1+2];
                            a[i+2] = (1+3)+4;
                            a = fooo(30)+b+c;
                            a = 0[10];
                        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,232))
    def test_call_func_stm1(self):
        input = """ Function: foo 
                        Parameter:a[1]
                        Body:
                            b = a[1+2];
                            a[i+2] = (1+3)+4;
                            foo(30)
                            a = 0[10];
                        EndBody."""
        expect = "Error on line 7 col 28: a"
        self.assertTrue(TestParser.checkParser(input,expect,233))
    def test_call_func_stm2(self):
        input = """ Function: foo 
                        Parameter:a[1]
                        Body:
                            b = a[1+2];
                            a[i+2] = (1+3)+4;
                            a = foo(30;
                            a = 0[10];
                        EndBody."""
        expect = "Error on line 6 col 38: ;"
        self.assertTrue(TestParser.checkParser(input,expect,234))
    def test_call_func_stm3(self):
        input = """ Function: foo 
                        Parameter:a[1]
                        Body:
                            b = a[1+2];
                            a[i+2] = (1+3)+4;
                            a = foo(,,,,);
                            a = 0[10];
                        EndBody."""
        expect = "Error on line 6 col 36: ,"
        self.assertTrue(TestParser.checkParser(input,expect,235))
    def test_call_func_stm4(self):
        input = """ Function: foo 
                        Parameter:a[1]
                        Body:
                            a = True;
                            foo(True,12,"abc",12.0,12e1,12.,000.e-1);
                        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,236))
    def test_call_func_stm5(self):
        input = """ Function: foo 
                        Parameter:a[1]
                        Body:
                            a = True;
                            foo(a == 1,a < 2,"abc" > 12.0,b >. d,e <.f,1==3,12e4 != 5,000.e-1 <=0, 12.1 >= 8, 1.0 =/=2);
                        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,237))
    def test_assign_stm(self):
        input = """ Function: foo 
                        Parameter:a[1]
                        Body:
                            Var: a[1],b,c,x,y,z;
                            a[1] = {True,False,12,0x12A,0X12B,0o123,0.12,12.,1e-1,1.e12,"abc","asd"};
                            b = a[a[b[c[d[e[g[f[h[1]]]]]]]]];
                            c = a[12][b[12]][d[c[e[123]]]];
                            x = (1+.2)*(3+8)-(2\\10)*a[12]+7-a;
                            y = !!!!!!!!!!!!!!!!!!!!!!a[1];
                            z = (1%2*(3+4*(6-.2\\(4*(2*1)+.3))));
                        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,238))
    def test_assign_stm1(self):
        input = """ Function: foo 
                        Parameter:a[1]
                        Body:
                            Var: a[1],b,c,x,y,z;
                            a[1] == {True,False,12,0x12A,0X12B,0o123,0.12,12.,1e-1,1.e12,"abc","asd"};
                            b = a[a[b[c[d[e[g[f[h[1]]]]]]]]];
                            c = a[12][b[12]][d[c[e[123]]]];
                            x = (1+.2)*(3+8)-(2\\10)*a[12]+7-a;
                            y = !!!!!!!!!!!!!!!!!!!!!!a[1];
                            z = (1%2*(3+4*(6-.2\\(4*(2*1)+.3))));
                        EndBody."""
        expect = "Error on line 5 col 33: =="
        self.assertTrue(TestParser.checkParser(input,expect,239))
    #Test Expression
    def test_exp(self):
        input = """ Function: foo 
                        Parameter:a[1]
                        Body:
                            Var: a[1],b,c,x,y,z;
                            a[1] = {True,False,12,0x12A,0X12B,0o123,0.12,12.,1e-1,1.e12,"abc","asd"};
                            b = a[a[b[c[d[e[g[f[h[1]]]]]]]]];
                            c = a[12][b[12]][d[c[e[123]]]];
                            x = (1+.2)*(3+8)-(2\\10)*a[12]+7-a;
                            y = !!!!!!!!!!!!!!!!!!!!!!a[1];
                            z = (1%2*(3+4*(6-.2\\(4*(2*1)+.3))));
                        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,239))
    def test_exp1(self):
        input = """ Function: foo 
                        Parameter:a[1]
                        Body:
                            Var: a[1],b,c,x,y,z;
                            a[1] = (a>b)&&(c<d);
                            b = (c >= d) && (e >. g);
                            c = ((c>=d) && e) >. g;
                            x = !(((c > 1)&&c)||d);
                        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,241))
    def test_exp2(self):
        input = """ Function: foo 
                        Parameter:a[1]
                        Body:
                            Var: a[1],b,c,x,y,z;
                            a[1] = (a>b)&&(c<d);
                            b = c >= d && e >. g;
                            c = ((c>=d) && e) >. g;
                            x = !(((c > 1)&&c)||d);
                        EndBody."""
        expect = "Error on line 6 col 44: >."
        self.assertTrue(TestParser.checkParser(input,expect,242))
    def test_exp3(self):
        input = """ Function: foo 
                        Parameter:a[1]
                        Body:
                            Var: a[1],b,c,x,y,z;
                            a[1] = (a>b)&&(c<d);
                            b = (c >= d) && e >. g;
                            c = ((c>=d) && e) >. g;
                            x = !(((c > 1)&&c)||d);
                        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,243))
    #Test mix
    def test_mix1(self):
        input = """
                    Var: x = -1;
                    Function: foo 
                        Parameter:a[1]
                        Body:
                        EndBody."""
        expect = "Error on line 2 col 29: -"
        self.assertTrue(TestParser.checkParser(input,expect,244))
    def test_mix2(self):
        input = """ Var: x = 1;
                    Function: foo 
                        Parameter:a[1]
                        Body:
                        EndBody.
                    Var: y = 2;"""
        expect = "Error on line 6 col 20: Var"
        self.assertTrue(TestParser.checkParser(input,expect,245))
    def test_mix3(self):
        input = """ Var: x = 1;
                    Function: foo 
                        Parameter:a[1]
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
                        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,246))
    def test_mix4(self):
        input = """ Var: x = 1;
                    Var: y,z = 2,3;
                    Function: foo 
                        Parameter:a[1]
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
                        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,247))
    def test_mix5(self):
        input = """ Var: x = 1;
                    Var: y,z = 2,3;
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,248))
    def test_mix6(self):
        input = """ Var: x = 1;
                    Var: y,z = 2,3;
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
                        EndBody.
                    """
        expect = "Error on line 15 col 28: Var"
        self.assertTrue(TestParser.checkParser(input,expect,249))
    def test_mix7(self):
        input = """ Var: x = 1;
                    Var: y,z = 2,3;
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
                        EndBody.
                    """
        expect = "Error on line 14 col 32: Var"
        self.assertTrue(TestParser.checkParser(input,expect,250))
    def test_mix8(self):
        input = """ Var: x = 1;
                    Var: y,z = 2,3;
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
                            Else
                                Var:b;
                            EndIf.
                            For (i = 0, i < 10,i+1) Do
                                Var: x = 1;
                                printLn();
                            EndFor.
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,251))
    def test_mix9(self):
        input = """ Var: x = 1;
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
                        EndBody.
                    """
        expect = "Error on line 11 col 32: Var"
        self.assertTrue(TestParser.checkParser(input,expect,252))
    def test_mix10(self):
        input = """ Var: x = 1;
                    Var: y,z = 2,3;
                    Function: foo 
                        Parameter:a[1],a,b,c
                        Body:
                            Var: x,y;
                            Var:z;
                            Do 
                                Var: x,y;
                                x = x+1;
                                y = y+1;
                            While (x < 10)&&(y<5)
                            EndDo.
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,253))
    def test_mix11(self):
        input = """ Var: x = 1;
                    Var: y,z = 2,3;
                    Function: foo 
                        Parameter:a[1],a,b,c
                        Body:
                            Var: x,y;
                            Var:z;
                            Do 
                                Var: x,y;
                                x = x+1;
                                y = y+1;
                            While (x < 10)&&(y<5)
                            EndDo.
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,253))
    def test_mix12(self):
        input = """ Var: x = 1;
                    Var: y,z = 2,3;
                    Function: foo 
                        Parameter:a[1],a,b,c
                        Body:
                            Var: x,y;
                            Var:z;
                            While i < 10 Do
                                Var: x,y;
                                x = x+1;
                                y = y+1;
                                Var:a;
                            While (x < 10)&&(y<5)
                            EndDo.
                        EndBody.
                    """
        expect = "Error on line 12 col 32: Var"
        self.assertTrue(TestParser.checkParser(input,expect,254))
    def test_mix12(self):
        input = """ Var: x = 1;
                    Var: y,z = 2,3;
                    Function: foo 
                        Parameter:a[1],a,b,c
                        Body:
                            Var: x,y;
                            Var:z;
                            While i < 10 Do
                                Var: x,y;
                                x = x+1;
                                y = y+1;
                            EndWhile.
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,255))
    def test_mix13(self):
        input = """ Var: x = 1;
                    Var: y,z = 2,3;
                    Function: foo 
                        Parameter:a[1],a,b,c
                        Body:
                            Var: x,y;
                            Var:z;
                            While i < 10 Do
                                Var: x,y;
                                x = x+1;
                                y = y+1;
                                Var:a;
                            EndWhile.
                        EndBody.
                    """
        expect = "Error on line 12 col 32: Var"
        self.assertTrue(TestParser.checkParser(input,expect,256))
    def test_mix14(self):
        input = """ Var: x = 1;
                    Var: y,z = 2,3;
                    Function: foo 
                        Parameter:a[1],a,b,c
                        Body:
                            Var: x,y;
                            Var:z;
                            While i < 10 Do
                                Var: x,y;
                                x = x+1;
                                y = y+1;
                            EndWhile.
                        EndBody.
                    Function: facb
                        Parameter: a,b,c
                        Body:
                            Var: x,y;
                            foo(c,b,a);
                            Return 1;
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,257))  
    def test_mix15(self):
        input = """ Var: x = 1;
                    Var: y,z = 2,3;
                    Function: foo 
                        Parameter:a[1],a,b,c
                        Body:
                            Var: x,y;
                            Var:z;
                            While i < 10 Do
                                Var: x,y;
                                x = x+1;
                                y = y+1;
                            EndWhile.
                        EndBody.
                    Function: facb
                        Parameter: a,b,c
                        Body:
                            Var: x,y;
                            foo(c,b,a);
                            Return 1;
                        EndBody.
                    Function: main
                        Parameter:
                        Body:
                            foo(1,2,3);
                            facb(4,5,6);
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,258))
    def test_mix16(self):
        input = """ Var: x = 1;
                    Var: y,z = 2,3;
                    Function: foo 
                        Parameter:a[1],a,b,c
                        Body:
                            Var: x,y;
                            Var:z;
                            While i < 10 Do
                                Var: x,y;
                                x = x+1;
                                y = y+1;
                            EndWhile.
                        EndBody.
                    Function: facb
                        Parameter: a,b,c
                        Body:
                            Var: x,y;
                            foo(c,b,a);
                            Return 1;
                        EndBody.
                    Function: main
                        Parameter:
                        Body:
                            foo(1,2,3);
                            facb(\n,1,2);
                        EndBody.
                    """
        expect = "Error on line 26 col 0: ,"
        self.assertTrue(TestParser.checkParser(input,expect,259))
    def test_mix17(self):
        input = """ Var: x = 1;
                    Var: y,z = 2,3;
                    Function: foo 
                        Parameter:a[1],a,b,c
                        Body:
                            ** This is a comment
                                *aa
                                v
                                c
                            **
                            Var: x,y;
                            Var:z;
                            While i < 10 Do
                                Var: x,y;
                                x = x+1;
                                y = y+1;
                            EndWhile.
                        EndBody.
                    Function: facb
                        Parameter: a,b,c
                        Body:
                            Var: x,y;
                            foo(c,b,a);
                            Return 1;
                        EndBody.
                    Function: main
                        Parameter:
                        Body:
                            foo(1,2,3);
                            facb(a,1,2);
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,260))
    def test_mix18(self):
        input = """ Var: x = 1;
                    Var: y,z = 2,3;
                    Function: foo 
                        Parameter:a[1],a,b,c
                        Body:
                            Var: x,y;
                            Var:z;
                            While i < 10 Do
                                Var: x,y;
                                x = x+1;
                                y = y+1;
                                If a == 0 Then
                                    Var: b;
                                    x = x*2;
                                EndIf.
                            EndWhile.
                        EndBody.
                    Function: facb
                        Parameter: a,b,c
                        Body:
                            Var: x,y;
                            foo(c,b,a);
                            Return 1;
                        EndBody.
                    Function: main
                        Parameter:
                        Body:
                            foo(1,2,3);
                            facb(a,1,2);
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,261))
    def test_mix19(self):
        input = """ Var: x = 1;
                    Var: y,z = 2,3;
                    Function: foo 
                        Parameter:a[1],a,b,c
                        Body:
                            Body:

                            EndBody.
                        EndBody.
                    Function: main
                        Parameter:
                        Body:
                            foo(1,2,3);
                            facb(a,1,2);
                        EndBody.
                    """
        expect = "Error on line 6 col 28: Body"
        self.assertTrue(TestParser.checkParser(input,expect,262))
    def test_mix20(self):
        input = """ Var: x = 1;
                    Var: y,z = 2,3;
                    Function: foo 
                        Parameter:a[1],a,b,c
                        Body:
                        Function: abc
                            Parameter: x,y,z
                            Body:

                            EndBody.
                        EndBody.
                    Function: main
                        Parameter:
                        Body:
                            foo(1,2,3);
                            facb(a,1,2);
                        EndBody.
                    """
        expect = "Error on line 6 col 24: Function"
        self.assertTrue(TestParser.checkParser(input,expect,263))
    def test_mix21(self):
        input = """ Var: x = 1;
                    Var: y,z = 2,3;
                    Function: foo 
                        Parameter:a[1],a,b,c
                        Body:
                        If n == 10 Then
                            For(i = 1, i < 9, 1) Do
                                While i < 0 Do
                                    Do 
                                        Var: a;
                                        a = a+1;
                                        If a < 50 Then 
                                            Continue;
                                        ElseIf a > 50 Then
                                            Break;
                                        Else
                                            Return 0;
                                        EndIf.
                                    While a < 100
                                    EndDo.
                                EndWhile.
                            EndFor.
                        EndIf.
                        EndBody.
                    Function: main
                        Parameter:
                        Body:
                            foo(1,2,3);
                            facb(a,1,2);
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,264))
    def test_mix22(self):
        input = """ Var: x = 1;
                    Var: y,z = 2,3;
                    Function: foo 
                        Parameter:a[1],a,b,c
                        Body:
                            Var: i = 2;
                            While i < 10 Do
                                i = i + 1;
                                Do
                                    i = i + 2;
                                While i < 7
                                EndDo.
                                Return 1;
                            EndWhile.    
                        EndBody.
                    Function: main
                        Parameter:
                        Body:
                            foo(1,2,3);
                            facb(a,1,2);
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,265))
    def test_mix23(self):
        input = """ Var: x = 1;
                    Var: y,z = 2,3;
                    Function: foo 
                        Parameter:a[1],a,b,c
                        Body:
                        Var: i = 1;
                            While i < 0 Do
                                i = i + 1;
                                While i > 10 Do
                                    a = a + 1;
                                While i < 10
                                EndDo.
                                EndWhile.
                            EndWhile.
                        EndBody.
                    Function: main
                        Parameter:
                        Body:
                            foo(1,2,3);
                            facb(a,1,2);
                        EndBody.
                    """
        expect = "Error on line 11 col 32: While"
        self.assertTrue(TestParser.checkParser(input,expect,266))
    def test_mix24(self):
        input = """ Var: x = 1;
                    Var: y,z = 2,3;
                    Function: foo 
                        Parameter:a[1],a,b,c
                        Body:
                            foo[123);
                        EndBody.
                    Function: main
                        Parameter:
                        Body:
                            foo(1,2,3);
                            facb(a,1,2);
                        EndBody.
                    """
        expect = "Error on line 6 col 35: )"
        self.assertTrue(TestParser.checkParser(input,expect,267))
    def test_mix25(self):
        input = """ Var: x = 1;
                    Var: y,z = 2,3;
                    Function: foo 
                        Parameter:a,b,c
                        Body:
                            a = c()+d()+f();
                            Return a;
                        EndBody.
                    Function: main
                        Parameter:
                        Body:
                            foo(1,2,3);
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,268))
    def test_mix26(self):
        input = """ Var: x = 1;
                    Var: y,z = 2,3;
                    Function: foo 
                        Parameter:a,b
                        Body:
                            a = c()+d()+f();
                            For( i = a(),i < b(),c()) Do
                                Return d();
                            EndFor.
                            Return a;
                        EndBody.
                    Function: main
                        Parameter:
                        Body:
                            foo(1,2,3);
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,269))
    def test_mix27(self):
        input = """ Var: x = 1;
                    Var: y,z = 2,3;
                    Function: foo 
                        Parameter:a = c(),b
                        Body:
                            a = c()+d()+f();
                            For( i = a(),i < b(),c()) Do
                                Return d();
                            EndFor.
                            Return a;
                        EndBody.
                    Function: main
                        Parameter:
                        Body:
                            foo(1,2,3);
                        EndBody.
                    """
        expect = "Error on line 4 col 36: ="
        self.assertTrue(TestParser.checkParser(input,expect,270))
    def test_mix28(self):
        input = """ Var: x = 1;
                    Var: y,z = 2,3;
                    Function: foo 
                        Parameter:a,b
                        Body:
                            a = c()+d()+f();
                            b = (c(d(e(f(g(1))))));
                            For( i = a(),i < b(),c()) Do
                                Return d();
                            EndFor.
                            Return a;
                        EndBody.
                    Function: main
                        Parameter:
                        Body:
                            foo(1,2,3);
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,271))
    def test_mix29(self):
        input = """ Var: x = 1;
                    Var: y,z = 2,3;
                    Function: foo 
                        Parameter:a,b
                        Body:
                            a = c()+d()+f();
                            ** Cmt ** 
                            b = (c(d(e(f(g(1-2)*3)\\4)%5)+6));
                            For( i = a(),i < b(),c()) Do
                                Return d();
                            EndFor.
                            Return a;
                        EndBody.
                    Function: main
                        Parameter:
                        Body:
                            foo(1,2,3);
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,272))
    def test_mix30(self):
        input = """ Var: x = 1;
                    Var: y,z = 2,3;
                    Function: foo 
                        Parameter:a,b
                        Body:
                            a = c()+d()+f();
                            ** Cmt \r\b\t\f\n** 
                            b = (c(d(e(f(g(1-2)*3)\\4)%5)+6));
                            For( i = a(****),i < b(**Cmt \r\b\t\f\n**),c()) Do
                                Return d();
                            EndFor.
                            Return a;
                        EndBody.
                    Function: main
                        Parameter:
                        Body:
                            foo(1,2,3);
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,273))
    def test_mix31(self):
        input = """ Var: x = 1;
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
                        EndBody.
                    Function: main
                        Parameter:
                        Body:
                            foo(1,2,3);
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,274))
    def test_mix32(self):
        input = """ Var: x = 1;
                    Var: y,z = 2,3;
                    Function: foo 
                        Parameter:a,b
                        Body:
                            a = c()+d()+f();
                            ** Cmt \r\b\t\f\n** 
                            b = (c(d(e(f(g(1-2)*3)\\4)%5)+6));
                            For( i = a(****),i < b(****),c("'"")"'"") Do
                                Return d();
                            EndFor.
                            Return a;
                        EndBody.
                    Function: main
                        Parameter:
                        Body:
                            foo(1,2,3);
                        EndBody.
                    """
        expect = r'''Error on line 10 col 64: '"'''
        self.assertTrue(TestParser.checkParser(input,expect,275))
    def test_mix33(self):
        input = """ Var: x = 1;
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
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,276))
    def test_mix34(self):
        input = """ Var: x = 1;
                    Var: y,z = 2,3;
                    Function: foo 
                        Parameter:a,b
                        Body:
                            a = c()+d()+f();
                            ** Cmt \r\b\t\f\n** 
                            b = (c(d(e(f(g(1-2)*3)\\4)%5)+6));
                            While a[{5}] Do 
                                printLn("Goodbye world");
                            EndWhile.
                            Return a;
                        EndBody.
                    Function: main
                        Parameter:
                        Body:
                            foo(1,2,3);
                        EndBody.
                    """ ######################################3333
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,277))
    def test_mix35(self):
        input = """ Var: x = 1;
                    Var: y,z[12.0] = 2,3;
                    Function: main
                        Parameter:
                        Body:
                            foo(1,2,3,print("abc"));
                        EndBody.
                    """
        expect = "Error on line 2 col 29: 12.0"
        self.assertTrue(TestParser.checkParser(input,expect,278))
    def test_mix36(self):
        input = """ Var: x = 1;
                    Var: y,z[12][1][1234567890000] = 2,3;
                    Function: main
                        Parameter:
                        Body:
                            foo(1[0x1245ABCDF],a(0o1234567),True);
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,279))
    def test_mix37(self):
        input = """ Var: x = 1;
                    Var: y,z[12][1][1234567890000] = 2,3;
                    Function: main
                        Parameter:
                        Body:
                            Var: x,a = 1,"a";
                            a = !!!!!!!!!x;
                            a = x!!!!!!!!;
                            foo(a,a(0o1234567),True);
                        EndBody.
                    """
        expect = "Error on line 8 col 33: !"
        self.assertTrue(TestParser.checkParser(input,expect,280))
    def test_mix38(self):
        input = """ Var: x = 1;
                    Var: y,z[12][1][1234567890000] = 2,3;
                    Function: main
                        Parameter:
                        Body:
                            Var: x,a = 1,"a";
                            a = !!!!!!!!!x;
                            a = (a&&(&&b));
                            foo(a,a(0o1234567),True);
                        EndBody.
                    """
        expect = "Error on line 8 col 37: &&"
        self.assertTrue(TestParser.checkParser(input,expect,281))
    def test_mix39(self):
        input = """ Var: x = 1;
                    Var: y,z[12][1][1234567890000] = 2,3;
                    Function: main
                        Parameter:
                        Body:
                            While (i-.(1&&(4||2)))=/=5>=.7 Do
                                printLn(1);
                                Continue;
                            EndWhile.
                        EndBody.
                    """
        expect = "Error on line 6 col 54: >=."
        self.assertTrue(TestParser.checkParser(input,expect,282))
    def test_mix40(self):
        input = """ Var: x = 1;
                    Var: y,z[12][1][1234567890000] = 2,3;
                    Function: main
                        Parameter:
                        Body:
                            While ((i-.(1&&(4||2)))=/=5)>=.7-. Do
                                printLn(1);
                                Continue;
                            EndWhile.
                        EndBody.
                    """
        expect = "Error on line 6 col 63: Do"
        self.assertTrue(TestParser.checkParser(input,expect,283))
    def test_mix41(self):
        input = """ Var: x = 1;
                    Var: y,z[12][1][1234567890000] = 2,3;
                    Function: main
                        Parameter:
                        Body:
                            While ((i-.(1&&(4||2)))=/=5)>=.7&& foo() Do
                                printLn(1);
                                Continue;
                            EndWhile.
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,284))
    def test_mix42(self):
        input = """ Var: x = 1;
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
                        EndBody.
                    """
        expect = "Error on line 9 col 67: ["
        self.assertTrue(TestParser.checkParser(input,expect,285))
    def test_mix43(self):
        input = """ Function: main
                        Parameter:
                        Body:
                            foo((1+2*(3-0x1\\(12.0 -. 0o1236*(True+"abc"\\.(**This is cmt***.12e1))))),2,3);
                        EndBody.
                    """
        expect = "Error on line 4 col 89: *."
        self.assertTrue(TestParser.checkParser(input,expect,286))
    def test_mix44(self):
        input = """ Var: x = 1;
                    Var: y,z = 2,3;
                    Function: foo 
                        Parameter:a[0x123ABC][0o12345],a,b,c
                        Body:
                            Var: x,y;
                            Var:z;
                            Do
                                Var: x,y;
                                x = x+1 + ** Error here??** 1;
                            While !!!!(x < 0x123A)!!!! 
                            EndDo.
                        EndBody.
                    """
        expect = "Error on line 11 col 50: !"
        self.assertTrue(TestParser.checkParser(input,expect,287))
    def test_mix45(self):
        input = """ Var: x = 1;
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
                            While !!!!(x < 0x123A-.) 
                            EndDo.
                        EndBody.
                    """
        expect = "Error on line 13 col 51: )"
        self.assertTrue(TestParser.checkParser(input,expect,288))
    def test_mix46(self):
        input = """ Function: main 
                        Parameter:a[0x123ABC][0o12345],a,b,c
                        Body:
                            printLn(1234,0xAAA,{{{{12,34}}}},a[1][2][3][4.0+0x123]);
                            print("Goodbye world","Happy Women Day");
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,289))
    def test_mix47(self):
        input = """ Function: main 
                        Parameter:a[0x123ABC][0o12345],a,b,c
                        Body:
                            int_of_float(12);
                            float_to_int(12.0);
                            int_of_string(12);
                            string_of_int("12");
                            float_of_string(12.1);
                            string_of_float("12.0");
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,290))
    def test_mix48(self):
        input = """ Function: main 
                        Parameter:a[0x123ABC][0o12345],a,b,c
                        Var: x = 1;
                        Body:
                            **Goodbye world**
                        EndBody.
                    """
        expect = "Error on line 3 col 24: Var"
        self.assertTrue(TestParser.checkParser(input,expect,291))
    def test_mix49(self):
        input = """ Function: main 
                        Parameter:a[0x123ABC][0o12345],a,b,c
                        Body:
                            x[{1,2}+True\\.False =/= {True,"False"}*.12e1] = 1;
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,292))
    def test_mix50(self):
        input = """ Function: main 
                        Parameter:a[0x123ABC][0o12345],a,b,c
                        Body:
                            x[({1,2}+True\\.False) =/= ({True,"False"}*.12e1) **People!!! This is a comment, Okey**] = 1;
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,293))
    def test_mix51(self):
        input = """ Function: main 
                        Parameter:a[0x123ABC][0o12345],a,b,c
                        Body:
                            x[({{1,2},{True\\.False}}) =/= ({True,"False"}*.12e1) **People!!! This is a comment, Okey**] = 1;
                        EndBody.
                    """
        expect = "Error on line 4 col 43: \."
        self.assertTrue(TestParser.checkParser(input,expect,294))
    def test_mix52(self):
        input = """ Var: x = 1;
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
                        EndBody.
                    """
        expect = "Error on line 13 col 61: b"
        self.assertTrue(TestParser.checkParser(input,expect,295))
    def test_mix53(self):
        input = """ Var: x = 1;
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
                            While a[!!(x < 0x123A)][!!(1-1.0)*b[15]] 
                            EndDo.
                            Do
                            While a[!!(x < 0x123A)][!!(1-1.0)*b[15]] 
                            EndDo.
                            If (n_123_ACV____ == 1e12123) || a[b[c[d[e[f[g["a"]]]]]]] Then
                            EndIf.
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,296))
    def test_mix54(self):
        input = """ Function: foo 
                        Parameter:a[0x123ABC][0o12345],a,b,c
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
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,297))
    def test_mix55(self):
        input = """ Function: foo 
                        Parameter:a[0x123ABC][0o12345],a,b,c
                        Body:
                            Var:a;
                            Var:a_;
                            Var:aB;
                            Var:a_B**This is cmt**;
                            Var:a123a_123A;
                            Var:a_b_123_B[123][0x123];
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,298))
    def test_mix56(self):
        input = """ Function: foo 
                        Parameter:a[0x123ABC][0o12345],a,b,c
                        Body:
                            Var:a;
                            Var:a_;
                            Var:aB;
                            Var:a_B**This is cmt**;
                            Var:a123a_123A;
                            Var:a_b_123_B[123][0x123];
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,299))
    def test_mix57(self):
        input = """ Function: foo 
                        Parameter:a[0x123ABC][0o12345],a,b,c
                        Body:
                            Var:a;
                            Var:a_;
                            Var:aB;
                            Var:a_B**This is cmt**;
                            Var:a123a_123A;
                            Var:a_b_123_B[123][0x123];
                            If True Then
                            EndIf.
                            Var: error[1][2][3];
                        EndBody.
                    """
        expect = "Error on line 12 col 28: Var"
        self.assertTrue(TestParser.checkParser(input,expect,300))
        
    
    