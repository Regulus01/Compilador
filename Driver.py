from antlr4 import *
from Gerador.SimpleLexer import SimpleLexer
from Gerador.SimpleParser import SimpleParser
from DictTokens import token_dict


def main(arquivo):
    input_stream = FileStream(arquivo)
    lexer = SimpleLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SimpleParser(stream)
    parser.programa()

    if parser.getNumberOfSyntaxErrors() == 0:
        imprimirTokens(arquivo)


def imprimirTokens(arquivo):
    # É necessário consumir o lexer novamente
    input_stream = FileStream(arquivo)
    lexer = SimpleLexer(input_stream)
    tokens = lexer.getAllTokens()
    analise_tokens = tokens

    for token in analise_tokens:
        # token 28 é id
        if token.type == 29 and len(token.text) > 16:
            raise ValueError(f"O token ID: {token.text} tem {len(token.text)} caracteres o maximo permitido é 16 "
                             f"caracteres")
        if token.type == 30 and len(token.text) > 16:
            raise ValueError(f"O token CTE: {token.text} tem {len(token.text)} bytes o maximo permitido são 2 bytes")

    print("\n\t\t  Tokens  \n")

    for token in tokens:
        print(f"\033[0;31mTipo:\033[0;0m [ {token_dict[token.type]} ] \033[0;33mValor:\033[0;00m {token.text}")


if __name__ == '__main__':
    main("CodigoTeste.txt")


