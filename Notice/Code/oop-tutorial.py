from abc import ABC
class O:
    pass
class A(O):
    def foo(self,x:int):
        print(x)
class B(O):
    pass
class C(O):
    def foo(self,x:int):
        print(x+1)
class D(A,B,O):
    pass
class E(C,A,O):
    pass
class F(D,E,C,A,B,O):
    pass
class Relation:
    def __init__(self,n:int = 0,d:int = 1):
        if d == 0:
            raise SystemExit("d == 0")
        else:
            self.n = n
            self.d = d
            self.__g = self.__gcd(n,d)
            self.numer = n//self.__g
            self.denom = d//self.__g
    
    def __gcd(self,a:int,b:int):
        if b == 0:
            return a
        else:
            return self.__gcd(b,a % b)
    def add(self,that):
        if isinstance(that,int):
            return self + Relation(that)
        else:
            return Relation(self.numer*that.denom + that.numer*self.denom,self.denom*that.denom)
    def __str__(self):
        return str(self.numer)+ '/' + str(self.denom)

class Expr(ABC):
    pass
class Var(Expr):
    def __init__(self,name:str):
        self.name = name
class Number(Expr):
    def __init__(self,num:str):
        self.num = num
    def print(self):
        print(self.num)
class UnOp(Expr):
    def __init__(self,operator:str,arg:Expr):
        self.operator = operator
        self.arg = arg
class BinOp(Expr):
    def __init__(self,operator:str,left:Expr,right:Expr):
        self.operator = operator
        self.left = left
        self.right = right
    def eval(self):
        if self.operator == "+":
            return Number(self.left + self.right)
        if self.operator == "-":
            return Number(self.left - self.right)
        if self.operator == "*":
            return Number(self.left * self.right)
        if self.operator == "/":
            return Number(self.left / self.right)
        
if __name__ == "__main__":
    t = BinOp('*',1.2,3)
    t.eval().print()
    