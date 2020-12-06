
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
Symbol("float_of_int",MType([IntType()],FloatType())),
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
        # prog_envi = c[:]
        prog_envi = []
        
        # Through the decls of program
        for decl in ast.decl:
            
            #Check vardecl in the program
            if isinstance(decl,VarDecl):
                prog_envi.append(self.visit(decl,prog_envi))
            
            elif isinstance(decl,FuncDecl):
                #Check redeclare function
                if not self.lookup(decl.name.name,prog_envi,lambda x: x.name) is None:
                    raise Redeclared(k=Function(),n=decl.name.name)
                #Update global enviroment and unused function list
                # param_type = [self.visit(param,None) for param in decl.param]
                else:
                    prog_envi += [Symbol(name=decl.name.name,mtype=MType(intype=[],restype=Unknown()))]
                    self.visit(decl,[prog_envi])

        

    def visitVarDecl(self,ast,c):
        """ Looking up variable has had already apreared in the global scope"""
        if self.lookup(ast.variable.name,c,lambda x : x.name) is None:
            """ Checking declartion had init value? """
            if ast.varInit and not ast.varDimen:
                varType = self.visit(ast.varInit,c)
                return Symbol(name=ast.variable.name,mtype=MType(intype=[],restype=varType))
            """ Variable declaretion with no init value"""
            if not (ast.varInit and ast.varDimen):
                return Symbol(name=ast.variable.name,mtype=MType(intype=[],restype=Unknown()))
        else:
            raise Redeclared(k=Variable(),n=ast.variable.name)
    
    def visitFuncDecl(self,ast,c):
        #Set up variable reference follow to: [[recently],[parent],[2nd parent(grand-dad)],[3th...] ]
        #Create lst of the local variable
        local_envi = []
        if ast.param:
            for param in ast.param:
                #Check redeclare parameter
                if self.lookup(param.variable.name,local_envi,lambda x: x.name) is None:
                    local_envi.append(self.visit(param,local_envi))
                else:
                    raise Redeclared(k=Parameter(),n=param.variable.name)
        
        if ast.body[0]:
            for var_decl in ast.body[0]:
                local_envi += [self.visit(var_decl,local_envi)] 

        if ast.body[1]:
            for stm in ast.body[1]:
                self.visit(stm,[local_envi]+c) 

    def visitAssign(self,ast,c):
        #Get name of lhs, the type of lhs and rhs,with lsh is a id
        if isinstance(ast.lhs,Id):
            name_lhs = ast.lhs.name
            type_lhs = self.visit(ast.lhs,c)
            type_rhs = self.visit(ast.rhs,c)
            print(typ)
            # If the rhs is a Mtype, re-get type of rhs and create name_rhs is the name of rhs
            if isinstance(type_rhs,MType):
                type_rhs = type_rhs.restype
                name_rhs = ast.rhs.name
        #Get name of lhs, with lhs is a arraycell
        elif isinstance(ast.lhs, ArrayCell):
            if isinstance(ast.arr,Id):
                name_lhs = ast.arr.name
        
        
        """Get name of rhs"""
        #If ast.rhs is idenfitier
        # if isinstance(ast.rhs,Id):
        #     name_rhs = ast.rhs.name
        
        """ Check type of the lsh and type of rhs"""
        #If the lhs and rhs not are the same type
        if not isinstance(type_lhs.restype,type(type_rhs)):
            # If lhs is unknow type and rhs not is void type, inferer type for lhs
            if isinstance(type_lhs.restype,Unknown):
                self.addtype(name_lhs,type_rhs,c,lambda x: x.name)
            # If rhs is unknow type, and type of the lhs is resolved type, inferer type for rhs
            elif isinstance(type_rhs,Unknown):
                self.addtype(name_rhs,type_lhs.restype,c,lambda x: x.name)
            # If the rhs the and lsh are resoleved type, but their are not the same type, raise exception 
            else:
                raise TypeMismatchInStatement(ast)
        #If the lhs and rhs are the same type
        else:
            #If the lhs and the rhs are the unknow type together, raise exception
            if isinstance(type_lhs.restype,Unknown) and isinstance(type_rhs,Unknown):
                raise TypeCannotBeInferred(ast)
            
    
        
            
    def visitIf(self,ast,c):
        # print(c)
        local_envi = []
        for ifthenstm in ast.ifthenStmt:
            expr = self.visit(ifthenstm[0],[local_envi]+c)
            if isinstance(expr,BoolType):
                for var_decl in ifthenstm[1]:
                    local_envi.append(self.visit(var_decl,local_envi))
                for stm in ifthenstm[2]:
                    self.visit(stm,[local_envi]+c)
            else:
                raise TypeMismatchInStatement(ast)
        if ast.elseStmt:
            for var_decl in ast.elseStmt[0]:
                local_envi.append(self.visit(var_decl,local_envi))
            for stm in ast.elseStmt[1]:
                self.visit(stm,[local_envi]+c)
        # print([local_envi]+c)

    def visitFor(self,ast,c):
        local_envi = []
        idx1 = self.visit(ast.idx1,c)
        if not isinstance(idx1.restype,IntType):
            raise TypeMismatchInStatement(ast)
        else:
            expr1 = self.visit(ast.expr1,c)
            if not isinstance(expr1,IntType):
                raise TypeMismatchInStatement(ast)
            expr2 = self.visit(ast.expr2,c)
            if not isinstance(expr2,BoolType):
                raise TypeMismatchInStatement(ast)
            expr3 = self.visit(ast.expr3,c)
            if not isinstance(expr3,IntType):
                raise TypeMismatchInStatement(ast)
        
        for var_decl in ast.loop[0]:
            local_envi.append(self.visit(var_decl,local_envi))
        for stm in ast.loop[1]:
            self.visit(stm,[local_envi]+c)
        print([local_envi]+c)
        

    """ Visit operators"""
    def visitBinaryOp(self,ast,c):
        op = ast.op
        left_type = self.visit(ast.left,c)
        right_type = self.visit(ast.right,c)
        def checkType(acceptType):
            left = left_type.restype if isinstance(left_type,MType) else left_type
            right = right_type.restype if isinstance(right_type,MType) else right_type
            
            """ Note: IF expression can be inferred to some type, example is (x + y) is left,
                x and y is resolved the type=> Can be inffered the expression. But, either theirs 
                cannot is resolved type, will be raised exception not inferred"""
            if isinstance(left,Unknown) or isinstance(right,Unknown):
                raise TypeCannotBeInferred(ast)
            
            elif not isinstance(left,acceptType) or not isinstance(right,acceptType):
                raise TypeMismatchInExpression(ast)

        if op in ["+","-","*","\\","%"]:
            checkType(IntType)
            return IntType()
        elif op in ["+.","-.","*.","\\."]:
            checkType(FloatType)
            return FloatType()
        elif op in ["&&","||"]:
            checkType(BoolType)
            return BoolType()
        elif op in ["==","!=","<",">","<=",">="]:
            checkType(IntType)
            return BoolType()
        elif op in ["=/=","<.",">.","<=.",">=."]:
            checkType(FloatType)
            return BoolType()

    def visitUnaryOp(self,ast,c):
        op = ast.op
        body = self.visit(ast.body,c)

        def checkType(acceptType):
            if not isinstance(body,acceptType):
                raise TypeMismatchInExpression(ast)
        if op == "-":
            checkType(IntType)
            return IntType()
        if op == "-.":
            checkType(FloatType)
            return FloatType()


    
        
    """ Visit identifier"""
    def visitId(self,ast,c):
        for ele in c:
            id_symbol = self.lookup(ast.name,ele,lambda x : x.name)
            if not id_symbol is None:
                break
        if id_symbol is None:
            raise Undeclared(k=Identifier(),n=ast.name)
        else:
            return id_symbol.mtype
    

    """ Visit literals"""
    def visitArrayLiteral(self,ast,c):
        pass

    def visitIntLiteral(self,ast,c):
        return IntType()
    def visitFloatLiteral(self,ast,c):
        return FloatType()
    def visitBooleanLiteral(self,ast,c):
        return BoolType()
    def visitStringLiteral(self,ast,c):
        return StringType()

    """ Support functions """
    def addtype(self,name,typ,lst,func):
        flag = False
        for x in lst:
            for sym in x:
                if name == func(sym):
                    sym.mtype.restype = typ
                    flag = True
                    break
            if flag: break

    def lookup(self,name,lst,func):
        for x in lst:
            if name == func(x):
                return x
        return None
    






        
