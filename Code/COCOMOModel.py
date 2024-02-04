from antlr4 import *

def calculateCOCOMO(lexer):
    token = lexer.nextToken()

    num = 0
    while token.type != Token.EOF:
        if(token.type != lexer.LINE_COMMENT & token.type != lexer.COMMENT ):
            num += 1
        token = lexer.nextToken()

    KLOC = num/1000
    E = 2.4*(KLOC**1.05)
    D = 2.5*(E**0.36)
    print("------------------------------------------------------------")
    print("COCOMO Mode metrics:")
    print(f"E (the effort applied in person-month) is : {E}")
    print(f"D (the development time in chronological months) is : {D}")
    print("------------------------------------------------------------")