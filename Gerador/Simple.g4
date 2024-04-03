grammar Simple;
import lexerSimple;

//Semantica
programa: PROGRAM ID PVIG declaracao* comando* BEGIN comando* END;

declaracao: VAR (declaracaoVar | declaracaoVarExplicita);

declaracaoVar: ID (VIG ID)* DPONTOS tipo PVIG;

declaracaoVarExplicita: ID DPONTOS tipo PVIG;

tipo: INTEGER | REAL | TEXTO;

comando: atribuicao PVIG | comandoLeitura | comandoEscrita | comandoEscritaCadeia | comandoRepeticao | cmdIf | cmdIfElse;

atribuicao: ID ATRIB expressao;

expressao: relacional | expressao 'or' relacional | expressao 'and' relacional;

relacional: aditiva | relacional OPREL aditiva;

aditiva: multiplicativa | aditiva OPAD multiplicativa;

multiplicativa: primaria | multiplicativa OPMULT primaria;

primaria: ID | CTE | NUMERO_INTEIRO | NUMERO_REAL | '(' expressao ')' | NOT notCond;

notCond: primaria (OPMULT | OPAD) notCond | primaria;

comandoLeitura: READ '(' ID ')' PVIG;

comandoEscrita: WRITE '(' expressao ')' PVIG;

comandoEscritaCadeia: WRITE '(' CADEIA ')' PVIG;

comandoRepeticao: WHILE expressao DO comando*;

// ambiguidade retirada
cmdIf: IF expressao THEN comando;

cmdIfElse: IF expressao THEN comando ELSE comando;