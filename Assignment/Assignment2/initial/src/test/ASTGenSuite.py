import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """a := b := 4 := 5"""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

 
   