from Gen.JavaParser import *
import networkx as nx

class node :
    def __int__(self):
        self.number = 0
        self.next = None
        self.next_divert = None

class graph:
    def __init__(self):
        self.nodes = []
        # self.edges = {}
        self.edges_numbers = 0
        self.current_node = None
        self.last_node_numbers = 0

    def create_node_for_while(self):
        first = node()
        second = node()
        third = node()
        if self.current_node == None:
            self.current_node = first
        else:
            self.current_node.next = first
            self.edges_numbers = self.edges_numbers + 1
        
        first.number = self.last_node_numbers + 1
        self.last_node_numbers = self.last_node_numbers + 1
        first.next = second
        self.edges_numbers = self.edges_numbers + 1
        self.nodes.append(first)
        
        second.number = self.last_node_numbers + 1
        self.last_node_numbers = self.last_node_numbers + 1
        second.next_divert = third
        self.edges_numbers = self.edges_numbers + 1
        self.nodes.append(second)
        
        third.number = self.last_node_numbers + 1
        self.last_node_numbers = self.last_node_numbers + 1
        third.next = first
        self.edges_numbers = self.edges_numbers + 1
        self.nodes.append(third)
        
        second.next = None
        self.current_node = second

    def create_node_if_else(self):
        first = node()
        second = node()
        third = node()
        if self.current_node == None:
            self.current_node = first
        else:
            self.current_node.next = first
            self.edges_numbers = self.edges_numbers + 1
        
        first.number = self.last_node_numbers + 1
        self.last_node_numbers = self.last_node_numbers + 1
        first.next = second
        self.edges_numbers = self.edges_numbers + 1
        self.nodes.append(first)
        first.next_divert = third
        self.edges_numbers = self.edges_numbers + 1
        
        second.number = self.last_node_numbers + 1
        self.last_node_numbers = self.last_node_numbers + 1
        second.next = None
        self.nodes.append(second)
        
        third.number = self.last_node_numbers + 1
        self.last_node_numbers = self.last_node_numbers + 1
        third.next = second
        self.edges_numbers = self.edges_numbers + 1
        self.nodes.append(third)
        
        self.current_node = second

    def create_node_assignement(self):
        first = node()
        if self.current_node == None:
            self.current_node = first
        else:
            self.current_node.next = first
            self.edges_numbers = self.edges_numbers + 1
        
        first.number = self.last_node_numbers + 1
        self.last_node_numbers = self.last_node_numbers + 1
        first.next = None
        self.nodes.append(first)
        
        self.current_node = first

class McCabeCyclomaticComplexityMetricsCustomListener(ParseTreeListener):
    def __init__(self):
        self.graph = nx.DiGraph()
        self.graphh = graph()
        self.graphh.current_node = None

    def exitVariableDeclarator(self, ctx:JavaParser.VariableDeclaratorContext):
        self.graphh.create_node_assignement()

    def exitIfThenStatement(self, ctx:JavaParser.IfThenStatementContext):
        self.graphh.create_node_if_else()

    def exitBasicForStatement(self, ctx:JavaParser.BasicForStatementContext):
        self.graphh.create_node_for_while()

    def exitWhileStatement(self, ctx:JavaParser.WhileStatementContext):
        self.graphh.create_node_for_while()

    def exitCompilationUnit(self, ctx: JavaParser.CompilationUnitContext):
        print("McCabe’s Cyclomatic complexity metrics:")
        print(f"Number of nodes = {self.graphh.last_node_numbers}")
        print(f"Number of edges = {self.graphh.edges_numbers}")
        print(f"Number of proper sub graphs = {self.graphh.last_node_numbers - self.graphh.edges_numbers + 2}")
        print(f"The formula for calculating the cyclomatic complexity = The number of edges - The number of nodes + 2")
        print(f"Cyclomatic complexity = {self.graphh.edges_numbers - self.graphh.last_node_numbers + 2}")
        print(f"The essential complexity proposed by McCable = The cyclomatic complexity - The number of proper sub graphs")
        print(f"Essential complexity = {self.graphh.edges_numbers - self.graphh.last_node_numbers + 2 - (self.graphh.last_node_numbers - self.graphh.edges_numbers + 2)}")
        print("---------------------------------------------------------------------")
