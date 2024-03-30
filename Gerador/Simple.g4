grammar Simple;
import lexerSimple;

//Semantica
programa: PROGRAM ID PVIG declaracao* comando* BEGIN comando* END;

declaracao: VAR (declaracaoVar | declaracaoVarExplicita);

declaracaoVar: ID (VIG ID)* DPONTOS tipo PVIG;

declaracaoVarExplicita: ID DPONTOS tipo PVIG;

tipo: CTE | REAL | TEXTO;

comando: atribuicao PVIG | comandoLeitura | comandoEscrita | comandoRepeticao;

atribuicao: ID ATRIB expressao;

expressao: relacional | expressao 'or' relacional | expressao 'and' relacional;

relacional: aditiva | relacional OPREL aditiva;

aditiva: multiplicativa | aditiva OPAD multiplicativa;

multiplicativa: primaria | multiplicativa OPMULT primaria;

primaria: ID | NUMERO_INTEIRO | NUMERO_REAL | '(' expressao ')';

comandoLeitura: READ '(' ID ')' PVIG;

comandoEscrita: WRITE '(' expressao ')' PVIG | WRITE '(' CADEIA ')' PVIG;

comandoRepeticao: WHILE expressao DO comando* END;