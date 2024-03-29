grammar Simple;

//Semantica
programa: PROGRAM ID PVIG declaracao* comando* BEGIN comando* END PONTO;

declaracao: VAR (declaracaoVar | declaracaoVarExplicita);

declaracaoVar: ID (VIG ID)* DPONTOS tipo PVIG;

declaracaoVarExplicita: ID DPONTOS tipo PVIG;

tipo: INTEGER | REAL | TEXTO;

comando: atribuicao PVIG | comandoLeitura | comandoEscrita | comandoRepeticao;

atribuicao: ID ATRIB expressao;

expressao: relacional | expressao 'or' relacional | expressao 'and' relacional;

relacional: aditiva | relacional OPREL aditiva;

aditiva: multiplicativa | aditiva OPAD multiplicativa;

multiplicativa: primaria | multiplicativa OPMULT primaria;

primaria: ID | NUMERO_INTEIRO | NUMERO_REAL | '(' expressao ')';

comandoLeitura: READ '(' ID ')' PVIG;

comandoEscrita: WRITE '(' expressao ')' PVIG;

comandoRepeticao: WHILE expressao DO comando* END;


// Ignora espaços em branco e comentários (/ comentario /)
COMMENT: '/' ~[/]* ('/' ~[/]*)* '/' -> skip;
WS: [ \t\r\n]+ -> skip;

// Regras para tokens
PROGRAM: 'PROGRAM' | 'program';
VAR: 'VAR' | 'var';
BEGIN: 'BEGIN' | 'begin';
END: 'END' | 'end';
READ: 'READ' | 'read';
WRITE: 'WRITE' | 'write';
INTEGER: 'INTEGER' | 'integer';
REAL: 'REAL' | 'real';
TEXTO: 'TEXTO' | 'texto';
WHILE: 'WHILE' | 'while';
DO: 'DO' | 'do';

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