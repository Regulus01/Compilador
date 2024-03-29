# Generated from Simple.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,28,171,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,1,0,1,0,1,0,5,0,35,8,0,10,0,12,0,38,9,0,1,0,5,0,41,
        8,0,10,0,12,0,44,9,0,1,0,1,0,5,0,48,8,0,10,0,12,0,51,9,0,1,0,1,0,
        1,0,1,1,1,1,1,1,3,1,59,8,1,1,2,1,2,1,2,5,2,64,8,2,10,2,12,2,67,9,
        2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,5,1,5,1,5,1,5,1,
        5,1,5,3,5,86,8,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,5,7,101,8,7,10,7,12,7,104,9,7,1,8,1,8,1,8,1,8,1,8,1,8,5,8,112,
        8,8,10,8,12,8,115,9,8,1,9,1,9,1,9,1,9,1,9,1,9,5,9,123,8,9,10,9,12,
        9,126,9,9,1,10,1,10,1,10,1,10,1,10,1,10,5,10,134,8,10,10,10,12,10,
        137,9,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,146,8,11,1,12,1,
        12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,
        14,1,14,5,14,164,8,14,10,14,12,14,167,9,14,1,14,1,14,1,14,0,4,14,
        16,18,20,15,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,0,1,1,0,11,13,
        172,0,30,1,0,0,0,2,55,1,0,0,0,4,60,1,0,0,0,6,72,1,0,0,0,8,77,1,0,
        0,0,10,85,1,0,0,0,12,87,1,0,0,0,14,91,1,0,0,0,16,105,1,0,0,0,18,
        116,1,0,0,0,20,127,1,0,0,0,22,145,1,0,0,0,24,147,1,0,0,0,26,153,
        1,0,0,0,28,159,1,0,0,0,30,31,5,5,0,0,31,32,5,26,0,0,32,36,5,19,0,
        0,33,35,3,2,1,0,34,33,1,0,0,0,35,38,1,0,0,0,36,34,1,0,0,0,36,37,
        1,0,0,0,37,42,1,0,0,0,38,36,1,0,0,0,39,41,3,10,5,0,40,39,1,0,0,0,
        41,44,1,0,0,0,42,40,1,0,0,0,42,43,1,0,0,0,43,45,1,0,0,0,44,42,1,
        0,0,0,45,49,5,7,0,0,46,48,3,10,5,0,47,46,1,0,0,0,48,51,1,0,0,0,49,
        47,1,0,0,0,49,50,1,0,0,0,50,52,1,0,0,0,51,49,1,0,0,0,52,53,5,8,0,
        0,53,54,5,20,0,0,54,1,1,0,0,0,55,58,5,6,0,0,56,59,3,4,2,0,57,59,
        3,6,3,0,58,56,1,0,0,0,58,57,1,0,0,0,59,3,1,0,0,0,60,65,5,26,0,0,
        61,62,5,22,0,0,62,64,5,26,0,0,63,61,1,0,0,0,64,67,1,0,0,0,65,63,
        1,0,0,0,65,66,1,0,0,0,66,68,1,0,0,0,67,65,1,0,0,0,68,69,5,21,0,0,
        69,70,3,8,4,0,70,71,5,19,0,0,71,5,1,0,0,0,72,73,5,26,0,0,73,74,5,
        21,0,0,74,75,3,8,4,0,75,76,5,19,0,0,76,7,1,0,0,0,77,78,7,0,0,0,78,
        9,1,0,0,0,79,80,3,12,6,0,80,81,5,19,0,0,81,86,1,0,0,0,82,86,3,24,
        12,0,83,86,3,26,13,0,84,86,3,28,14,0,85,79,1,0,0,0,85,82,1,0,0,0,
        85,83,1,0,0,0,85,84,1,0,0,0,86,11,1,0,0,0,87,88,5,26,0,0,88,89,5,
        25,0,0,89,90,3,14,7,0,90,13,1,0,0,0,91,92,6,7,-1,0,92,93,3,16,8,
        0,93,102,1,0,0,0,94,95,10,2,0,0,95,96,5,1,0,0,96,101,3,16,8,0,97,
        98,10,1,0,0,98,99,5,2,0,0,99,101,3,16,8,0,100,94,1,0,0,0,100,97,
        1,0,0,0,101,104,1,0,0,0,102,100,1,0,0,0,102,103,1,0,0,0,103,15,1,
        0,0,0,104,102,1,0,0,0,105,106,6,8,-1,0,106,107,3,18,9,0,107,113,
        1,0,0,0,108,109,10,1,0,0,109,110,5,16,0,0,110,112,3,18,9,0,111,108,
        1,0,0,0,112,115,1,0,0,0,113,111,1,0,0,0,113,114,1,0,0,0,114,17,1,
        0,0,0,115,113,1,0,0,0,116,117,6,9,-1,0,117,118,3,20,10,0,118,124,
        1,0,0,0,119,120,10,1,0,0,120,121,5,17,0,0,121,123,3,20,10,0,122,
        119,1,0,0,0,123,126,1,0,0,0,124,122,1,0,0,0,124,125,1,0,0,0,125,
        19,1,0,0,0,126,124,1,0,0,0,127,128,6,10,-1,0,128,129,3,22,11,0,129,
        135,1,0,0,0,130,131,10,1,0,0,131,132,5,18,0,0,132,134,3,22,11,0,
        133,130,1,0,0,0,134,137,1,0,0,0,135,133,1,0,0,0,135,136,1,0,0,0,
        136,21,1,0,0,0,137,135,1,0,0,0,138,146,5,26,0,0,139,146,5,27,0,0,
        140,146,5,28,0,0,141,142,5,23,0,0,142,143,3,14,7,0,143,144,5,24,
        0,0,144,146,1,0,0,0,145,138,1,0,0,0,145,139,1,0,0,0,145,140,1,0,
        0,0,145,141,1,0,0,0,146,23,1,0,0,0,147,148,5,9,0,0,148,149,5,23,
        0,0,149,150,5,26,0,0,150,151,5,24,0,0,151,152,5,19,0,0,152,25,1,
        0,0,0,153,154,5,10,0,0,154,155,5,23,0,0,155,156,3,14,7,0,156,157,
        5,24,0,0,157,158,5,19,0,0,158,27,1,0,0,0,159,160,5,14,0,0,160,161,
        3,14,7,0,161,165,5,15,0,0,162,164,3,10,5,0,163,162,1,0,0,0,164,167,
        1,0,0,0,165,163,1,0,0,0,165,166,1,0,0,0,166,168,1,0,0,0,167,165,
        1,0,0,0,168,169,5,8,0,0,169,29,1,0,0,0,13,36,42,49,58,65,85,100,
        102,113,124,135,145,165
    ]

