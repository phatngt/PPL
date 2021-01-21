from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *

class ASTGeneration(BKITVisitor):

    def visitProgram(self,ctx:BKITParser.ProgramContext):
        exp = self.visit(ctx.exp())
        return exp

    def visitExp(self,ctx:BKITParser.ExpContext):
        result = None
        if ctx.ASSIGN():
            for i in range(len(ctx.term())-1):
                op = ctx.ASSIGN()[-(i+1)].getText()
                left = self.visit(ctx.term()[-(i+2)])
                right = self.visit(ctx.term()[-1])
                if not result:
                    result = Binary(op,left,right)
                else:
                    result = Binary(op,left,result)
            return result
        else:
            return self.visit(ctx.term()[-1])

    def visitTerm(self,ctx:BKITParser.TermContext): 
        if ctx.COMPARE():
            op = ctx.COMPARE().getText()
            left = self.visit(ctx.factor(0))
            right = self.visit(ctx.factor(1))
            return Binary(op,left,right)
        else:
            return self.visit(ctx.factor(0))

    def visitFactor(self,ctx:BKITParser.FactorContext):
        result = None
        if ctx.ANDOR():
            for i in range(2,len(ctx.operand())):
                op = ctx.ANDOR()[i-2].getText()
                left = self.visit(ctx.operand()[-i])
                right = self.visit(ctx.operand()[-1])
                if not result:
                    result = Binary(op,left,right)
                else:
                    result = Binary(op,left,result)
        else:
            return self.visit(ctx.operand()[-1])

    def visitOperand(self,ctx:BKITParser.OperandContext):
        if ctx.ID():
            id = ctx.ID().getText()
            return Id(id)
        if ctx.INTLIT():
            intlit = ctx.INTLIT().getText()
            return IntLiteral(int(intlit))
        if ctx.BOOLIT():
            bol = ctx.BOOLIT().getText()
            return BooleanLiteral(bool(bol))
        else:
            self.visit(ctx.exp())

    

