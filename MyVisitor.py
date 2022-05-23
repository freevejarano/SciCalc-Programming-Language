from gramVisitor import gramVisitor
from gramParser import gramParser

import math

var_globales = {}

class MyVisitor(gramVisitor):
    def __init__(self):
        self.memory = {}

    def visitAsignacion(self, ctx):
        var = ctx.ID().getText()
        valor = ctx.arg().getText()
        if '[' in valor:
            characters = "[]"
            string = ''.join( x for x in valor if x not in characters)
            valor = string.split(",")
        var_globales.update(dict({var:valor}))
        print("Variable guardada")

    def visitFor(self, ctx):        
        print(ctx.ID()[0].getText(), ctx.ID()[1].getText())

    def visitDeg(self, ctx):
        valor = ctx.arg().getText()
        print("El valor en grados es:", valor)