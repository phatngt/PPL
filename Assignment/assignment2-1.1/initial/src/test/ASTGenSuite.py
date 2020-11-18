import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    
    def test_vardecl(self):
        input = """ Var:x;"""
        expect = Program([VarDecl(variable=Id(name="x"),varDimen=[],varInit=None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,300))
   
    def test_vardecl1(self):
        input = """ Var:x = 1;"""
        expect = Program([VarDecl(variable=Id(name="x"),varDimen=[],varInit=IntLiteral(value=1))])
        self.assertTrue(TestAST.checkASTGen(input,expect,301))

    def test_vardecl2(self):
        input = """ Var:x,y;"""
        expect = Program([VarDecl(variable=Id(name="x"),varDimen=[],varInit=None),VarDecl(variable=Id(name="y"),varDimen=[],varInit=None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,302))
    
    def test_vardecl3(self):
        input = """ Var:x,y=True,z[1] = {1};"""
        expect = Program([VarDecl(variable=Id(name="x"),varDimen=[],varInit=None),
        VarDecl(variable=Id(name="y"),varDimen=[],varInit=BooleanLiteral(value=True)),
        VarDecl(variable=Id(name="z"),varDimen=[1],varInit=ArrayLiteral([IntLiteral(value=1)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,303))
    
    def test_vardecl4(self):
        input = """ Var:z[4] = {1,True,12e1,"abc"};"""
        expect = Program([VarDecl(
            variable=Id(name="z"),
            varDimen=[4],
            varInit=ArrayLiteral([IntLiteral(value=1),BooleanLiteral(value=True),FloatLiteral(value=12e1),StringLiteral(value="abc")]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,304))
    
    def test_vardecl5(self):
        input = """ Var: x = 12;
                    Var: y = 12e1;
                    Var: z = False;
                    Var: w = "abc"; """
        expect = Program([VarDecl(variable=Id(name="x"),varDimen=[],varInit=IntLiteral(value=12)),
        VarDecl(variable=Id(name="y"),varDimen=[],varInit=FloatLiteral(value=12e1)),
        VarDecl(variable=Id(name="z"),varDimen=[],varInit=BooleanLiteral(value=False)),
        VarDecl(variable=Id(name="w"),varDimen=[],varInit=StringLiteral(value="abc"))])
        self.assertTrue(TestAST.checkASTGen(input,expect,305))
    
    def test_vardecl6(self):
        input = """ Var: t[1][2] = {{1,2},{3,4}}; """
        expect = Program([VarDecl(variable=Id(name="t"),varDimen=[1,2],varInit=ArrayLiteral(value=[ArrayLiteral(value=[IntLiteral(1),IntLiteral(2)]),ArrayLiteral([IntLiteral(3),IntLiteral(4)])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,306))

    def test_funcdecl1(self):
        input = """ Function: foo
                        Body:
                        EndBody. """
        expect = Program([FuncDecl(name=Id(name="foo"),param=[],body=([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,307))
    def test_funcdecl2(self):
        input = """ Function: foo
                        Parameter:n,m
                        Body:
                            
                        EndBody. """
        expect = Program([FuncDecl(name=Id(name="foo"),
        param=[VarDecl(variable=Id("n"),varDimen=[],varInit=None),VarDecl(variable=Id("m"),varDimen=[],varInit=None)],
        body=([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,308))
    
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
    def test_program1(self):
        input = """
                Var: x = "Done assignment 2 :))";
                Function: main
                Parameter: a,b
                Body:
                    Var: score;
                    score = (a*b)\\(a+b);
                    If score <. 5.0 Then
                        print("Googbye,See you ki sau :))");
                    ElseIf (score >=. 5.0) && (score <=. 8.0) Then
                        print("Dung chu quan, co gang bai thi cuoi ki va ass 3");
                    Else
                        print("10 con rot kia ban oi :))");
                    EndIf.
                    Return result; 
                EndBody.
                """
        expect = Program([
            VarDecl(variable=Id(name="x"),varDimen=[],varInit=StringLiteral(value="Done assignment 2 :))")),
            FuncDecl(
                name=Id(name="main"),
                param = [
                    VarDecl(variable=Id(name="a"),varDimen=[],varInit=None),
                    VarDecl(variable=Id(name="b"),varDimen=[],varInit=None)],
                body=(
                    [VarDecl(variable=Id(name="score"),varDimen=[],varInit=None)],
                    [
                        Assign(
                            lhs=Id(name="score"),
                            rhs = BinaryOp(
                                op="\\",
                                left=BinaryOp(
                                    op="*",
                                    left=Id(name="a"),
                                    right=Id(name="b")
                                ),
                                right=BinaryOp(
                                    op="+",
                                    left=Id(name="a"),
                                    right=Id(name="b")
                                )
                            )
                        ),
                        If(
                            ifthenStmt=[
                                (BinaryOp(op="<.",left=Id(name="score"),right=FloatLiteral(value=5.0)),[],[CallStmt(method=Id(name="print"),param=[StringLiteral(value="Googbye,See you ki sau :))")])]),
                                (BinaryOp(
                                    op="&&",
                                    left=BinaryOp(op=">=.",left=Id(name="score"),right=FloatLiteral(value=5.0)),
                                    right=BinaryOp(op="<=.",left=Id(name="score"),right=FloatLiteral(value=8.0)),
                                    ),
                                    [],
                                    [CallStmt(method=Id(name="print"),param=[StringLiteral(value="Dung chu quan, co gang bai thi cuoi ki va ass 3")])]
                                )
                            ],
                            elseStmt=([],[CallStmt(method=Id(name="print"),param=[StringLiteral(value="10 con rot kia ban oi :))")])])
                        ),
                        Return(expr=Id(name="result"))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,310))
    
    def test_stm_assign(self):
        input = """ Function: foo
                        Body:
                            a = 1;
                        EndBody. """
        expect = Program([FuncDecl(
                            name=Id(name="foo"),
                            param=[],
                            body=([
                                [],
                                [Assign(lhs=Id(name="a"),rhs=IntLiteral(value=1))]
                            ])
                            )
                        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    def test_stm_assign1(self):
        input = """ Function: foo
                        Body:
                            a = 1;
                            (a+1)[1+b][3+c] = x+1;
                        EndBody. """
        expect = Program([FuncDecl(
                            name=Id("foo"),
                            param=[],
                            body=([
                                [],
                                [
                                Assign(lhs=Id(name="a"),rhs=IntLiteral(value=1)),
                                Assign(
                                    lhs=ArrayCell(
                                        arr=BinaryOp(op="+",left=Id(name="a"),right=IntLiteral(value=1)),
                                        idx=[
                                            BinaryOp(op="+",left=IntLiteral(value=1),right=Id(name="b")),
                                            BinaryOp(op="+",left=IntLiteral(value=3),right=Id(name="c"))
                                            ]
                                        ),
                                    rhs= BinaryOp(op="+",left=Id(name="x"),right=IntLiteral(value=1))
                                    )
                                ]
                            ])
                        )
                    ])
        self.assertTrue(TestAST.checkASTGen(input,expect,312))

    def test_stm_assign2(self):
        input = """ Function: foo
                        Body:
                            (a+1)[1+(b+1)[1+d]][3+c(1)] = x+1;
                        EndBody. """
        expect = Program([FuncDecl(
                        name=Id(name="foo"),
                        param = [],
                        body = (
                            [],
                            [Assign(
                                lhs= ArrayCell(
                                    arr=BinaryOp(op="+",left=Id(name="a"),right=IntLiteral(value=1)),
                                    idx = 
                                    [
                                        BinaryOp(
                                            op="+",
                                            left=IntLiteral(value=1),
                                            right= ArrayCell(
                                                    arr=BinaryOp(op="+",left=Id(name="b"),right=IntLiteral(value=1)),
                                                    idx = [BinaryOp(op="+",left=IntLiteral(value=1),right=Id(name="d"))]
                                                    )
                                            ),
                                        BinaryOp(
                                            op="+",
                                            left=IntLiteral(value=3),
                                            right=CallExpr(method=Id(name="c"),param=[IntLiteral(value=1)])
                                            )
                                    ]
                                    ),
                                rhs= BinaryOp(op="+",left=Id(name="x"),right=IntLiteral(value=1))
                                )
                            ]
                            )
                        )
                    ])
        self.assertTrue(TestAST.checkASTGen(input,expect,313))

    def test_stm_assign3(self):
        input = """ Function: foo
                        Body:
                            (a+1)[3+c(1)] = x+1;
                        EndBody. """
        expect = Program([FuncDecl(
                        name=Id(name="foo"),
                        param = [],
                        body = (
                            [],
                            [Assign(
                                lhs= ArrayCell(
                                    arr=BinaryOp(op="+",left=Id(name="a"),right=IntLiteral(value=1)),
                                    idx = 
                                    [
                                        BinaryOp(op="+",left=IntLiteral(3),right=CallExpr(method=Id(name="c"),param=[IntLiteral(value=1)]))
                                    ]
                                    ),
                                rhs= BinaryOp(op="+",left=Id(name="x"),right=IntLiteral(value=1))
                                )
                            ]
                            )
                        )
                    ])
        self.assertTrue(TestAST.checkASTGen(input,expect,314))
    
    def test_arraycell(self):
        input = """ Function: foo
                        Body:
                            (a > 1)[1+(a==1)[b+c(1,2)[a+8]]] = 1;
                        EndBody. """
        expect = Program([FuncDecl(
                            name=Id(name="foo"),
                            param=[],
                            body=([
                                [],
                                [Assign(
                                    lhs=ArrayCell(
                                        arr = BinaryOp(op=">",left=Id(name="a"),right=IntLiteral(value=1)),
                                        idx = 
                                        [
                                            BinaryOp(
                                                op="+",
                                                left = IntLiteral(value=1),
                                                right = ArrayCell(
                                                    arr=BinaryOp(op="==",left=Id(name="a"),right=IntLiteral(value=1)),
                                                    idx = 
                                                    [   
                                                        BinaryOp(
                                                            op="+",
                                                            left=Id(name="b"),
                                                            right=ArrayCell(
                                                                arr = CallExpr(
                                                                    method=Id(name="c"),
                                                                    param=[IntLiteral(value=1),IntLiteral(value=2)]
                                                                    ),
                                                                idx = 
                                                                [
                                                                    BinaryOp(op="+",left=Id(name="a"),right=IntLiteral(value=8))
                                                                ]
                                                            ))
                                                    ]
                                                    )
                                                )
                                        ]
                                    ),
                                    rhs = IntLiteral(value=1)
                                )]
                            ])
                            )
                        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,315))
    
    def test_stm_assign4(self):
        input = """ Function: foo
                        Body:
                            (a+1)[3+c(1)] = x+f(1,2,3+x)[0];
                        EndBody. """
        expect = Program([FuncDecl(
                        name=Id(name="foo"),
                        param = [],
                        body = (
                            [],
                            [Assign(
                                lhs= ArrayCell(
                                    arr=BinaryOp(op="+",left=Id(name="a"),right=IntLiteral(value=1)),
                                    idx = 
                                    [
                                        BinaryOp(op="+",left=IntLiteral(3),right=CallExpr(method=Id(name="c"),param=[IntLiteral(value=1)]))
                                    ]
                                    ),
                                rhs= BinaryOp(
                                    op="+",
                                    left=Id(name="x"),
                                    right=ArrayCell(
                                        arr=CallExpr(
                                            method = Id(name="f"),
                                            param = [IntLiteral(value=1),IntLiteral(value=2),BinaryOp(op="+",left=IntLiteral(value=3),right=Id(name="x"))]
                                            ),
                                        idx = [IntLiteral(value=0)]
                                        )
                                    )
                                )
                            ]
                            )
                        )
                    ])
        self.assertTrue(TestAST.checkASTGen(input,expect,316))
    
    def test_if_stm(self):
        input = """
                Function: foo
                        Body:
                            If a > 0 Then a = a +1;
                            EndIf.
                        EndBody.
                """
        expect = Program([FuncDecl(
                        name=Id(name="foo"),
                        param = [],
                        body = (
                            [],
                            [If(
                                ifthenStmt=
                                [
                                    (BinaryOp(op=">",left=Id(name="a"),right=IntLiteral(value=0)),[],
                                    [
                                        Assign(lhs = Id(name="a"),rhs=BinaryOp(op="+",left=Id(name="a"),right=IntLiteral(value=1)))
                                    ])
                                ],
                                elseStmt=([],[])
                            )
                            ]
                            )
                        )])
        self.assertTrue(TestAST.checkASTGen(input,expect,317))

    def test_if_stm1(self):
        input = """
                Function: foo
                        Body:
                            If a > 0 Then
                                Var: x = 1; 
                                x = x +1;
                            EndIf.
                        EndBody.
                """
        expect = Program([FuncDecl(
                        name=Id(name="foo"),
                        param = [],
                        body = (
                            [],
                            [If(
                                ifthenStmt=
                                [
                                    (
                                    BinaryOp(op=">",left=Id(name="a"),right=IntLiteral(value=0)),
                                    [VarDecl(variable=Id(name="x"),varDimen=[],varInit=IntLiteral(value=1))],
                                    [
                                        Assign(lhs = Id(name="x"),rhs=BinaryOp(op="+",left=Id(name="x"),right=IntLiteral(value=1)))
                                    ]
                                    )
                                ],
                                elseStmt=([],[])
                            )
                            ]
                            )
                        )])
        self.assertTrue(TestAST.checkASTGen(input,expect,318))
    
    def test_if_stm2(self):
        input = """
                Function: foo
                        Body:
                            If a > 0 Then
                                Var: x = 1; 
                                x = x +1;
                            ElseIf b < 0 Then
                                Var: y = 1;
                                y = y+1;
                            EndIf.
                        EndBody.
                """
        expect = Program([FuncDecl(
                        name=Id(name="foo"),
                        param = [],
                        body = (
                            [],
                            [If(
                                ifthenStmt=
                                [
                                    (
                                        BinaryOp(op=">",left=Id(name="a"),right=IntLiteral(value=0)),
                                        [VarDecl(variable=Id(name="x"),varDimen=[],varInit=IntLiteral(value=1))],
                                        [
                                            Assign(lhs = Id(name="x"),rhs=BinaryOp(op="+",left=Id(name="x"),right=IntLiteral(value=1)))
                                        ]
                                    ),
                                    (
                                        BinaryOp(op="<",left=Id(name="b"),right=IntLiteral(value=0)),
                                        [VarDecl(variable=Id(name="y"),varDimen=[],varInit=IntLiteral(value=1))],
                                        [
                                            Assign(lhs = Id(name="y"),rhs=BinaryOp(op="+",left=Id(name="y"),right=IntLiteral(value=1)))
                                        ]
                                    )
                                ],
                                elseStmt=([],[])
                            )
                            ]
                            )
                        )])
        self.assertTrue(TestAST.checkASTGen(input,expect,319))
    
    def test_if_stm3(self):
        input = """
                Function: foo
                        Body:
                            If a > 0 Then
                                Var: x = 1; 
                                x = x +1;
                            ElseIf b < 0 Then
                                Var: y = 1;
                                y = y+1;
                            Else
                                Var: z=1;
                                z = z + 1;
                            EndIf.
                        EndBody.
                """
        expect = Program([FuncDecl(
                        name=Id(name="foo"),
                        param = [],
                        body = (
                            [],
                            [If(
                                ifthenStmt=
                                [
                                    (
                                        BinaryOp(op=">",left=Id(name="a"),right=IntLiteral(value=0)),
                                        [VarDecl(variable=Id(name="x"),varDimen=[],varInit=IntLiteral(value=1))],
                                        [
                                            Assign(lhs = Id(name="x"),rhs=BinaryOp(op="+",left=Id(name="x"),right=IntLiteral(value=1)))
                                        ]
                                    ),
                                    (
                                        BinaryOp(op="<",left=Id(name="b"),right=IntLiteral(value=0)),
                                        [VarDecl(variable=Id(name="y"),varDimen=[],varInit=IntLiteral(value=1))],
                                        [
                                            Assign(lhs = Id(name="y"),rhs=BinaryOp(op="+",left=Id(name="y"),right=IntLiteral(value=1)))
                                        ]
                                    )
                                ],
                                elseStmt=
                                (
                                    [VarDecl(variable=Id(name="z"),varDimen=[],varInit=IntLiteral(value=1))],
                                    [
                                        Assign(lhs = Id(name="z"),rhs=BinaryOp(op="+",left=Id(name="z"),right=IntLiteral(value=1)))
                                    ]
                                )
                            )
                            ]
                            )
                        )])
        self.assertTrue(TestAST.checkASTGen(input,expect,320))
    
    def test_if_stm4(self):
        input = """
                Function: foo
                        Body:
                            If a > 0 Then
                                Var: x = 1; 
                                Var: y = 2;
                                x = x + 1;
                                y = y + 2;
                            Else
                                Var: z = 1;
                                Var: t = 1;
                                z = z + 1;
                                t = t + 3;
                            EndIf.
                        EndBody.
                """
        expect = Program([FuncDecl(
                    name=Id(name="foo"),
                    param = [],
                    body = (
                        [],
                        [If(
                            ifthenStmt=
                            [
                                (
                                    BinaryOp(op=">",left=Id(name="a"),right=IntLiteral(value=0)),
                                    [
                                        VarDecl(variable=Id(name="x"),varDimen=[],varInit=IntLiteral(value=1)),
                                        VarDecl(variable=Id(name="y"),varDimen=[],varInit=IntLiteral(value=2))
                                    ],
                                    [
                                        Assign(lhs = Id(name="x"),rhs=BinaryOp(op="+",left=Id(name="x"),right=IntLiteral(value=1))),
                                        Assign(lhs = Id(name="y"),rhs=BinaryOp(op="+",left=Id(name="y"),right=IntLiteral(value=2)))
                                    ]
                                )
                                
                            ],
                            elseStmt=
                            (
                                [
                                    VarDecl(variable=Id(name="z"),varDimen=[],varInit=IntLiteral(value=1)),
                                    VarDecl(variable=Id(name="t"),varDimen=[],varInit=IntLiteral(value=1))
                                ],
                                [
                                    Assign(lhs = Id(name="z"),rhs=BinaryOp(op="+",left=Id(name="z"),right=IntLiteral(value=1))),
                                    Assign(lhs = Id(name="t"),rhs=BinaryOp(op="+",left=Id(name="t"),right=IntLiteral(value=3)))
                                ]
                            )
                        )
                        ]
                        )
                    )])
        self.assertTrue(TestAST.checkASTGen(input,expect,321))

    def test_for_stm(self):
        input = """
                Function: foo
                        Body:
                            For (x = 1, x < 100, 1) Do
                                print(x);
                            EndFor.
                        EndBody.
                """
        expect = Program([FuncDecl(
                    name=Id(name="foo"),
                    param = [],
                    body = (
                        [],
                        [
                            For(
                                idx1 = Id(name="x"),
                                expr1 = IntLiteral(value=1),
                                expr2 = BinaryOp(op="<",left=Id(name="x"),right=IntLiteral(value=100)),
                                expr3 = IntLiteral(value=1),
                                loop = 
                                (
                                    [],
                                    [
                                        CallStmt(method=Id("print"),param=[Id(name="x")])
                                    ]
                                )
                            )
                        ]
                        )
                    )])
        self.assertTrue(TestAST.checkASTGen(input,expect,322))
    
    def test_for_stm1(self):
        input = """
                Function: foo
                        Body:
                            For (x = 1, x < 100, 1) Do
                                Var: y;
                                print(x,y);
                            EndFor.
                        EndBody.
                """
        expect = Program([FuncDecl(
                    name=Id(name="foo"),
                    param = [],
                    body = (
                        [],
                        [
                            For(
                                idx1 = Id(name="x"),
                                expr1 = IntLiteral(value=1),
                                expr2 = BinaryOp(op="<",left=Id(name="x"),right=IntLiteral(value=100)),
                                expr3 = IntLiteral(value=1),
                                loop = 
                                (
                                    [
                                        VarDecl(variable=Id(name="y"),varDimen=[],varInit=None)
                                    ],
                                    [
                                        CallStmt(method=Id("print"),param=[Id(name="x"),Id(name="y")])
                                    ]
                                )
                            )
                        ]
                        )
                    )])
        self.assertTrue(TestAST.checkASTGen(input,expect,323))

    def test_for_stm2(self):
        input = """
                Function: foo
                        Body:
                            For (x = 1+a, x <= 100, a+a) Do
                                Var: y;
                                print(x,y);
                            EndFor.
                        EndBody.
                """
        expect = Program([FuncDecl(
                    name=Id(name="foo"),
                    param = [],
                    body = (
                        [],
                        [
                            For(
                                idx1 = Id(name="x"),
                                expr1 = BinaryOp(op="+",left=IntLiteral(value=1),right=Id(name="a")),
                                expr2 = BinaryOp(op="<=",left=Id(name="x"),right=IntLiteral(value=100)),
                                expr3 = BinaryOp(op="+",left=Id(name="a"),right=Id(name="a")),
                                loop = 
                                (
                                    [
                                        VarDecl(variable=Id(name="y"),varDimen=[],varInit=None)
                                    ],
                                    [
                                        CallStmt(method=Id("print"),param=[Id(name="x"),Id(name="y")])
                                    ]
                                )
                            )
                        ]
                        )
                    )])
        self.assertTrue(TestAST.checkASTGen(input,expect,324))
    
    def test_for_stm3(self):
        input = """
                Function: foo
                        Body:
                            For (x = 1+a, x <= 100, a+a) Do
                                Var: y;
                                Var: z = 1;
                                Var: x[1][2];
                                print(x,y,z);
                                y = 2 + z;
                            EndFor.
                        EndBody.
                """
        expect = Program([FuncDecl(
                    name=Id(name="foo"),
                    param = [],
                    body = (
                        [],
                        [
                            For(
                                idx1 = Id(name="x"),
                                expr1 = BinaryOp(op="+",left=IntLiteral(value=1),right=Id(name="a")),
                                expr2 = BinaryOp(op="<=",left=Id(name="x"),right=IntLiteral(value=100)),
                                expr3 = BinaryOp(op="+",left=Id(name="a"),right=Id(name="a")),
                                loop = 
                                (
                                    [
                                        VarDecl(variable=Id(name="y"),varDimen=[],varInit=None),
                                        VarDecl(variable=Id(name="z"),varDimen=[],varInit=IntLiteral(value=1)),
                                        VarDecl(variable=Id(name="x"),varDimen=[1,2],varInit=None)
                                    ],
                                    [
                                        CallStmt(method=Id("print"),param=[Id(name="x"),Id(name="y"),Id(name="z")]),
                                        Assign(lhs=Id(name="y"),rhs = BinaryOp(op="+",left=IntLiteral(value=2),right=Id(name="z")))
                                    ]
                                )
                            )
                        ]
                        )
                    )])
        self.assertTrue(TestAST.checkASTGen(input,expect,325))
    
    def test_for_stm4(self):
        input = """
                Function: foo
                        Body:
                            For (x = 1+a, x <= 100, a+a) Do
                                For ( x = 1+b, x < 1000, b+1) Do
                                    Var: y = "x";
                                    print(y);
                                EndFor.
                            EndFor.
                        EndBody.
                """
        expect = Program([FuncDecl(
                    name=Id(name="foo"),
                    param = [],
                    body = (
                        [],
                        [
                            For(
                                idx1 = Id(name="x"),
                                expr1 = BinaryOp(op="+",left=IntLiteral(value=1),right=Id(name="a")),
                                expr2 = BinaryOp(op="<=",left=Id(name="x"),right=IntLiteral(value=100)),
                                expr3 = BinaryOp(op="+",left=Id(name="a"),right=Id(name="a")),
                                loop = 
                                (
                                    [
                                
                                    ],
                                    [
                                        For
                                        (
                                            idx1 = Id(name="x"),
                                            expr1 = BinaryOp(op="+",left=IntLiteral(value=1),right=Id(name="b")),
                                            expr2 = BinaryOp(op="<",left=Id(name="x"),right=IntLiteral(value=1000)),
                                            expr3 = BinaryOp(op="+",left=Id(name="b"),right=IntLiteral(value=1)),
                                            loop = 
                                            (
                                                [
                                                    VarDecl(variable=Id(name="y"),varDimen=[],varInit=StringLiteral(value="x"))
                                                ],
                                                [
                                                    CallStmt(method=Id(name="print"),param=[Id(name="y")])
                                                ]
                                            )
                                        )
                                    ]
                                )
                            )
                        ]
                        )
                    )])
        self.assertTrue(TestAST.checkASTGen(input,expect,326))

    def test_while_stm(self):
        input = """
                Function: foo
                        Body:
                            While x < 1 Do
                                print(x);
                                x = x +1;
                            EndWhile.
                        EndBody.
                """
        expect = Program([FuncDecl(
                    name=Id(name="foo"),
                    param = [],
                    body = (
                        [],
                        [
                            While
                            (
                                exp = BinaryOp(op="<",left=Id(name="x"),right=IntLiteral(value=1)),
                                sl = 
                                (
                                    [],
                                    [
                                        CallStmt(method=Id(name="print"),param = [Id(name="x")]),
                                        Assign(lhs=Id(name="x"),rhs=BinaryOp(op="+",left=Id(name="x"),right=IntLiteral(value=1)))
                                    ]
                                )

                            )
                            
                        ]
                        )
                    )])
        self.assertTrue(TestAST.checkASTGen(input,expect,327))
    
    def test_while_stm1(self):
        input = """
                Function: foo
                        Body:
                            While x < 1 Do
                                print(x);
                                x = x+1;
                                While y > 10 Do
                                    y = y-1;
                                    print(y,x,q);
                                EndWhile.
                            EndWhile.
                        EndBody.
                """
        expect = Program([FuncDecl(
                    name=Id(name="foo"),
                    param = [],
                    body = (
                        [],
                        [
                            While
                            (
                                exp = BinaryOp(op="<",left=Id(name="x"),right=IntLiteral(value=1)),
                                sl = 
                                (
                                    [],
                                    [
                                        CallStmt(method=Id(name="print"),param = [Id(name="x")]),
                                        Assign(lhs=Id(name="x"),rhs=BinaryOp(op="+",left=Id(name="x"),right=IntLiteral(value=1))),
                                        While
                                        (
                                            exp = BinaryOp(op=">",left=Id(name="y"),right=IntLiteral(value=10)),
                                            sl=
                                            (
                                                [],
                                                [
                                                    Assign(lhs=Id(name="y"),rhs=BinaryOp(op="-",left=Id(name="y"),right=IntLiteral(value=1))),
                                                    CallStmt(method=Id(name="print"),param=[Id(name="y"),Id(name="x"),Id(name="q")])
                                                ]
                                            )
                                        )
                                    ]
                                )

                            )
                            
                        ]
                        )
                    )])
        self.assertTrue(TestAST.checkASTGen(input,expect,328))
    
    
    def test_while_stm2(self):
        input = """
                Function: foo
                        Body:
                            While x < 1 Do
                                Var: x,y,z=1;
                                Var: m,n,t;
                                print(x);
                                x = x+1;
                                While y > 10 Do
                                    Var: x = True, y[1][2] = {{1,2},{"abc","xyz"}};
                                    Var: a,b,c;
                                    y = y-1;
                                    print(y,x,q);
                                EndWhile.
                            EndWhile.
                        EndBody.
                """
        expect = Program([FuncDecl(
                    name=Id(name="foo"),
                    param = [],
                    body = (
                        [],
                        [
                            While
                            (
                                exp = BinaryOp(op="<",left=Id(name="x"),right=IntLiteral(value=1)),
                                sl = 
                                (
                                    [
                                        VarDecl(variable=Id(name="x"),varDimen=[],varInit=None),
                                        VarDecl(variable=Id(name="y"),varDimen=[],varInit=None),
                                        VarDecl(variable=Id(name="z"),varDimen=[],varInit=IntLiteral(value=1)),
                                        VarDecl(variable=Id(name="m"),varDimen=[],varInit=None),
                                        VarDecl(variable=Id(name="n"),varDimen=[],varInit=None),
                                        VarDecl(variable=Id(name="t"),varDimen=[],varInit=None),
                                        
                                    ],
                                    [
                                        CallStmt(method=Id(name="print"),param = [Id(name="x")]),
                                        Assign(lhs=Id(name="x"),rhs=BinaryOp(op="+",left=Id(name="x"),right=IntLiteral(value=1))),
                                        While
                                        (
                                            exp = BinaryOp(op=">",left=Id(name="y"),right=IntLiteral(value=10)),
                                            sl=
                                            (
                                                [
                                                    VarDecl(variable=Id(name="x"),varDimen=[],varInit=BooleanLiteral(value=True)),
                                                    VarDecl(
                                                        variable=Id(name="y"),
                                                        varDimen=[1,2],
                                                        varInit=ArrayLiteral
                                                        (
                                                            value=
                                                            [
                                                                ArrayLiteral(value=[IntLiteral(value=1),IntLiteral(value=2)]),
                                                                ArrayLiteral(value=[StringLiteral(value="abc"),StringLiteral(value="xyz")])
                                                            ]
                                                        )),
                                                    VarDecl(variable=Id(name="a"),varDimen=[],varInit=None),
                                                    VarDecl(variable=Id(name="b"),varDimen=[],varInit=None),
                                                    VarDecl(variable=Id(name="c"),varDimen=[],varInit=None)
                                                    
                                                ],
                                                [
                                                    Assign(lhs=Id(name="y"),rhs=BinaryOp(op="-",left=Id(name="y"),right=IntLiteral(value=1))),
                                                    CallStmt(method=Id(name="print"),param=[Id(name="y"),Id(name="x"),Id(name="q")])
                                                ]
                                            )
                                        )
                                    ]
                                )

                            )
                            
                        ]
                        )
                    )])
        self.assertTrue(TestAST.checkASTGen(input,expect,329))
    
    def test_while_stm3(self):
        input = """
                Function: foo
                        Body:
                            While x < 1 Do
                            EndWhile.
                        EndBody.
                """
        expect = Program([FuncDecl(
                    name=Id(name="foo"),
                    param = [],
                    body = (
                        [],
                        [
                            While
                            (
                                exp = BinaryOp(op="<",left=Id(name="x"),right=IntLiteral(value=1)),
                                sl = 
                                (
                                    [],
                                    []
                                )

                            )
                            
                        ]
                        )
                    )])
        self.assertTrue(TestAST.checkASTGen(input,expect,330))
    
    def test_dowhile_stm(self):
        input = """
                Function: foo
                        Body:
                            Do 
                                print(x,y,z);
                            While x > 10
                            EndDo.
                        EndBody.
                """
        expect = Program([FuncDecl(
                    name=Id(name="foo"),
                    param = [],
                    body = (
                        [],
                        [
                            Dowhile
                            (
                                sl = 
                                (
                                    [],
                                    [
                                        CallStmt(method=Id(name="print"),param=[Id(name="x"),Id(name="y"),Id(name="z")])
                                    ]
                                ),
                                exp = BinaryOp(op=">",left=Id(name="x"),right=IntLiteral(value=10))
                            )
                            
                        ]
                        )
                    )])
        self.assertTrue(TestAST.checkASTGen(input,expect,331))
    
    def test_dowhile_stm1(self):
        input = """
                Function: foo
                        Body:
                            Do 
                                Var: x,y,z;
                                Var: t=12.2,d=True,blabla="haha";
                                print(x,y,z);
                            While x > 10
                            EndDo.
                        EndBody.
                """
        expect = Program([FuncDecl(
                    name=Id(name="foo"),
                    param = [],
                    body = (
                        [],
                        [
                            Dowhile
                            (
                                sl = 
                                (
                                    [
                                        VarDecl(variable=Id(name="x"),varDimen=[],varInit=None),
                                        VarDecl(variable=Id(name="y"),varDimen=[],varInit=None),
                                        VarDecl(variable=Id(name="z"),varDimen=[],varInit=None),
                                        VarDecl(variable=Id(name="t"),varDimen=[],varInit=FloatLiteral(value=12.2)),
                                        VarDecl(variable=Id(name="d"),varDimen=[],varInit=BooleanLiteral(value=True)),
                                        VarDecl(variable=Id(name="blabla"),varDimen=[],varInit=StringLiteral(value="haha")),
                                        

                                    ],
                                    [
                                        CallStmt(method=Id(name="print"),param=[Id(name="x"),Id(name="y"),Id(name="z")])
                                    ]
                                ),
                                exp = BinaryOp(op=">",left=Id(name="x"),right=IntLiteral(value=10))
                            )
                            
                        ]
                        )
                    )])
        self.assertTrue(TestAST.checkASTGen(input,expect,332))
    
    def test_dowhile_stm2(self):
        input = """
                Function: foo
                        Body:
                            Do 
                            While x > 10
                            EndDo.
                        EndBody.
                """
        expect = Program([FuncDecl(
                    name=Id(name="foo"),
                    param = [],
                    body = (
                        [],
                        [
                            Dowhile
                            (
                                sl = 
                                (
                                    [],
                                    []
                                ),
                                exp = BinaryOp(op=">",left=Id(name="x"),right=IntLiteral(value=10))
                            )
                            
                        ]
                        )
                    )])
        self.assertTrue(TestAST.checkASTGen(input,expect,333))
    
    def test_dowhile_stm3(self):
        input = """
                Function: foo
                        Body:
                            Do 
                                Var: x,y,z;
                                Var: t=12.2,d=True,blabla="haha";
                                print(x,y,z);
                                x = func(x) + 1;
                            While x > 10
                            EndDo.
                        EndBody.
                """
        expect = Program([FuncDecl(
                    name=Id(name="foo"),
                    param = [],
                    body = (
                        [],
                        [
                            Dowhile
                            (
                                sl = 
                                (
                                    [
                                        VarDecl(variable=Id(name="x"),varDimen=[],varInit=None),
                                        VarDecl(variable=Id(name="y"),varDimen=[],varInit=None),
                                        VarDecl(variable=Id(name="z"),varDimen=[],varInit=None),
                                        VarDecl(variable=Id(name="t"),varDimen=[],varInit=FloatLiteral(value=12.2)),
                                        VarDecl(variable=Id(name="d"),varDimen=[],varInit=BooleanLiteral(value=True)),
                                        VarDecl(variable=Id(name="blabla"),varDimen=[],varInit=StringLiteral(value="haha")),
                                        

                                    ],
                                    [
                                        CallStmt(method=Id(name="print"),param=[Id(name="x"),Id(name="y"),Id(name="z")]),
                                        Assign(lhs=Id(name="x"),rhs = BinaryOp(op="+",left=CallExpr(method=Id(name="func"),param=[Id(name="x")]),right = IntLiteral(value=1)))
                                    ]
                                ),
                                exp = BinaryOp(op=">",left=Id(name="x"),right=IntLiteral(value=10))
                            )
                            
                        ]
                        )
                    )])
        self.assertTrue(TestAST.checkASTGen(input,expect,334))
    
    def test_return_stm(self):
        input = """
                Function: foo
                        Body:
                            Return a+b;
                        EndBody.
                """
        expect = Program([FuncDecl(
                    name=Id(name="foo"),
                    param = [],
                    body = (
                        [],
                        [
                            Return(expr = BinaryOp(op="+",left=Id(name="a"),right=Id(name="b")))
                        ]
                        )
                    )])
        self.assertTrue(TestAST.checkASTGen(input,expect,335))

    def test_return_stm1(self):
        input = """
                Function: foo
                        Body:
                            Return;
                        EndBody.
                """
        expect = Program([FuncDecl(
                    name=Id(name="foo"),
                    param = [],
                    body = (
                        [],
                        [
                            Return(expr = None)
                        ]
                        )
                    )])
        self.assertTrue(TestAST.checkASTGen(input,expect,336))
    
    def test_return_stm2(self):
        input = """
                Function: foo
                        Body:
                            Return a;
                        EndBody.
                Function: main
                        Body:
                            a = foo();
                            Return True;
                        EndBody.
                """
        expect = Program([FuncDecl(
                    name=Id(name="foo"),
                    param = [],
                    body = (
                        [],
                        [
                            Return(expr = Id(name="a"))
                        ]
                        )
                    ),
                    FuncDecl(
                    name=Id(name="main"),
                    param = [],
                    body = (
                        [],
                        [
                            Assign(lhs=Id(name="a"),rhs=CallExpr(method=Id(name="foo"),param=[])),
                            Return(expr = BooleanLiteral(value=True))
                        ]
                        )
                    )])
        self.assertTrue(TestAST.checkASTGen(input,expect,337))
    
    def test_return_stm3(self):
        input = """
                Function: foo
                        Body:
                            Return a;
                        EndBody.
                Function: main
                        Body:
                            Var:z = 2;
                            Return z;
                            a = foo();
                            Return True;
                        EndBody.
                """
        expect = Program([FuncDecl(
                    name=Id(name="foo"),
                    param = [],
                    body = (
                        [],
                        [
                            Return(expr = Id(name="a"))
                        ]
                        )
                    ),
                    FuncDecl(
                    name=Id(name="main"),
                    param = [],
                    body = (
                        [
                            VarDecl(variable=Id(name="z"),varDimen=[],varInit=IntLiteral(value=2))
                        ],
                        [
                            Return(expr = Id(name="z")),
                            Assign(lhs=Id(name="a"),rhs=CallExpr(method=Id(name="foo"),param=[])),
                            Return(expr = BooleanLiteral(value=True))
                        ]
                        )
                    )])
        self.assertTrue(TestAST.checkASTGen(input,expect,338))
    
    def test_ctn_stm(self):
        """ Test continue statement"""
        input = """
                Function: foo
                        Body:
                            Continue;
                        EndBody.
                """
        expect = Program([FuncDecl(
                    name=Id(name="foo"),
                    param = [],
                    body = (
                        [],
                        [
                            Continue()
                        ]
                        )
                    ),
                    ])
        self.assertTrue(TestAST.checkASTGen(input,expect,339))
    
    def test_ctn_stm1(self):
        """ Test continue statement"""
        input = """
                Function: foo
                        Body:
                            For (x = 1, x < 100, 1) Do
                                If x % 2 == 0 Then
                                    Continue;
                                Else
                                    print(x);
                                EndIf.
                            EndFor.
                        EndBody.
                """
        expect = Program([FuncDecl(
                    name=Id(name="foo"),
                    param = [],
                    body = (
                        [],
                        [
                            For
                            (
                                idx1 = Id(name="x"),
                                expr1 = IntLiteral(value=1),
                                expr2 = BinaryOp(op="<",left=Id(name="x"),right=IntLiteral(value=100)),
                                expr3 = IntLiteral(value=1),
                                loop = 
                                (
                                    [],
                                    [
                                        If
                                        (
                                            ifthenStmt = 
                                            [
                                                (
                                                    BinaryOp(op="==",left=BinaryOp(op="%",left=Id(name="x"),right=IntLiteral(value=2)),right=IntLiteral(value=0)),
                                                    [],
                                                    [
                                                        Continue()
                                                    ]
                                                )
                                            ],
                                            elseStmt = 
                                            (
                                                [],
                                                [
                                                    CallStmt(method=Id(name="print"),param=[Id(name="x")])
                                                ]
                                            )
                                        )
                                    ]
                                )

                            )
                        ]
                        )
                    ),
                    ])
        self.assertTrue(TestAST.checkASTGen(input,expect,340))
    
    def test_break_stm(self):
        """ Test break statement"""
        input = """
                Function: foo
                        Body:
                            Break;
                        EndBody.
                """
        expect = Program([FuncDecl(
                    name=Id(name="foo"),
                    param = [],
                    body = (
                        [],
                        [
                            Break()
                        ]
                        )
                    ),
                    ])
        self.assertTrue(TestAST.checkASTGen(input,expect,341))
    
    def test_break_stm1(self):
        """ Test break and continue statement"""
        input = """
                Function: foo
                        Body:
                            Break;
                            Break;
                            Continue;
                        EndBody.
                """
        expect = Program([FuncDecl(
                    name=Id(name="foo"),
                    param = [],
                    body = (
                        [],
                        [
                            Break(),
                            Break(),
                            Continue()
                        ]
                        )
                    ),
                    ])
        self.assertTrue(TestAST.checkASTGen(input,expect,342))
    
    def test_callfunc_stm(self):
        """ Test call function statement"""
        input = """
                Function: foo
                        Body:
                            print(x);
                            fun(print(x),print(y),x);
                        EndBody.
                """
        expect = Program([FuncDecl(
                    name=Id(name="foo"),
                    param = [],
                    body = (
                        [],
                        [
                            CallStmt(method=Id(name="print"),param=[Id(name="x")]),
                            CallStmt(method=Id(name="fun"),param=
                                [
                                CallExpr(method=Id(name="print"),param=[Id(name="x")]),
                                CallExpr(method=Id(name="print"),param=[Id(name="y")]),
                                Id(name="x")
                                ]
                                )
                        ]
                        )
                    ),
                    ])
        self.assertTrue(TestAST.checkASTGen(input,expect,343))
    
    def test_callfunc_stm1(self):
        """ Test call function statement"""
        input = """
                Function: foo
                        Body:
                            print(a+b,a[1][b+foo()]);
                        EndBody.
                """
        expect = Program([FuncDecl(
                    name=Id(name="foo"),
                    param = [],
                    body = (
                        [],
                        [
                            CallStmt
                            (
                                method = Id(name="print"),
                                param = 
                                [
                                    BinaryOp(op="+",left=Id(name="a"),right=Id(name="b")),
                                    ArrayCell
                                    (
                                        arr = Id(name="a"),
                                        idx = 
                                        [
                                            IntLiteral(value=1),
                                            BinaryOp(op="+",left=Id(name="b"),right=CallExpr(method=Id(name="foo"),param=[]))
                                        ]
                                    )
                                ]
                            )
                        ]
                        )
                    ),
                    ])
        self.assertTrue(TestAST.checkASTGen(input,expect,344))
    
    def test_callfunc_stm2(self):
        """ Test call function statement"""
        input = """
                Function: foo
                        Body:
                            print(a+b,a[1][b+foo()]);
                        EndBody.
                """
        expect = Program([FuncDecl(
                    name=Id(name="foo"),
                    param = [],
                    body = (
                        [],
                        [
                            CallStmt
                            (
                                method = Id(name="print"),
                                param = 
                                [
                                    BinaryOp(op="+",left=Id(name="a"),right=Id(name="b")),
                                    ArrayCell
                                    (
                                        arr = Id(name="a"),
                                        idx = 
                                        [
                                            IntLiteral(value=1),
                                            BinaryOp(op="+",left=Id(name="b"),right=CallExpr(method=Id(name="foo"),param=[]))
                                        ]
                                    )
                                ]
                            )
                        ]
                        )
                    ),
                    ])
        self.assertTrue(TestAST.checkASTGen(input,expect,345))
    
    def test_exp(self):
        """ Test expression"""
        input = """
                Function: foo
                        Body:
                            a = b == c && d;
                        EndBody.
                """
        expect = Program([FuncDecl(
                    name=Id(name="foo"),
                    param = [],
                    body = (
                        [],
                        [
                            Assign(lhs=Id(name="a"),
                            rhs=BinaryOp(
                                op="==",
                                left=Id(name="b"),
                                right=BinaryOp(op="&&",left=Id(name="c"),right=Id(name="d"))
                                ))
                        ]
                        )
                    ),
                    ])
        self.assertTrue(TestAST.checkASTGen(input,expect,346))
    
    def test_exp1(self):
        """ Test expression"""
        input = """
                Function: foo
                        Body:
                            a = b -. c && d;
                        EndBody.
                """
        expect = Program([FuncDecl(
                    name=Id(name="foo"),
                    param = [],
                    body = (
                        [],
                        [
                            Assign(lhs=Id(name="a"),
                            rhs=BinaryOp(
                                op="&&",
                                right=Id(name="d"),
                                left=BinaryOp(op="-.",left=Id(name="b"),right=Id(name="c"))
                                ))
                        ]
                        )
                    ),
                    ])
        self.assertTrue(TestAST.checkASTGen(input,expect,347))
    
    def test_exp1_1(self):
        """ Test expression"""
        input = """
                Function: foo
                        Body:
                            a = b -. c && d||e;
                        EndBody.
                """
        expect = Program([FuncDecl(
                    name=Id(name="foo"),
                    param = [],
                    body = (
                        [],
                        [
                            Assign(lhs=Id(name="a"),
                                rhs=BinaryOp(
                                    op="||",
                                    left=BinaryOp(
                                        op="&&",
                                        right=Id(name="d"),
                                        left=
                                            BinaryOp(
                                                op="-.",
                                                left=Id(name="b"),
                                                right=Id(name="c"))
                                        ),
                                    right = Id(name="e")
                                )
                            )
                        ]
                        )
                    ),
                    ])
        self.assertTrue(TestAST.checkASTGen(input,expect,348))
    
    def test_exp2(self):
        """ Test expression"""
        input = """
                Function: foo
                        Body:
                            a = b + c*.d;
                        EndBody.
                """
        expect = Program([FuncDecl(
                    name=Id(name="foo"),
                    param = [],
                    body = (
                        [],
                        [
                            Assign(
                                lhs=Id(name="a"),
                                rhs=BinaryOp(
                                    op="+",
                                    right=BinaryOp(
                                        op="*.",
                                        right=Id(name="d"),
                                        left= Id(name="c")
                                        ),
                                    left = Id(name="b")
                                )
                            )
                        ]
                        )
                    ),
                    ])
        self.assertTrue(TestAST.checkASTGen(input,expect,349))

    def test_exp2_1(self):
        """ Test expression"""
        input = """
                Function: foo
                        Body:
                            a = b + c +. d - e -. f;
                        EndBody.
                """
        expect = Program([FuncDecl(
                    name=Id(name="foo"),
                    param = [],
                    body = (
                        [],
                        [
                            Assign(
                                lhs=Id(name="a"),
                                rhs=BinaryOp(
                                    op="-.",
                                    right=Id(name="f"),
                                    left = BinaryOp(
                                        op="-",
                                        right = Id(name="e"),
                                        left = BinaryOp(
                                            op="+.",
                                            right= Id(name="d"),
                                            left = BinaryOp(
                                                op="+",
                                                right=Id(name="c"),
                                                left=Id(name="b")
                                            )
                                        )
                                    )
                                )
                            )
                        ]
                        )
                    ),
                    ])
        self.assertTrue(TestAST.checkASTGen(input,expect,350))
    
   
    
    def test_exp3(self):
        """ Test expression"""
        input = """
                Function: foo
                        Body:
                            a = b * c *. d \\ e \\. f % g;
                        EndBody.
                """
        expect = Program([FuncDecl(
                    name=Id(name="foo"),
                    param = [],
                    body = (
                        [],
                        [
                            Assign(
                                lhs=Id(name="a"),
                                rhs=BinaryOp(
                                    op="%",
                                    right=Id(name="g"),
                                    left = BinaryOp(
                                        op="\\.",
                                        right= Id(name="f"),
                                        left= BinaryOp(
                                            op="\\",
                                            right=Id(name="e"),
                                            left = BinaryOp(
                                                op="*.",
                                                right=Id(name="d"),
                                                left = BinaryOp(
                                                    op="*",
                                                    right=Id(name="c"),
                                                    left=Id(name="b")
                                                )
                                            )
                                        )
                                    ) 
                                    
                                )
                            )
                        ]
                        )
                    ),
                    ])
        self.assertTrue(TestAST.checkASTGen(input,expect,351))
    
    def test_exp3_1(self):
        """ Test expression"""
        input = """
                Function: foo
                        Body:
                            a = !(b * c);
                        EndBody.
                """
        expect = Program([FuncDecl(
                    name=Id(name="foo"),
                    param = [],
                    body = (
                        [],
                        [
                            Assign(
                                lhs=Id(name="a"),
                                rhs= UnaryOp(
                                    op="!",
                                    body=BinaryOp(
                                        op="*",
                                        left=Id(name="b"),
                                        right=Id(name="c")
                                    )
                                )
                            )
                        ]
                        )
                    ),
                    ])
        self.assertTrue(TestAST.checkASTGen(input,expect,352))

    def test_exp4(self):
        """ Test expression"""
        input = """
                Function: foo
                        Body:
                            a = !!!!b;
                        EndBody.
                """
        expect = Program([FuncDecl(
                    name=Id(name="foo"),
                    param = [],
                    body = (
                        [],
                        [
                            Assign(
                                lhs=Id(name="a"),
                                rhs= UnaryOp(
                                    op="!",
                                    body=UnaryOp(
                                        op="!",
                                        body = UnaryOp(
                                            op="!",
                                            body = UnaryOp(
                                                op="!",
                                                body= Id(name="b")
                                            )
                                        )
                                    )
                                )
                            )
                        ]
                        )
                    ),
                    ])
        self.assertTrue(TestAST.checkASTGen(input,expect,353))
    
    def test_exp4_1(self):
        """ Test expression"""
        input = """
                Function: foo
                        Body:
                            a = !!!!-b;
                        EndBody.
                """
        expect = Program([FuncDecl(
                    name=Id(name="foo"),
                    param = [],
                    body = (
                        [],
                        [
                            Assign(
                                lhs=Id(name="a"),
                                rhs= UnaryOp(
                                    op="!",
                                    body=UnaryOp(
                                        op="!",
                                        body = UnaryOp(
                                            op="!",
                                            body = UnaryOp(
                                                op="!",
                                                body= UnaryOp(
                                                    op="-",
                                                    body=Id(name="b")
                                                )
                                            )
                                        )
                                    )
                                )
                            )
                        ]
                        )
                    ),
                    ])
        self.assertTrue(TestAST.checkASTGen(input,expect,354))
    
    def test_exp5(self):
        """ Test expression"""
        input = """
                Function: foo
                        Body:
                            a = -b;
                            b = -.c;
                        EndBody.
                """
        expect = Program([FuncDecl(
                    name=Id(name="foo"),
                    param = [],
                    body = (
                        [],
                        [
                            Assign(
                                lhs=Id(name="a"),
                                rhs= UnaryOp(
                                    op="-",
                                    body=Id(name="b")
                                )
                            ),
                            Assign(
                                lhs=Id(name="b"),
                                rhs= UnaryOp(
                                    op="-.",
                                    body=Id(name="c")
                                )
                            )
                        ]
                        )
                    ),
                    ])
        self.assertTrue(TestAST.checkASTGen(input,expect,355))
    
    def test_exp5_1(self):
        """ Test expression"""
        input = """
                Function: foo
                        Body:
                            a = -b[1];
                            b = -.c[1];
                        EndBody.
                """
        expect = Program([FuncDecl(
                    name=Id(name="foo"),
                    param = [],
                    body = (
                        [],
                        [
                            Assign(
                                lhs=Id(name="a"),
                                rhs= UnaryOp(
                                    op="-",
                                    body=ArrayCell(
                                        arr=Id(name="b"),
                                        idx=[IntLiteral(value=1)]
                                    )
                                )
                            ),
                            Assign(
                                lhs=Id(name="b"),
                                rhs= UnaryOp(
                                    op="-.",
                                    body=ArrayCell(
                                        arr=Id(name="c"),
                                        idx=[IntLiteral(value=1)]
                                    )
                                )
                            )
                        ]
                        )
                    ),
                    ])
        self.assertTrue(TestAST.checkASTGen(input,expect,356))
    
    def test_exp6(self):
        """ Test expression"""
        input = """
                Function: foo
                        Body:
                            a[1+foo(-2)] = -b[1][a()][-c];
                        EndBody.
                """
        expect = Program([FuncDecl(
                    name=Id(name="foo"),
                    param = [],
                    body = (
                        [],
                        [
                            Assign(
                                lhs=ArrayCell(
                                    arr = Id(name="a"),
                                    idx = 
                                    [
                                        BinaryOp(op="+",left=IntLiteral(value=1),right=CallExpr(method=Id(name="foo"),param=[UnaryOp(op="-",body=IntLiteral(value=2))]))
                                    ]
                                ),
                                rhs= UnaryOp(
                                    op="-",
                                    body=ArrayCell(
                                        arr=Id(name="b"),
                                        idx=[
                                            IntLiteral(value=1),
                                            CallExpr(method=Id(name="a"),param=[]),
                                            UnaryOp(op="-",body=Id(name="c"))
                                            ]
                                    )
                                )
                            )
                        ]
                        )
                    ),
                    ])
        self.assertTrue(TestAST.checkASTGen(input,expect,357))
    
    def test_exp7(self):
        """ Test expression"""
        input = """
                Function: foo
                        Body:
                            a[1+foo(-2)] = foo(foo(foo(x)));
                        EndBody.
                """
        expect = Program([FuncDecl(
                    name=Id(name="foo"),
                    param = [],
                    body = (
                        [],
                        [
                            Assign(
                                lhs=ArrayCell(
                                    arr = Id(name="a"),
                                    idx = 
                                    [
                                        BinaryOp(op="+",left=IntLiteral(value=1),right=CallExpr(method=Id(name="foo"),param=[UnaryOp(op="-",body=IntLiteral(value=2))]))
                                    ]
                                ),
                                rhs= CallExpr(
                                    method=Id(name="foo"),
                                    param = [CallExpr(
                                        method=Id(name="foo"),
                                        param= [CallExpr(
                                            method = Id(name="foo"),
                                            param = [Id(name="x")]
                                        )]
                                    )]
                                )
                            )
                        ]
                        )
                    ),
                    ])
        self.assertTrue(TestAST.checkASTGen(input,expect,358))
    
    def test_exp8(self):
        """ Test expression"""
        input = """
                Function: foo
                        Body:
                            a = (b+d)*(d-f);
                        EndBody.
                """
        expect = Program([FuncDecl(
                    name=Id(name="foo"),
                    param = [],
                    body = (
                        [],
                        [
                            Assign(
                                lhs = Id(name="a"),
                                rhs = BinaryOp(
                                    op="*",
                                    left=BinaryOp(
                                        op="+",
                                        left=Id(name="b"),
                                        right=Id(name="d")
                                    ),
                                    right=BinaryOp(
                                        op="-",
                                        left=Id(name="d"),
                                        right=Id(name="f")
                                    )
                                )
                            )
                        ]
                        )
                    ),
                    ])
        self.assertTrue(TestAST.checkASTGen(input,expect,359))
    
    def test_exp8_1(self):
        """ Test expression"""
        input = """
                Function: foo
                        Body:
                            a = ((b+d)*(d-f))[1+foo()];
                        EndBody.
                """
        expect = Program([FuncDecl(
                    name=Id(name="foo"),
                    param = [],
                    body = (
                        [],
                        [
                            Assign(
                                lhs = Id(name="a"),
                                rhs = ArrayCell(
                                    arr = BinaryOp(
                                        op="*",
                                        left = BinaryOp(
                                            op="+",
                                            left=Id(name="b"),
                                            right=Id(name="d")
                                        ),
                                        right=BinaryOp(
                                            op="-",
                                            left=Id(name="d"),
                                            right=Id(name="f")
                                        )
                                    ),
                                    idx = [
                                        BinaryOp(
                                            op="+",
                                            left=IntLiteral(value=1),
                                            right=CallExpr(method=Id(name="foo"),param=[])
                                        )
                                    ]
                                )
                            )
                        ]
                        )
                    ),
                    ])
        self.assertTrue(TestAST.checkASTGen(input,expect,360))
    
    def test_exp8_2(self):
        """ Test expression"""
        input = """
                Function: foo
                        Body:
                            a = (b+d)*(d-f)[1+foo()];
                        EndBody.
                """
        expect = Program([FuncDecl(
                    name=Id(name="foo"),
                    param = [],
                    body = (
                        [],
                        [
                            Assign(
                                lhs = Id(name="a"),
                                rhs = BinaryOp(
                                    op = "*",
                                
                                    left = BinaryOp(
                                                op="+",
                                                left=Id(name="b"),
                                                right=Id(name="d")
                                            ),
                                    right = ArrayCell(
                                        arr = BinaryOp(
                                                op="-",
                                                left=Id(name="d"),
                                                right=Id(name="f")
                                            ),
                                        idx = [
                                            BinaryOp(
                                                op="+",
                                                left=IntLiteral(value=1),
                                                right=CallExpr(method=Id(name="foo"),param=[])
                                            )
                                        ]
                                    )
                                )
                            )
                        ]
                        )
                    ),
                    ])
        self.assertTrue(TestAST.checkASTGen(input,expect,361))
    
    def test_program2(self):
        """ Test simple program 2"""
        input = """
                Var: x;
                Function: foo
                        Body:
                            Return;
                        EndBody.
                """
        expect = Program([
            VarDecl(variable=Id(name="x"),varDimen=[],varInit=None),
            FuncDecl(
                    name=Id(name="foo"),
                    param = [],
                    body = (
                        [],
                        [
                            Return(expr=None)
                        ]
                        )
                    ),
                    ])
        self.assertTrue(TestAST.checkASTGen(input,expect,362))
    
    def test_program3(self):
        """ Test simple program"""
        input = """
                Var: x,y,z;
                Var: t = 1, m = "abc";
                Function: foo
                        Parameter: a,b,c
                        Body:
                            
                        EndBody.
                """
        expect = Program([
            VarDecl(variable=Id(name="x"),varDimen=[],varInit=None),
            VarDecl(variable=Id(name="y"),varDimen=[],varInit=None),
            VarDecl(variable=Id(name="z"),varDimen=[],varInit=None),
            VarDecl(variable=Id(name="t"),varDimen=[],varInit=IntLiteral(value=1)),
            VarDecl(variable=Id(name="m"),varDimen=[],varInit=StringLiteral(value="abc")),
            FuncDecl(
                    name=Id(name="foo"),
                    param = [
                        VarDecl(variable=Id(name="a"),varDimen=[],varInit=None),
                        VarDecl(variable=Id(name="b"),varDimen=[],varInit=None),
                        VarDecl(variable=Id(name="c"),varDimen=[],varInit=None),
                    ],
                    body = ([],[])
                    ),
                    ])
        self.assertTrue(TestAST.checkASTGen(input,expect,363))
    
    def test_program4(self):
        """ Test simple program"""
        input = """
                Var: x,y,z;
                Var: t = 1, m = "abc";
                Function: foo
                        Parameter: a,b,c
                        Body:
                            Var: a = 10, b = 0xA,c = 0o16;
                        EndBody.
                """
        expect = Program([
            VarDecl(variable=Id(name="x"),varDimen=[],varInit=None),
            VarDecl(variable=Id(name="y"),varDimen=[],varInit=None),
            VarDecl(variable=Id(name="z"),varDimen=[],varInit=None),
            VarDecl(variable=Id(name="t"),varDimen=[],varInit=IntLiteral(value=1)),
            VarDecl(variable=Id(name="m"),varDimen=[],varInit=StringLiteral(value="abc")),
            FuncDecl(
                    name=Id(name="foo"),
                    param = [
                        VarDecl(variable=Id(name="a"),varDimen=[],varInit=None),
                        VarDecl(variable=Id(name="b"),varDimen=[],varInit=None),
                        VarDecl(variable=Id(name="c"),varDimen=[],varInit=None),
                    ],
                    body = (
                        [
                        VarDecl(variable=Id(name="a"),varDimen=[],varInit=IntLiteral(value=10)),
                        VarDecl(variable=Id(name="b"),varDimen=[],varInit=IntLiteral(value=0xA)),
                        VarDecl(variable=Id(name="c"),varDimen=[],varInit=IntLiteral(value=0o16))
                        ],
                        [])
                    ),
                    ])
        self.assertTrue(TestAST.checkASTGen(input,expect,364))
    
    def test_program5(self):
        """ Test simple program"""
        input = """
                Var: x,y,z;
                Var: t = 1, m = "abc";
                Function: foo
                        Parameter: a,b,c
                        Body:
                            Var: a = 10, b = 0xA,c = 0o16;
                            If x == 0 Then print(a);
                            ElseIf x != 0 Then print(b);
                            Else print(c);
                            EndIf.
                        EndBody.
                """
        expect = Program([
            VarDecl(variable=Id(name="x"),varDimen=[],varInit=None),
            VarDecl(variable=Id(name="y"),varDimen=[],varInit=None),
            VarDecl(variable=Id(name="z"),varDimen=[],varInit=None),
            VarDecl(variable=Id(name="t"),varDimen=[],varInit=IntLiteral(value=1)),
            VarDecl(variable=Id(name="m"),varDimen=[],varInit=StringLiteral(value="abc")),
            FuncDecl(
                    name=Id(name="foo"),
                    param = [
                        VarDecl(variable=Id(name="a"),varDimen=[],varInit=None),
                        VarDecl(variable=Id(name="b"),varDimen=[],varInit=None),
                        VarDecl(variable=Id(name="c"),varDimen=[],varInit=None),
                    ],
                    body = (
                        [
                        VarDecl(variable=Id(name="a"),varDimen=[],varInit=IntLiteral(value=10)),
                        VarDecl(variable=Id(name="b"),varDimen=[],varInit=IntLiteral(value=0xA)),
                        VarDecl(variable=Id(name="c"),varDimen=[],varInit=IntLiteral(value=0o16))
                        ],
                        [
                            If
                            (
                                ifthenStmt = [
                                    (BinaryOp(op="==",left=Id(name="x"),right=IntLiteral(value=0)),[],[CallStmt(method=Id(name="print"),param=[Id(name="a")])]),
                                    (BinaryOp(op="!=",left=Id(name="x"),right=IntLiteral(value=0)),[],[CallStmt(method=Id(name="print"),param=[Id(name="b")])])
                                ],
                                elseStmt= (
                                    [],
                                    [
                                        CallStmt(method=Id(name="print"),param=[Id(name="c")])
                                    ]
                                ) 
                            )
                        ])
                    ),
                    ])
        self.assertTrue(TestAST.checkASTGen(input,expect,365))
    
    def test_program6(self):
        """ Test simple program"""
        input = """
                Var: x,y,z;
                Var: t = 1, m = "abc";
                Function: foo
                        Parameter: a,b,c
                        Body:
                            Var: a = 10, b = 0xA,c = 0o16;
                            Var: x[3] = {1,2.0,True}, y[1][1][1] = {{{1}}};
                            For(x = 1+x, x < b,x+1) Do
                            EndFor.
                        EndBody.
                """
        expect = Program([
            VarDecl(variable=Id(name="x"),varDimen=[],varInit=None),
            VarDecl(variable=Id(name="y"),varDimen=[],varInit=None),
            VarDecl(variable=Id(name="z"),varDimen=[],varInit=None),
            VarDecl(variable=Id(name="t"),varDimen=[],varInit=IntLiteral(value=1)),
            VarDecl(variable=Id(name="m"),varDimen=[],varInit=StringLiteral(value="abc")),
            FuncDecl(
                    name=Id(name="foo"),
                    param = [
                        VarDecl(variable=Id(name="a"),varDimen=[],varInit=None),
                        VarDecl(variable=Id(name="b"),varDimen=[],varInit=None),
                        VarDecl(variable=Id(name="c"),varDimen=[],varInit=None),
                    ],
                    body = (
                        [
                        VarDecl(variable=Id(name="a"),varDimen=[],varInit=IntLiteral(value=10)),
                        VarDecl(variable=Id(name="b"),varDimen=[],varInit=IntLiteral(value=0xA)),
                        VarDecl(variable=Id(name="c"),varDimen=[],varInit=IntLiteral(value=0o16)),
                        VarDecl(variable=Id(name="x"),varDimen=[3],varInit=ArrayLiteral([IntLiteral(value=1),FloatLiteral(value=2.0),BooleanLiteral(value=True)])),
                        VarDecl(variable=Id(name="y"),varDimen=[1,1,1],varInit=ArrayLiteral(value=[ArrayLiteral(value=[ArrayLiteral(value=[IntLiteral(value=1)])])]))
                        ],
                        [
                            For(
                                idx1=Id(name="x"),
                                expr1=BinaryOp(op="+",left=IntLiteral(value=1),right=Id(name="x")),
                                expr2=BinaryOp(op="<",left=Id(name="x"),right=Id(name="b")),
                                expr3=BinaryOp(op="+",right=IntLiteral(value=1),left=Id(name="x")),
                                loop = ([],[])
                            )
                        ])
                    ),
                    ])
        self.assertTrue(TestAST.checkASTGen(input,expect,366))

    def test_program7(self):
        """ Test simple program"""
        input = """
                Var: x,y,z;
                Var: t = 1, m = "abc";
                Function: foo
                        Parameter: a,b,c
                        Body:
                            Var: a = 10, b = 0xA,c = 0o16;
                            Var: x[3] = {1,2.0,True}, y[1][1][1] = {{{1}}};
                            While x <= 10 Do
                            EndWhile.
                        EndBody.
                """
        expect = Program([
            VarDecl(variable=Id(name="x"),varDimen=[],varInit=None),
            VarDecl(variable=Id(name="y"),varDimen=[],varInit=None),
            VarDecl(variable=Id(name="z"),varDimen=[],varInit=None),
            VarDecl(variable=Id(name="t"),varDimen=[],varInit=IntLiteral(value=1)),
            VarDecl(variable=Id(name="m"),varDimen=[],varInit=StringLiteral(value="abc")),
            FuncDecl(
                    name=Id(name="foo"),
                    param = [
                        VarDecl(variable=Id(name="a"),varDimen=[],varInit=None),
                        VarDecl(variable=Id(name="b"),varDimen=[],varInit=None),
                        VarDecl(variable=Id(name="c"),varDimen=[],varInit=None),
                    ],
                    body = (
                        [
                        VarDecl(variable=Id(name="a"),varDimen=[],varInit=IntLiteral(value=10)),
                        VarDecl(variable=Id(name="b"),varDimen=[],varInit=IntLiteral(value=0xA)),
                        VarDecl(variable=Id(name="c"),varDimen=[],varInit=IntLiteral(value=0o16)),
                        VarDecl(variable=Id(name="x"),varDimen=[3],varInit=ArrayLiteral([IntLiteral(value=1),FloatLiteral(value=2.0),BooleanLiteral(value=True)])),
                        VarDecl(variable=Id(name="y"),varDimen=[1,1,1],varInit=ArrayLiteral(value=[ArrayLiteral(value=[ArrayLiteral(value=[IntLiteral(value=1)])])]))
                        ],
                        [
                            While(
                                exp=BinaryOp(op="<=",right=IntLiteral(value=10),left=Id(name="x")),
                                sl = ([],[])
                            )
                        ])
                    ),
                    ])
        self.assertTrue(TestAST.checkASTGen(input,expect,367))
    
    def test_program8(self):
        """ Test simple program"""
        input = """
                Var: x,y,z;
                Var: t = 1, m = "abc";
                Function: foo
                        Parameter: a,b,c
                        Body:
                            While x <= 10 Do
                            EndWhile.
                        EndBody.
                Function: main
                        Parameter: a,b,c
                        Body:
                            Do
                            While x < 10
                            EndDo.
                        EndBody.
                """
        expect = Program([
            VarDecl(variable=Id(name="x"),varDimen=[],varInit=None),
            VarDecl(variable=Id(name="y"),varDimen=[],varInit=None),
            VarDecl(variable=Id(name="z"),varDimen=[],varInit=None),
            VarDecl(variable=Id(name="t"),varDimen=[],varInit=IntLiteral(value=1)),
            VarDecl(variable=Id(name="m"),varDimen=[],varInit=StringLiteral(value="abc")),
            FuncDecl(
                    name=Id(name="foo"),
                    param = [
                        VarDecl(variable=Id(name="a"),varDimen=[],varInit=None),
                        VarDecl(variable=Id(name="b"),varDimen=[],varInit=None),
                        VarDecl(variable=Id(name="c"),varDimen=[],varInit=None),
                    ],
                    body = (
                        []
                        ,
                        [
                            While(
                                exp=BinaryOp(op="<=",right=IntLiteral(value=10),left=Id(name="x")),
                                sl = ([],[])
                            )
                        ])
                    ),
            FuncDecl(
                    name=Id(name="main"),
                    param = [
                        VarDecl(variable=Id(name="a"),varDimen=[],varInit=None),
                        VarDecl(variable=Id(name="b"),varDimen=[],varInit=None),
                        VarDecl(variable=Id(name="c"),varDimen=[],varInit=None),
                    ],
                    body = (
                        []
                        ,
                        [
                            Dowhile(
                                exp=BinaryOp(op="<",right=IntLiteral(value=10),left=Id(name="x")),
                                sl = ([],[])
                            )
                        ])
                    ),
                    ])
        self.assertTrue(TestAST.checkASTGen(input,expect,368))

    def test_program9(self):
        """ Test simple program"""
        input = """
                Var: x,y,z;
                Var: t = 1, m = "abc";
                Function: foo
                        Body:
                        EndBody.
                Function: main
                        Body:
                        EndBody.
                Function: abc
                        Body:
                        EndBody.
                """
        expect = Program([
            VarDecl(variable=Id(name="x"),varDimen=[],varInit=None),
            VarDecl(variable=Id(name="y"),varDimen=[],varInit=None),
            VarDecl(variable=Id(name="z"),varDimen=[],varInit=None),
            VarDecl(variable=Id(name="t"),varDimen=[],varInit=IntLiteral(value=1)),
            VarDecl(variable=Id(name="m"),varDimen=[],varInit=StringLiteral(value="abc")),
            FuncDecl(
                    name=Id(name="foo"),
                    param = [],
                    body = (
                        [],[])
                    ),
            FuncDecl(
                    name=Id(name="main"),
                    param = [],
                    body = (
                        [],
                        [])
                    ),
               FuncDecl(
                    name=Id(name="abc"),
                    param = [],
                    body = (
                        [],
                        [])
                    ),
                    ])
        self.assertTrue(TestAST.checkASTGen(input,expect,369))
    def test_program10(self):
        """ Test simple program"""
        input = """
                Var: x,y,z;
                Var: t = 1, m = "abc";
                Function: foo
                        Body:
                        EndBody.
                Function: main
                        Body:
                        EndBody.
                **Function: abc
                        Body:
                        EndBody.**
                """
        expect = Program([
            VarDecl(variable=Id(name="x"),varDimen=[],varInit=None),
            VarDecl(variable=Id(name="y"),varDimen=[],varInit=None),
            VarDecl(variable=Id(name="z"),varDimen=[],varInit=None),
            VarDecl(variable=Id(name="t"),varDimen=[],varInit=IntLiteral(value=1)),
            VarDecl(variable=Id(name="m"),varDimen=[],varInit=StringLiteral(value="abc")),
            FuncDecl(
                    name=Id(name="foo"),
                    param = [],
                    body = (
                        [],[])
                    ),
            FuncDecl(
                    name=Id(name="main"),
                    param = [],
                    body = (
                        [],
                        [])
                    ),
                    ])
        self.assertTrue(TestAST.checkASTGen(input,expect,370))

    def test_program11(self):
        """ Test simple program"""
        input = """
                Var: x,y,z;
                Function: foo
                        Body:
                        Return foo;
                        EndBody.
                Function: main
                        Body:
                        Return main;
                        EndBody.
                Function: abc
                        Body:
                        abc = main();
                        EndBody.
                """
        expect = Program([
            VarDecl(variable=Id(name="x"),varDimen=[],varInit=None),
            VarDecl(variable=Id(name="y"),varDimen=[],varInit=None),
            VarDecl(variable=Id(name="z"),varDimen=[],varInit=None),
            FuncDecl(
                    name=Id(name="foo"),
                    param = [],
                    body = (
                        [],[
                            Return(expr=Id(name="foo"))
                        ])
                    ),
            FuncDecl(
                    name=Id(name="main"),
                    param = [],
                    body = (
                        [],
                        [
                            Return(expr=Id(name="main"))
                            
                        ])
                    ),
            FuncDecl(
                    name=Id(name="abc"),
                    param = [],
                    body = (
                        [],
                        [
                            Assign(lhs=Id(name="abc"),rhs=CallExpr(method=Id(name="main"),param=[]))
                        ])
                    ),
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,371))

    def test_program12(self):
        """ Test simple program"""
        input = """
                Var: x,y,z;
                Function: foo
                        Body:
                            If x > 10 Then Return;
                            EndIf. 
                        EndBody.
                Function: main
                        Body:
                            While True Do
                            EndWhile.
                        EndBody.
                Function: abc
                        Body:
                            Var:a_zZ = 0XABC,b_a = 0o1123;
                        EndBody.
                """
        expect = Program([
            VarDecl(variable=Id(name="x"),varDimen=[],varInit=None),
            VarDecl(variable=Id(name="y"),varDimen=[],varInit=None),
            VarDecl(variable=Id(name="z"),varDimen=[],varInit=None),
            FuncDecl(
                    name=Id(name="foo"),
                    param = [],
                    body = (
                        [],[
                            If(
                                ifthenStmt = [(BinaryOp(op=">",left=Id(name="x"),right=IntLiteral(value=10)),[],[Return(expr=None)])],
                                elseStmt = ([],[])
                            )
                        ])
                    ),
            FuncDecl(
                    name=Id(name="main"),
                    param = [],
                    body = (
                        [],
                        [
                            While(
                                exp= BooleanLiteral(value=True),
                                sl = ([],[])
                            )
                            
                        ])
                    ),
            FuncDecl(
                    name=Id(name="abc"),
                    param = [],
                    body = (
                        [
                            VarDecl(variable=Id(name="a_zZ"),varDimen=[],varInit=IntLiteral(value=0XABC)),
                            VarDecl(variable=Id(name="b_a"),varDimen=[],varInit=IntLiteral(value=0o1123)),
                        ],
                        [])
                    ),
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,372))
 
    def test_program13(self):
        """ Test simple program"""
        input = """
                Var: x,y,z;
                Function: foo
                        Body:
                            If x > 10 Then Return;
                            EndIf. 
                        EndBody.
                Function: main
                        Body:
                            While True Do
                                a = b + c +. d - e -. f;
                            EndWhile.
                            
                        EndBody.
                """
        expect = Program([
            VarDecl(variable=Id(name="x"),varDimen=[],varInit=None),
            VarDecl(variable=Id(name="y"),varDimen=[],varInit=None),
            VarDecl(variable=Id(name="z"),varDimen=[],varInit=None),
            FuncDecl(
                    name=Id(name="foo"),
                    param = [],
                    body = (
                        [],[
                            If(
                                ifthenStmt = [(BinaryOp(op=">",left=Id(name="x"),right=IntLiteral(value=10)),[],[Return(expr=None)])],
                                elseStmt = ([],[])
                            )
                        ])
                    ),
            FuncDecl(
                    name=Id(name="main"),
                    param = [],
                    body = (
                        [],
                        [
                            While(
                                exp= BooleanLiteral(value=True),
                                sl = ([],
                                [
                                    Assign(
                                lhs=Id(name="a"),
                                rhs=BinaryOp(
                                    op="-.",
                                    right=Id(name="f"),
                                    left = BinaryOp(
                                        op="-",
                                        right = Id(name="e"),
                                        left = BinaryOp(
                                            op="+.",
                                            right= Id(name="d"),
                                            left = BinaryOp(
                                                op="+",
                                                right=Id(name="c"),
                                                left=Id(name="b")
                                            )
                                        )
                                    )
                                )
                            )
                                ])
                            )
                            
                        ])
                    ),
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,373))
    
    def test_program14(self):
        """If else in function"""
        input = """
        Function: doST
            Parameter: n 
            Body:
                Var: x = 1;
                If x < 2 Then 
                    Var: n = 3;
                    x = n;
                ElseIf x < 1 Then 
                    Var: m = 0;
                    x = m;
                ElseIf x < 0 Then
                    n = True;
                Else 
                    Var: t = 1;
                    x = {{1,2},{3,4},{5,6}};
                EndIf.
            EndBody."""
        expect = Program(decl=[FuncDecl(name=Id(name="doST"),param=[VarDecl(variable=Id(name="n"),varDimen=[],varInit=None)],
        body=([VarDecl(variable=Id(name="x"),varDimen=[],varInit=IntLiteral(1))],[If(
            ifthenStmt=
            [
                (BinaryOp(op="<",left=Id(name="x"),right=IntLiteral(value=2)),[VarDecl(variable=Id(name="n"),varDimen=[],varInit=IntLiteral(3))],[Assign(lhs=Id(name="x"),rhs=Id(name="n"))]),
                (BinaryOp(op="<",left=Id(name="x"),right=IntLiteral(1)),[VarDecl(variable=Id(name="m"),varDimen=[],varInit=IntLiteral(0))],[Assign(lhs=Id("x"),rhs=Id(name="m"))]),
                (BinaryOp(op="<",left=Id(name="x"),right=IntLiteral(0)),[],[Assign(lhs=Id(name="n"),rhs=BooleanLiteral(value=True))])
            ],
            elseStmt=([VarDecl(variable=Id(name="t"),varDimen=[],varInit=IntLiteral(1))],[Assign(lhs=Id(name="x"),
            rhs=ArrayLiteral(value=[
                ArrayLiteral(value=[IntLiteral(value=1),IntLiteral(value=2)]),
                ArrayLiteral(value=[IntLiteral(value=3),IntLiteral(value=4)]),
                ArrayLiteral(value=[IntLiteral(value=5),IntLiteral(value=6)])
            ]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,374))

    def test_program15(self):
        """Complex program"""
        input = """
        Var: a, b, c;
        Var: x = 1, y[1] = 2;
        Function: doST
            Parameter: n, m
            Body:
                For (i = 0, i < 10, 1) Do
                    a = b + 2;
                    x = y [1] * 3;
                EndFor.
                While c < 3 Do
                    c = c * 2;
                EndWhile.
            EndBody."""
        expect = Program(decl=[VarDecl(variable=Id(name="a"),varDimen=[],varInit=None),VarDecl(variable=Id(name="b"),varDimen=[],varInit=None),
        VarDecl(variable=Id(name="c"),varDimen=[],varInit=None),VarDecl(variable=Id(name="x"),varDimen=[],varInit=IntLiteral(value=1)),
        VarDecl(variable=Id(name="y"),varDimen=[1],varInit=IntLiteral(value=2)),
        FuncDecl(name=Id(name="doST"),
        param=[VarDecl(variable=Id(name="n"),varDimen=[],varInit=None),VarDecl(variable=Id(name="m"),varDimen=[],varInit=None)],
        body=([],[For(idx1=Id(name="i"),expr1=IntLiteral(value=0),expr2=BinaryOp(op="<",left=Id(name="i"),right=IntLiteral(value=10)),
        expr3=IntLiteral(value=1),loop=([],[Assign(lhs=Id(name="a"),rhs=BinaryOp(op="+",left=Id(name="b"),right=IntLiteral(value=2))),
        Assign(lhs=Id(name="x"),rhs=BinaryOp(op="*",left=ArrayCell(arr=Id(name="y"),idx=[IntLiteral(value=1)]),right=IntLiteral(value=3)))])),
        While(exp=BinaryOp(op="<",left=Id(name="c"),right=IntLiteral(value=3)),
        sl=([],[Assign(lhs=Id(name="c"),rhs=BinaryOp(op="*",left=Id(name="c"),right=IntLiteral(value=2)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,375))

    def test_program16(self):
        """Complex program"""
        input = """
        Var: a, b, c;
        Var: x = 1, y[1] = 2;
        Var: t = {"A","B"};
        Function: doST
            Parameter: n, m
            Body:
                For (i = 0, i < 10, 1) Do
                    a = b + 2;
                    x = y[1] * 3;
                EndFor.
                While c < 3 Do
                    c = c * 2 +. t;
                EndWhile.
            EndBody."""
        expect = Program(decl=[VarDecl(variable=Id(name="a"),varDimen=[],varInit=None),VarDecl(variable=Id(name="b"),varDimen=[],varInit=None),
        VarDecl(variable=Id(name="c"),varDimen=[],varInit=None),VarDecl(variable=Id(name="x"),varDimen=[],varInit=IntLiteral(value=1)),
        VarDecl(variable=Id(name="y"),varDimen=[1],varInit=IntLiteral(value=2)),
        VarDecl(variable=Id(name="t"),varDimen=[],varInit=ArrayLiteral(value=[StringLiteral(value="A"),StringLiteral(value="B")])),
        FuncDecl(name=Id(name="doST"),
        param=[VarDecl(variable=Id(name="n"),varDimen=[],varInit=None),VarDecl(variable=Id(name="m"),varDimen=[],varInit=None)],
        body=([],[For(idx1=Id(name="i"),expr1=IntLiteral(value=0),expr2=BinaryOp(op="<",left=Id(name="i"),right=IntLiteral(value=10)),
        expr3=IntLiteral(value=1),loop=([],[Assign(lhs=Id(name="a"),rhs=BinaryOp(op="+",left=Id(name="b"),right=IntLiteral(value=2))),
        Assign(lhs=Id(name="x"),rhs=BinaryOp(op="*",left=ArrayCell(arr=Id(name="y"),idx=[IntLiteral(value=1)]),right=IntLiteral(value=3)))])),
        While(exp=BinaryOp(op="<",left=Id(name="c"),right=IntLiteral(value=3)),
        sl=([],[Assign(lhs=Id(name="c"),rhs=BinaryOp(op="+.",left=BinaryOp(op="*",left=Id(name="c"),right=IntLiteral(2)),right=Id(name="t")))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,376))

    def test_program17(self):
        """Complex program"""
        input = """
        Var: a, b, c;
        Var: x = 1, y[1] = 2;
        Function: doST
            Parameter: n, m
            Body:
                For (i = 0, i < 10, 1) Do
                    a = b + 2;
                    x = y [1] * 3;
                EndFor.
                While c < 3 Do
                    c = c * 2;
                EndWhile.
                Return (n + m * c);
            EndBody."""
        expect = Program(decl=[
            VarDecl(variable=Id(name="a"),varDimen=[],varInit=None),
            VarDecl(variable=Id(name="b"),varDimen=[],varInit=None),
            VarDecl(variable=Id(name="c"),varDimen=[],varInit=None),
            VarDecl(variable=Id(name="x"),varDimen=[],varInit=IntLiteral(value=1)),
            VarDecl(variable=Id(name="y"),varDimen=[1],varInit=IntLiteral(value=2)),
            FuncDecl(name=Id(name="doST"),
            param=[
                VarDecl(variable=Id(name="n"),varDimen=[],varInit=None),
                VarDecl(variable=Id(name="m"),varDimen=[],varInit=None)
                ],
            body=([],[
                For(idx1=Id(name="i"),
                expr1=IntLiteral(value=0),
                expr2=BinaryOp(op="<",left=Id(name="i"),right=IntLiteral(value=10)),
                expr3=IntLiteral(value=1),
                loop=([],[
                    Assign(lhs=Id(name="a"),rhs=BinaryOp(op="+",left=Id(name="b"),right=IntLiteral(value=2))),
                    Assign(lhs=Id(name="x"),rhs=BinaryOp(op="*",left=ArrayCell(arr=Id(name="y"),idx=[IntLiteral(value=1)]),right=IntLiteral(value=3)))])),
                While(
                    exp=BinaryOp(op="<",left=Id(name="c"),right=IntLiteral(value=3)),
                    sl=([],[Assign(lhs=Id(name="c"),rhs=BinaryOp(op="*",left=Id(name="c"),right=IntLiteral(value=2)))])),
                Return(BinaryOp(op="+",left=Id(name="n"),right=BinaryOp(op="*",left=Id(name="m"),right=Id(name="c"))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,377))

    def test_program18(self):
        """Continue statement in function"""
        input = """
        Var: a, b;
        Function: doST
            Parameter: n
            Body:
                Do 
                    m = m + 1;
                    a = doST(b);
                    Continue;
                While
                    n < 4
                EndDo.
            EndBody."""
        expect = Program(decl=[VarDecl(variable=Id(name="a"),varDimen=[],varInit=None),VarDecl(variable=Id(name="b"),varDimen=[],varInit=None),
        FuncDecl(name=Id(name="doST"),param=[VarDecl(variable=Id(name="n"),varDimen=[],varInit=None)],
        body=([],
        [Dowhile(sl=([],
        [Assign(lhs=Id(name="m"),rhs=BinaryOp(op="+",left=Id(name="m"),right=IntLiteral(value=1))),
        Assign(lhs=Id(name="a"),rhs=CallExpr(method=Id(name="doST"),param=[Id(name="b")])),Continue()]),
        exp=BinaryOp(op="<",left=Id(name="n"),right=IntLiteral(value=4)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,378))

    def test_program19(self):
        """Continue statement in function"""
        input = """
        Var: a, b, c;
        Var: x = {1.2,2.3,3.4};
        Function: doST
            Parameter: n
            Body:
                Var: m = 1;
                Var: n = "abc";
                While n < 4 Do
                    m = m + 1;
                    n = n * 2;
                    Continue;
                EndWhile.
                While m > 4 Do
                    m = m - 3;
                    x = x + doST(b);
                EndWhile.
            EndBody."""
        expect = Program(decl=[
        VarDecl(variable=Id(name="a"),varDimen=[],varInit=None),VarDecl(variable=Id(name="b"),varDimen=[],varInit=None),
        VarDecl(variable=Id(name="c"),varDimen=[],varInit=None),
        VarDecl(variable=Id(name="x"),varDimen=[],varInit=ArrayLiteral(value=[FloatLiteral(value=1.2),FloatLiteral(value=2.3),FloatLiteral(value=3.4)])),
        FuncDecl(
            name=Id(name="doST"),
            param=[
                VarDecl(variable=Id(name="n"),varDimen=[],varInit=None)
                ],
            body=(
                [
                    VarDecl(variable=Id(name="m"),varDimen=[],varInit=IntLiteral(value=1)),
                    VarDecl(variable=Id(name="n"),varDimen=[],varInit=StringLiteral(value="abc"))
                ],
                [
                    While(
                        exp=BinaryOp(op="<",left=Id(name="n"),right=IntLiteral(value=4)),
                        sl=([],
                            [
                                Assign(lhs=Id(name="m"),rhs=BinaryOp(op="+",left=Id(name="m"),right=IntLiteral(value=1))),
                                Assign(lhs=Id(name="n"),rhs=BinaryOp(op="*",left=Id(name="n"),right=IntLiteral(value=2))),
                                Continue()
                            ])
                        ),
                    While(
                        exp=BinaryOp(op=">",left=Id(name="m"),right=IntLiteral(value=4)),
                        sl=([],
                        [
                            Assign(lhs=Id(name="m"),rhs=BinaryOp(op="-",left=Id(name="m"),right=IntLiteral(value=3))),
                            Assign(lhs=Id(name="x"),rhs=BinaryOp(op="+",left=Id(name="x"),right=CallExpr(method=Id(name="doST"),param=[Id(name="b")])))
                        ])
                        )
                ])
            )])
        self.assertTrue(TestAST.checkASTGen(input,expect,379))

    def test_program20(self):
        """Continue statement in function"""
        input = """
        Function: doST
            Parameter: n, m
            Body:
                Var: a, b;
                n[a][b] = m * a \\ 6 + 3;
                m = n[2] && b;
                Continue;
            EndBody."""
        expect = Program(decl=[FuncDecl(name=Id(name="doST"),
        param=[VarDecl(variable=Id(name="n"),varDimen=[],varInit=None),VarDecl(variable=Id(name="m"),varDimen=[],varInit=None)],
        body=([VarDecl(variable=Id(name="a"),varDimen=[],varInit=None),VarDecl(variable=Id(name="b"),varDimen=[],varInit=None)],
        [Assign(lhs=ArrayCell(arr=Id(name="n"),idx=[Id(name="a"),Id(name="b")]),
        rhs=BinaryOp(op="+",left=BinaryOp(op="\\",left=BinaryOp(op="*",left=Id(name="m"),
        right=Id(name="a")),right=IntLiteral(value=6)),right=IntLiteral(value=3))),
        Assign(lhs=Id(name="m"),rhs=BinaryOp(op="&&",left=ArrayCell(arr=Id(name="n"),idx=[IntLiteral(value=2)]),right=Id(name="b"))),
        Continue()]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,380))

    def test_program21(self):
        """Continue statement in function"""
        input = """
        Function: doST
            Parameter: n, m
            Body:
                n[1][2] = m * 2;
                Continue;
                Continue;
            EndBody."""
        expect = Program(decl=[FuncDecl(name=Id(name="doST"),
        param=[VarDecl(variable=Id(name="n"),varDimen=[],varInit=None),VarDecl(variable=Id(name="m"),varDimen=[],varInit=None)],
        body=([],[Assign(lhs=ArrayCell(arr=Id(name="n"),idx=[IntLiteral(value=1),IntLiteral(value=2)]),
        rhs=BinaryOp(op="*",left=Id(name="m"),right=IntLiteral(value=2))),Continue(),Continue()]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,381))

    def test_program22(self):
        """Continue statement in function"""
        input = """
        Var: a, b, c;
        Var: x = {1.2,2.3,3.4};
        Function: doST
            Parameter: n
            Body:
                Var: m = 1;
                Continue;
                While n < 4 Do
                    m = m + 1;
                    n = n * 2;
                EndWhile.
                Continue;
            EndBody."""
        expect = Program(decl=[
        VarDecl(variable=Id(name="a"),varDimen=[],varInit=None),VarDecl(variable=Id(name="b"),varDimen=[],varInit=None),
        VarDecl(variable=Id(name="c"),varDimen=[],varInit=None),
        VarDecl(variable=Id(name="x"),varDimen=[],varInit=ArrayLiteral(value=[FloatLiteral(value=1.2),FloatLiteral(value=2.3),FloatLiteral(value=3.4)])),
        FuncDecl(
            name=Id(name="doST"),
            param=[VarDecl(variable=Id(name="n"),varDimen=[],varInit=None)],
            body=(
                [
                    VarDecl(variable=Id(name="m"),varDimen=[],varInit=IntLiteral(value=1))
                ],
                [
                    Continue(),
                    While(
                        exp=BinaryOp(op="<",left=Id(name="n"),right=IntLiteral(value=4)),
                        sl=(
                            [],
                            [
                                Assign(lhs=Id(name="m"),rhs=BinaryOp(op="+",left=Id(name="m"),right=IntLiteral(value=1))),
                                Assign(lhs=Id(name="n"),rhs=BinaryOp(op="*",left=Id(name="n"),right=IntLiteral(value=2)))
                            ])
                        ),
                    Continue()
                ])
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,382))

    def test_program23(self):
            """Break statement in function"""
            input = """
            Var: a, b, c;
            Function: doST
                Parameter: n
                Body:
                    Var: m = 1;
                    While n < 4 Do
                        m = m + 1;
                        n = n * 2;
                        Break;
                    EndWhile.
                EndBody."""
            expect = Program(decl=[
                VarDecl(variable=Id(name="a"),varDimen=[],varInit=None),
                VarDecl(variable=Id(name="b"),varDimen=[],varInit=None),
                VarDecl(variable=Id(name="c"),varDimen=[],varInit=None),
                FuncDecl(name=Id(name="doST"),
                param=[VarDecl(variable=Id(name="n"),varDimen=[],varInit=None)],
                body=([VarDecl(variable=Id(name="m"),varDimen=[],varInit=IntLiteral(value=1))],
                        [
                            While(
                                exp=BinaryOp(op="<",left=Id(name="n"),right=IntLiteral(value=4)),
                                sl=([],
                                    [
                                        Assign(lhs=Id(name="m"),rhs=BinaryOp(op="+",left=Id(name="m"),right=IntLiteral(value=1))),
                                        Assign(lhs=Id(name="n"),
                                            rhs=BinaryOp(op="*",left=Id(name="n"),right=IntLiteral(value=2))),
                                        Break()
                                    ])
                                )
                        ]
                    ))
                ])
            self.assertTrue(TestAST.checkASTGen(input,expect,383))


    def test_program24(self):
            """DoWhile statement in function"""
            input = """
            Var: a, b;
            Function: doST
                Parameter: n
                Body:
                    Do 
                        m = m + 1;
                        a = doST(b);
                    While
                        n == True
                    EndDo.
                    (b + 2)[a] = m;
                EndBody."""
            expect = Program(decl=[VarDecl(variable=Id(name="a"),varDimen=[],varInit=None),VarDecl(variable=Id(name="b"),varDimen=[],varInit=None),
            FuncDecl(name=Id(name="doST"),param=[VarDecl(variable=Id(name="n"),varDimen=[],varInit=None)],
            body=([],
            [Dowhile(sl=([],
            [Assign(lhs=Id(name="m"),rhs=BinaryOp(op="+",left=Id(name="m"),right=IntLiteral(value=1))),
            Assign(lhs=Id(name="a"),rhs=CallExpr(method=Id(name="doST"),param=[Id(name="b")]))]),
            exp=BinaryOp(op="==",left=Id(name="n"),right=BooleanLiteral(value=True))),
            Assign(lhs=ArrayCell(arr=BinaryOp(op="+",left=Id(name="b"),right=IntLiteral(value=2)),idx=[Id(name="a")]),rhs=Id(name="m"))]))])
            self.assertTrue(TestAST.checkASTGen(input,expect,384))

    def test_program25(self):
        """DoWhile statement in function"""
        input = """
        Var: a, b;
        Function: doST
            Parameter: n
            Body:
                Var: z[1] = 12.e5;
                Do 
                    m = m + 1;
                    a = doST(b);
                While
                    n == True
                EndDo.
                (b + 2)[a] = m;
            EndBody."""
        expect = Program(decl=[VarDecl(variable=Id(name="a"),varDimen=[],varInit=None),VarDecl(variable=Id(name="b"),varDimen=[],varInit=None),
        FuncDecl(name=Id(name="doST"),param=[VarDecl(variable=Id(name="n"),varDimen=[],varInit=None)],
        body=([VarDecl(variable=Id(name="z"),varDimen=[1],varInit=FloatLiteral(value=1200000.0))],[Dowhile(
        sl=([],[Assign(lhs=Id(name="m"),rhs=BinaryOp(op="+",left=Id(name="m"),right=IntLiteral(value=1))),
        Assign(lhs=Id(name="a"),rhs=CallExpr(method=Id(name="doST"),param=[Id(name="b")]))]),
        exp=BinaryOp(op="==",left=Id(name="n"),right=BooleanLiteral(value=True))),
        Assign(lhs=ArrayCell(arr=BinaryOp(op="+",left=Id(name="b"),right=IntLiteral(value=2)),idx=[Id(name="a")]),rhs=Id(name="m"))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,385))

    def test_program26(self):
        """DoWhile statement in function"""
        input = """
        Var: a, b;
        Function: doST
            Parameter: n
            Body:
                Var: z[1] = 12.e5;
                Do
                    m = m + 1;
                    b = z[1] && n;
                    a = doST(b);
                While
                    n == True
                EndDo.
                (b + 2)[a] = m;
            EndBody."""
        expect = Program(decl=[VarDecl(variable=Id(name="a"),varDimen=[],varInit=None),VarDecl(variable=Id(name="b"),varDimen=[],varInit=None),
        FuncDecl(name=Id(name="doST"),param=[VarDecl(variable=Id(name="n"),varDimen=[],varInit=None)],
        body=([VarDecl(variable=Id(name="z"),varDimen=[1],varInit=FloatLiteral(value=1200000.0))],[Dowhile(
        sl=([],[Assign(lhs=Id(name="m"),rhs=BinaryOp(op="+",left=Id(name="m"),right=IntLiteral(value=1))),
        Assign(lhs=Id(name="b"),rhs=BinaryOp(op="&&",left=ArrayCell(arr=Id(name="z"),idx=[IntLiteral(value=1)]),right=Id(name="n"))),
        Assign(lhs=Id(name="a"),rhs=CallExpr(method=Id(name="doST"),param=[Id(name="b")]))]),
        exp=BinaryOp(op="==",left=Id(name="n"),right=BooleanLiteral(value=True))),
        Assign(lhs=ArrayCell(arr=BinaryOp(op="+",left=Id(name="b"),right=IntLiteral(value=2)),idx=[Id(name="a")]),rhs=Id(name="m"))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,386))

    def test_program27(self):
        """DoWhile statement in function"""
        input = """
        Var: a, b;
        Function: doST
            Parameter: n
            Body:
                Var: z[1] = 12.e5;
                Do
                    m = m + 1;
                    b = z[1] && n;
                    a = doST(b);
                While
                    (n == True) || (b > 1)
                EndDo.
                (b + 2)[a] = m;
            EndBody."""
        expect = Program(decl=[VarDecl(variable=Id(name="a"),varDimen=[],varInit=None),VarDecl(variable=Id(name="b"),varDimen=[],varInit=None),
        FuncDecl(name=Id(name="doST"),param=[VarDecl(variable=Id(name="n"),varDimen=[],varInit=None)],
        body=([VarDecl(variable=Id(name="z"),varDimen=[1],varInit=FloatLiteral(value=1200000.0))],[Dowhile(
        sl=([],[Assign(lhs=Id(name="m"),rhs=BinaryOp(op="+",left=Id(name="m"),right=IntLiteral(value=1))),
        Assign(lhs=Id(name="b"),rhs=BinaryOp(op="&&",left=ArrayCell(arr=Id(name="z"),idx=[IntLiteral(value=1)]),right=Id(name="n"))),
        Assign(lhs=Id(name="a"),rhs=CallExpr(method=Id(name="doST"),param=[Id(name="b")]))]),
        exp=BinaryOp(op="||",left=BinaryOp(op="==",left=Id(name="n"),right=BooleanLiteral(value=True)),
        right=BinaryOp(op=">",left=Id(name="b"),right=IntLiteral(value=1)))),
        Assign(lhs=ArrayCell(arr=BinaryOp(op="+",left=Id(name="b"),right=IntLiteral(value=2)),idx=[Id(name="a")]),rhs=Id(name="m"))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,387))
    
    def test_program28(self):
        """While nest while"""
        input = """
        Function: main
            Body:
                While x < 10 Do
                    Do 
                        While y > 10 Do
                            y = y + 1;
                        EndWhile.
                    While x < 100
                    EndDo.
                EndWhile.
            EndBody."""
        expect = Program([
            FuncDecl(
                name = Id(name="main"),
                param=[],
                body=([],
                [
                    While(
                        exp = BinaryOp(op="<",left=Id(name="x"),right=IntLiteral(value=10)),
                        sl = ([],
                        [
                            Dowhile(
                                exp = BinaryOp(op="<",left=Id(name="x"),right=IntLiteral(value=100)),
                                sl = ([],
                                [
                                    While(
                                        exp = BinaryOp(op=">",left = Id(name="y"),right=IntLiteral(value=10)),
                                        sl =([],
                                        [
                                            Assign(lhs=Id(name="y"),rhs=BinaryOp(op="+",left=Id(name="y"),right=IntLiteral(value=1)))
                                        ])
                                    )
                                ])
                            )
                        ])
                    )
                ])

            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,388))
    
    def test_program29(self):
        """For nest For"""
        input = """
        Function: main
            Body:
                For (x = 1,x < 100,1) Do
                    For (y = x , y < 1000, 2) Do
                        For ( z = y,z < 10000, 3) Do
                            print(10000000);
                        EndFor.
                    EndFor.
                EndFor.
            EndBody."""
        expect = Program([
            FuncDecl(
                name = Id(name="main"),
                param=[],
                body=([],
                [
                    For(
                        idx1=Id(name="x"),
                        expr1=IntLiteral(value=1),
                        expr2=BinaryOp(op="<",left=Id(name="x"),right=IntLiteral(value=100)),
                        expr3=IntLiteral(value=1),
                        loop = ([],
                        [
                            For(
                                idx1=Id(name="y"),
                                expr1=Id(name="x"),
                                expr2=BinaryOp(op="<",left=Id(name="y"),right=IntLiteral(value=1000)),
                                expr3=IntLiteral(value=2),
                                loop = ([],
                                [
                                    For(
                                        idx1=Id(name="z"),
                                        expr1=Id(name="y"),
                                        expr2=BinaryOp(op="<",left=Id(name="z"),right=IntLiteral(value=10000)),
                                        expr3=IntLiteral(value=3),
                                        loop = ([],
                                        [
                                            CallStmt(method=Id(name="print"),param=[IntLiteral(value=10000000)])
                                        ])
                                    )
                                ])
                            )
                        ])
                    )
                ])

            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,389))
    
    def test_program30(self):
        """ If condition"""
        input = """
        Function: main
            Body:
                If ((x == 1)&&(y!=2))||(z =/= 2.0)||(t >. 100.1e2) Then
                    donotst(haha);
                EndIf.
            EndBody."""
        expect = Program([
            FuncDecl(
                name=Id(name="main"),
                param=[],
                body=([],
                [
                    If(
                        ifthenStmt = 
                        [(
                            BinaryOp(
                                op="||",
                                left=BinaryOp(
                                    op="||",
                                    left=BinaryOp(
                                        op="&&",
                                        left=BinaryOp(
                                            op="==",
                                            left=Id(name="x"),
                                            right=IntLiteral(value=1)
                                            ),
                                        right=BinaryOp(
                                            op="!=",
                                            left=Id(name="y"),
                                            right=IntLiteral(value=2)
                                            )
                                        ),
                                    right=BinaryOp(
                                            op="=/=",
                                            left=Id(name="z"),
                                            right=FloatLiteral(value=2.0)
                                    )),
                                right=BinaryOp(
                                    op=">.",
                                    left=Id(name="t"),
                                    right=FloatLiteral(value=10010.0))
                                ),
                            [],
                            [
                                CallStmt(method=Id(name="donotst"),param=[Id(name="haha")])
                            ])],
                        elseStmt=([],[])
                    )
                ])
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,390))
    
    def test_program31(self):
        """For loop in function"""
        input = """
        Function: doST
            Parameter: i, n
            Body:
                For (i = 0, i < 5, 1) Do
                    n = n \\ 2;
                EndFor.
            EndBody."""
        expect = Program(decl=[FuncDecl(name=Id(name="doST"),
        param=[VarDecl(variable=Id(name="i"),varDimen=[],varInit=None),VarDecl(variable=Id(name="n"),varDimen=[],varInit=None)],
        body=([],[For(idx1=Id(name="i"),expr1=IntLiteral(value=0),expr2=BinaryOp(op="<",left=Id(name="i"),right=IntLiteral(value=5)),
        expr3=IntLiteral(value=1),loop=([[],[Assign(lhs=Id(name="n"),rhs=BinaryOp(op="\\",left=Id(name="n"),right=IntLiteral(value=2)))]]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,391))
    
    def test_program32(self):
        """For loop in function"""
        input = """
        Function: doST
            Parameter: n, m
            Body:
                Var: i;
                n = 30;
                m = 0;
                z = 1;
                For (i = 0, i < 5, 1) Do
                    n = n \\ 2;
                    m = m + 3 ;
                    z = z * 3 - n[1];
                EndFor.
            EndBody."""
        expect = Program(decl=[FuncDecl(name=Id(name="doST"),
        param=[VarDecl(variable=Id(name="n"),varDimen=[],varInit=None),VarDecl(variable=Id(name="m"),varDimen=[],varInit=None)],
        body=([VarDecl(variable=Id(name="i"),varDimen=[],varInit=None)],
        [Assign(lhs=Id(name="n"),rhs=IntLiteral(value=30)),Assign(lhs=Id(name="m"),rhs=IntLiteral(value=0)),
        Assign(lhs=Id(name="z"),rhs=IntLiteral(value=1)),
        For(idx1=Id(name="i"),expr1=IntLiteral(value=0),expr2=BinaryOp(op="<",left=Id(name="i"),right=IntLiteral(value=5)),
        expr3=IntLiteral(value=1),loop=([],[Assign(lhs=Id(name="n"),rhs=BinaryOp(op="\\",left=Id(name="n"),right=IntLiteral(value=2))),
        Assign(lhs=Id(name="m"),rhs=BinaryOp(op="+",left=Id(name="m"),right=IntLiteral(value=3))),
        Assign(lhs=Id(name="z"),rhs=BinaryOp(op="-",left=BinaryOp(op="*",left=Id(name="z"),right=IntLiteral(value=3)),
        right=ArrayCell(arr=Id(name="n"),idx=[IntLiteral(value=1)])))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,392))
    
    def test_program33(self):
        "Test array"
        input= """
                Function: main
                    Parameter: a[2],b[1]
                    Body:
                        Var: a[1];
                        a[a[1]] = 1;
                    EndBody.
        """
        expect = Program([
            FuncDecl(
                name=Id(name="main"),
                param = [
                        VarDecl(variable=Id(name="a"),varDimen=[2],varInit=None),
                        VarDecl(variable=Id(name="b"),varDimen=[1],varInit=None)],
                body = (
                    [VarDecl(variable=Id(name="a"),varDimen=[1],varInit=None)],
                    [
                        Assign(
                            lhs=ArrayCell(
                                arr= Id(name="a"),
                                idx = [
                                    ArrayCell(
                                        arr=Id(name="a"),
                                        idx = [IntLiteral(value=1)]
                                    )
                                ]
                            ),
                            rhs= IntLiteral(value=1) 
                        )
                        
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,393))
    
    def test_program34(self):
        "Test array"
        input= """
                Function: main
                    Parameter: a[2],b[1]
                    Body:
                        Var: a[1];
                        a[a[a[1+func(a[1],1+x)[1]]]][1] = 1;
                    EndBody.
        """
        expect = Program([
            FuncDecl(
                name=Id(name="main"),
                param = [
                        VarDecl(variable=Id(name="a"),varDimen=[2],varInit=None),
                        VarDecl(variable=Id(name="b"),varDimen=[1],varInit=None)],
                body = (
                    [VarDecl(variable=Id(name="a"),varDimen=[1],varInit=None)],
                    [
                        Assign(
                            lhs=ArrayCell(
                                arr= Id(name="a"),
                                idx = [
                                    ArrayCell(
                                        arr=Id(name="a"),
                                        idx = [
                                            ArrayCell(
                                                arr=Id(name="a"),
                                                idx = [
                                                    BinaryOp(
                                                        op="+",
                                                        left=IntLiteral(value=1),
                                                        right=ArrayCell(
                                                            arr = CallExpr(
                                                                method=Id(name="func"),
                                                                param=[
                                                                    ArrayCell(arr=Id(name="a"),idx=[IntLiteral(value=1)]),
                                                                    BinaryOp(op="+",left=IntLiteral(value=1),right=Id(name="x"))   
                                                                ]),
                                                            idx=[IntLiteral(value=1)]
                                                        )
                                                    )
                                                ]
                                            )
                                        ]
                                    ),
                                    IntLiteral(value=1)
                                ]
                            ),
                            rhs= IntLiteral(value=1) 
                        )
                        
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,394))

    def test_program35(self):
        """ Test mix"""
        input = """
                Var: a,b=1,c=2.0,d=False,e="s",f[2]={0x2,0o7};
                Var: x[1][2] = {{1,"abc"},{True,1e2}};
                Function: main
                    Parameter: a,b[1],c[1][2]
                    Body:
                        Var: x, y,z;
                        Var: a,b,c;
                        If a =/= 100.0 Then
                            For (y = 10,y <. 1000.0,y +. 10.0) Do
                                Continue;
                            EndFor.
                        EndIf.
                    EndBody.
                    """
        expect = Program(
            [
                VarDecl(variable=Id(name="a"),varDimen=[],varInit=None),
                VarDecl(variable=Id(name="b"),varDimen=[],varInit=IntLiteral(value=1)),
                VarDecl(variable=Id(name="c"),varDimen=[],varInit=FloatLiteral(value=2.0)),
                VarDecl(variable=Id(name="d"),varDimen=[],varInit=BooleanLiteral(value=False)),
                VarDecl(variable=Id(name="e"),varDimen=[],varInit=StringLiteral(value="s")),
                VarDecl(variable=Id(name="f"),varDimen=[2],varInit=ArrayLiteral(value=[IntLiteral(value=0x2),IntLiteral(value=0o7)])),
                VarDecl(variable=Id(name="x"),varDimen=[1,2],varInit=ArrayLiteral(value=
                [
                    ArrayLiteral(value=[IntLiteral(value=1),StringLiteral(value="abc")]),
                    ArrayLiteral(value=[BooleanLiteral(value=True),FloatLiteral(value=1e2)])
                ])),
                FuncDecl(
                    name=Id(name="main"),
                    param=
                    [
                        VarDecl(variable=Id(name="a"),varDimen=[],varInit=None),
                        VarDecl(variable=Id(name="b"),varDimen=[1],varInit=None),
                        VarDecl(variable=Id(name="c"),varDimen=[1,2],varInit=None)
                    ],
                    body=(
                        [
                            VarDecl(variable=Id(name="x"),varDimen=[],varInit=None),
                            VarDecl(variable=Id(name="y"),varDimen=[],varInit=None),
                            VarDecl(variable=Id(name="z"),varDimen=[],varInit=None),
                            VarDecl(variable=Id(name="a"),varDimen=[],varInit=None),
                            VarDecl(variable=Id(name="b"),varDimen=[],varInit=None),
                            VarDecl(variable=Id(name="c"),varDimen=[],varInit=None),
                        ],
                        [
                            If(
                                ifthenStmt=
                                [
                                    (BinaryOp(op="=/=",left=Id(name="a"),right=FloatLiteral(value=100.0)),[],
                                    [
                                        For(
                                            idx1=Id(name="y"),
                                            expr1=IntLiteral(value=10),
                                            expr2=BinaryOp(op="<.",left=Id(name="y"),right=FloatLiteral(value=1000.0)),
                                            expr3=BinaryOp(op="+.",left=Id(name="y"),right=FloatLiteral(value=10.0)),
                                            loop = ([],[Continue()])
                                        )
                                    ])
                                ],
                                elseStmt=([],[])
                            )
                        ]
                    )
                )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,395))
    
    def test_program36(self):
        """ Test mix"""
        input = """
                Var: a,b=1,c=2.0,d=False,e="s",f[2]={0x2,0o7};
                Var: x[1][2] = {{1,"abc"},{True,1e2}};
                Function: main
                    Parameter: a,b[1],c[1][2]
                    Body:
                        Var: x, y,z;
                        Var: a,b,c;
                        If a =/= 100.0 Then
                            For (y = 10,y <. 1000.0,y +. 10.0) Do
                                Continue;
                            EndFor.
                        ElseIf b >= 0x16 Then
                            Var: t = 1;
                            While a <=. 10.5 Do
                                Break;
                            EndWhile.
                        EndIf.
                    EndBody.
                    """
        expect = Program(
            [
                VarDecl(variable=Id(name="a"),varDimen=[],varInit=None),
                VarDecl(variable=Id(name="b"),varDimen=[],varInit=IntLiteral(value=1)),
                VarDecl(variable=Id(name="c"),varDimen=[],varInit=FloatLiteral(value=2.0)),
                VarDecl(variable=Id(name="d"),varDimen=[],varInit=BooleanLiteral(value=False)),
                VarDecl(variable=Id(name="e"),varDimen=[],varInit=StringLiteral(value="s")),
                VarDecl(variable=Id(name="f"),varDimen=[2],varInit=ArrayLiteral(value=[IntLiteral(value=0x2),IntLiteral(value=0o7)])),
                VarDecl(variable=Id(name="x"),varDimen=[1,2],varInit=ArrayLiteral(value=
                [
                    ArrayLiteral(value=[IntLiteral(value=1),StringLiteral(value="abc")]),
                    ArrayLiteral(value=[BooleanLiteral(value=True),FloatLiteral(value=1e2)])
                ])),
                FuncDecl(
                    name=Id(name="main"),
                    param=
                    [
                        VarDecl(variable=Id(name="a"),varDimen=[],varInit=None),
                        VarDecl(variable=Id(name="b"),varDimen=[1],varInit=None),
                        VarDecl(variable=Id(name="c"),varDimen=[1,2],varInit=None)
                    ],
                    body=(
                        [
                            VarDecl(variable=Id(name="x"),varDimen=[],varInit=None),
                            VarDecl(variable=Id(name="y"),varDimen=[],varInit=None),
                            VarDecl(variable=Id(name="z"),varDimen=[],varInit=None),
                            VarDecl(variable=Id(name="a"),varDimen=[],varInit=None),
                            VarDecl(variable=Id(name="b"),varDimen=[],varInit=None),
                            VarDecl(variable=Id(name="c"),varDimen=[],varInit=None),
                        ],
                        [
                            If(
                                ifthenStmt=
                                [
                                    (BinaryOp(op="=/=",left=Id(name="a"),right=FloatLiteral(value=100.0)),[],
                                    [
                                        For(
                                            idx1=Id(name="y"),
                                            expr1=IntLiteral(value=10),
                                            expr2=BinaryOp(op="<.",left=Id(name="y"),right=FloatLiteral(value=1000.0)),
                                            expr3=BinaryOp(op="+.",left=Id(name="y"),right=FloatLiteral(value=10.0)),
                                            loop = ([],[Continue()])
                                        )
                                    ]),
                                    (BinaryOp(op=">=",left=Id(name="b"),right=IntLiteral(value=0x16)),
                                    [
                                        VarDecl(variable=Id(name="t"),varDimen=[],varInit=IntLiteral(value=1))
                                    ],
                                    [
                                        While(
                                            exp=BinaryOp(op="<=.",left=Id(name="a"),right=FloatLiteral(value=10.5)),
                                            sl=([],[Break()])
                                        )
                                    ])
                                    
                                ],
                                elseStmt=([],[])
                            )
                        ]
                    )
                )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,396))
    
    def test_program37(self):
        """ Test mix"""
        input = """
                Var: a,b=1,c=2.0,d=False,e="s",f[2]={0x2,0o7};
                Var: x[1][2] = {{1,"abc"},{True,1e2}};
                Function: main
                    Parameter: a,b[1],c[1][2]
                    Body:
                        Var: x, y,z;
                        Var: a,b,c;
                        (((a&&x)+(b||y))+func(x,y))[1+func(1+func()[1])]=1;
                    EndBody.
                    """
        expect = Program(
            [
                VarDecl(variable=Id(name="a"),varDimen=[],varInit=None),
                VarDecl(variable=Id(name="b"),varDimen=[],varInit=IntLiteral(value=1)),
                VarDecl(variable=Id(name="c"),varDimen=[],varInit=FloatLiteral(value=2.0)),
                VarDecl(variable=Id(name="d"),varDimen=[],varInit=BooleanLiteral(value=False)),
                VarDecl(variable=Id(name="e"),varDimen=[],varInit=StringLiteral(value="s")),
                VarDecl(variable=Id(name="f"),varDimen=[2],varInit=ArrayLiteral(value=[IntLiteral(value=0x2),IntLiteral(value=0o7)])),
                VarDecl(variable=Id(name="x"),varDimen=[1,2],varInit=ArrayLiteral(value=
                [
                    ArrayLiteral(value=[IntLiteral(value=1),StringLiteral(value="abc")]),
                    ArrayLiteral(value=[BooleanLiteral(value=True),FloatLiteral(value=1e2)])
                ])),
                FuncDecl(
                    name=Id(name="main"),
                    param=
                    [
                        VarDecl(variable=Id(name="a"),varDimen=[],varInit=None),
                        VarDecl(variable=Id(name="b"),varDimen=[1],varInit=None),
                        VarDecl(variable=Id(name="c"),varDimen=[1,2],varInit=None)
                    ],
                    body=(
                        [
                            VarDecl(variable=Id(name="x"),varDimen=[],varInit=None),
                            VarDecl(variable=Id(name="y"),varDimen=[],varInit=None),
                            VarDecl(variable=Id(name="z"),varDimen=[],varInit=None),
                            VarDecl(variable=Id(name="a"),varDimen=[],varInit=None),
                            VarDecl(variable=Id(name="b"),varDimen=[],varInit=None),
                            VarDecl(variable=Id(name="c"),varDimen=[],varInit=None),
                        ],
                        [
                            Assign(
                                lhs=ArrayCell(
                                    arr=BinaryOp(
                                        op="+",
                                        left=BinaryOp(
                                            op="+",
                                            left=BinaryOp(
                                                op="&&",
                                                left=Id(name="a"),
                                                right=Id(name="x")
                                            ),
                                            right=BinaryOp(
                                                op="||",
                                                left=Id(name="b"),
                                                right=Id(name="y")
                                            )
                                        ),
                                        right=CallExpr(method=Id(name="func"),param=[Id(name="x"),Id(name="y")])
                                    ),
                                    idx = [
                                        BinaryOp(
                                            op="+",
                                            left=IntLiteral(value=1),
                                            right=CallExpr(
                                                method=Id(name="func"),
                                                param=[
                                                    BinaryOp(
                                                        op="+",
                                                        left=IntLiteral(value=1),
                                                        right=ArrayCell(
                                                            arr=CallExpr(method=Id(name="func"),param=[]),
                                                            idx=[IntLiteral(value=1)]
                                                        )
                                                    )
                                                ]
                                            )
                                        )
                                    ]
                                ),
                                rhs=IntLiteral(value=1)
                            )
                        ]
                    )
                )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,397))
    def test_program38(self):
        """Text mix"""
        input = """
                Var: x = "include<stdio.h>";
                Function: main
                    Body:
                        cout("Moi ban nhap ten: ");
                        name = cin();
                        cout("Ten cua ban la:",name);
                        cout("Ban thay tui hay khong, tui biet duoc ten ban luon day nhe");
                        cout("Moi ban nhap tai khoan ngan hang cua ban");
                        acount = cin();
                        cout("Moi ban nhap mat khau ngan hang cua ban");
                        pswd = cin();
                        cout("Ban da bi hawchs, ha ha :))");
                        Return 1;
                    EndBody.
        """
        expect = Program([
            VarDecl(variable=Id(name="x"),varDimen=[],varInit=StringLiteral(value="include<stdio.h>")),
            FuncDecl(
                name=Id(name="main"),
                param=[],
                body = ([],
                [
                    CallStmt(method=Id(name="cout"),param=[StringLiteral(value="Moi ban nhap ten: ")]),
                    Assign(lhs=Id(name="name"),rhs=CallExpr(method=Id(name="cin"),param=[])),
                    CallStmt(method=Id(name="cout"),param=[StringLiteral(value="Ten cua ban la:"),Id(name="name")]),
                    CallStmt(method=Id(name="cout"),param=[StringLiteral(value="Ban thay tui hay khong, tui biet duoc ten ban luon day nhe")]),
                    CallStmt(method=Id(name="cout"),param=[StringLiteral(value="Moi ban nhap tai khoan ngan hang cua ban")]),
                    Assign(lhs=Id(name="acount"),rhs=CallExpr(method=Id(name="cin"),param=[])),
                    CallStmt(method=Id(name="cout"),param=[StringLiteral(value="Moi ban nhap mat khau ngan hang cua ban")]),
                    Assign(lhs=Id(name="pswd"),rhs=CallExpr(method=Id(name="cin"),param=[])),
                    CallStmt(method=Id(name="cout"),param=[StringLiteral(value="Ban da bi hawchs, ha ha :))")]),
                    Return(expr=IntLiteral(value=1))
                ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,398))
    
    def test_program39(self):
        """Complex program"""
        input = """
        Var: a, b, c;
        Var: x = 1, y[1] = 2;
        Function: doST
            Parameter: n, m
            Body:
                If x == True Then n = n % 2;
                ElseIf y >. 3.9 Then y = y \\. 2.4;
                Else c = -b;
                EndIf.
                For (i = 0, i < 10, 1) Do
                    a = b + 2;
                    x = y [1] * 3;
                EndFor.
                While c < 3 Do
                    c = c * 2;
                EndWhile.
                Return (n + m * c);
            EndBody."""
        expect = Program(decl=[
            VarDecl(variable=Id(name="a"),varDimen=[],varInit=None),
            VarDecl(variable=Id(name="b"),varDimen=[],varInit=None),
            VarDecl(variable=Id(name="c"),varDimen=[],varInit=None),
            VarDecl(variable=Id(name="x"),varDimen=[],varInit=IntLiteral(value=1)),
            VarDecl(variable=Id(name="y"),varDimen=[1],varInit=IntLiteral(value=2)),
            FuncDecl(name=Id(name="doST"),
            param=[
                VarDecl(variable=Id(name="n"),varDimen=[],varInit=None),
                VarDecl(variable=Id(name="m"),varDimen=[],varInit=None)
                ],
            body=([],[
                If(
                    ifthenStmt=[
                        (BinaryOp(op="==",left=Id(name="x"),right=BooleanLiteral(value=True)),[],
                        [Assign(lhs=Id(name="n"),rhs=BinaryOp(op="%",left=Id(name="n"),right=IntLiteral(value=2)))]),
                        (BinaryOp(op=">.",left=Id(name="y"),right=FloatLiteral(value=3.9)),[],
                        [Assign(lhs=Id(name="y"),rhs=BinaryOp(op="\\.",left=Id(name="y"),right=FloatLiteral(value=2.4)))])
                    ],
                    elseStmt=([],[Assign(lhs=Id(name="c"),rhs=UnaryOp(op="-",body=Id(name="b")))])),
                For(idx1=Id(name="i"),
                expr1=IntLiteral(value=0),
                expr2=BinaryOp(op="<",left=Id(name="i"),right=IntLiteral(value=10)),
                expr3=IntLiteral(value=1),
                loop=([],[
                    Assign(lhs=Id(name="a"),rhs=BinaryOp(op="+",left=Id(name="b"),right=IntLiteral(value=2))),
                    Assign(lhs=Id(name="x"),rhs=BinaryOp(op="*",left=ArrayCell(arr=Id(name="y"),idx=[IntLiteral(value=1)]),right=IntLiteral(value=3)))])),
                While(
                    exp=BinaryOp(op="<",left=Id(name="c"),right=IntLiteral(value=3)),
                    sl=([],[Assign(lhs=Id(name="c"),rhs=BinaryOp(op="*",left=Id(name="c"),right=IntLiteral(value=2)))])),
                Return(BinaryOp(op="+",left=Id(name="n"),right=BinaryOp(op="*",left=Id(name="m"),right=Id(name="c"))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,399))
    
    
    
    