from antlr4 import *
from Gerador.SimpleLexer import SimpleLexer
from Gerador.SimpleParser import SimpleParser

token_dict = {
    3: 'COMMENT',
    4: 'WS',
    5: 'PROGRAM',
    6: 'VAR',
    7: 'BEGIN',
    8: 'END',
    9: 'READ',
    10: 'WRITE',
    11: 'INTEGER',
    12: 'REAL',
    13: 'TEXTO',
    14: 'WHILE',
    15: 'DO',
    16: 'OPREL',
    17: 'OPAD',
    18: 'OPMULT',
    19: 'PVIG',
    20: 'PONTO',
    21: 'DPONTOS',
    22: 'VIG',
    23: 'ABPAR',
    24: 'FPAR',
    25: 'ATRIB',
    26: 'ID',
    27: 'NUMERO_INTEIRO',
    28: 'NUMERO_REAL'
}


def main(arquivo):
    input_stream = FileStream(arquivo)
    lexer = SimpleLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SimpleParser(stream)
    tree = parser.programa()

    if tree.exception is None:
        imprimirTokens(arquivo)


def imprimirTokens(arquivo):
    # É necessário consumir o lexer novamente
    input_stream = FileStream(arquivo)
    lexer = SimpleLexer(input_stream)
    tokens = lexer.getAllTokens()

    print("\n\t\t  Tokens  \n")

    for token in tokens:
        print(f"\033[0;31mTipo:\033[0;0m {token_dict[token.type]}, \033[0;33mValor:\033[0;00m {token.text}")


if __name__ == '__main__':
    main("CodigoTeste.txt")


