import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):

    def test_undeclared_function(self):
        """Simple test: Redeclare var"""
        input = """ Var: t;
                    Var: x = 1.1;
                    Function: main
                    Body:
                        Var:y;
                         y = x +. 2;
                    EndBody."""
        expect = str(Redeclared(Variable(),"y"))
        self.assertTrue(TestChecker.test(input,expect,400))
