from Gen.JavaParser import *
import math

class HalsteadSoftwareMetricsListener(ParseTreeListener):
    def __init__(self):
        self.n1_uniquieoperators = 0
        self.n2_uniqueoperands = 0
        self.N1_operators = 0
        self.N2_operands = 0
        self.operators = {}
        self.operands = {}

    def add_to_operators(self, operator):
        if operator in self.operators:
            self.operators[operator] = self.operators[operator] + 1
        else:
            self.operators[operator] = 1
    
    def add_to_operands(self, operand):
        if operand in self.operands:
            self.operands[operand] = self.operands[operand] + 1
        else:
            self.operands[operand] = 1

    def exitAdditiveExpression(self, ctx:JavaParser.AdditiveExpressionContext):
        if ctx.getChildCount() == 1:
            pass
        if (ctx.getChildCount() > 1):
            left = ctx.getChild(0).getText()
            middle = ctx.getChild(1).getText()
            right = ctx.getChild(2).getText()
            self.add_to_operands(left)
            self.add_to_operators(middle)
            self.add_to_operands(right)

    def exitMultiplicativeExpression(self, ctx:JavaParser.MultiplicativeExpressionContext):
        if ctx.getChildCount() == 1:
            pass
        if (ctx.getChildCount() > 1):
            left = ctx.getChild(0).getText()
            middle = ctx.getChild(1).getText()
            right = ctx.getChild(2).getText()
            self.add_to_operands(left)
            self.add_to_operators(middle)
            self.add_to_operands(right)

    def exitVariableDeclarator(self, ctx:JavaParser.VariableDeclaratorContext):
        if ctx.getChildCount() == 1:
            pass
        if (ctx.getChildCount() > 1):
            left = ctx.getChild(0).getText()
            middle = ctx.getChild(1).getText()
            right = ctx.getChild(2).getText()
            self.add_to_operands(left)
            self.add_to_operators(middle)
            self.add_to_operands(right)

    def exitLocalVariableDeclaration(self, ctx:JavaParser.LocalVariableDeclarationContext):
        if ctx.getChildCount() == 1:
            pass
        if (ctx.getChildCount() > 1):
            left = ctx.getChild(0).getText()
            right = ctx.getChild(1).getText()
            self.add_to_operators(left)
            self.add_to_operands(right)

    def exitIfThenStatement(self, ctx:JavaParser.IfThenStatementContext):
        if ctx.getChildCount() == 1:
            pass
        if (ctx.getChildCount() > 1):
            iff = ctx.getChild(0).getText()
            self.add_to_operators(iff)

    def exitRelationalExpression(self, ctx:JavaParser.RelationalExpressionContext):
        if ctx.getChildCount() == 1:
            pass
        if (ctx.getChildCount() > 1):
            left = ctx.getChild(0).getText()
            middle = ctx.getChild(1).getText()
            right = ctx.getChild(2).getText()
            self.add_to_operands(left)
            self.add_to_operators(middle)
            self.add_to_operands(right)

    def exitAssignment(self, ctx:JavaParser.AssignmentContext):
        if ctx.getChildCount() == 1:
            pass
        if (ctx.getChildCount() > 1):
            left = ctx.getChild(0).getText()
            middle = ctx.getChild(1).getText()
            right = ctx.getChild(2).getText()
            self.add_to_operands(left)
            self.add_to_operators(middle)
            self.add_to_operands(right)

    def exitMethodDeclaration(self, ctx:JavaParser.MethodDeclarationContext):
        if ctx.getChildCount() == 1:
            pass
        if (ctx.getChildCount() > 1):
            left = ctx.getChild(0).getText()
            right = ctx.getChild(1).getText()
            self.add_to_operators(left)
            self.add_to_operators(right)

    def exitMethodHeader(self, ctx:JavaParser.MethodHeaderContext):
        if ctx.getChildCount() == 1:
            pass
        if (ctx.getChildCount() > 1):
            left = ctx.getChild(0).getText()
            self.add_to_operators(left)

    def exitMethodDeclarator(self, ctx:JavaParser.MethodDeclaratorContext):
        if ctx.getChildCount() == 1:
            pass
        if (ctx.getChildCount() > 1):
            left = ctx.getChild(0).getText()
            self.add_to_operands(left)

    def exitBasicForStatement(self, ctx:JavaParser.BasicForStatementContext):
        if ctx.getChildCount() == 1:
            pass
        if (ctx.getChildCount() > 1):
            forr = ctx.getChild(0).getText()
            self.add_to_operators(forr)

    def exitPostIncrementExpression(self, ctx:JavaParser.PostIncrementExpressionContext):
        if ctx.getChildCount() == 1:
            pass
        if (ctx.getChildCount() > 1):
            id = ctx.getChild(0).getText()
            right = ctx.getChild(1).getText()
            self.add_to_operands(id)
            self.add_to_operators(right)

    def exitCompilationUnit(self, ctx: JavaParser.CompilationUnitContext):
        print("---------------------------------------------------------------------")
        print("Halstead’s Software Metrics:")
        print(f"The operators table is as follows: {self.operators}")
        print(f"The operands table is  is as follows: {self.operands}")
        self.N1_operators = len(self.operators)
        self.N2_operands = len(self.operands)
        print(f"N1 = {self.N1_operators}")
        print(f"N2 = {self.N2_operands}")
        for i in self.operators:
            if self.operators[i] == 1:
                self.n1_uniquieoperators = self.n1_uniquieoperators + 1
        for i in self.operands:
            if self.operands[i] == 1:
                self.n2_uniqueoperands = self.n2_uniqueoperands + 1
        print(f"n1 = {self.n1_uniquieoperators}")
        print(f"n2 = {self.n2_uniqueoperands}")
        print(f"Vocabulary = {self.N1_operators + self.N2_operands}")
        print(f"Program length = {self.N1_operators + self.N2_operands}")
        print(f"Length = {self.N1_operators + self.N2_operands}")
        print(f"Calculated program length = {self.n1_uniquieoperators * math.log(self.n1_uniquieoperators,2) + self.n2_uniqueoperands * math.log(self.n2_uniqueoperands,2)}")
        print(f"The formula for Voulume is as follows: Volume = (N1 + N2) * log2(n1 + n2)")
        print(f"Volume = {(self.N1_operators + self.N2_operands) * (math.log(self.n1_uniquieoperators + self.n2_uniqueoperands,2))}")
        print(f"The formula for Difficulty is as follows: (n1/2) * (N2/n2)")
        print(f"Difficulty = {(self.n1_uniquieoperators/2) * (self.N2_operands/self.n2_uniqueoperands)}")
        print(f"The formula for Effort is as follows: Effort = Difficulty * Volume")
        print(f"Effort = {(self.n1_uniquieoperators/2) * (self.N2_operands/self.n2_uniqueoperands) * ((self.N1_operators + self.N2_operands) * (math.log(self.n1_uniquieoperators + self.n2_uniqueoperands,2)))}")
        print(f"The formula for Time is as follows: Time = Effort / 18")
        print(f"Time = {(self.n1_uniquieoperators/2) * (self.N2_operands/self.n2_uniqueoperands) * ((self.N1_operators + self.N2_operands) * (math.log(self.n1_uniquieoperators + self.n2_uniqueoperands,2))) / 18}")
        print(f"The formula for Size is as follows: Size = Effort / 3000")
        print(f"Size = {(self.n1_uniquieoperators/2) * (self.N2_operands/self.n2_uniqueoperands) * ((self.N1_operators + self.N2_operands) * (math.log(self.n1_uniquieoperators + self.n2_uniqueoperands,2))) / 3000}")
        print("---------------------------------------------------------------------")
