import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):
    
    def test_revar_decl(self):
        """Simple test: Redeclare var"""
        input = """ Var: x,x;
                    Function: main
                    Parameter: x,y,z
                    Body:
                    EndBody."""
        expect = str(Redeclared(Variable(),"x"))
        self.assertTrue(TestChecker.test(input,expect,401))
    
    def test_revar_decl1(self):
        """Simple test: Redeclare var"""
        input = """ Var: x,y;
                    Var: y;
                    Function: main
                    Parameter: x,y,z
                    Body:
                    EndBody."""
        expect = str(Redeclared(Variable(),"y"))
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_inferred_type(self):
        """Simple test: Inferred var decl"""
        input = """ Var: x=1;
                    Function: main
                    Body:
                        x = 1.1;
                    EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id(name="x"),FloatLiteral(1.1))))
        self.assertTrue(TestChecker.test(input,expect,403))
    
    def test_inferredtype1(self):
        """Simple test: Inferred var decl"""
        input = """ Var: x=1.1;
                    Function: main
                    Body:
                        x = 1;
                    EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id(name="x"),IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_inferredtype2(self):
        """Simple test: Inferred var decl"""
        input = """ Var: x=1.1;
                    Var: y = 1;
                    Function: main
                    Body:
                        x = y;
                        Return 1.1;
                    EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id(name="x"),Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,405))
    def test_inferredtype3(self):
        """Simple test: Inferred var decl"""
        input = """ Var: x=True;
                    Var: y = "abc";
                    Function: main
                    Body:
                        x = y;
                        Return 1.1;
                    EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("x"),Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,406))

    ################!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!###################
    def test_inferredtype4(self):
        """Simple test: Inferred var decl"""
        input = """ Var: x[1][2];
                    Var: y = "abc";
                    Function: main
                    Body:
                        Var: t;
                        x = y;
                        Return 1.1;
                    EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("x"),Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,407))
    
    def test_inferredtype5(self):
        """Simple test: Inferred var decl"""
        input = """ Var: x = True;
                    Var: y = "abc";
                    Var: z = 1.2;
                    Var: w = 123;
                    Var: t[1] = {1};
                    Function: main
                    Parameter: x
                    Body:
                        x = y;
                        y = x;
                        w = z;
                        Return 1.1;
                    EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("w"),Id("z"))))
        self.assertTrue(TestChecker.test(input,expect,408))
    def test_inferredtype6(self):
        """Simple test: Inferred var decl"""
        input = """ Var: x = True;
                    Var: y = "abc";
                    Var: z = 1.2;
                    Var: w = 123;
                    Var: t[1] = {1};
                    Function: main
                    Parameter: x
                    Body:
                        x = y;
                        x = z;
                    EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("x"),Id("z"))))
        self.assertTrue(TestChecker.test(input,expect,409))
    def test_redecl_para(self):
        """Simple test: Redeclare parameter"""
        input = """ 
                    Function: main
                    Parameter: x,x
                    Body:
                    EndBody."""
        expect = str(Redeclared(Parameter(),"x"))
        self.assertTrue(TestChecker.test(input,expect,410))
    def test_redecl_para1(self):
        """Simple test: Redeclare parameter"""
        input = """ 
                    Function: main
                    Parameter: x,y
                    Body:
                        Var: x;
                    EndBody."""
        expect = str(Redeclared(Variable(),"x"))
        self.assertTrue(TestChecker.test(input,expect,411))
    
    def test_redecl_func(self):
        """Simple test: Redeclare fucntion"""
        input = """ 
                    Function: main
                    Body:
                    EndBody.
                    Function: main
                    Parameter: x,y
                    Body:
                        Var: t;
                    EndBody."""
        expect = str(Redeclared(Function(),"main"))
        self.assertTrue(TestChecker.test(input,expect,412))
    def test_redecl_func1(self):
        """Simple test: Redeclare function"""
        input = """ 
                    Function: foo
                    Body:
                    EndBody.
                    Function: main
                    Parameter: x,y
                    Body:
                        Var: t;
                    EndBody.
                    Function: foo
                    Body:
                    EndBody."""
        expect = str(Redeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,413))
    
    def test_undeclare_id(self):
        """ Simple test: Undeclare identifier"""
        input = """ 
                    Function: main
                    Parameter: x,y
                    Body:
                        t = x;
                    EndBody.
                    """
        expect = str(Undeclared(Identifier(),"t"))
        self.assertTrue(TestChecker.test(input,expect,414))
    
    def test_undeclare_id1(self):
        """ Simple test: Undeclare identifier"""
        input = """ 
                    Function: main
                    Parameter: x,y
                    Body:
                        t = x;
                    EndBody.
                    """
        expect = str(Undeclared(Identifier(),"t"))
        self.assertTrue(TestChecker.test(input,expect,415))
    
    def test_undeclare_id2(self):
        """ Simple test: Undeclare identifier"""
        input = """ Var: x;
                    Function: main
                    Parameter: x,y
                    Body:
                        main(t,t);
                    EndBody.
                    """
        expect = str(Undeclared(Identifier(),"t"))
        self.assertTrue(TestChecker.test(input,expect,416))
    
    def test_undeclare_func(self):
        """ Simple test: Undeclare function"""
        input = """ Var: x;
                    Function: main
                    Parameter: x,y
                    Body:
                        foo(1,2);
                        Return ;
                    EndBody.
                    """
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,417))
    
    def test_typecannotinfferd(self):
        """ Simple test: Test type cannot inferred"""
        input = """ Var: z;
                    Function: main
                    Parameter: x,y
                    Body:
                        z = x;
                    EndBody.
                    """
        expect = str(TypeCannotBeInferred(Assign(Id("z"),Id("x"))))
        self.assertTrue(TestChecker.test(input,expect,418))
    
    def test_typecannotinfferd1(self):
        """ Simple test: Test type cannot inferred"""
        input = """ Var: z;
                    Function: foo
                    Parameter: x,y
                    Body:
                    EndBody.
                    Function: main
                    Parameter: x,y
                    Body:
                        foo(x,y);
                    EndBody.
                    """
        expect = str(TypeCannotBeInferred(CallStmt(Id(name="foo"),[Id(name="x"),Id(name="y")])))
        self.assertTrue(TestChecker.test(input,expect,419))
    
   
    def test_typecannotinfferd2(self):
        """ Simple test: Test type cannot inferred"""
        input = """ Var: z;
                    Function: foo
                    Parameter: x,y
                    Body:
                    EndBody.
                    Function: main
                    Parameter: x,y
                    Body:
                        If x > 1 Then
                            Var: t;
                            y = t;
                        EndIf.
                    EndBody.
                    """
        expect = str(TypeCannotBeInferred(Assign(Id("y"),Id("t"))))
        self.assertTrue(TestChecker.test(input,expect,420))
    
    def test_typecannotinfferd3(self):
        """ Simple test: Test type cannot inferred"""
        input = """Function: foo
                    Parameter: x,y
                    Body:
                    EndBody.
                    Function: main
                    Parameter: x,y
                    Body:
                        x = 1;
                        For(x =1, x < 1, 1) Do
                            Var: t;
                            t = y;
                        EndFor.
                    EndBody.
                    """
        expect = str(TypeCannotBeInferred(Assign(Id("t"),Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,421))
    
    def test_typecannotinfferd4(self):
        """ Simple test: Test type cannot inferred"""
        input = """Function: foo
                    Parameter: x,y
                    Body:
                    EndBody.
                    Function: main
                    Parameter: x,y
                    Body:
                        x = 1;
                        For(x =1, x < 1, 1) Do
                            Var: t;
                            t = y;
                        EndFor.
                    EndBody.
                    """
        expect = str(TypeCannotBeInferred(Assign(Id("t"),Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,422))
    def test_typecannotinfferd5(self):
        """ Simple test: Test type cannot inferred"""
        input = """Function: foo
                    Parameter: x,y
                    Body:
                    EndBody.
                    Function: main
                    Parameter: x,y,z
                    Body:
                        x = 1;
                        While y Do
                            Var: t;
                            t = z;
                        EndWhile.
                    EndBody.
                    """
        expect = str(TypeCannotBeInferred(Assign(Id("t"),Id("z"))))
        self.assertTrue(TestChecker.test(input,expect,423))
    
    def test_typecannotinfferd6(self):
        """ Simple test: Test type cannot inferred"""
        input = """Function: foo
                    Parameter: x,y
                    Body:
                    EndBody.
                    Function: main
                    Parameter: x,y,z
                    Body:
                        x = 1;
                        Do
                            Var: t;
                            t = z;
                        While y
                        EndDo.
                    EndBody.
                    """
        expect = str(TypeCannotBeInferred(Assign(Id("t"),Id("z"))))
        self.assertTrue(TestChecker.test(input,expect,424))
    
    def test_typemismatchinstatment(self):
        """ Simple test: Test type mismatch in statment - if"""
        input = """Function: foo
                    Parameter: x,y
                    Body:
                    EndBody.
                    Function: main
                    Parameter: x,y,z
                    Body:
                        x = 1;
                        If x Then
                            Var: t;
                        EndIf.
                    EndBody.
                    """
        expect = str(TypeMismatchInStatement(If([(Id("x"),[VarDecl(Id("t"),[],None)],[])],([],[]))))
        self.assertTrue(TestChecker.test(input,expect,425))
    

    def test_typemismatchinstatment2(self):
        """ Simple test: Test type mismatch in statment -if1"""
        input = """Function: foo
                    Parameter: x,y
                    Body:
                    EndBody.
                    Function: main
                    Parameter: x,y,z
                    Body:
                        y = 1.2;
                        If x Then
                            Var: t;
                            t = x;
                        ElseIf y Then
                            Var: z;
                            t = x;
                        Else
                            Var: a;
                            t = a;
                        EndIf.
                    EndBody.
                    """
        expect = str(TypeMismatchInStatement(If([(Id("x"),[VarDecl(Id("t"),[],None)],[Assign(Id("t"),Id("x"))]),(Id("y"),[VarDecl(Id("z"),[],None)],[Assign(Id("t"),Id("x"))])],([VarDecl(Id("a"),[],None)],[Assign(Id("t"),Id("a"))]))))
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_typemismatchinstatment3(self):
        """ Simple test: Test type mismatch in statment -if 2"""
        input = """Function: foo
                Parameter: x,y
                Body:
                EndBody.
                Function: main
                Parameter: x,y,z
                Body:
                    y = 1.1;
                    If x Then
                        Var: t;
                        t = x;
                    ElseIf y Then
                        Var: z;
                        t = x;
                    Else
                        Var: a;
                        t = a;
                    EndIf.
                EndBody.
                """
        expect = str(TypeMismatchInStatement(If([(Id("x"),[VarDecl(Id("t"),[],None)],[Assign(Id("t"),Id("x"))]),(Id("y"),[VarDecl(Id("z"),[],None)],[Assign(Id("t"),Id("x"))])],([VarDecl(Id("a"),[],None)],[Assign(Id("t"),Id("a"))]))))
        self.assertTrue(TestChecker.test(input,expect,427))
    def test_typemismatchinstatment3(self):
        """ Simple test: Test type mismatch in statment -if 3"""
        input = """Function: foo
                Parameter: x,y
                Body:
                EndBody.
                Function: main
                Parameter: x,y,z
                Body:
                    If x Then
                        Var: t;
                        t = x;
                    ElseIf y+1 Then
                        Var: z;
                        t = x;
                    Else
                        Var: a;
                        t = a;
                    EndIf.
                EndBody.
                """
        expect = str(TypeMismatchInStatement(If([(Id("x"),[VarDecl(Id("t"),[],None)],[Assign(Id("t"),Id("x"))]),(BinaryOp("+",Id("y"),IntLiteral(1)),[VarDecl(Id("z"),[],None)],[Assign(Id("t"),Id("x"))])],([VarDecl(Id("a"),[],None)],[Assign(Id("t"),Id("a"))]))))
        self.assertTrue(TestChecker.test(input,expect,428))
    def test_typemismatchinstatment4(self):
        """ Simple test: Test type mismatch in statment -for """
        input = """
                Function: main
                Parameter: x
                Body:
                    Var: y=1.2;
                    For(x = y, x < 10, 1) Do
                        Var: t;
                        t = x;
                    EndFor.
                EndBody.
                """
        expect = str(TypeMismatchInStatement(For(Id("x"),Id("y"),BinaryOp("<",Id("x"),IntLiteral(10)),IntLiteral(1),([VarDecl(Id("t"),[],None)],[Assign(Id("t"),Id("x"))]))))
        self.assertTrue(TestChecker.test(input,expect,428))
    
    def test_typemismatchinstatment5(self):
        """ Simple test: Test type mismatch in statment -for 1"""
        input = """
                Function: main
                Parameter: x
                Body:
                    Var: y;
                    For(x = 1, x + 1, 1) Do
                        Var: t;
                        t = x;
                    EndFor.
                EndBody.
                """
        expect = str(TypeMismatchInStatement(For(Id("x"),IntLiteral(1),BinaryOp("+",Id("x"),IntLiteral(1)),IntLiteral(1),([VarDecl(Id("t"),[],None)],[Assign(Id("t"),Id("x"))]))))
        self.assertTrue(TestChecker.test(input,expect,429))
    
    def test_typemismatchinstatment6(self):
        """ Simple test: Test type mismatch in statment -for 2"""
        input = """
                Function: main
                Parameter: x
                Body:
                    Var: y;
                    For(x = 1, x < 1, 1.1) Do
                        Var: t;
                        t = x;
                    EndFor.
                EndBody.
                """
        expect = str(TypeMismatchInStatement(For(Id("x"),IntLiteral(1),BinaryOp("<",Id("x"),IntLiteral(1)),FloatLiteral(1.1),([VarDecl(Id("t"),[],None)],[Assign(Id("t"),Id("x"))]))))
        self.assertTrue(TestChecker.test(input,expect,430))
    
    def test_typemismatchinstatment7(self):
        """ Simple test: Test type mismatch in statment - 2"""
        input = """
                Function: main
                Parameter: x
                Body:
                    Var: y;
                    While y+1 Do
                        Var: x;
                        x = y
                    EndWhile.
                EndBody.
                """
        expect = str(TypeMismatchInStatement(While(BinaryOp("+",Id("y"),IntLiteral(1)),([VarDecl(Id("x"),[],None)],[Assign(Id("x"),Id("y"))]))))
        self.assertTrue(TestChecker.test(input,expect,431))
    
    def test_typemismatchinstatment7(self):
        """ Simple test: Test type mismatch in statment - while"""
        input = """
                Function: main
                Parameter: x
                Body:
                    Var: y;
                    While y+1 Do
                        Var: x;
                        x = y;
                    EndWhile.
                EndBody.
                """
        expect = str(TypeMismatchInStatement(While(BinaryOp("+",Id("y"),IntLiteral(1)),([VarDecl(Id("x"),[],None)],[Assign(Id("x"),Id("y"))]))))
        self.assertTrue(TestChecker.test(input,expect,432))
    
    def test_typemismatchinstatment8(self):
        """ Simple test: Test type mismatch in statment - do"""
        input = """
                Function: main
                Parameter: x
                Body:
                    Var: y;
                    Do
                        Var: x;
                        x = y;
                    While y+1
                    EndDo.
                EndBody.
                """
        expect = str(TypeMismatchInStatement(Dowhile(([VarDecl(Id("x"),[],None)],[Assign(Id("x"),Id("y"))]),BinaryOp("+",Id("y"),IntLiteral(1)))))
        self.assertTrue(TestChecker.test(input,expect,433))
    
    def test_typemismatchinstatment9(self):
        """ Simple test: Test type mismatch in statment - assign"""
        input = """
                Function: main
                Parameter: x
                Body:
                    Var: y;
                    foo("x","y");
                EndBody.
                Function: foo
                Parameter: x,y
                Body:
                     x = 1;
                     y = 1;
                EndBody.
                """
        expect = str(TypeMismatchInStatement(Assign(Id("x"),IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,434))
    
    def test_typemismatchinstatment10(self):
        """ Simple test: Test type mismatch in statment - assign"""
        input = """
                Function: main
                Parameter: x
                Body:
                    Var: y;
                     y = foo("x","y");
                EndBody.
                Function: foo
                Parameter: x,y
                Body:
                     x = 1;
                     y = 1;
                EndBody.
                """
        expect = str(TypeCannotBeInferred(Assign(Id("y"),CallExpr(Id("foo"),[StringLiteral("x"),StringLiteral("y")]))))
        self.assertTrue(TestChecker.test(input,expect,435))
    
    def test_typemismatchinstatment11(self):
        """ Simple test: Test type mismatch in statment - assign 1"""
        input = """
                Function: main
                Parameter: x
                Body:
                    Var: y ;
                     y = foo("x","y");
                EndBody.
                Function: foo
                Parameter: x,y
                Body:
                     x = 1;
                     y = 1;
                EndBody.
                """
        expect = str(TypeCannotBeInferred(Assign(Id("y"),CallExpr(Id("foo"),[StringLiteral("x"),StringLiteral("y")]))))
        self.assertTrue(TestChecker.test(input,expect,436))
    
   
    
    def test_typemismatchinstatment13(self):
        """ Simple test: Test type mismatch in statment - assign 2"""
        input = """
                Function: main
                Parameter: x
                Body:
                    Var: y = True;
                    If x Then 
                        Var: t;
                        x = 1;
                    EndIf.
                EndBody.
                Function: foo
                Parameter: x,y
                Body:
                     x = 1;
                     y = 1;
                EndBody.
                """
        expect = str(TypeMismatchInStatement(Assign(Id("x"),IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,437))
    def test_typemismatchinstatment14(self):
        """ Simple test: Test type mismatch in statment - assign 2"""
        input = """
                Function: main
                Parameter: x
                Body:
                    Var: y = True;
                    If x Then 
                        Var: t;
                        x = y + foo(t);
                    EndIf.
                EndBody.
                Function: foo
                Parameter: x
                Body:
                     x = 1;
                EndBody.
                """
        expect = str(TypeCannotBeInferred(Assign(Id("x"),BinaryOp("+",Id("y"),CallExpr(Id("foo"),[Id("t")])))))
        self.assertTrue(TestChecker.test(input,expect,438))
    
    def test_typemismatchinstatment15(self):
        """ Simple test: Test type mismatch in statment - assign 2"""
        input = """
                Function: main
                Parameter: x
                Body:
                    Var: y = True;
                    If x Then 
                        Var: t;
                        x = y + foo(1);
                    EndIf.
                EndBody.
                Function: foo
                Parameter: x
                Body:
                     x = 1;
                EndBody.
                """
        expect = str(TypeMismatchInExpression(BinaryOp("+",Id("y"),CallExpr(Id("foo"),[IntLiteral(1)]))))
        self.assertTrue(TestChecker.test(input,expect,439))
    
    def test_typemismatchinstatment16(self):
        """ Simple test: Test type mismatch in statment - call stmt"""
        input = """
                Function: main
                Parameter: x
                Body:
                    Var: y = True;
                    foo();
                EndBody.
                Function: foo
                Parameter: x
                Body:
                     x = 1;
                EndBody.
                """
        expect = str(TypeMismatchInStatement(CallStmt(Id("foo"),[])))
        self.assertTrue(TestChecker.test(input,expect,440))
    def test_typemismatchinstatment17(self):
        """ Simple test: Test type mismatch in statment - call stmt"""
        input = """
                Function: main
                Parameter: x
                Body:
                    Var: y = True;
                    foo(1,2);
                EndBody.
                Function: foo
                Parameter: x
                Body:
                     x = 1;
                EndBody.
                """
        expect = str(TypeMismatchInStatement(CallStmt(Id("foo"),[IntLiteral(1),IntLiteral(2)])))
        self.assertTrue(TestChecker.test(input,expect,441))
    
    def test_typemismatchinstatment18(self):
        """ Simple test: Test type mismatch in statment - return stmt"""
        input = """
                Function: main
                Parameter: x
                Body:
                    Var: y = True;
                    main(1);
                    Return 1;
                EndBody.
                Function: foo
                Parameter: x
                Body:
                    x = 1;
                    Return 1.1;
                EndBody.
                """
        expect = str(TypeMismatchInStatement(Return(IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,442))
    
    def test_typemismatchinstatment19(self):
        """ Simple test: Test type mismatch in statment - return stmt"""
        input = """
                Function: main
                Parameter: x
                Body:
                    Var: y = True;
                    x = 1+ foo(1);
                    Return 1;
                EndBody.
                Function: foo
                Parameter: x
                Body:
                    x = 1;
                    Return 1.1;
                EndBody.
                """
        expect = str(TypeMismatchInStatement(Return(FloatLiteral(1.1))))
        self.assertTrue(TestChecker.test(input,expect,443))
    
    def test_typemismatchinstatment20(self):
        """ Simple test: Test type mismatch in statment - return stmt"""
        input = """
                Function: main
                Parameter: x
                Body:
                    Var:y;
                    If x Then 
                        Var:y ;
                        Return 1.1;
                    ElseIf y Then
                        Return 1;
                    EndIf.
                EndBody.
                Function: foo
                Parameter: x
                Body:
                    x = 1;
                    Return 1.1;
                EndBody.
                """
        expect = str(TypeMismatchInStatement(Return(IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,444))
    
    def test_typemismatchinstatment21(self):
        """ Simple test: Test type mismatch in statment - return stmt"""
        input = """
                Function: main
                Parameter: x
                Body:
                    Return 2+foo(1);
                    Return 1.1;
                EndBody.
                Function: foo
                Parameter: x
                Body:
                    x = 1;
                EndBody.
                """
        expect = str(TypeMismatchInStatement(Return(FloatLiteral(1.1))))
        self.assertTrue(TestChecker.test(input,expect,445))
    
    def test_typemismatchexpression(self):
        """ Simple test: Test type mismatch in expression - add-int"""
        input = """
                Var: x = 1,y = 1.1,z;
                Function: main
                Parameter: x
                Body:
                    x = y + z;
                EndBody.
                Function: foo
                Parameter: x
                Body:
                    x = 1;
                EndBody.
                """
        expect = str(TypeMismatchInExpression(BinaryOp("+",Id("y"),Id("z"))))
        self.assertTrue(TestChecker.test(input,expect,446))
    
    def test_typemismatchexpression1(self):
        """ Simple test: Test type mismatch in expression - add-float"""
        input = """
                Var: x = 1,y = 1.1,z;
                Function: main
                Parameter: x
                Body:
                    x = y +. z;
                    x = 1 + z;
                EndBody.
                Function: foo
                Parameter: x
                Body:
                    x = 1;
                EndBody.
                """
        expect = str(TypeMismatchInExpression(BinaryOp("+",IntLiteral(1),Id("z"))))
        self.assertTrue(TestChecker.test(input,expect,447))
    
    def test_typemismatchexpression2(self):
        """ Simple test: Test type mismatch in expression - exp if"""
        input = """
                Var: x = 1,y = 1.1,z;
                Function: main
                Parameter: x
                Body:
                    If x+.1 Then
                    EndIf.
                EndBody.
                Function: foo
                Parameter: x
                Body:
                    x = 1;
                EndBody.
                """
        expect = str(TypeMismatchInExpression(BinaryOp("+.",Id("x"),IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_typemismatchexpression3(self):
        """ Simple test: Test type mismatch in expression - exp if"""
        input = """
                Var: x = 1,y = 1.1,z;
                Function: main
                Parameter: x
                Body:
                    If x+.1 Then
                    EndIf.
                EndBody.
                Function: foo
                Parameter: x
                Body:
                    x = 1;
                EndBody.
                """
        expect = str(TypeMismatchInExpression(BinaryOp("+.",Id("x"),IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,448))
    
    def test_typemismatchexpression4(self):
        """ Simple test: Test type mismatch in expression - exp if"""
        input = """
                Var: x = 1,y = 1.1,z;
                Function: main
                Parameter: x
                Body:
                    If x Then
                    ElseIf x + 1 Then
                    EndIf.
                EndBody.
                Function: foo
                Parameter: x
                Body:
                    x = 1;
                EndBody.
                """
        expect = str(TypeMismatchInExpression(BinaryOp("+",Id("x"),IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,449))
    
    def test_typemismatchexpression5(self):
        """ Simple test: Test type mismatch in expression - exp for"""
        input = """
                Var: x = 1,y = 1.1,z;
                Function: main
                Parameter: x
                Body:
                    For(x = 1+.2, x < 2,2) Do
                    EndFor.
                EndBody.
                Function: foo
                Parameter: x
                Body:
                    x = 1;
                EndBody.
                """
        expect = str(TypeMismatchInExpression(BinaryOp("+.",IntLiteral(1),IntLiteral(2))))
        self.assertTrue(TestChecker.test(input,expect,450))
    
    def test_typemismatchexpression5(self):
        """ Simple test: Test type mismatch in expression - exp for"""
        input = """
                Var: x = 1,y = 1.1,z;
                Function: main
                Parameter: x
                Body:
                    For(x = 1, x -. 2,2) Do
                    EndFor.
                EndBody.
                Function: foo
                Parameter: x
                Body:
                    x = 1;
                EndBody.
                """
        expect = str(TypeMismatchInExpression(BinaryOp("-.",Id("x"),IntLiteral(2))))
        self.assertTrue(TestChecker.test(input,expect,451))
    
    def test_typemismatchexpressio6(self):
        """ Simple test: Test type mismatch in expression - exp for"""
        input = """
                Var: x = 1,y = 1.1,z;
                Function: main
                Parameter: x
                Body:
                    For(x = 1, x > 2,!x) Do
                    EndFor.
                EndBody.
                Function: foo
                Parameter: x
                Body:
                    x = 1;
                EndBody.
                """
        expect = str(TypeMismatchInExpression(UnaryOp("!",Id("x"))))
        self.assertTrue(TestChecker.test(input,expect,452))
    
    def test_typemismatchexpressio7(self):
        """ Simple test: Test type mismatch in expression - exp while"""
        input = """
                Var: x = 1,y = 1.1,z;
                Function: main
                Parameter: x
                Body:
                    While x\\.1 Do
                    EndWhile.
                EndBody.
                Function: foo
                Parameter: x
                Body:
                    x = 1;
                EndBody.
                """
        expect = str(TypeMismatchInExpression(BinaryOp("\.",Id("x"),IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,453))
    
    def test_typemismatchexpressio8(self):
        """ Simple test: Test type mismatch in expression - exp while"""
        input = """
                Var: x = 1,y = 1.1,z;
                Function: main
                Parameter: t
                Body:
                    While -.x Do
                    EndWhile.
                EndBody.
                Function: foo
                Parameter: x
                Body:
                    x = 1;
                EndBody.
                """
        expect = str(TypeMismatchInExpression(UnaryOp("-.",Id("x"))))
        self.assertTrue(TestChecker.test(input,expect,454))
    
    def test_typemismatchexpressio9(self):
        """ Simple test: Test type mismatch in expression - exp dowhile"""
        input = """
                Var: x = 1,y = 1.1,z;
                Function: main
                Parameter: t
                Body:
                    Do
                    While x == y
                    EndDo.
                EndBody.
                Function: foo
                Parameter: x
                Body:
                    x = 1;
                EndBody.
                """
        expect = str(TypeMismatchInExpression(BinaryOp("==",Id("x"),Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,455))
    
    def test_typemismatchexpressio10(self):
        """ Simple test: Test type mismatch in expression - exp dowhile"""
        input = """
                Var: x = 1,y = 1.1,z;
                Function: main
                Parameter: t
                Body:
                    Do
                    While -y
                    EndDo.
                EndBody.
                Function: foo
                Parameter: x
                Body:
                    x = 1;
                EndBody.
                """
        expect = str(TypeMismatchInExpression(UnaryOp("-",Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_array(self):
        """ Simple test: Test array"""
        input = """
                Var: x=1,y[1][2][3];
                Function: main
                Parameter: t
                Body:
                    If !y[1][2][3] + 1Then
                    EndIf.
                EndBody.
                
                """
        expect = str(TypeMismatchInExpression(BinaryOp("+",UnaryOp("!",ArrayCell(Id("y"),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])),IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,457))
    def test_array1(self):
        """ Simple test: Test array"""
        input = """
                Var: x=1,y[1][2][3];
                Function: main
                Parameter: t
                Body:
                    y[1][2][3] = x;
                    t = y[1][2][3] +. 1.1;
                EndBody.
                
                """
        expect = str(TypeMismatchInExpression(BinaryOp("+.",ArrayCell(Id("y"),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]),FloatLiteral(1.1))))
        self.assertTrue(TestChecker.test(input,expect,458))
    
    def test_array2(self):
        """ Simple test: Test array"""
        input = """
                Var: x=1,y[2];
                Function: main
                Parameter: t
                Body:
                    y[2] = {1,2} + 1;
                EndBody.
                
                """
        expect = str(TypeMismatchInExpression(BinaryOp("+",ArrayLiteral([IntLiteral(1),IntLiteral(2)]),IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,459))
    
    def test_array3(self):
        """ Simple test: Test array"""
        input = """
                Var: x=1,y[2];
                Function: main
                Parameter: t
                Body:
                    y[2] = {1,2} + {1,2};
                EndBody.
                
                """
        expect = str(TypeMismatchInExpression(BinaryOp("+",ArrayLiteral([IntLiteral(1),IntLiteral(2)]),ArrayLiteral([IntLiteral(1),IntLiteral(2)]))))
        self.assertTrue(TestChecker.test(input,expect,460))
    
    def test_array4(self):
        """ Simple test: Test array"""
        input = """
                Var: x=1,y[2] = {1};
                Function: foo
                Parameter: x
                Body:
                    Return y;
                EndBody.
                Function: main
                Parameter: t[1]
                Body:
                    t = 1 +. foo(1);
                EndBody.
                
                """
        expect = str(TypeMismatchInExpression(BinaryOp("+.",IntLiteral(1),CallExpr(Id("foo"),[IntLiteral(1)]))))
        self.assertTrue(TestChecker.test(input,expect,461))
    
    def test_array5(self):
        """ Simple test: Test array"""
        input = """
                Var: x=1,y[2] = {1};
                Function: foo
                Parameter: x
                Body:
                    Return y;
                EndBody.
                Function: main
                Parameter: t[1]
                Body:
                    Var: a;
                    t[1] = foo(1)[1];
                    a = t[1] +. 1.1;
                EndBody.
                
                """
        expect = str(TypeMismatchInExpression(BinaryOp("+.",ArrayCell(Id("t"),[IntLiteral(1)]),FloatLiteral(1.1))))
        self.assertTrue(TestChecker.test(input,expect,462))
    
    def test_exprfunc(self):
        """ Simple test: Test expr func"""
        input = """
                Var: x=1,y[2] = {1};
                Function: foo
                Parameter: x,y
                Body:
                    x = 1;
                    y = "abc";
                    Return y;
                EndBody.
                Function: main
                Parameter: t[1]
                Body:
                    Var: a;
                    t[1] = foo(1.1,"2")[1];
                    a = t[1] +. 1.1;
                EndBody.
                
                """
        expect = str(TypeMismatchInExpression(CallExpr(Id("foo"),[FloatLiteral(1.1),StringLiteral("2")])))
        self.assertTrue(TestChecker.test(input,expect,463))

    def test_type_mismatch_in_expr_binop_4(self):
        """Simple program"""
        input = """
        Var: t = 6;
        Var: m = 0;
        Function: main
            Parameter: a, b
            Body:
                Var: z = 1;
                Do 
                    m = m + 1;
                    z = m - z;
                While
                    t < m
                EndDo.
                Return z;
            EndBody.
        
        Function: doST
            Body:
                t = main(1, 2) *. 1.2 \\. 2.9;
            EndBody.
        """
        expect = str(TypeMismatchInExpression(
            BinaryOp(op="*.",left=CallExpr(method=Id(name="main"),param=[IntLiteral(value=1),IntLiteral(value=2)]),right=FloatLiteral(value=1.2))
        ))
        self.assertTrue(TestChecker.test(input,expect,464))
    
    def test_exprfunc1(self):
        """ Simple test: Test expr func"""
        input = """
                Var: x=1,y[2] = {1};
                Function: foo
                Parameter: x,y,z
                Body:
                    x = 1;
                    y = "abc";
                    Return y;
                EndBody.
                Function: main
                Parameter: t[1]
                Body:
                    Var: a;
                    t[1] = foo(1,"2")[1];
                    a = t[1] +. 1.1;
                EndBody.
                
                """
        expect = str(TypeMismatchInExpression(CallExpr(Id("foo"),[IntLiteral(1),StringLiteral("2")])))
        self.assertTrue(TestChecker.test(input,expect,465))
    
    def test_type_mismatch_in_expr_binop_1(self):
        """Simple program: """
        input = """
        Var: x = 0;
        Function: main
            Parameter: c, d
            Body:
                Var: check = True;
                If check && c Then c = False;
                ElseIf c + d Then x = 1;
                EndIf.
            EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp(op="+",left=Id(name="c"),right=Id(name="d"))))
        self.assertTrue(TestChecker.test(input,expect,466))

    def test_type_mismatch_in_expr_binop_2(self):
        """Simple program"""
        input = """
        Var: t = 6;
        Var: m = 0;
        Function: main
            Body:
                Do 
                    Var: z = "a";
                    m = m + 1;
                    z = m - z;
                While
                    t < m
                EndDo.
            EndBody.
        """
        expect = str(TypeMismatchInExpression(
            BinaryOp(op="-",left=Id(name="m"),right=Id(name="z"))
        ))
        self.assertTrue(TestChecker.test(input,expect,467))

    def test_type_mismatch_in_expr_arraycell_4(self):
        """Simple program"""
        input = """
        Var: x[2][2] = {{1,2},{3,4}};
        Var: y[1] = {"a"};
        Function: main
            Parameter: n, m
            Body:
                x[1][1] = 2;
                y[x] = "b";
            EndBody.
        """
        expect = str(TypeMismatchInExpression(
            ArrayCell(arr=Id(name="y"),idx=[Id(name="x")])
        ))
        self.assertTrue(TestChecker.test(input,expect,468))
    def test_type_cannot_be_inferred_1(self):
        """Simple program: """
        input = """
        Var: b;
        Function: main
            Parameter: c
            Body:
                b = c;
            EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(lhs=Id(name="b"),rhs=Id(name="c"))))
        self.assertTrue(TestChecker.test(input,expect,469))

    def test_type_cannot_be_inferred_2(self):
        """Simple program: """
        input = """
        Var: y;
        Function: main
            Parameter: a
            Body:
                Var: x;
                y = a + main(x);
            EndBody.
        """
        expect = str(TypeCannotBeInferred( Assign(Id("y"),BinaryOp("+",Id("a"),CallExpr(Id("main"),[Id("x")])))))
        self.assertTrue(TestChecker.test(input,expect,470))
    
    def test_type_cannot_be_inferred_3(self):
        """Simple program: """
        input = """
        Var: y;
        Function: main
            Parameter: a
            Body:
                Var: x;
                If main(x) Then
                EndIf.
            EndBody.
        """
        expect = str(TypeCannotBeInferred(If([(CallExpr(Id("main"),[Id("x")]),[],[])],([],[]))))
        self.assertTrue(TestChecker.test(input,expect,471))
    
    def test_type_cannot_be_inferred_4(self):
        """Simple program: """
        input = """
        Var: y;
        Function: main
            Parameter: t
            Body:
                Var:x,a;
                For(a = main(x),a < 10, 2) Do
                EndFor.
            EndBody.
        """
        expect = str(TypeCannotBeInferred(For(Id("a"),CallExpr(Id("main"),[Id("x")]),BinaryOp("<",Id("a"),IntLiteral(10)),IntLiteral(2),([],[]))))
        self.assertTrue(TestChecker.test(input,expect,472))
    
    def test_type_cannot_be_inferred_5(self):
        """Simple program: """
        input = """
        Var: y;
        Function: main
            Parameter: t
            Body:
                Var:x,a;
                For(a = 1,main(x), 2) Do
                EndFor.
            EndBody.
        """
        expect = str(TypeCannotBeInferred(For(Id("a"),IntLiteral(1),CallExpr(Id("main"),[Id("x")]),IntLiteral(2),([],[]))))
        self.assertTrue(TestChecker.test(input,expect,473))
    
    def test_type_cannot_be_inferred_6(self):
        """Simple program: """
        input = """
        Var: y;
        Function: main
            Parameter: t
            Body:
                Var:x,a;
                For(a = 1,a<2, main(x)) Do
                EndFor.
            EndBody.
        """
        expect = str(TypeCannotBeInferred(For(Id("a"),IntLiteral(1),BinaryOp("<",Id("a"),IntLiteral(2)),CallExpr(Id("main"),[Id("x")]),([],[]))))
        self.assertTrue(TestChecker.test(input,expect,474))
    
    def test_type_mismatch_in_stmt_assign_2(self):
        """Simple program: """
        input = """
        Var: x = 0;
        Function: main
            Parameter: c, d
            Body:
                c = x;
                c = 1.2;
            EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(lhs=Id(name="c"),rhs=FloatLiteral(value=1.2))))
        self.assertTrue(TestChecker.test(input,expect,475))

    def test_type_mismatch_in_stmt_assign_3(self):
        """Simple program"""
        input = """
        Var: t = 1.2;
        Function: main
            Parameter: x, y
            Body:
                Var: t = True;
                If True Then
                    Var: t = 4.3;
                    If True Then
                        t = False;
                    EndIf.
                EndIf.
                **t = False;**
            EndBody.
        """
        expect = str(TypeMismatchInStatement(
            Assign(lhs=Id(name="t"),rhs=BooleanLiteral(value=False))
        ))
        self.assertTrue(TestChecker.test(input,expect,476))

    def test_type_mismatch_in_stmt_assign_4(self):
        """Simple program"""
        input = """
        Var: x = 1;
        Function: main
            Parameter: x, y
            Body:
                Var: z = "a";
                z = 1;
            EndBody.
        """
        expect = str(TypeMismatchInStatement(
            Assign(lhs=Id(name="z"),rhs=IntLiteral(value=1))
        ))
        self.assertTrue(TestChecker.test(input,expect,477))

    def test_type_mismatch_in_stmt_assign_5(self):
        """Simple program"""
        input = """
        Var: t = 1.2;
        Function: main
            Parameter: x, y
            Body:
                Var: t = True;
                If True Then
                    Var: t = 4.3;
                    If True Then
                        t = 3.4;
                    EndIf.
                EndIf.
                t = 1.9;
            EndBody.
        """
        expect = str(TypeMismatchInStatement(
            Assign(lhs=Id(name="t"),rhs=FloatLiteral(value=1.9))
        ))
        self.assertTrue(TestChecker.test(input,expect,478))

    def test_type_mismatch_in_stmt_assign_6(self):
        """Simple program: """
        input = """
        Var: x = 2, y = 3;
        Var: z = "zz";
        Function: doST
            Parameter: n, m
            Body:
                n = 1;
                m = 2;
                Return n + m;
            EndBody.

        Function: main
            Body:
                z = doST(x,y);
            EndBody.
        """
        expect = str(TypeMismatchInStatement(
            Assign(lhs=Id(name="z"),rhs=CallExpr(method=Id(name="doST"),param=[Id(name="x"),Id(name="y")]))
        ))
        self.assertTrue(TestChecker.test(input,expect,479))
    
    
    def test_type_cannot_be_inferred_7(self):
        """Simple program: """
        input = """
        Var: y;
        Function: main
            Parameter: t
            Body:
                Var:x,a;
                While main(x) Do
                EndWhile.
            EndBody.
        """
        expect = str(TypeCannotBeInferred(While(CallExpr(Id("main"),[Id("x")]),([],[]))))
        self.assertTrue(TestChecker.test(input,expect,480))
    
    def test_type_cannot_be_inferred_8(self):
        """Simple program: """
        input = """
        Var: y;
        Function: main
            Parameter: t
            Body:
                Var:x,a;
                Do
                While main(x)
                EndDo.
            EndBody.
        """
        expect = str(TypeCannotBeInferred(Dowhile(([],[]),CallExpr(Id("main"),[Id("x")]))))
        self.assertTrue(TestChecker.test(input,expect,481))
    
    def test_type_cannot_be_inferred_9(self):
        """Simple program: """
        input = """
        Var: y;
        Function: main
            Parameter: t
            Body:
                Var:x,a;
                main(x);
            EndBody.
        """
        expect = str(TypeCannotBeInferred(CallStmt(Id("main"),[Id("x")])))
        self.assertTrue(TestChecker.test(input,expect,482))
    
    def test_type_mismatch_in_stmt_if_1(self):
        """Simple program: """
        input = """
        Var: x = 0;
        Function: main
            Parameter: c
            Body:
                If x Then x = 3;
                EndIf.
            EndBody.
        """
        expect = str(TypeMismatchInStatement(If(
            ifthenStmt=
            [
                (Id(name="x"),[],[Assign(lhs=Id(name="x"),rhs=IntLiteral(value=3))]),
            ],
            elseStmt=([],[])
        )))
        self.assertTrue(TestChecker.test(input,expect,483))

    def test_type_mismatch_in_stmt_if_2(self):
        """Simple program"""
        input = """
        Var: t = 1.2;
        Function: main
            Parameter: x, y
            Body:
                Var: t = 1;
                If t * 2 Then
                    Var: x;
                    x = 1; 
                EndIf.
            EndBody.
        """
        expect = str(TypeMismatchInStatement(If(
            ifthenStmt=
            [
                (BinaryOp(op="*",left=Id(name="t"),right=IntLiteral(value=2)),
                [VarDecl(variable=Id(name="x"),varDimen=[],varInit=None)],
                [Assign(lhs=Id(name="x"),rhs=IntLiteral(value=1))]),
            ],
            elseStmt=([],[])
        )))
        self.assertTrue(TestChecker.test(input,expect,484))

    def test_type_mismatch_in_stmt_if_3(self):
        """Simple program"""
        input = """
        Var: t = 1.2;
        Var: m = 1;
        Function: main
            Parameter: x, y
            Body:
                Var: t = True;
                If True Then
                    x = 1;
                ElseIf m + 1 Then
                    x = 2; 
                EndIf.
            EndBody.
        """
        expect = str(TypeMismatchInStatement(If(
            ifthenStmt=
            [
                (BooleanLiteral(value=True),
                [],
                [Assign(lhs=Id(name="x"),rhs=IntLiteral(value=1))]),
                (BinaryOp(op="+",left=Id(name="m"),right=IntLiteral(value=1)),
                [],
                [Assign(lhs=Id(name="x"),rhs=IntLiteral(value=2))]),
            ],
            elseStmt=([],[])
        )))
        self.assertTrue(TestChecker.test(input,expect,485))

    def test_type_mismatch_in_stmt_if_4(self):
        """Simple program"""
        input = """
        Var: t = 1.2;
        Function: main
            Parameter: x, y
            Body:
                Var: t = True;
                x = 1;
                If t Then
                    Var: x;
                    x = 1; 
                ElseIf x Then 
                    x = 2;
                Else x = 3;
                EndIf.
            EndBody.
        """
        expect = str(TypeMismatchInStatement(If(
            ifthenStmt=
            [
                (Id(name="t"),
                [VarDecl(variable=Id(name="x"),varDimen=[],varInit=None)],
                [Assign(lhs=Id(name="x"),rhs=IntLiteral(value=1))]),
                (Id(name="x"),
                [],
                [Assign(lhs=Id(name="x"),rhs=IntLiteral(value=2))]),
            ],
            elseStmt=([],[Assign(lhs=Id(name="x"),rhs=IntLiteral(value=3))])
        )))
        self.assertTrue(TestChecker.test(input,expect,486))

    def test_type_mismatch_in_stmt_if_5(self):
        """Simple program"""
        input = """
        Var: t = 1.2;
        Function: main
            Parameter: x, y
            Body:
                Var: t = True;
                x = 1;
                If t Then
                    Var: x;
                    x = 1; 
                ElseIf x + 1 Then 
                    x = 2;
                Else x = 3;
                EndIf.
            EndBody.
        """
        expect = str(TypeMismatchInStatement(If(
            ifthenStmt=
            [
                (Id(name="t"),
                [VarDecl(variable=Id(name="x"),varDimen=[],varInit=None)],
                [Assign(lhs=Id(name="x"),rhs=IntLiteral(value=1))]),
                (BinaryOp(op="+",left=Id(name="x"),right=IntLiteral(value=1)),
                [],
                [Assign(lhs=Id(name="x"),rhs=IntLiteral(value=2))]),
            ],
            elseStmt=([],[Assign(lhs=Id(name="x"),rhs=IntLiteral(value=3))])
        )))
        self.assertTrue(TestChecker.test(input,expect,487))

    def test_type_mismatch_in_stmt_if_6(self):
        """Simple program"""
        input = """
        Var: t = 1.2;
        Var: n[2] = {1,2};
        Function: main
            Parameter: x, y
            Body:
                Var: t = True;
                x = 1;
                If t Then
                    Var: x;
                    x = 1; 
                ElseIf n[1] Then 
                    x = 2;
                Else x = 3;
                EndIf.
            EndBody.
        """
        expect = str(TypeMismatchInStatement(If(
            ifthenStmt=
            [
                (Id(name="t"),
                [VarDecl(variable=Id(name="x"),varDimen=[],varInit=None)],
                [Assign(lhs=Id(name="x"),rhs=IntLiteral(value=1))]),
                (ArrayCell(arr=Id(name="n"),idx=[IntLiteral(value=1)]),
                [],
                [Assign(lhs=Id(name="x"),rhs=IntLiteral(value=2))]),
            ],
            elseStmt=([],[Assign(lhs=Id(name="x"),rhs=IntLiteral(value=3))])
        )))
        self.assertTrue(TestChecker.test(input,expect,488))
    
    def test_globalfunc(self):
        """Simple program: """
        input = """
        Var: int_of_float;
        Function: main
            Parameter: t
            Body:
                
            EndBody.
        """
        expect = str(Redeclared(Variable(),"int_of_float"))
        self.assertTrue(TestChecker.test(input,expect,489))
    def test_globalfunc1(self):
        """Simple program: """
        input = """
        Var: x;
        Function: string_of_bool
        Parameter: x,y
        Body:
        EndBody.
        Function: main
            Parameter: t
            Body:
                
            EndBody.
        """
        expect = str(Redeclared(Function(),"string_of_bool"))
        self.assertTrue(TestChecker.test(input,expect,490))
    
    def test_globalfunc2(self):
        """Simple program: """
        input = """
        Var: x;
        Function: string
        Parameter: x,y
        Body:
        EndBody.
        Function: main
            Parameter: t
            Body:
                Var:x = 1.2,y;
                y = int_of_float(x);
                t = x +. y;
            EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp("+.",Id("x"),Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,491))
    
    def test_globalfunc3(self):
        """Simple program: """
        input = """
        Var: x;
        Function: string
        Parameter: x,y
        Body:
        EndBody.
        Function: main
            Parameter: t
            Body:
                Var:x = "True",y;
                If bool_of_string(x) Then
                    x = True;
                EndIf.
            EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id("x"),BooleanLiteral(True))))
        self.assertTrue(TestChecker.test(input,expect,492))
    
    def test_globalfunc4(self):
        """Simple program: """
        input = """
        Var: x;
        Function: string
        Parameter: x,y
        Body:
        EndBody.
        Function: main
            Parameter: a
            Body:
                Var:x = "True",y, t = 1;
                If bool_of_string(x) Then
                    y = read();
                    t = y + 1;
                EndIf.
            EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp("+",Id("y"),IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,493))
    
    def test_globalfunc5(self):
        """Simple program: """
        input = """
        Var: x;
        Function: string
        Parameter: x,y
        Body:
        EndBody.
        Function: main
            Parameter: a
            Body:
                Var:x = "True",y, t = 1;
                If bool_of_string(x) Then
                    y = read(1,2);
                    t = y + 1;
                EndIf.
            EndBody.
        """
        expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(1),IntLiteral(2)])))
        self.assertTrue(TestChecker.test(input,expect,494))
    
    def test_globalfunc6(self):
        """Simple program: """
        input = """
        Var: x;
        Function: string
        Parameter: x,y
        Body:
        EndBody.
        Function: main
            Parameter: a
            Body:
                Var:x = "True",y, t = 1;
                If bool_of_string(x) Then
                    y = printLn();
                    t = y + 1;
                EndIf.
            EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id("y"),CallExpr(Id("printLn"),[]))))
        self.assertTrue(TestChecker.test(input,expect,495))
    def test_globalfunc7(self):
        """Simple program: """
        input = """
        Var: x;
        Function: string
        Parameter: x,y
        Body:
        EndBody.
        Function: main
            Parameter: a
            Body:
                Var:x = "True",y, t = 1;
                If bool_of_string(x) Then
                    printLn();
                    y = float_of_string("abc") +. float_to_int(1);
                    t = y + 1;
                EndIf.
            EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp("+",Id("y"),IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,496))
    
    def test_globalfunc8(self):
        """Simple program: """
        input = """
        Var: x;
        Function: string
        Parameter: x,y
        Body:
        EndBody.
        Function: main
            Parameter: a
            Body:
                Var:x = "True",y, t = 1;
                If bool_of_string(x) Then
                    printLn();
                    y = float_of_string("abc") +. float_to_int(1);
                    x = read();
                    x = string_of_float(y);
                    x = True;
                EndIf.
            EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id("x"),BooleanLiteral(True))))
        self.assertTrue(TestChecker.test(input,expect,497))
    
    def test_visitvar(self):
        """Simple program: """
       	input = """
        Var: var;
        Function: string
        Parameter: x,y
        Body:
        EndBody.
        Function: main
            Parameter: a
            Body:
                Var:x = "True",y, t = 1;
                If bool_of_string(x) Then
                    For(t = 2, t < 10, 2) Do
                        var = 1;
                        var = "String";
                    EndFor.
                EndIf.
            EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id("var"),StringLiteral("String"))))
        self.assertTrue(TestChecker.test(input,expect,498))
    
    def test_noentry(self):
        """Simple program: """
       	input = """
        Var: main; 
        """
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,499))
    
    def test_redec(self):
        """Simple program: """
       	input = """
        Var: main; 
        Function:main
        Parameter: main,main
        Body:
            Var: main;
        EndBody.
        """
        expect = str(Redeclared(Function(),"main"))
        self.assertTrue(TestChecker.test(input,expect,500))
    
    def test_redec1(self):
        """Simple program: """
       	input = """
        Var: foo; 
        Function:main
        Parameter: main,main
        Body:
            Var: main;
        EndBody.
        """
        expect = str(Redeclared(Parameter(),"main"))
        self.assertTrue(TestChecker.test(input,expect,501))
    
    def test_type_mismatch_in_stmt_return_3(self):
        """Simple program: """
        input = """
        Var: t = 1.2;
        Var: re_val = 2.4;
        Function: main
            Parameter: x, y
            Body:
                Var: t = True;
                x = 1;
                If t Then
                    Var: x;
                    x = 1;
                    Return x; 
                ElseIf !t Then 
                    Return re_val;
                Else x = 3;
                EndIf.
            EndBody.
        """
        expect = str(TypeMismatchInStatement(
            Return(Id(name="re_val"))
        ))
        self.assertTrue(TestChecker.test(input,expect,502))