from Gen.JavaParser import *

class InformationMetricsListener(ParseTreeListener):
    def __init__(self):
        self.fanin = 0
        self.fanout = 0
        self.methods = {}
        self.metrics = {}
        self.IFC=0

    def enterMethodDeclaration(self, ctx: JavaParser.MethodDeclarationContext):
        method: str = ctx.methodHeader().methodDeclarator().Identifier().getText()
        self.methods[method] = {
            'fanin': 0,
            'fanout': 0
        }

    def exitMethodDeclaration(self, ctx: JavaParser.MethodDeclarationContext):
        method: str = ctx.methodHeader().methodDeclarator().Identifier().getText()
        fanin: int = self.methods[method]['fanin']
        fanout: int = self.methods[method]['fanout']

        if method not in self.metrics:
            self.metrics[method] = []

        self.metrics[method].append({'fanin': fanin, 'fanout': fanout})

    def enterMethodInvocation(self, ctx: JavaParser.MethodInvocationContext):
        method: str = ctx.Identifier().getText()

        if method in self.methods:
            self.methods[method]['fanout'] += 1
        else:
            self.methods[method] = {
                'fanin': 1,
                'fanout': 0
            }
    
    def exitMethodInvocation(self, ctx: JavaParser.MethodInvocationContext):
        method: str = ctx.Identifier().getText()

        if method in self.methods:
            self.fanin += 1

    def exitCompilationUnit(self, ctx: JavaParser.CompilationUnitContext):

        for method in self.methods:
            self.IFC += ( self.methods[method]['fanin'] * self.methods[method]['fanout'])**2

        self.IFC *=len(self.methods)
        print(f"Henry and Kafura’s Information Metrics:")
        print(f"Length: {len(self.methods)}, Fan-In: {self.fanin}, Fan-Out: {self.fanout}")
        print(f"Information Flow Complexity (IFC): {self.IFC}")
        print("--------------------------------------------------")
