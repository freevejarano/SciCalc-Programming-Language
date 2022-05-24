from gramVisitor import gramVisitor
from gramParser import gramParser

import math

class MyVisitor(gramVisitor):
    def __init__(self):
        self.memory = {}

    def visitAssign(self, ctx):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[name] = value
        return value

    def visitPrintExpr(self, ctx):
        value = self.visit(ctx.expr())
        print(value)
        return 0

    def visitNum(self, ctx):
        return ctx.NUM().getText()

    def visitBool(self, ctx):
        return ctx.BOOL().getText()

    def visitArray(self, ctx):
        valor = ctx.arreglo()
        characters = "[],"
        values = []
        for i in valor:
            aux = i.getText()
            string = ''.join( x for x in aux if x not in characters)
            values.append(string)
        return values

    def visitId(self, ctx):
        name = ctx.ID().getText()
        if name in self.memory:
            return self.memory[name]
        else:
            if name == "True" or "False":
                return name
            else:
                return 0

    def visitMulDiv(self, ctx):
        left = float(self.visit(ctx.expr(0)))
        right = float(self.visit(ctx.expr(1)))
        if ctx.op.type == gramParser.MUL:
            return left * right
        else:
            if right == 0.0:
                return "División por cero"
            else:
                return left / right

    def visitAddSub(self, ctx):
        left = float(self.visit(ctx.expr(0)))
        right = float(self.visit(ctx.expr(1)))
        if ctx.op.type == gramParser.ADD:
            return left + right
        return left - right
    
    def visitMod(self, ctx):
        left = float(self.visit(ctx.expr(0)))
        right = float(self.visit(ctx.expr(1)))
        return left%right
    
    def visitPow(self, ctx):
        left = float(self.visit(ctx.expr(0)))
        right = float(self.visit(ctx.expr(1)))
        return left**right
    
    def visitSqrt(self, ctx):
        left = float(self.visit(ctx.expr(0)))
        right = float(self.visit(ctx.expr(1)))
        if right == 0.0:
            return "Operación invalida"
        else:
            return math.pow(left,(1/right))

    def visitSin(self, ctx):
        value = float(self.visit(ctx.expr()))
        return math.sin(value)

    def visitCos(self, ctx):
        value = float(self.visit(ctx.expr()))
        return math.cos(value)

    def visitTan(self, ctx):
        value = float(self.visit(ctx.expr()))
        return math.tan(value)

    def visitArcsin(self, ctx):
        value = float(self.visit(ctx.expr()))
        if value > 1 or value < -1:
            return "Operación invalida"
        else:
            return math.asin(value)

    def visitArccos(self, ctx):
        value = float(self.visit(ctx.expr()))
        if value > 1 or value < -1:
            return "Operación invalida"
        else:
            return math.acos(value)

    def visitArctan(self, ctx):
        value = float(self.visit(ctx.expr()))
        if value > 1 or value < -1:
            return "Operación invalida"
        else:
            return math.atan(value)

    def visitPi(self, ctx):
        return math.pi

    def visitLog(self, ctx):
        left = float(self.visit(ctx.expr(0)))
        right = float(self.visit(ctx.expr(1)))
        return math.log(left,right)

    def visitFactorial(self, ctx):
        value = float(self.visit(ctx.expr()))
        return math.factorial(int(value))

    def visitEuler(self, ctx):
        value = float(self.visit(ctx.expr()))
        return math.exp(value)  

    def visitRad(self, ctx):
        value = float(self.visit(ctx.expr()))
        return math.radians(value)       

    def visitDeg(self, ctx):
        value = float(self.visit(ctx.expr()))
        return math.degrees(value)         

    def visitParens(self, ctx):
        return self.visit(ctx.expr())