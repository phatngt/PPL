import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    
    # def test_vardecl(self):
    #     input = """ Var:x;"""
    #     expect = Program([VarDecl(variable=Id(name="x"),varDimen=[],varInit=None)])
    #     self.assertTrue(TestAST.checkASTGen(input,expect,300))
   
    # def test_vardecl1(self):
    #     input = """ Var:x = 1;"""
    #     expect = Program([VarDecl(variable=Id(name="x"),varDimen=[],varInit=IntLiteral(value=1))])
    #     self.assertTrue(TestAST.checkASTGen(input,expect,301))

    # def test_vardecl2(self):
    #     input = """ Var:x,y;"""
    #     expect = Program([VarDecl(variable=Id(name="x"),varDimen=[],varInit=None),VarDecl(variable=Id(name="y"),varDimen=[],varInit=None)])
    #     self.assertTrue(TestAST.checkASTGen(input,expect,302))
    
    # def test_vardecl3(self):
    #     input = """ Var:x,y=True,z[1] = {1};"""
    #     expect = Program([VarDecl(variable=Id(name="x"),varDimen=[],varInit=None),
    #     VarDecl(variable=Id(name="y"),varDimen=[],varInit=BooleanLiteral(value=True)),
    #     VarDecl(variable=Id(name="z"),varDimen=[1],varInit=ArrayLiteral([IntLiteral(value=1)]))])
    #     self.assertTrue(TestAST.checkASTGen(input,expect,303))
    
    # def test_vardecl4(self):
    #     input = """ Var:z[4] = {1,True,12e1,"abc"};"""
    #     expect = Program([VarDecl(
    #         variable=Id(name="z"),
    #         varDimen=[4],
    #         varInit=ArrayLiteral([IntLiteral(value=1),BooleanLiteral(value=True),FloatLiteral(value=12e1),StringLiteral(value="abc")]))])
    #     self.assertTrue(TestAST.checkASTGen(input,expect,304))
    
    # def test_vardecl5(self):
    #     input = """ Var: x = 12;
    #                 Var: y = 12e1;
    #                 Var: z = False;
    #                 Var: w = "abc"; """
    #     expect = Program([VarDecl(variable=Id(name="x"),varDimen=[],varInit=IntLiteral(value=12)),
    #     VarDecl(variable=Id(name="y"),varDimen=[],varInit=FloatLiteral(value=12e1)),
    #     VarDecl(variable=Id(name="z"),varDimen=[],varInit=BooleanLiteral(value=False)),
    #     VarDecl(variable=Id(name="w"),varDimen=[],varInit=StringLiteral(value="abc"))])
    #     self.assertTrue(TestAST.checkASTGen(input,expect,305))
    
    # def test_vardecl6(self):
    #     input = """ Var: t[1][2] = {{1,2},{3,4}}; """
    #     expect = Program([VarDecl(variable=Id(name="t"),varDimen=[1,2],varInit=ArrayLiteral(value=[ArrayLiteral(value=[IntLiteral(1),IntLiteral(2)]),ArrayLiteral([IntLiteral(3),IntLiteral(4)])]))])
    #     self.assertTrue(TestAST.checkASTGen(input,expect,306))

    # def test_funcdecl1(self):
    #     input = """ Function: foo
    #                     Body:
    #                     EndBody. """
    #     expect = Program([FuncDecl(name=Id(name="foo"),param=[],body=([],[]))])
    #     self.assertTrue(TestAST.checkASTGen(input,expect,307))
    # def test_funcdecl2(self):
    #     input = """ Function: foo
    #                     Parameter:n,m
    #                     Body:
                            
    #                     EndBody. """
    #     expect = Program([FuncDecl(name=Id(name="foo"),
    #     param=[VarDecl(variable=Id("n"),varDimen=[],varInit=None),VarDecl(variable=Id("m"),varDimen=[],varInit=None)],
    #     body=([],[]))])
    #     self.assertTrue(TestAST.checkASTGen(input,expect,308))
    
    def test_program(self):
        input = """ Var: x,y,z;
                    Function: foo
                        Body:
                            Var: x,y,z;
                        EndBody. """
        expect = Program([
            VarDecl(variable=Id(name="x"),varDimen=[],varInit=None),
            VarDecl(variable=Id(name="y"),varDimen=[],varInit=None),
            VarDecl(variable=Id(name="z"),varDimen=[],varInit=None),
            FuncDecl(name=Id(name="foo"),param = [],body=([VarDecl(variable=Id(name="x"),varDimen=[],varInit=None),
            VarDecl(variable=Id(name="y"),varDimen=[],varInit=None),
            VarDecl(variable=Id(name="z"),varDimen=[],varInit=None)],[]))
            ])
        self.assertTrue(TestAST.checkASTGen(input,expect,309))
    
    # def test_exp3(self):
    #     input = """ Function: foo
    #                     Body:
    #                         While x < 10 Do
    #                             x = x + 1
    #                         EndWhile.
    #                     EndBody. """
    #     expect = Program([VarDecl(variable=Id(name="x"),varDimen=[],varInit=None)])
    #     self.assertTrue(TestAST.checkASTGen(input,expect,310))
    
    # def test_exp4(self):
    #     input = """ Function: foo
    #                     Body:
    #                         Do x = x + 1;
    #                         While x < 10
    #                         EndDo.
    #                     EndBody. """
    #     expect = Program([VarDecl(variable=Id(name="x"),varDimen=[],varInit=None)])
    #     self.assertTrue(TestAST.checkASTGen(input,expect,311))

    # def test_exp4(self):
    #     input = """ Function: foo
    #                     Body:
    #                         (a+1)[1+b][3+c] = x+1;
    #                     EndBody. """
    #     expect = Program([VarDecl(variable=Id(name="x"),varDimen=[],varInit=None)])
    #     self.assertTrue(TestAST.checkASTGen(input,expect,312))
    