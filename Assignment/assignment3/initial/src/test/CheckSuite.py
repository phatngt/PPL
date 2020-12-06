import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):

    def test_undeclared_function(self):
        """Simple test: Redeclare var"""
        input = """ Var: t;
                """
        expect = str(Redeclared(Variable(),"y"))
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_if_exp(self):
        """Simple test: Redeclare var"""
        input = """ Var: t;
                    Var: x = 11;
                    Function: main
                    Body:
                        For(x = 1, x >20, x + 1) Do
                            Var: w,z;
                            Var: a,b,c;
                        EndFor.
                    EndBody."""
        expect = str(Redeclared(Variable(),"y"))
        self.assertTrue(TestChecker.test(input,expect,401))

