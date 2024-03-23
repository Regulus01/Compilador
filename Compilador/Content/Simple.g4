grammar Simple;

programa: PROGRAM ID PVIG declaracao* comando* BEGIN comando* END PONTO;

declaracao: VAR (declaracaoVar | declaracaoVarExplicita);

declaracaoVar: ID (VIG ID)* DPONTOS tipo PVIG;

declaracaoVarExplicita: ID DPONTOS tipo PVIG;

tipo: INTEGER | REAL | TEXTO;

comando: atribuicao PVIG | comandoLeitura | comandoEscrita | comandoCondicional | comandoRepeticao;

atribuicao: ID ATRIB expressao;

expressao: relacional | expressao 'ou' relacional | expressao 'e' relacional;

relacional: aditiva | relacional OPREL aditiva;

aditiva: multiplicativa | aditiva OPAD multiplicativa;

multiplicativa: primaria | multiplicativa OPMULT primaria;

primaria: ID | NUMERO_INTEIRO | NUMERO_REAL | '(' expressao ')';

comandoLeitura: READ '(' ID ')' PVIG;

comandoEscrita: WRITE '(' expressao ')' PVIG;

comandoCondicional: WHILE expressao DO comando* END;

comandoRepeticao: WHILE expressao DO comando* END;

// Regras para tokens

PROGRAM: 'PROGRAM';
VAR: 'VAR';
BEGIN: 'BEGIN';
END: 'END';
READ: 'READ';
WRITE: 'WRITE';
INTEGER: 'INTEGER';
REAL: 'REAL';
TEXTO: 'TEXTO';
WHILE: 'WHILE';
DO: 'DO';

OPREL: '<' | '<=' | '>' | '>=' | '==' | '<>';
OPAD: '+' | '-';
OPMULT: '*' | '/';

PVIG: ';';
PONTO: '.';
DPONTOS: ':';
VIG: ',';
ABPAR: '(';
FPAR: ')';
ATRIB: ':=';

ID: [a-zA-Z]+;
NUMERO_INTEIRO: ('+' | '-')?[0-9]+;
NUMERO_REAL: ('+' | '-')?[0-9]+ '.' [0-9]+;

// Ignorar espaços em branco e comentários

WS: [ \t\r\n]+ -> skip;
COMMENT: '//' .* -> skip;