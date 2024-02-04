from Gen.JavaParser import JavaParser
from antlr4 import ParseTreeListener

class EjioguMetricsListener(ParseTreeListener):
    def __init__(self):
        self.height = 0
        self.twin_number = 0
        self.monadicity = 0
        self.total_nodes = 0

    def enterEveryRule(self, ctx):
        self.total_nodes += 1

    def enterMethodDeclaration(self, ctx: JavaParser.MethodDeclarationContext):
        # Reset metrics for each method
        self.height = 0
        self.twin_number = 0
        self.monadicity = 0

    def exitEveryRule(self, ctx):
        # if ctx.getChildCount() == 0:  # Leaf node (monad)
        if ctx.getChildCount() == 0 or ctx.getChildCount() == 1 and ctx.getChild(0).getChildCount() == 0:
            self.monadicity += 1
        elif ctx.getChildCount() > 1:  # Higher level node (twin)
            self.twin_number += ctx.getChildCount() - 1

    def exitMethodDeclaration(self, ctx: JavaParser.MethodDeclarationContext):
        # Calculate height for the method
        self.height = self.calculate_height(ctx)

        # Calculate and print Ejiogu’s Software Metrics
        structural_complexity = self.height * self.twin_number * self.monadicity
        software_size = self.total_nodes - 1  # Exclude the root node
        print(f"Ejiogu’s Software Metrics:")
        print(f"height: {self.height} , twin number: {self.twin_number}, monadicity: {self.monadicity}")
        print(f"Structural Complexity (Sc): {structural_complexity}")
        print(f"Software Size (S): {software_size}")
        print("-------------------------------------------------")


    def calculate_height(self, ctx):
        # Helper function to calculate the height of a node
        height = 0
        while ctx.parentCtx is not None:
            height += 1
            ctx = ctx.parentCtx
        return height
