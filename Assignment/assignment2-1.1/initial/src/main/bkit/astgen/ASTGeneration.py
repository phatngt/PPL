from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *

class ASTGeneration(BKITVisitor):
    #Visit program block
    def visitProgram(self,ctx:BKITParser.ProgramContext):
        declist = list()
        for x in ctx.declaration():
            decl = self.visitDeclaration(x)
            if isinstance(decl,list):
                declist.extend(decl)
            else:
                declist.append(decl)
        return Program(decl=declist)
    
    def visitDeclaration(self,ctx:BKITParser.DeclarationContext):
        return self.visitChildren(ctx)
    
    #Visit declaration block
    def visitVardeclare(self,ctx:BKITParser.VardeclareContext):
        varlist = self.visit(ctx.varlist())
        return [VarDecl(variable=Id(params[0]),varDimen=params[1],varInit=params[2]) for params in varlist]
    
    def visitVarlist(self,ctx:BKITParser.VarlistContext):
        return [self.visit(x) for x in ctx.varinit()] 
    
    def visitVarinit(self,ctx:BKITParser.VarinitContext):
        if ctx.ASSIGN():
            return self.visit(ctx.var())+[self.visit(x) for x in ctx.valuelist()]
        else:
            return self.visit(ctx.var()) + [None]

    def visitValuelist(self,ctx:BKITParser.ValuelistContext):
        return self.visit(ctx.litlist())

    def visitLitlist(self,ctx:BKITParser.LitlistContext):
        if ctx.INTLIT():
            return IntLiteral(value=int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(value=float(ctx.FLOATLIT().getText()))
        elif ctx.TRUE():
            return BooleanLiteral(value=True)
        elif ctx.FALSE():
            return  BooleanLiteral(value=False)
        elif ctx.STRINGLIT():
            return StringLiteral(value=ctx.STRINGLIT().getText())
        elif ctx.arraylist():
            return self.visit(ctx.arraylist())

    def visitArraylist(self,ctx:BKITParser.ArraylistContext):
        # print(ctx.litlist())
        if ctx.litlist():
            return ArrayLiteral(value=[self.visit(x) for x in ctx.litlist()])
        else:
            return ArrayLiteral(value=[]) ###

    def visitVar(self,ctx:BKITParser.VarContext):
        if ctx.INTLIT():
            return [ctx.ID().getText(),[int(x.getText()) for x in ctx.INTLIT()]]
        else:
            return [ctx.ID().getText(),[]]
    #Visit function block
    def visitFuncdeclare(self,ctx:BKITParser.FuncdeclareContext):   
        id = Id(ctx.ID().getText())
        lst = [self.visit(ctx.paralist()),self.visit(ctx.blockstm())] if ctx.paralist() else [[],self.visit(ctx.blockstm())]
        print(id,lst[1])
        return FuncDecl(name=id,param=lst[0],body=lst[1])
    
    def visitParalist(self,ctx:BKITParser.ParalistContext):
        lst = [(self.visit(x)) for x in ctx.var()]
        # print(lst)
        return [VarDecl(variable=Id(x[0]),varDimen=x[1],varInit=None) for x in lst]
    
    def visitBlockstm(self,ctx:BKITParser.BlockstmContext):
        return self.visit(ctx.var_decl_and_stm())
    
    def visitVar_decl_and_stm(self,ctx:BKITParser.Var_decl_and_stmContext):
        return ([self.visit(x) for x in ctx.vardeclare()],[self.visit(x) for x in ctx.stm()])
    
    def visitStm(self,ctx:BKITParser.StmContext):
        return self.visitChildren(ctx)
    
    #Visit statements
    
    
    def visitAssign_stm(self,ctx:BKITParser.Assign_stmContext):
        if ctx.ID():
            lhs = ctx.ID().getText()
        elif ctx.exp6():
            lhs = self.visit(ctx.exp6())
        rhs = self.visit(ctx.exp())
        return Assign(lhs=lhs,rhs=rhs)
    
    def visitFor_stm(self,ctx:BKITParser.For_stmContext):
        idx1 = Id(ctx.ID().getText())
        expr1 = self.visit(ctx.exp(0))
        expr2 = self.visit(ctx.exp(1))
        expr3 = self.visit(ctx.exp(2))
        loop = self.visit(ctx.var_decl_and_stm())
        return For(idx1=idx1,expr1=expr1,expr2=expr2,expr3=expr3,loop=loop)

    
    def visitIf_stm(self,ctx:BKITParser.If_stmContext):
        ifthenStmt = [(self.visit(ctx.exp(i)),self.visit(ctx.var_decl_and_stm(i))[0],self.visit(ctx.var_decl_and_stm(i))[1]) for i in range(len(ctx.exp()))]
        elseStmttemp = [self.visit(ctx.var_decl_and_stm(i)) for i in range(len(ctx.exp()),len(ctx.var_decl_and_stm()))][0]
        elseStmt = (elseStmttemp[0],elseStmttemp[1])
        return If(ifthenStmt=ifthenStmt,elseStmt=elseStmt)

    def visitWhile_stm(self,ctx:BKITParser.While_stmContext):
        exp = self.visit(ctx.exp())
        sl = self.visit(ctx.var_decl_and_stm())
        return While(exp=exp,sl=sl)
    
    def visitDo_while_stm(self,ctx:BKITParser.Do_while_stmContext):
        sl = self.visit(ctx.var_decl_and_stm())
        exp = self.visit(ctx.exp())
        return Dowhile(sl=sl,exp=exp)

    def visitReturn_stm(self,ctx:BKITParser.Return_stmContext):
        if ctx.exp():
            exp = self.visit(ctx.exp())
            return Return(expr=exp)
        return None
    
    def visitContinue_stm(self,ctx:BKITParser.Continue_stmContext):
        return Continue()
    
    def visitBreak_stm(self,ctx:BKITParser.Break_stmContext):
        return Break()

    def visitCallfunc_stm(self,ctx:BKITParser.Callfunc_stmContext):
        call_func = self.visit(ctx.call_func())
        print(call_func)
        id = call_func[0]
        lstexp = call_func[1]
        return CallStmt(method=id,param=lstexp)
    
    #Visit temp Parser
    def visitCall_func(self,ctx:BKITParser.Call_funcContext):
        lstexp = [self.visit(x) for x in ctx.exp()] if ctx.exp() else []
        id = ctx.ID().getText()
        return (id,lstexp)
    
    #Visit expression block
    def visitExp(self,ctx:BKITParser.ExpContext):
        if ctx.EQ():
            op = ctx.EQ().getText()
        elif ctx.INEQ():
            op = ctx.INEQ().getText() 
        elif ctx.ILT():
            op = ctx.ILT().getText()
        elif ctx.IGT():
            op = ctx.IGT().getText()
        elif ctx.ILTOEQ():
            op = ctx.ILTOEQ().getText()
        elif ctx.IGTOEQ():
            op = ctx.IGTOEQ().getText()
        elif ctx.FNEQ():
            op = ctx.FNEQ().getText()
        elif ctx.FLT():
            op = ctx.FLT().getText()
        elif ctx.FGLT():
            op = ctx.FGLT().getText()
        elif ctx.FLTOEQ():
            op = ctx.FLTOEQ().getText()
        elif ctx.FGTOEQ():
            op = ctx.FGTOEQ().getText()                   
        else:
            return self.visit(ctx.exp1(0))   
        left = self.visit(ctx.exp1(0))
        right = self.visit(ctx.exp1(1))
        return BinaryOp(op=op,left=left,right=right)
        
    def visitExp1(self,ctx:BKITParser.Exp1Context):
        if ctx.AND():
            op = ctx.AND().getText()
        elif ctx.OR():
            op = ctx.OR().getText()
        else:
            return self.visit(ctx.exp2())
        left = self.visit(ctx.exp1())
        right = self.visit(ctx.exp2())
        return BinaryOp(op=op,left=left,right=right)

    def visitExp2(self,ctx:BKITParser.Exp2Context):
        if ctx.INTADD():
            op = ctx.INTADD().getText()
        elif ctx.FLOATADD():
            op = ctx.FLOATADD().getText()
        elif ctx.INTSIGNNEG():
            op = ctx.INTSIGNNEG().getText()
        elif ctx.FLOATSIGNNEG():
            op = ctx.FLOATSIGNNEG().getText()
        else:
            return self.visit(ctx.exp3())
        left = self.visit(ctx.exp2())
        right = self.visit(ctx.exp3())
        return BinaryOp(op=op,left=left,right=right)
    
    def visitExp3(self,ctx:BKITParser.Exp3Context):
        if ctx.INTMUL():
            op = ctx.INTMUL().getText()
        elif ctx.FLOATMUL():
            op = ctx.FLOATMUL().getText()
        elif ctx.INTDIV():
            op = ctx.INTDIV().getText()
        elif ctx.FLOATDIV():
            op = ctx.FLOATDIV().getText()
        elif ctx.INTREM():
            op = ctx.INTREM().getText()
        else:
            return self.visit(ctx.exp4())
        left = self.visit(ctx.exp3())
        right = self.visit(ctx.exp4())
        return BinaryOp(op=op,left=left,right=right)

    def visitExp4(self,ctx:BKITParser.Exp4Context):
        if ctx.NEG():
            op = ctx.NEG().getText()
            body = self.visit(ctx.exp4())
            return UnaryOp(op=op,body=body)
        else:
            return self.visit(ctx.exp5())

    def visitExp5(self,ctx:BKITParser.Exp5Context):
        if ctx.INTSIGNNEG():
            op = ctx.INTSIGNNEG().getText()
        elif ctx.FLOATSIGNNEG():
            op = ctx.FLOATSIGNNEG().getText()
        else:
            return self.visit(ctx.exp6())
        body = self.visit(ctx.exp5())
        return UnaryOp(op=op,body=body)

    def visitExp6(self,ctx:BKITParser.Exp6Context):
        if ctx.LSB():
            arr = self.visit(ctx.exp6())
            idx = [self.visit(x) for x in ctx.exp()]
            return ArrayCell(arr=arr,idx=idx)
        return self.visit(ctx.exp7())

    def visitExp7(self,ctx:BKITParser.Exp7Context):
        if ctx.ID() and ctx.LPAREN():
            lstexp = [self.visit(x) for x in ctx.exp()] if ctx.exp() else []
            id = ctx.ID().getText()
            return CallStmt(method=id,param=lstexp)
        return self.visit(ctx.exp8())

    def visitExp8(self,ctx:BKITParser.Exp8Context):
        if ctx.LPAREN():
            return self.visit(ctx.exp())
        return self.visit(ctx.operand())

    def visitOperand(self,ctx:BKITParser.OperandContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        return self.visit(ctx.litlist())


    