class SimpleParser ( Parser ):

    grammarFileName = "Simple.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'or'", "'and'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "';'", "'.'", "':'", "','", 
                     "'('", "')'", "':='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "COMMENT", 
                      "WS", "PROGRAM", "VAR", "BEGIN", "END", "READ", "WRITE", 
                      "INTEGER", "REAL", "TEXTO", "WHILE", "DO", "OPREL", 
                      "OPAD", "OPMULT", "PVIG", "PONTO", "DPONTOS", "VIG", 
                      "ABPAR", "FPAR", "ATRIB", "ID", "NUMERO_INTEIRO", 
                      "NUMERO_REAL" ]

    RULE_programa = 0
    RULE_declaracao = 1
    RULE_declaracaoVar = 2
    RULE_declaracaoVarExplicita = 3
    RULE_tipo = 4
    RULE_comando = 5
    RULE_atribuicao = 6
    RULE_expressao = 7
    RULE_relacional = 8
    RULE_aditiva = 9
    RULE_multiplicativa = 10
    RULE_primaria = 11
    RULE_comandoLeitura = 12
    RULE_comandoEscrita = 13
    RULE_comandoRepeticao = 14

    ruleNames =  [ "programa", "declaracao", "declaracaoVar", "declaracaoVarExplicita", 
                   "tipo", "comando", "atribuicao", "expressao", "relacional", 
                   "aditiva", "multiplicativa", "primaria", "comandoLeitura", 
                   "comandoEscrita", "comandoRepeticao" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    COMMENT=3
    WS=4
    PROGRAM=5
    VAR=6
    BEGIN=7
    END=8
    READ=9
    WRITE=10
    INTEGER=11
    REAL=12
    TEXTO=13
    WHILE=14
    DO=15
    OPREL=16
    OPAD=17
    OPMULT=18
    PVIG=19
    PONTO=20
    DPONTOS=21
    VIG=22
    ABPAR=23
    FPAR=24
    ATRIB=25
    ID=26
    NUMERO_INTEIRO=27
    NUMERO_REAL=28

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROGRAM(self):
            return self.getToken(SimpleParser.PROGRAM, 0)

        def ID(self):
            return self.getToken(SimpleParser.ID, 0)

        def PVIG(self):
            return self.getToken(SimpleParser.PVIG, 0)

        def BEGIN(self):
            return self.getToken(SimpleParser.BEGIN, 0)

        def END(self):
            return self.getToken(SimpleParser.END, 0)

        def PONTO(self):
            return self.getToken(SimpleParser.PONTO, 0)

        def declaracao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleParser.DeclaracaoContext)
            else:
                return self.getTypedRuleContext(SimpleParser.DeclaracaoContext,i)


        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleParser.ComandoContext)
            else:
                return self.getTypedRuleContext(SimpleParser.ComandoContext,i)


        def getRuleIndex(self):
            return SimpleParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = SimpleParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(SimpleParser.PROGRAM)
            self.state = 31
            self.match(SimpleParser.ID)
            self.state = 32
            self.match(SimpleParser.PVIG)
            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 33
                self.declaracao()
                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 67126784) != 0):
                self.state = 39
                self.comando()
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 45
            self.match(SimpleParser.BEGIN)
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 67126784) != 0):
                self.state = 46
                self.comando()
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 52
            self.match(SimpleParser.END)
            self.state = 53
            self.match(SimpleParser.PONTO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(SimpleParser.VAR, 0)

        def declaracaoVar(self):
            return self.getTypedRuleContext(SimpleParser.DeclaracaoVarContext,0)


        def declaracaoVarExplicita(self):
            return self.getTypedRuleContext(SimpleParser.DeclaracaoVarExplicitaContext,0)


        def getRuleIndex(self):
            return SimpleParser.RULE_declaracao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracao" ):
                listener.enterDeclaracao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracao" ):
                listener.exitDeclaracao(self)




    def declaracao(self):

        localctx = SimpleParser.DeclaracaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaracao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(SimpleParser.VAR)
            self.state = 58
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 56
                self.declaracaoVar()
                pass

            elif la_ == 2:
                self.state = 57
                self.declaracaoVarExplicita()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracaoVarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(SimpleParser.ID)
            else:
                return self.getToken(SimpleParser.ID, i)

        def DPONTOS(self):
            return self.getToken(SimpleParser.DPONTOS, 0)

        def tipo(self):
            return self.getTypedRuleContext(SimpleParser.TipoContext,0)


        def PVIG(self):
            return self.getToken(SimpleParser.PVIG, 0)

        def VIG(self, i:int=None):
            if i is None:
                return self.getTokens(SimpleParser.VIG)
            else:
                return self.getToken(SimpleParser.VIG, i)

        def getRuleIndex(self):
            return SimpleParser.RULE_declaracaoVar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracaoVar" ):
                listener.enterDeclaracaoVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracaoVar" ):
                listener.exitDeclaracaoVar(self)




    def declaracaoVar(self):

        localctx = SimpleParser.DeclaracaoVarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaracaoVar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(SimpleParser.ID)
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22:
                self.state = 61
                self.match(SimpleParser.VIG)
                self.state = 62
                self.match(SimpleParser.ID)
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 68
            self.match(SimpleParser.DPONTOS)
            self.state = 69
            self.tipo()
            self.state = 70
            self.match(SimpleParser.PVIG)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracaoVarExplicitaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SimpleParser.ID, 0)

        def DPONTOS(self):
            return self.getToken(SimpleParser.DPONTOS, 0)

        def tipo(self):
            return self.getTypedRuleContext(SimpleParser.TipoContext,0)


        def PVIG(self):
            return self.getToken(SimpleParser.PVIG, 0)

        def getRuleIndex(self):
            return SimpleParser.RULE_declaracaoVarExplicita

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracaoVarExplicita" ):
                listener.enterDeclaracaoVarExplicita(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracaoVarExplicita" ):
                listener.exitDeclaracaoVarExplicita(self)




    def declaracaoVarExplicita(self):

        localctx = SimpleParser.DeclaracaoVarExplicitaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declaracaoVarExplicita)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(SimpleParser.ID)
            self.state = 73
            self.match(SimpleParser.DPONTOS)
            self.state = 74
            self.tipo()
            self.state = 75
            self.match(SimpleParser.PVIG)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(SimpleParser.INTEGER, 0)

        def REAL(self):
            return self.getToken(SimpleParser.REAL, 0)

        def TEXTO(self):
            return self.getToken(SimpleParser.TEXTO, 0)

        def getRuleIndex(self):
            return SimpleParser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)




    def tipo(self):

        localctx = SimpleParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14336) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atribuicao(self):
            return self.getTypedRuleContext(SimpleParser.AtribuicaoContext,0)


        def PVIG(self):
            return self.getToken(SimpleParser.PVIG, 0)

        def comandoLeitura(self):
            return self.getTypedRuleContext(SimpleParser.ComandoLeituraContext,0)


        def comandoEscrita(self):
            return self.getTypedRuleContext(SimpleParser.ComandoEscritaContext,0)


        def comandoRepeticao(self):
            return self.getTypedRuleContext(SimpleParser.ComandoRepeticaoContext,0)


        def getRuleIndex(self):
            return SimpleParser.RULE_comando

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando" ):
                listener.enterComando(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando" ):
                listener.exitComando(self)




    def comando(self):

        localctx = SimpleParser.ComandoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_comando)
        try:
            self.state = 85
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 79
                self.atribuicao()
                self.state = 80
                self.match(SimpleParser.PVIG)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 82
                self.comandoLeitura()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 83
                self.comandoEscrita()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 4)
                self.state = 84
                self.comandoRepeticao()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtribuicaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SimpleParser.ID, 0)

        def ATRIB(self):
            return self.getToken(SimpleParser.ATRIB, 0)

        def expressao(self):
            return self.getTypedRuleContext(SimpleParser.ExpressaoContext,0)


        def getRuleIndex(self):
            return SimpleParser.RULE_atribuicao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtribuicao" ):
                listener.enterAtribuicao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtribuicao" ):
                listener.exitAtribuicao(self)




    def atribuicao(self):

        localctx = SimpleParser.AtribuicaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_atribuicao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(SimpleParser.ID)
            self.state = 88
            self.match(SimpleParser.ATRIB)
            self.state = 89
            self.expressao(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relacional(self):
            return self.getTypedRuleContext(SimpleParser.RelacionalContext,0)


        def expressao(self):
            return self.getTypedRuleContext(SimpleParser.ExpressaoContext,0)


        def getRuleIndex(self):
            return SimpleParser.RULE_expressao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressao" ):
                listener.enterExpressao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressao" ):
                listener.exitExpressao(self)



    def expressao(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SimpleParser.ExpressaoContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expressao, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.relacional(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 102
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 100
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = SimpleParser.ExpressaoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expressao)
                        self.state = 94
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 95
                        self.match(SimpleParser.T__0)
                        self.state = 96
                        self.relacional(0)
                        pass

                    elif la_ == 2:
                        localctx = SimpleParser.ExpressaoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expressao)
                        self.state = 97
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 98
                        self.match(SimpleParser.T__1)
                        self.state = 99
                        self.relacional(0)
                        pass

             
                self.state = 104
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class RelacionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def aditiva(self):
            return self.getTypedRuleContext(SimpleParser.AditivaContext,0)


        def relacional(self):
            return self.getTypedRuleContext(SimpleParser.RelacionalContext,0)


        def OPREL(self):
            return self.getToken(SimpleParser.OPREL, 0)

        def getRuleIndex(self):
            return SimpleParser.RULE_relacional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelacional" ):
                listener.enterRelacional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelacional" ):
                listener.exitRelacional(self)



    def relacional(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SimpleParser.RelacionalContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_relacional, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.aditiva(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 113
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SimpleParser.RelacionalContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_relacional)
                    self.state = 108
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 109
                    self.match(SimpleParser.OPREL)
                    self.state = 110
                    self.aditiva(0) 
                self.state = 115
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AditivaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativa(self):
            return self.getTypedRuleContext(SimpleParser.MultiplicativaContext,0)


        def aditiva(self):
            return self.getTypedRuleContext(SimpleParser.AditivaContext,0)


        def OPAD(self):
            return self.getToken(SimpleParser.OPAD, 0)

        def getRuleIndex(self):
            return SimpleParser.RULE_aditiva

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAditiva" ):
                listener.enterAditiva(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAditiva" ):
                listener.exitAditiva(self)



    def aditiva(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SimpleParser.AditivaContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_aditiva, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.multiplicativa(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 124
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SimpleParser.AditivaContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_aditiva)
                    self.state = 119
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 120
                    self.match(SimpleParser.OPAD)
                    self.state = 121
                    self.multiplicativa(0) 
                self.state = 126
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class MultiplicativaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primaria(self):
            return self.getTypedRuleContext(SimpleParser.PrimariaContext,0)


        def multiplicativa(self):
            return self.getTypedRuleContext(SimpleParser.MultiplicativaContext,0)


        def OPMULT(self):
            return self.getToken(SimpleParser.OPMULT, 0)

        def getRuleIndex(self):
            return SimpleParser.RULE_multiplicativa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativa" ):
                listener.enterMultiplicativa(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativa" ):
                listener.exitMultiplicativa(self)



    def multiplicativa(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SimpleParser.MultiplicativaContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_multiplicativa, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.primaria()
            self._ctx.stop = self._input.LT(-1)
            self.state = 135
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SimpleParser.MultiplicativaContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicativa)
                    self.state = 130
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 131
                    self.match(SimpleParser.OPMULT)
                    self.state = 132
                    self.primaria() 
                self.state = 137
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PrimariaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SimpleParser.ID, 0)

        def NUMERO_INTEIRO(self):
            return self.getToken(SimpleParser.NUMERO_INTEIRO, 0)

        def NUMERO_REAL(self):
            return self.getToken(SimpleParser.NUMERO_REAL, 0)

        def ABPAR(self):
            return self.getToken(SimpleParser.ABPAR, 0)

        def expressao(self):
            return self.getTypedRuleContext(SimpleParser.ExpressaoContext,0)


        def FPAR(self):
            return self.getToken(SimpleParser.FPAR, 0)

        def getRuleIndex(self):
            return SimpleParser.RULE_primaria

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaria" ):
                listener.enterPrimaria(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaria" ):
                listener.exitPrimaria(self)




    def primaria(self):

        localctx = SimpleParser.PrimariaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_primaria)
        try:
            self.state = 145
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.match(SimpleParser.ID)
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 2)
                self.state = 139
                self.match(SimpleParser.NUMERO_INTEIRO)
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 3)
                self.state = 140
                self.match(SimpleParser.NUMERO_REAL)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 4)
                self.state = 141
                self.match(SimpleParser.ABPAR)
                self.state = 142
                self.expressao(0)
                self.state = 143
                self.match(SimpleParser.FPAR)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoLeituraContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def READ(self):
            return self.getToken(SimpleParser.READ, 0)

        def ABPAR(self):
            return self.getToken(SimpleParser.ABPAR, 0)

        def ID(self):
            return self.getToken(SimpleParser.ID, 0)

        def FPAR(self):
            return self.getToken(SimpleParser.FPAR, 0)

        def PVIG(self):
            return self.getToken(SimpleParser.PVIG, 0)

        def getRuleIndex(self):
            return SimpleParser.RULE_comandoLeitura

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComandoLeitura" ):
                listener.enterComandoLeitura(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComandoLeitura" ):
                listener.exitComandoLeitura(self)




    def comandoLeitura(self):

        localctx = SimpleParser.ComandoLeituraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_comandoLeitura)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(SimpleParser.READ)
            self.state = 148
            self.match(SimpleParser.ABPAR)
            self.state = 149
            self.match(SimpleParser.ID)
            self.state = 150
            self.match(SimpleParser.FPAR)
            self.state = 151
            self.match(SimpleParser.PVIG)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoEscritaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WRITE(self):
            return self.getToken(SimpleParser.WRITE, 0)

        def ABPAR(self):
            return self.getToken(SimpleParser.ABPAR, 0)

        def expressao(self):
            return self.getTypedRuleContext(SimpleParser.ExpressaoContext,0)


        def FPAR(self):
            return self.getToken(SimpleParser.FPAR, 0)

        def PVIG(self):
            return self.getToken(SimpleParser.PVIG, 0)

        def getRuleIndex(self):
            return SimpleParser.RULE_comandoEscrita

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComandoEscrita" ):
                listener.enterComandoEscrita(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComandoEscrita" ):
                listener.exitComandoEscrita(self)




    def comandoEscrita(self):

        localctx = SimpleParser.ComandoEscritaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_comandoEscrita)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(SimpleParser.WRITE)
            self.state = 154
            self.match(SimpleParser.ABPAR)
            self.state = 155
            self.expressao(0)
            self.state = 156
            self.match(SimpleParser.FPAR)
            self.state = 157
            self.match(SimpleParser.PVIG)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoRepeticaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(SimpleParser.WHILE, 0)

        def expressao(self):
            return self.getTypedRuleContext(SimpleParser.ExpressaoContext,0)


        def DO(self):
            return self.getToken(SimpleParser.DO, 0)

        def END(self):
            return self.getToken(SimpleParser.END, 0)

        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleParser.ComandoContext)
            else:
                return self.getTypedRuleContext(SimpleParser.ComandoContext,i)


        def getRuleIndex(self):
            return SimpleParser.RULE_comandoRepeticao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComandoRepeticao" ):
                listener.enterComandoRepeticao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComandoRepeticao" ):
                listener.exitComandoRepeticao(self)




    def comandoRepeticao(self):

        localctx = SimpleParser.ComandoRepeticaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_comandoRepeticao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(SimpleParser.WHILE)
            self.state = 160
            self.expressao(0)
            self.state = 161
            self.match(SimpleParser.DO)
            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 67126784) != 0):
                self.state = 162
                self.comando()
                self.state = 167
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 168
            self.match(SimpleParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[7] = self.expressao_sempred
        self._predicates[8] = self.relacional_sempred
        self._predicates[9] = self.aditiva_sempred
        self._predicates[10] = self.multiplicativa_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expressao_sempred(self, localctx:ExpressaoContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         

    def relacional_sempred(self, localctx:RelacionalContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         

    def aditiva_sempred(self, localctx:AditivaContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         

    def multiplicativa_sempred(self, localctx:MultiplicativaContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 1)
         




