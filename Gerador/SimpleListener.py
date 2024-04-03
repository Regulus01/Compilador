# Generated from Simple.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .SimpleParser import SimpleParser
else:
    from SimpleParser import SimpleParser

# This class defines a complete listener for a parse tree produced by SimpleParser.
class SimpleListener(ParseTreeListener):

    # Enter a parse tree produced by SimpleParser#programa.
    def enterPrograma(self, ctx:SimpleParser.ProgramaContext):
        pass

    # Exit a parse tree produced by SimpleParser#programa.
    def exitPrograma(self, ctx:SimpleParser.ProgramaContext):
        pass


    # Enter a parse tree produced by SimpleParser#declaracao.
    def enterDeclaracao(self, ctx:SimpleParser.DeclaracaoContext):
        pass

    # Exit a parse tree produced by SimpleParser#declaracao.
    def exitDeclaracao(self, ctx:SimpleParser.DeclaracaoContext):
        pass


    # Enter a parse tree produced by SimpleParser#declaracaoVar.
    def enterDeclaracaoVar(self, ctx:SimpleParser.DeclaracaoVarContext):
        pass

    # Exit a parse tree produced by SimpleParser#declaracaoVar.
    def exitDeclaracaoVar(self, ctx:SimpleParser.DeclaracaoVarContext):
        pass


    # Enter a parse tree produced by SimpleParser#declaracaoVarExplicita.
    def enterDeclaracaoVarExplicita(self, ctx:SimpleParser.DeclaracaoVarExplicitaContext):
        pass

    # Exit a parse tree produced by SimpleParser#declaracaoVarExplicita.
    def exitDeclaracaoVarExplicita(self, ctx:SimpleParser.DeclaracaoVarExplicitaContext):
        pass


    # Enter a parse tree produced by SimpleParser#tipo.
    def enterTipo(self, ctx:SimpleParser.TipoContext):
        pass

    # Exit a parse tree produced by SimpleParser#tipo.
    def exitTipo(self, ctx:SimpleParser.TipoContext):
        pass


    # Enter a parse tree produced by SimpleParser#comando.
    def enterComando(self, ctx:SimpleParser.ComandoContext):
        pass

    # Exit a parse tree produced by SimpleParser#comando.
    def exitComando(self, ctx:SimpleParser.ComandoContext):
        pass


    # Enter a parse tree produced by SimpleParser#atribuicao.
    def enterAtribuicao(self, ctx:SimpleParser.AtribuicaoContext):
        pass

    # Exit a parse tree produced by SimpleParser#atribuicao.
    def exitAtribuicao(self, ctx:SimpleParser.AtribuicaoContext):
        pass


    # Enter a parse tree produced by SimpleParser#expressao.
    def enterExpressao(self, ctx:SimpleParser.ExpressaoContext):
        pass

    # Exit a parse tree produced by SimpleParser#expressao.
    def exitExpressao(self, ctx:SimpleParser.ExpressaoContext):
        pass


    # Enter a parse tree produced by SimpleParser#relacional.
    def enterRelacional(self, ctx:SimpleParser.RelacionalContext):
        pass

    # Exit a parse tree produced by SimpleParser#relacional.
    def exitRelacional(self, ctx:SimpleParser.RelacionalContext):
        pass


    # Enter a parse tree produced by SimpleParser#aditiva.
    def enterAditiva(self, ctx:SimpleParser.AditivaContext):
        pass

    # Exit a parse tree produced by SimpleParser#aditiva.
    def exitAditiva(self, ctx:SimpleParser.AditivaContext):
        pass


    # Enter a parse tree produced by SimpleParser#multiplicativa.
    def enterMultiplicativa(self, ctx:SimpleParser.MultiplicativaContext):
        pass

    # Exit a parse tree produced by SimpleParser#multiplicativa.
    def exitMultiplicativa(self, ctx:SimpleParser.MultiplicativaContext):
        pass


    # Enter a parse tree produced by SimpleParser#primaria.
    def enterPrimaria(self, ctx:SimpleParser.PrimariaContext):
        pass

    # Exit a parse tree produced by SimpleParser#primaria.
    def exitPrimaria(self, ctx:SimpleParser.PrimariaContext):
        pass


    # Enter a parse tree produced by SimpleParser#notCond.
    def enterNotCond(self, ctx:SimpleParser.NotCondContext):
        pass

    # Exit a parse tree produced by SimpleParser#notCond.
    def exitNotCond(self, ctx:SimpleParser.NotCondContext):
        pass


    # Enter a parse tree produced by SimpleParser#comandoLeitura.
    def enterComandoLeitura(self, ctx:SimpleParser.ComandoLeituraContext):
        pass

    # Exit a parse tree produced by SimpleParser#comandoLeitura.
    def exitComandoLeitura(self, ctx:SimpleParser.ComandoLeituraContext):
        pass


    # Enter a parse tree produced by SimpleParser#comandoEscrita.
    def enterComandoEscrita(self, ctx:SimpleParser.ComandoEscritaContext):
        pass

    # Exit a parse tree produced by SimpleParser#comandoEscrita.
    def exitComandoEscrita(self, ctx:SimpleParser.ComandoEscritaContext):
        pass


    # Enter a parse tree produced by SimpleParser#comandoRepeticao.
    def enterComandoRepeticao(self, ctx:SimpleParser.ComandoRepeticaoContext):
        pass

    # Exit a parse tree produced by SimpleParser#comandoRepeticao.
    def exitComandoRepeticao(self, ctx:SimpleParser.ComandoRepeticaoContext):
        pass


    # Enter a parse tree produced by SimpleParser#cmdIf.
    def enterCmdIf(self, ctx:SimpleParser.CmdIfContext):
        pass

    # Exit a parse tree produced by SimpleParser#cmdIf.
    def exitCmdIf(self, ctx:SimpleParser.CmdIfContext):
        pass


    # Enter a parse tree produced by SimpleParser#cmdIfElse.
    def enterCmdIfElse(self, ctx:SimpleParser.CmdIfElseContext):
        pass

    # Exit a parse tree produced by SimpleParser#cmdIfElse.
    def exitCmdIfElse(self, ctx:SimpleParser.CmdIfElseContext):
        pass



del SimpleParser