
"""
 * @author nhphung
"""
from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List, Tuple
from AST import * 
from Visitor import *
from StaticError import *
from functools import *

class Type(ABC):
    __metaclass__ = ABCMeta
    pass
class Prim(Type):
    __metaclass__ = ABCMeta
    pass
class IntType(Prim):
    pass
class FloatType(Prim):
    pass
class StringType(Prim):
    pass
class BoolType(Prim):
    pass
class VoidType(Type):
    pass
class Unknown(Type):
    pass

@dataclass
class ArrayType(Type):
    dimen:List[int]
    eletype: Type

@dataclass
class MType:
    #input type
    intype:List[Type]
    #returns type
    restype:Type

@dataclass
class Symbol:
    name: str
    mtype:Type

class StaticChecker(BaseVisitor):
    def __init__(self,ast):
        self.ast = ast
        self.global_envi = [
Symbol("int_of_float",MType([FloatType()],IntType())),
Symbol("float_to_int",MType([IntType()],FloatType())),
Symbol("int_of_string",MType([StringType()],IntType())),
Symbol("string_of_int",MType([IntType()],StringType())),
Symbol("float_of_string",MType([StringType()],FloatType())),
Symbol("string_of_float",MType([FloatType()],StringType())),
Symbol("bool_of_string",MType([StringType()],BoolType())),
Symbol("string_of_bool",MType([BoolType()],StringType())),
Symbol("read",MType([],StringType())),
Symbol("printLn",MType([],VoidType())),
Symbol("printStr",MType([StringType()],VoidType())),
Symbol("printStrLn",MType([StringType()],VoidType()))]       

   
    def check(self):
        return self.visit(self.ast,self.global_envi)

    def visitProgram(self,ast, c):
        #Enviroment constrant of program
        prog_envi = c[:]
        # prog_envi = []
        entry_point = False
        for decl in ast.decl:
            if isinstance(decl,FuncDecl):
                if decl.name.name == 'main':
                    entry_point = True
            
        if not entry_point:
            raise NoEntryPoint()

        
        # Through the decls of program
        for decl in ast.decl:
            #Check vardecl in the program
            if isinstance(decl,VarDecl):
                prog_envi.append(self.visit(decl,prog_envi))
            
            if isinstance(decl,FuncDecl):
                #Check redeclare function
                if not self.lookup(decl.name.name,prog_envi,lambda x: x.name) is None:
                    raise Redeclared(k=Function(),n=decl.name.name)
                #Update global enviroment and unused function list
                else:
                    prog_envi.append(Symbol(name=decl.name.name,mtype=MType(intype=[],restype=Unknown())))
                    flag_global = True
                    self.visit(decl,([prog_envi],flag_global))
        for decl in ast.decl:
            if isinstance(decl,FuncDecl):
                if not self.lookup(decl.name.name, prog_envi,lambda x:x.name) is None:
                    flag_global  = False
                    self.visit(decl,([prog_envi],flag_global))


    def visitVarDecl(self,ast,c):
        """ Looking up variable has had already apreared in the global scope"""
        if self.lookup(ast.variable.name,c,lambda x : x.name) is None:
            """ Checking declartion had init value? """
            if ast.varInit and ast.varDimen == []:
                var_type = self.visit(ast.varInit,c)
                return Symbol(name=ast.variable.name,mtype=MType(intype=[],restype=var_type))
            """ Variable declaretion with no init value"""
            if not ast.varInit and ast.varDimen == []:
                return Symbol(name=ast.variable.name,mtype=MType(intype=[],restype=Unknown()))
            if ast.varDimen and not ast.varInit:
                array_dimen = ast.varDimen
                return Symbol(name=ast.variable.name,mtype=MType(intype=[],restype=ArrayType(dimen=array_dimen,eletype=Unknown())))
            if ast.varDimen and ast.varInit:
                arr_typ = self.visit(ast.varInit,c)
                return Symbol(name=ast.variable.name,mtype=MType(intype=[],restype=arr_typ))
        else:
            raise Redeclared(k=Variable(),n=ast.variable.name)
    
    def visitFuncDecl(self,ast,c):
        #Set up variable reference follow to: [[recently],[parent],[2nd parent(grand-dad)],[3th...] ]
        global_envi = c[0]
        flag_global = c[1]
        #Create lst of the local variable
        local_envi = []
        #Create lst of the parameter variable
        lst_param = []
        if flag_global:
            if ast.param:
                for param in ast.param:
                    #Check redeclare parameter
                    if self.lookup(param.variable.name,lst_param,lambda x: x.name) is None:
                        lst_param.append(self.visit(param,lst_param))
                    else:
                        raise Redeclared(k=Parameter(),n=param.variable.name)
            if lst_param != []:
                # Add lst parameter into function are visiting
                self.add_parafunc(ast.name.name,lst_param,[global_envi[-1]],lambda x: x.name)
                #Update local enviroment
                local_envi += lst_param
        else:
            func = self.lookup(ast.name.name,global_envi[-1],lambda x: x.name)
            local_envi += func.mtype.intype
            if ast.body[0]:
                # Visit all variable is declared in the var-decl block
                for var_decl in ast.body[0]:
                    local_envi += [self.visit(var_decl,local_envi)] 

            if ast.body[1]:
                for stm in ast.body[1]:
                    self.visit(stm,([local_envi]+global_envi,ast.name.name))

    def visitAssign(self,ast,c):
        self.ast = ast
        global_envi = c[0]
        #Get name of lhs, the type of lhs and rhs,with lsh is a id
        if isinstance(ast.lhs,Id):
            # Get name of the Id in lhs
            name_lhs = ast.lhs.name
            # Get symbol lhs
            lhs = self.visit(ast.lhs,global_envi)
            type_lhs = lhs
            if isinstance(lhs,Symbol):
                type_lhs = lhs.mtype.restype
            # Get symbol rhs
            rhs = self.visit(ast.rhs,global_envi)
            # Get type of the rhs(Symbol or type of Literals)
            type_rhs = rhs
            # If the rhs is a Mtype, re-get type of rhs and create name_rhs is the name of rhs
            if isinstance(rhs,Symbol):
                type_rhs = rhs.mtype.restype
                name_rhs = rhs.name
            if isinstance(type_rhs,ArrayType):
                type_rhs = type_rhs.eletype
        # In this case the lhs is the arraycell
        elif isinstance(ast.lhs, ArrayCell):
            #Get name of the lhs which it is id 
            if isinstance(ast.lhs.arr,Id):
                name_lhs = ast.lhs.arr.name
            #Get type of the lhs
            lhs = self.visit(ast.lhs,global_envi)
            if isinstance(lhs,Symbol):
                type_lhs = lhs.mtype.restype
                if isinstance(type_lhs,ArrayType):
                    type_lhs = type_lhs.eletype
            #Get type of the rhs
            rhs = self.visit(ast.rhs,global_envi)
            if isinstance(rhs,Symbol):
                type_rhs = rhs.mtype.restype
                name_rhs = rhs.name
            else:
                type_rhs = rhs
            if isinstance(type_rhs,ArrayType):
                type_rhs = type_rhs.eletype

            
            
        """ Check type of the lsh and type of rhs"""
        #If the lhs and rhs not are the same type
        if not (isinstance(type_lhs,VoidType) or isinstance(type_rhs,VoidType)):
            if not isinstance(type_lhs,type(type_rhs)):
                if (isinstance(type_lhs,ArrayType) and not isinstance(type_rhs,ArrayType)) or (not isinstance(type_lhs,ArrayType) and isinstance(type_rhs,ArrayType)):
                    raise TypeMismatchInStatement(ast)
                # If lhs is unknow type and rhs not is void type, inferer type for lhs
                elif isinstance(type_lhs,Unknown):
                    self.addtype(name_lhs,type_rhs,global_envi,lambda x: x.name)
                # If rhs is unknow type, and type of the lhs is resolved type, inferer type for rhs
                elif isinstance(type_rhs,Unknown):
                    self.addtype(name_rhs,type_lhs,global_envi,lambda x: x.name)
                # If the rhs the and lsh are resoleved type, but their are not the same type, raise exception 
                else:
                    raise TypeMismatchInStatement(ast)
            #If the lhs and rhs are the same type
            else:
                #If the lhs and the rhs are the unknow type together, raise exception
                if isinstance(type_lhs,Unknown) and isinstance(type_rhs,Unknown):
                    raise TypeCannotBeInferred(ast)
        else:
            raise TypeMismatchInStatement(ast)
        
        
        
        
    """ Visit the statments"""
    #Visit if statement
    def visitIf(self,ast,c):
        self.ast = ast
        global_envi = c[0]
        local_envi = []
        for ifthenstm in ast.ifthenStmt:
            expr = self.visit(ifthenstm[0],global_envi)
            type_expr = expr
            if isinstance(expr,Symbol):
                if isinstance(expr.mtype.restype,Unknown):
                    self.addtype(expr.name,BoolType(),global_envi,lambda x:x.name)
                    type_expr = BoolType()
                else:
                    type_expr = expr.mtype.restype
                    
            if isinstance(type_expr,BoolType):
                for var_decl in ifthenstm[1]:
                    local_envi.append(self.visit(var_decl,local_envi))
                for stm in ifthenstm[2]:
                    self.visit(stm,([local_envi]+global_envi,c[1]))
            else:
                raise TypeMismatchInStatement(ast)
        if ast.elseStmt:
            for var_decl in ast.elseStmt[0]:
                local_envi.append(self.visit(var_decl,local_envi))
            for stm in ast.elseStmt[1]:
                self.visit(stm,([local_envi]+global_envi,c[1]))
    #Visit for statement
    def visitFor(self,ast,c):
        self.ast = ast
        global_envi = c[0]
        local_envi = []
        idx1 = self.visit(ast.idx1,global_envi)
        type_idx1 = idx1.mtype.restype
        if not isinstance(type_idx1,IntType):
            if isinstance(type_idx1,Unknown):
                self.addtype(idx1.name,IntType(),global_envi,lambda x: x.name)
                type_idx1 = IntType()
            else:
                raise TypeMismatchInStatement(ast)
        if isinstance(type_idx1,IntType):
            expr1 = self.visit(ast.expr1,global_envi)
            type_expr1 = expr1
            if isinstance(expr1,Symbol):
                type_expr1 = expr1.mtype.restype
                if isinstance(type_expr1,Unknown):
                    self.addtype(expr1.name,IntType(),global_envi,lambda x: x.name)
                    type_expr1 = IntType()
            if not isinstance(type_expr1,IntType):
                raise TypeMismatchInStatement(ast)
            expr2 = self.visit(ast.expr2,global_envi)
            type_expr2 = expr2
            if isinstance(expr2,Symbol):
                type_expr2 = expr2.mtype.restype
                if isinstance(type_expr2,Unknown):
                    self.addtype(expr2.name,BoolType(),global_envi,lambda x: x.name)
                    type_expr2 = BoolType()
            if not isinstance(type_expr2,BoolType):
                raise TypeMismatchInStatement(ast)
            expr3 = self.visit(ast.expr3,global_envi)
            type_expr3 = expr3
            if isinstance(expr3,Symbol):
                type_expr3 = expr3.mtype.restype
                if isinstance(type_expr3,Unknown):
                    self.addtype(expr3.name,IntType(),global_envi,lambda x: x.name)
                    type_expr3 = IntType()
            if not isinstance(type_expr3,IntType):
                raise TypeMismatchInStatement(ast)
        
        for var_decl in ast.loop[0]:
            local_envi.append(self.visit(var_decl,local_envi))
        for stm in ast.loop[1]:
            self.visit(stm,([local_envi]+global_envi,c[1]))
    #Visit do-while stmt
    def visitDowhile(self,ast,c):
        self.ast = ast
        global_envi = c[0]
        local_envi = []
        expr = self.visit(ast.exp,global_envi)
        type_expr = expr
        if isinstance(expr,Symbol):
            if isinstance(expr.mtype.restype,Unknown):
                self.addtype(expr.name,BoolType(),global_envi,lambda x:x.name)
                type_expr = BoolType()
            else:
                type_expr = expr.mtype.restype
        if not isinstance(type_expr,BoolType):
            raise TypeMismatchInStatement(ast)
        else:
            for var_decl in ast.sl[0]:
                local_envi.append(self.visit(var_decl,local_envi))
            for stmt in ast.sl[1]:
                self.visit(stmt,([local_envi]+global_envi,c[1]))
    #Visit while stmt
    def visitWhile(self,ast,c):
        self.ast = ast
        global_envi = c[0]
        local_envi = []
        expr = self.visit(ast.exp,global_envi)
        type_expr = expr
        if isinstance(expr,Symbol):
            if isinstance(expr.mtype.restype,Unknown):
                self.addtype(expr.name,BoolType(),global_envi,lambda x:x.name)
                type_expr = BoolType()
            else:
                type_expr = expr.mtype.restype
        if not isinstance(type_expr,BoolType):
            raise TypeMismatchInStatement(ast)
        else:
            for var_decl in ast.sl[0]:
                local_envi.append(self.visit(var_decl,local_envi))
            for stmt in ast.sl[1]:
                self.visit(stmt,([local_envi]+global_envi,c[1]))
    # Visit func-call stmt
    def visitCallStmt(self,ast,c):
        global_envi = c[0]
        """Check the function had declared in the program  """ 
        if self.lookup(ast.method.name,global_envi[-1],lambda x: x.name) is None:
            raise Undeclared(Function(),ast.method.name)
        """Get symbol of the function statement """
        method = self.visit(ast.method,[global_envi[-1]])
        # Type of the function
        method_restype = method.mtype.restype
        #List type parameter in the function
        method_intype = method.mtype.intype
        
        """ Check number the elements between paramters and arguments"""
        if len(ast.param) != len(method_intype):
            raise TypeMismatchInStatement(ast)
        """ Inffering all the parameters  """
        # Visit all arg is passed into call stmt
        for idx,arg in enumerate(ast.param):
            #Get type of the arg
            type_arg = self.visit(arg,global_envi)
            if isinstance(type_arg,Symbol):
                type_arg = type_arg.mtype.restype
            # Check the type of parameter
            if isinstance(method_intype[idx].mtype.restype,Unknown) and  isinstance(type_arg,Unknown):
                raise TypeCannotBeInferred(ast)
            if isinstance(method_intype[idx].mtype.restype,Unknown) and (not isinstance(type_arg,Unknown)):
                self.add_type_parafunc(name_func=ast.method.name,name_para=method_intype[idx].name,para_type=type_arg,lst=global_envi[-1],func=lambda x: x.name)
            if not isinstance(type_arg,type(method_intype[idx].mtype.restype)):
                raise TypeCannotBeInferred(ast)
        """ Check return of the call-statement"""
        if isinstance(method_restype,Unknown):
            self.addtype(ast.method.name,VoidType(),[global_envi[-1]],lambda x: x.name)
        elif not isinstance(method_restype,VoidType):
            raise TypeMismatchInStatement(ast)
    #TODO: Implement return stmt
    def visitReturn(self,ast,c):
        method = c[1]
        global_envi = c[0]
        typ_method = self.lookup(method,global_envi[-1],lambda x: x.name)
        if ast.expr:
            expr = self.visit(ast.expr,global_envi)
            type_expr = expr.mtype.restype if isinstance(expr,Symbol) else expr
            if isinstance(typ_method.mtype.restype,Unknown) and not isinstance(type_expr,Unknown):
                self.addtype(method,type_expr,[global_envi[-1]],lambda x: x.name)
            elif isinstance(typ_method.mtype.restype,Unknown) and isinstance(type_expr,Unknown):
                raise TypeCannotBeInferred(ast)
            else:
                raise TypeMismatchInStatement(ast)
        else:
            self.addtype(method,VoidType(),[global_envi[-1]],lambda x: x.name)

    def visitContinue(self,ast,c):
        pass
    def visitBreak(self,ast,c):
        pass
    
    """ Visit operators"""
    def visitBinaryOp(self,ast,c):
        op = ast.op
        left = self.visit(ast.left,c)
        right = self.visit(ast.right,c)
        left_type = left.mtype.restype if isinstance(left,Symbol) else left
        right_type = right.mtype.restype if isinstance(right,Symbol) else right
        if isinstance(left_type,ArrayType) and isinstance(left,Symbol):
            left_type = left_type.eletype
        if isinstance(right_type,ArrayType) and isinstance(right,Symbol):
            right_type = right_type.eletype
        def checkType(acceptType): 
            if not isinstance(left_type,acceptType) and not isinstance(left_type,Unknown):
                raise TypeMismatchInExpression(ast)
            elif not isinstance(right_type,acceptType) and not isinstance(right_type,Unknown):
                raise TypeMismatchInExpression(ast)
            if not isinstance(left_type,Unknown) and not isinstance(right_type,Unknown):
                if not (isinstance(left_type,acceptType) and isinstance(right_type,acceptType)):
                    raise TypeMismatchInExpression(ast)
        
        def infferedType(type_inffer):
            if isinstance(left_type,Unknown):
                self.addtype(left.name,type_inffer,c,lambda x: x.name)
            if isinstance(right_type,Unknown):
                self.addtype(right.name,type_inffer,c,lambda x: x.name)

        if op in ["+","-","*","\\","%"]:
            checkType(IntType)
            infferedType(IntType())
            return IntType()
        elif op in ["+.","-.","*.","\\."]:
            checkType(FloatType)
            infferedType(FloatType())
            return FloatType()
        elif op in ["&&","||"]:
            checkType(BoolType)
            infferedType(BoolType())
            return BoolType()
        elif op in ["==","!=","<",">","<=",">="]:
            checkType(IntType)
            infferedType(IntType())
            return BoolType()
        elif op in ["=/=","<.",">.","<=.",">=."]:
            checkType(FloatType)
            infferedType(FloatType())
            return BoolType()

    def visitUnaryOp(self,ast,c):
        op = ast.op
        body = self.visit(ast.body,c)
        body_type = body
        if isinstance(body,Symbol):
            body_type = body.mtype.restype
        if isinstance(body_type,ArrayType):
            body_type = body_type.eletype
        def checkType(acceptType):
            if not isinstance(body_type,Unknown):
                if not isinstance(body_type,acceptType):
                    raise TypeMismatchInExpression(ast)
        def infferedType(type_inffer):
            if isinstance(body_type,Unknown):
                self.addtype(body.name,type_inffer,c,lambda x: x.name)
        if op == "-":
            checkType(IntType)
            infferedType(IntType())
            return IntType()
        if op == "-.":
            checkType(FloatType)
            infferedType(FloatType())
            return FloatType()
        if op == "!":
            checkType(BoolType)
            infferedType(BoolType())
            return BoolType()
        
    """ Visit identifier"""
    def visitId(self,ast,c):
        for ele in c:
            id_symbol = self.lookup(ast.name,ele,lambda x : x.name)
            if not id_symbol is None:
                break
        if id_symbol is None:
            raise Undeclared(k=Identifier(),n=ast.name)
        else:
            return id_symbol
    
    """Visit array cell """

    def visitArrayCell(self,ast,c):
        global_envi = c
        arr_sym = self.visit(ast.arr,c)
        type_expr = arr_sym
        if isinstance(arr_sym,Symbol):
            type_expr = arr_sym.mtype.restype
        if not isinstance(type_expr,ArrayType):
            raise TypeMismatchInExpression(ast)
        dimen = type_expr.dimen
        if dimen:
            if len(dimen) != len(ast.idx):
                raise TypeMismatchInExpression(ast)
        
        for exp in ast.idx:
            type_idx = self.visit(exp,c)
            if not isinstance(type_idx,IntType):
                raise TypeMismatchInExpression(ast)
        return arr_sym

    """Visit Call Expr"""
    def visitCallExpr(self,ast,c):
        global_envi = c
        method = self.lookup(ast.method.name,global_envi[-1],lambda x: x.name)
        if method is None:
            raise Undeclared(Function(),ast.method.name)
        typ_method = method.mtype.restype 
        typ_param = method.mtype.intype
        #Check len between arg and param
        if len(typ_param) != len(ast.param):
            raise TypeMismatchInExpression(ast)
        for idx,arg in enumerate(ast.param):
            typ_arg = self.visit(arg,c)
            p_type = typ_param[idx]
            if isinstance(typ_arg,Symbol):
                typ_arg = typ_arg.mtype.restype
            if isinstance(typ_arg,ArrayType):
                typ_arg = typ_arg.eletype
            if isinstance(typ_param[idx],Symbol):
                p_type = typ_param[idx].mtype.restype
            if isinstance(p_type,ArrayType):
                p_type = p_type.eletype
            if isinstance(p_type,Unknown) and isinstance(typ_arg,Unknown):
                raise TypeCannotBeInferred(self.ast)
            elif isinstance(p_type,Unknown) and not isinstance(typ_arg,Unknown):
                self.addtype(typ_param[idx].name,typ_arg,[global_envi[-1]],lambda x:x.name)
            elif not isinstance(p_type,type(typ_arg)):
                raise TypeMismatchInExpression(ast)
        return method
  
    """ Some case of the array type:
        Var: a[1][2] = {1} => Error: dimen not equal to num lit
        Var: a[3] = {1,2,True}=> Error: Literals not the same type
        Var: a[1][2] = {{1,2}} => Successfully
        Var: a[1][2] = {{}} => Error: The nest array not contains literrals
        Var: """
    """ Visit literals"""
    #TODO: Fix some feature
    def visitArrayLiteral(self,ast,c):
        global_envi = c
        lst_dimen = []
        ele_type = Unknown()    
        while isinstance(ast.value, List):
            lst_dimen.append(len(ast.value))
            ast = ast.value[0]
        ele_type = self.visit(ast, global_envi)
        return ArrayType(lst_dimen, ele_type)

    def visitIntLiteral(self,ast,c):
        return IntType()
    def visitFloatLiteral(self,ast,c):
        return FloatType()
    def visitBooleanLiteral(self,ast,c):
        return BoolType()
    def visitStringLiteral(self,ast,c):
        return StringType()

    """ Support functions """
    def lookup(self,name,lst,func):
        # print(lst)
        for x in lst:
            if name == func(x):
                return x
        return None
    def addtype(self,name,typ,lst,func):
        flag = False
        for x in lst:
            for sym in x:
                if name == func(sym):
                    if isinstance(sym.mtype.restype,ArrayType):
                        sym.mtype.restype.eletype = typ
                    else:
                        sym.mtype.restype = typ
                    flag = True
                    break
            if flag: break
    def add_parafunc(self,name,lst_para,lst,func):
        for x in lst[-1]:
            if name == func(x):
                x.mtype.intype = lst_para
                break
    def add_type_parafunc(self,name_func,name_para,para_type,lst,func):
        flag = False
        if not self.lookup(name_func,lst,lambda x: x.name) is None:
            for sym in lst:
                if name_func == func(sym):
                    for in_type in sym.mtype.intype:
                        if in_type.name == name_para:
                            if isinstance(in_type.mtype.restype,ArrayType):
                                in_type.mtype.restype.eletype = typ
                            else:
                                in_type.mtype.restype = para_type
                            flag = True
                            break
                if flag: break
    
