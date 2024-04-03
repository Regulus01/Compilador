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
        4,1,34,207,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,1,0,1,0,1,
        0,5,0,43,8,0,10,0,12,0,46,9,0,1,0,5,0,49,8,0,10,0,12,0,52,9,0,1,
        0,1,0,5,0,56,8,0,10,0,12,0,59,9,0,1,0,1,0,1,1,1,1,1,1,3,1,66,8,1,
        1,2,1,2,1,2,5,2,71,8,2,10,2,12,2,74,9,2,1,2,1,2,1,2,1,2,1,3,1,3,
        1,3,1,3,1,3,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,96,8,
        5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,5,7,111,8,
        7,10,7,12,7,114,9,7,1,8,1,8,1,8,1,8,1,8,1,8,5,8,122,8,8,10,8,12,
        8,125,9,8,1,9,1,9,1,9,1,9,1,9,1,9,5,9,133,8,9,10,9,12,9,136,9,9,
        1,10,1,10,1,10,1,10,1,10,1,10,5,10,144,8,10,10,10,12,10,147,9,10,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,159,8,11,
        1,12,1,12,1,12,1,12,1,12,3,12,166,8,12,1,13,1,13,1,13,1,13,1,13,
        1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,
        1,16,1,16,1,16,1,16,5,16,190,8,16,10,16,12,16,193,9,16,1,17,1,17,
        1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,0,4,14,16,
        18,20,19,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,0,2,
        1,0,11,13,1,0,20,21,210,0,38,1,0,0,0,2,62,1,0,0,0,4,67,1,0,0,0,6,
        79,1,0,0,0,8,84,1,0,0,0,10,95,1,0,0,0,12,97,1,0,0,0,14,101,1,0,0,
        0,16,115,1,0,0,0,18,126,1,0,0,0,20,137,1,0,0,0,22,158,1,0,0,0,24,
        165,1,0,0,0,26,167,1,0,0,0,28,173,1,0,0,0,30,179,1,0,0,0,32,185,
        1,0,0,0,34,194,1,0,0,0,36,199,1,0,0,0,38,39,5,5,0,0,39,40,5,29,0,
        0,40,44,5,22,0,0,41,43,3,2,1,0,42,41,1,0,0,0,43,46,1,0,0,0,44,42,
        1,0,0,0,44,45,1,0,0,0,45,50,1,0,0,0,46,44,1,0,0,0,47,49,3,10,5,0,
        48,47,1,0,0,0,49,52,1,0,0,0,50,48,1,0,0,0,50,51,1,0,0,0,51,53,1,
        0,0,0,52,50,1,0,0,0,53,57,5,7,0,0,54,56,3,10,5,0,55,54,1,0,0,0,56,
        59,1,0,0,0,57,55,1,0,0,0,57,58,1,0,0,0,58,60,1,0,0,0,59,57,1,0,0,
        0,60,61,5,8,0,0,61,1,1,0,0,0,62,65,5,6,0,0,63,66,3,4,2,0,64,66,3,
        6,3,0,65,63,1,0,0,0,65,64,1,0,0,0,66,3,1,0,0,0,67,72,5,29,0,0,68,
        69,5,25,0,0,69,71,5,29,0,0,70,68,1,0,0,0,71,74,1,0,0,0,72,70,1,0,
        0,0,72,73,1,0,0,0,73,75,1,0,0,0,74,72,1,0,0,0,75,76,5,24,0,0,76,
        77,3,8,4,0,77,78,5,22,0,0,78,5,1,0,0,0,79,80,5,29,0,0,80,81,5,24,
        0,0,81,82,3,8,4,0,82,83,5,22,0,0,83,7,1,0,0,0,84,85,7,0,0,0,85,9,
        1,0,0,0,86,87,3,12,6,0,87,88,5,22,0,0,88,96,1,0,0,0,89,96,3,26,13,
        0,90,96,3,28,14,0,91,96,3,30,15,0,92,96,3,32,16,0,93,96,3,34,17,
        0,94,96,3,36,18,0,95,86,1,0,0,0,95,89,1,0,0,0,95,90,1,0,0,0,95,91,
        1,0,0,0,95,92,1,0,0,0,95,93,1,0,0,0,95,94,1,0,0,0,96,11,1,0,0,0,
        97,98,5,29,0,0,98,99,5,28,0,0,99,100,3,14,7,0,100,13,1,0,0,0,101,
        102,6,7,-1,0,102,103,3,16,8,0,103,112,1,0,0,0,104,105,10,2,0,0,105,
        106,5,1,0,0,106,111,3,16,8,0,107,108,10,1,0,0,108,109,5,2,0,0,109,
        111,3,16,8,0,110,104,1,0,0,0,110,107,1,0,0,0,111,114,1,0,0,0,112,
        110,1,0,0,0,112,113,1,0,0,0,113,15,1,0,0,0,114,112,1,0,0,0,115,116,
        6,8,-1,0,116,117,3,18,9,0,117,123,1,0,0,0,118,119,10,1,0,0,119,120,
        5,19,0,0,120,122,3,18,9,0,121,118,1,0,0,0,122,125,1,0,0,0,123,121,
        1,0,0,0,123,124,1,0,0,0,124,17,1,0,0,0,125,123,1,0,0,0,126,127,6,
        9,-1,0,127,128,3,20,10,0,128,134,1,0,0,0,129,130,10,1,0,0,130,131,
        5,20,0,0,131,133,3,20,10,0,132,129,1,0,0,0,133,136,1,0,0,0,134,132,
        1,0,0,0,134,135,1,0,0,0,135,19,1,0,0,0,136,134,1,0,0,0,137,138,6,
        10,-1,0,138,139,3,22,11,0,139,145,1,0,0,0,140,141,10,1,0,0,141,142,
        5,21,0,0,142,144,3,22,11,0,143,140,1,0,0,0,144,147,1,0,0,0,145,143,
        1,0,0,0,145,146,1,0,0,0,146,21,1,0,0,0,147,145,1,0,0,0,148,159,5,
        29,0,0,149,159,5,30,0,0,150,159,5,32,0,0,151,159,5,33,0,0,152,153,
        5,26,0,0,153,154,3,14,7,0,154,155,5,27,0,0,155,159,1,0,0,0,156,157,
        5,34,0,0,157,159,3,24,12,0,158,148,1,0,0,0,158,149,1,0,0,0,158,150,
        1,0,0,0,158,151,1,0,0,0,158,152,1,0,0,0,158,156,1,0,0,0,159,23,1,
        0,0,0,160,161,3,22,11,0,161,162,7,1,0,0,162,163,3,24,12,0,163,166,
        1,0,0,0,164,166,3,22,11,0,165,160,1,0,0,0,165,164,1,0,0,0,166,25,
        1,0,0,0,167,168,5,9,0,0,168,169,5,26,0,0,169,170,5,29,0,0,170,171,
        5,27,0,0,171,172,5,22,0,0,172,27,1,0,0,0,173,174,5,10,0,0,174,175,
        5,26,0,0,175,176,3,14,7,0,176,177,5,27,0,0,177,178,5,22,0,0,178,
        29,1,0,0,0,179,180,5,10,0,0,180,181,5,26,0,0,181,182,5,31,0,0,182,
        183,5,27,0,0,183,184,5,22,0,0,184,31,1,0,0,0,185,186,5,14,0,0,186,
        187,3,14,7,0,187,191,5,15,0,0,188,190,3,10,5,0,189,188,1,0,0,0,190,
        193,1,0,0,0,191,189,1,0,0,0,191,192,1,0,0,0,192,33,1,0,0,0,193,191,
        1,0,0,0,194,195,5,16,0,0,195,196,3,14,7,0,196,197,5,17,0,0,197,198,
        3,10,5,0,198,35,1,0,0,0,199,200,5,16,0,0,200,201,3,14,7,0,201,202,
        5,17,0,0,202,203,3,10,5,0,203,204,5,18,0,0,204,205,3,10,5,0,205,
        37,1,0,0,0,14,44,50,57,65,72,95,110,112,123,134,145,158,165,191
    ]

