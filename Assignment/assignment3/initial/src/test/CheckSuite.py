import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):

    # def test_if_exp(self):
    #     """Simple test: Redeclare var"""
    #     input = """ Var: x[2][2][3]={{{1,2,3},{3,4,7}},{{1,2,7},{3,4,9}}};
    #                 Var: t[2] = {1,2};
    #                 Var: a;
    #                 Function: main
    #                 Parameter: x,y,z
    #                 Body:
    #                 EndBody."""
    #     expect = str(Redeclared(Variable(),"y"))
    #     self.assertTrue(TestChecker.test(input,expect,401))
    
    # def test_revar_decl(self):
    #     """Simple test: Redeclare var"""
    #     input = """ Var: x,x;
    #                 Function: main
    #                 Parameter: x,y,z
    #                 Body:
    #                 EndBody."""
    #     expect = str(Redeclared(Variable(),"x"))
    #     self.assertTrue(TestChecker.test(input,expect,401))
    
    # def test_revar_decl1(self):
    #     """Simple test: Redeclare var"""
    #     input = """ Var: x,y;
    #                 Var: y;
    #                 Function: main
    #                 Parameter: x,y,z
    #                 Body:
    #                 EndBody."""
    #     expect = str(Redeclared(Variable(),"y"))
    #     self.assertTrue(TestChecker.test(input,expect,402))

    # def test_inferred_type(self):
    #     """Simple test: Inferred var decl"""
    #     input = """ Var: x=1;
    #                 Function: main
    #                 Body:
    #                     x = 1.1;
    #                 EndBody."""
    #     expect = str(TypeMismatchInStatement(Assign(Id(name="x"),FloatLiteral(1.1))))
    #     self.assertTrue(TestChecker.test(input,expect,403))
    
    # def test_inferredtype1(self):
    #     """Simple test: Inferred var decl"""
    #     input = """ Var: x=1.1;
    #                 Function: main
    #                 Body:
    #                     x = 1;
    #                 EndBody."""
    #     expect = str(TypeMismatchInStatement(Assign(Id(name="x"),IntLiteral(1))))
    #     self.assertTrue(TestChecker.test(input,expect,404))

    # def test_inferredtype2(self):
    #     """Simple test: Inferred var decl"""
    #     input = """ Var: x=1.1;
    #                 Var: y = 1;
    #                 Function: main
    #                 Body:
    #                     x = y;
    #                     Return 1.1;
    #                 EndBody."""
    #     expect = str(TypeMismatchInStatement(Assign(Id(name="x"),Id("y"))))
    #     self.assertTrue(TestChecker.test(input,expect,405))
    # def test_inferredtype3(self):
    #     """Simple test: Inferred var decl"""
    #     input = """ Var: x=True;
    #                 Var: y = "abc";
    #                 Function: main
    #                 Body:
    #                     x = y;
    #                     Return 1.1;
    #                 EndBody."""
    #     expect = str(TypeMismatchInStatement(Assign(Id("x"),Id("y"))))
    #     self.assertTrue(TestChecker.test(input,expect,406))

    # ################!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!###################
    # def test_inferredtype3(self):
    #     """Simple test: Inferred var decl"""
    #     input = """ Var: x[1][2];
    #                 Var: y = "abc";
    #                 Function: main
    #                 Body:
    #                     x = y;
    #                     Return 1.1;
    #                 EndBody."""
    #     expect = str(TypeMismatchInStatement(Assign(Id("x"),Id("y"))))
    #     self.assertTrue(TestChecker.test(input,expect,407))
    
    # def test_inferredtype4(self):
    #     """Simple test: Inferred var decl"""
    #     input = """ Var: x = True;
    #                 Var: y = "abc";
    #                 Var: z = 1.2;
    #                 Var: w = 123;
    #                 Var: t[1] = {1};
    #                 Function: main
    #                 Parameter: x
    #                 Body:
    #                     x = y;
    #                     y = x;
    #                     w = z;
    #                     Return 1.1;
    #                 EndBody."""
    #     expect = str(TypeMismatchInStatement(Assign(Id("w"),Id("z"))))
    #     self.assertTrue(TestChecker.test(input,expect,408))
    # def test_inferredtype5(self):
    #     """Simple test: Inferred var decl"""
    #     input = """ Var: x = True;
    #                 Var: y = "abc";
    #                 Var: z = 1.2;
    #                 Var: w = 123;
    #                 Var: t[1] = {1};
    #                 Function: main
    #                 Parameter: x
    #                 Body:
    #                     x = y;
    #                     x = z;
    #                 EndBody."""
    #     expect = str(TypeMismatchInStatement(Assign(Id("x"),Id("z"))))
    #     self.assertTrue(TestChecker.test(input,expect,409))
    # def test_redecl_para(self):
    #     """Simple test: Redeclare parameter"""
    #     input = """ 
    #                 Function: main
    #                 Parameter: x,x
    #                 Body:
    #                 EndBody."""
    #     expect = str(Redeclared(Parameter(),"x"))
    #     self.assertTrue(TestChecker.test(input,expect,410))
    # def test_redecl_para1(self):
    #     """Simple test: Redeclare parameter"""
    #     input = """ 
    #                 Function: main
    #                 Parameter: x,y
    #                 Body:
    #                     Var: x;
    #                 EndBody."""
    #     expect = str(Redeclared(Variable(),"x"))
    #     self.assertTrue(TestChecker.test(input,expect,411))
    
    # def test_redecl_func(self):
    #     """Simple test: Redeclare fucntion"""
    #     input = """ 
    #                 Function: main
    #                 Body:
    #                 EndBody.
    #                 Function: main
    #                 Parameter: x,y
    #                 Body:
    #                     Var: t;
    #                 EndBody."""
    #     expect = str(Redeclared(Function(),"main"))
    #     self.assertTrue(TestChecker.test(input,expect,412))
    # def test_redecl_func2(self):
    #     """Simple test: Redeclare function"""
    #     input = """ 
    #                 Function: foo
    #                 Body:
    #                 EndBody.
    #                 Function: main
    #                 Parameter: x,y
    #                 Body:
    #                     Var: t;
    #                 EndBody.
    #                 Function: foo
    #                 Body:
    #                 EndBody."""
    #     expect = str(Redeclared(Function(),"foo"))
    #     self.assertTrue(TestChecker.test(input,expect,413))
    
    # def test_undeclare_id(self):
    #     """ Simple test: Undeclare identifier"""
    #     input = """ 
    #                 Function: main
    #                 Parameter: x,y
    #                 Body:
    #                     t = x;
    #                 EndBody.
    #                 """
    #     expect = str(Undeclared(Identifier(),"t"))
    #     self.assertTrue(TestChecker.test(input,expect,414))
    
    # def test_undeclare_id(self):
    #     """ Simple test: Undeclare identifier"""
    #     input = """ 
    #                 Function: main
    #                 Parameter: x,y
    #                 Body:
    #                     t = x;
    #                 EndBody.
    #                 """
    #     expect = str(Undeclared(Identifier(),"t"))
    #     self.assertTrue(TestChecker.test(input,expect,415))
    
    # def test_undeclare_id(self):
    #     """ Simple test: Undeclare identifier"""
    #     input = """ Var: x;
    #                 Function: main
    #                 Parameter: x,y
    #                 Body:
    #                     main();
    #                 EndBody.
    #                 """
    #     expect = str(Undeclared(Identifier(),"t"))
    #     self.assertTrue(TestChecker.test(input,expect,416))
    
    # def test_undeclare_func(self):
    #     """ Simple test: Undeclare function"""
    #     input = """ Var: x;
    #                 Function: main
    #                 Parameter: x,y
    #                 Body:
    #                     foo(1,2);
    #                     Return ;
    #                 EndBody.
    #                 """
    #     expect = str(Undeclared(Function(),"foo"))
    #     self.assertTrue(TestChecker.test(input,expect,417))
    
    # def test_typecannotinfferd(self):
    #     """ Simple test: Test type cannot inferred"""
    #     input = """ Var: z;
    #                 Function: main
    #                 Parameter: x,y
    #                 Body:
    #                     z = x;
    #                 EndBody.
    #                 """
    #     expect = str(TypeCannotBeInferred(Assign(Id("z"),Id("x"))))
    #     self.assertTrue(TestChecker.test(input,expect,418))
    
    # def test_typecannotinfferd1(self):
    #     """ Simple test: Test type cannot inferred"""
    #     input = """ Var: z;
    #                 Function: foo
    #                 Parameter: x,y
    #                 Body:
    #                 EndBody.
    #                 Function: main
    #                 Parameter: x,y
    #                 Body:
    #                     foo(x,y);
    #                 EndBody.
    #                 """
    #     expect = str(TypeCannotBeInferred(CallStmt(Id(name="foo"),[Id(name="x"),Id(name="y")])))
    #     self.assertTrue(TestChecker.test(input,expect,419))
    
   
    # def test_typecannotinfferd2(self):
    #     """ Simple test: Test type cannot inferred"""
    #     input = """ Var: z;
    #                 Function: foo
    #                 Parameter: x,y
    #                 Body:
    #                 EndBody.
    #                 Function: main
    #                 Parameter: x,y
    #                 Body:
    #                     If x > 1 Then
    #                         Var: t;
    #                         y = t;
    #                     EndIf.
    #                 EndBody.
    #                 """
    #     expect = str(TypeCannotBeInferred(Assign(Id("y"),Id("t"))))
    #     self.assertTrue(TestChecker.test(input,expect,420))
    
    # def test_typecannotinfferd3(self):
    #     """ Simple test: Test type cannot inferred"""
    #     input = """Function: foo
    #                 Parameter: x,y
    #                 Body:
    #                 EndBody.
    #                 Function: main
    #                 Parameter: x,y
    #                 Body:
    #                     x = 1;
    #                     For(x =1, x < 1, 1) Do
    #                         Var: t;
    #                         t = y;
    #                     EndFor.
    #                 EndBody.
    #                 """
    #     expect = str(TypeCannotBeInferred(Assign(Id("t"),Id("y"))))
    #     self.assertTrue(TestChecker.test(input,expect,421))
    
    # def test_typecannotinfferd4(self):
    #     """ Simple test: Test type cannot inferred"""
    #     input = """Function: foo
    #                 Parameter: x,y
    #                 Body:
    #                 EndBody.
    #                 Function: main
    #                 Parameter: x,y
    #                 Body:
    #                     x = 1;
    #                     For(x =1, x < 1, 1) Do
    #                         Var: t;
    #                         t = y;
    #                     EndFor.
    #                 EndBody.
    #                 """
    #     expect = str(TypeCannotBeInferred(Assign(Id("t"),Id("y"))))
    #     self.assertTrue(TestChecker.test(input,expect,422))
    # def test_typecannotinfferd5(self):
    #     """ Simple test: Test type cannot inferred"""
    #     input = """Function: foo
    #                 Parameter: x,y
    #                 Body:
    #                 EndBody.
    #                 Function: main
    #                 Parameter: x,y,z
    #                 Body:
    #                     x = 1;
    #                     While y Do
    #                         Var: t;
    #                         t = z;
    #                     EndWhile.
    #                 EndBody.
    #                 """
    #     expect = str(TypeCannotBeInferred(Assign(Id("t"),Id("z"))))
    #     self.assertTrue(TestChecker.test(input,expect,423))
    
    # def test_typecannotinfferd6(self):
    #     """ Simple test: Test type cannot inferred"""
    #     input = """Function: foo
    #                 Parameter: x,y
    #                 Body:
    #                 EndBody.
    #                 Function: main
    #                 Parameter: x,y,z
    #                 Body:
    #                     x = 1;
    #                     Do
    #                         Var: t;
    #                         t = z;
    #                     While y
    #                     EndDo.
    #                 EndBody.
    #                 """
    #     expect = str(TypeCannotBeInferred(Assign(Id("t"),Id("z"))))
    #     self.assertTrue(TestChecker.test(input,expect,424))
    
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
    def test_typemismatchinstatment3(self):
        """ Simple test: Test type mismatch in statment -if 3"""
        input = """
                Function: main
                Parameter: x
                Body:

                    For(x = 1, x < 10, 1) Do
                        Var: t;
                        t = x;
                    EndFor.
                EndBody.
                """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,428))