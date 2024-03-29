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
def main(argv):
    input_stream = FileStream(argv)
    lexer = SimpleLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SimpleParser(stream)
    tree = parser.declaracao()
    tokens = lexer.getAllTokens()
    print("Tokens:")
    for token in tokens:
        print(f"Tipo: {token_dict[token.type]}, Valor: {token.text}")

'''
    print("Tokens:")
    for token in lexer.getAllTokens():
        print(f"Tipo: {token.type}")
        if token.type == SimpleLexer.ID:
            print(f"Valor: {token.text}")

        # Imprimir o tipo do token sem usar números
        if token.type in SimpleLexer.TOKEN_NAMES:
            print(f"Nome do Tipo: {SimpleLexer.TOKEN_NAMES[token.type]}")
'''

if __name__ == '__main__':
    main("CodigoTeste.txt")