class SimpleParser ( Parser ):

    grammarFileName = "Simple.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'or'", "'and'", "<INVALID>", "<INVALID>", 
                     "'PROGRAM'", "'VAR'", "'BEGIN'", "'END'", "'READ'", 
                     "'WRITE'", "'INTEGER'", "'REAL'", "'TEXTO'", "'WHILE'", 
                     "'DO'", "'IF'", "'THEN'", "'ELSE'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "';'", "'.'", "':'", "','", "'('", "')'", 
                     "':='", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'~'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "COMMENT", 
                      "WS", "PROGRAM", "VAR", "BEGIN", "END", "READ", "WRITE", 
                      "INTEGER", "REAL", "TEXTO", "WHILE", "DO", "IF", "THEN", 
                      "ELSE", "OPREL", "OPAD", "OPMULT", "PVIG", "PONTO", 
                      "DPONTOS", "VIG", "ABPAR", "FPAR", "ATRIB", "ID", 
                      "CTE", "CADEIA", "NUMERO_INTEIRO", "NUMERO_REAL", 
                      "NOT" ]

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
    RULE_notCond = 12
    RULE_comandoLeitura = 13
    RULE_comandoEscrita = 14
    RULE_comandoEscritaCadeia = 15
    RULE_comandoRepeticao = 16
    RULE_cmdIf = 17
    RULE_cmdIfElse = 18

    ruleNames =  [ "programa", "declaracao", "declaracaoVar", "declaracaoVarExplicita", 
                   "tipo", "comando", "atribuicao", "expressao", "relacional", 
                   "aditiva", "multiplicativa", "primaria", "notCond", "comandoLeitura", 
                   "comandoEscrita", "comandoEscritaCadeia", "comandoRepeticao", 
                   "cmdIf", "cmdIfElse" ]

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
    IF=16
    THEN=17
    ELSE=18
    OPREL=19
    OPAD=20
    OPMULT=21
    PVIG=22
    PONTO=23
    DPONTOS=24
    VIG=25
    ABPAR=26
    FPAR=27
    ATRIB=28
    ID=29
    CTE=30
    CADEIA=31
    NUMERO_INTEIRO=32
    NUMERO_REAL=33
    NOT=34

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
            self.state = 38
            self.match(SimpleParser.PROGRAM)
            self.state = 39
            self.match(SimpleParser.ID)
            self.state = 40
            self.match(SimpleParser.PVIG)
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 41
                self.declaracao()
                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 536954368) != 0):
                self.state = 47
                self.comando()
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 53
            self.match(SimpleParser.BEGIN)
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 536954368) != 0):
                self.state = 54
                self.comando()
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 60
            self.match(SimpleParser.END)
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
            self.state = 62
            self.match(SimpleParser.VAR)
            self.state = 65
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 63
                self.declaracaoVar()
                pass

            elif la_ == 2:
                self.state = 64
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
            self.state = 67
            self.match(SimpleParser.ID)
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 68
                self.match(SimpleParser.VIG)
                self.state = 69
                self.match(SimpleParser.ID)
                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 75
            self.match(SimpleParser.DPONTOS)
            self.state = 76
            self.tipo()
            self.state = 77
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
            self.state = 79
            self.match(SimpleParser.ID)
            self.state = 80
            self.match(SimpleParser.DPONTOS)
            self.state = 81
            self.tipo()
            self.state = 82
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
            self.state = 84
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


        def comandoEscritaCadeia(self):
            return self.getTypedRuleContext(SimpleParser.ComandoEscritaCadeiaContext,0)


        def comandoRepeticao(self):
            return self.getTypedRuleContext(SimpleParser.ComandoRepeticaoContext,0)


        def cmdIf(self):
            return self.getTypedRuleContext(SimpleParser.CmdIfContext,0)


        def cmdIfElse(self):
            return self.getTypedRuleContext(SimpleParser.CmdIfElseContext,0)


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
            self.state = 95
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.atribuicao()
                self.state = 87
                self.match(SimpleParser.PVIG)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 89
                self.comandoLeitura()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 90
                self.comandoEscrita()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 91
                self.comandoEscritaCadeia()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 92
                self.comandoRepeticao()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 93
                self.cmdIf()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 94
                self.cmdIfElse()
                pass


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
            self.state = 97
            self.match(SimpleParser.ID)
            self.state = 98
            self.match(SimpleParser.ATRIB)
            self.state = 99
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
            self.state = 102
            self.relacional(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 112
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 110
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = SimpleParser.ExpressaoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expressao)
                        self.state = 104
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 105
                        self.match(SimpleParser.T__0)
                        self.state = 106
                        self.relacional(0)
                        pass

                    elif la_ == 2:
                        localctx = SimpleParser.ExpressaoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expressao)
                        self.state = 107
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 108
                        self.match(SimpleParser.T__1)
                        self.state = 109
                        self.relacional(0)
                        pass

             
                self.state = 114
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
            self.state = 116
            self.aditiva(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 123
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SimpleParser.RelacionalContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_relacional)
                    self.state = 118
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 119
                    self.match(SimpleParser.OPREL)
                    self.state = 120
                    self.aditiva(0) 
                self.state = 125
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
            self.state = 127
            self.multiplicativa(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 134
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SimpleParser.AditivaContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_aditiva)
                    self.state = 129
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 130
                    self.match(SimpleParser.OPAD)
                    self.state = 131
                    self.multiplicativa(0) 
                self.state = 136
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
            self.state = 138
            self.primaria()
            self._ctx.stop = self._input.LT(-1)
            self.state = 145
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SimpleParser.MultiplicativaContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicativa)
                    self.state = 140
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 141
                    self.match(SimpleParser.OPMULT)
                    self.state = 142
                    self.primaria() 
                self.state = 147
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

        def CTE(self):
            return self.getToken(SimpleParser.CTE, 0)

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

        def NOT(self):
            return self.getToken(SimpleParser.NOT, 0)

        def notCond(self):
            return self.getTypedRuleContext(SimpleParser.NotCondContext,0)


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
            self.state = 158
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29]:
                self.enterOuterAlt(localctx, 1)
                self.state = 148
                self.match(SimpleParser.ID)
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
                self.match(SimpleParser.CTE)
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 3)
                self.state = 150
                self.match(SimpleParser.NUMERO_INTEIRO)
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 4)
                self.state = 151
                self.match(SimpleParser.NUMERO_REAL)
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 5)
                self.state = 152
                self.match(SimpleParser.ABPAR)
                self.state = 153
                self.expressao(0)
                self.state = 154
                self.match(SimpleParser.FPAR)
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 6)
                self.state = 156
                self.match(SimpleParser.NOT)
                self.state = 157
                self.notCond()
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


    class NotCondContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primaria(self):
            return self.getTypedRuleContext(SimpleParser.PrimariaContext,0)


        def notCond(self):
            return self.getTypedRuleContext(SimpleParser.NotCondContext,0)


        def OPMULT(self):
            return self.getToken(SimpleParser.OPMULT, 0)

        def OPAD(self):
            return self.getToken(SimpleParser.OPAD, 0)

        def getRuleIndex(self):
            return SimpleParser.RULE_notCond

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotCond" ):
                listener.enterNotCond(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotCond" ):
                listener.exitNotCond(self)




    def notCond(self):

        localctx = SimpleParser.NotCondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_notCond)
        self._la = 0 # Token type
        try:
            self.state = 165
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.primaria()
                self.state = 161
                _la = self._input.LA(1)
                if not(_la==20 or _la==21):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 162
                self.notCond()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
                self.primaria()
                pass


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
        self.enterRule(localctx, 26, self.RULE_comandoLeitura)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(SimpleParser.READ)
            self.state = 168
            self.match(SimpleParser.ABPAR)
            self.state = 169
            self.match(SimpleParser.ID)
            self.state = 170
            self.match(SimpleParser.FPAR)
            self.state = 171
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
        self.enterRule(localctx, 28, self.RULE_comandoEscrita)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(SimpleParser.WRITE)
            self.state = 174
            self.match(SimpleParser.ABPAR)
            self.state = 175
            self.expressao(0)
            self.state = 176
            self.match(SimpleParser.FPAR)
            self.state = 177
            self.match(SimpleParser.PVIG)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoEscritaCadeiaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WRITE(self):
            return self.getToken(SimpleParser.WRITE, 0)

        def ABPAR(self):
            return self.getToken(SimpleParser.ABPAR, 0)

        def CADEIA(self):
            return self.getToken(SimpleParser.CADEIA, 0)

        def FPAR(self):
            return self.getToken(SimpleParser.FPAR, 0)

        def PVIG(self):
            return self.getToken(SimpleParser.PVIG, 0)

        def getRuleIndex(self):
            return SimpleParser.RULE_comandoEscritaCadeia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComandoEscritaCadeia" ):
                listener.enterComandoEscritaCadeia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComandoEscritaCadeia" ):
                listener.exitComandoEscritaCadeia(self)




    def comandoEscritaCadeia(self):

        localctx = SimpleParser.ComandoEscritaCadeiaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_comandoEscritaCadeia)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.match(SimpleParser.WRITE)
            self.state = 180
            self.match(SimpleParser.ABPAR)
            self.state = 181
            self.match(SimpleParser.CADEIA)
            self.state = 182
            self.match(SimpleParser.FPAR)
            self.state = 183
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
        self.enterRule(localctx, 32, self.RULE_comandoRepeticao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.match(SimpleParser.WHILE)
            self.state = 186
            self.expressao(0)
            self.state = 187
            self.match(SimpleParser.DO)
            self.state = 191
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 188
                    self.comando() 
                self.state = 193
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdIfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(SimpleParser.IF, 0)

        def expressao(self):
            return self.getTypedRuleContext(SimpleParser.ExpressaoContext,0)


        def THEN(self):
            return self.getToken(SimpleParser.THEN, 0)

        def comando(self):
            return self.getTypedRuleContext(SimpleParser.ComandoContext,0)


        def getRuleIndex(self):
            return SimpleParser.RULE_cmdIf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdIf" ):
                listener.enterCmdIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdIf" ):
                listener.exitCmdIf(self)




    def cmdIf(self):

        localctx = SimpleParser.CmdIfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_cmdIf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(SimpleParser.IF)
            self.state = 195
            self.expressao(0)
            self.state = 196
            self.match(SimpleParser.THEN)
            self.state = 197
            self.comando()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdIfElseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(SimpleParser.IF, 0)

        def expressao(self):
            return self.getTypedRuleContext(SimpleParser.ExpressaoContext,0)


        def THEN(self):
            return self.getToken(SimpleParser.THEN, 0)

        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleParser.ComandoContext)
            else:
                return self.getTypedRuleContext(SimpleParser.ComandoContext,i)


        def ELSE(self):
            return self.getToken(SimpleParser.ELSE, 0)

        def getRuleIndex(self):
            return SimpleParser.RULE_cmdIfElse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdIfElse" ):
                listener.enterCmdIfElse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdIfElse" ):
                listener.exitCmdIfElse(self)




    def cmdIfElse(self):

        localctx = SimpleParser.CmdIfElseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_cmdIfElse)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(SimpleParser.IF)
            self.state = 200
            self.expressao(0)
            self.state = 201
            self.match(SimpleParser.THEN)
            self.state = 202
            self.comando()
            self.state = 203
            self.match(SimpleParser.ELSE)
            self.state = 204
            self.comando()
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
         




