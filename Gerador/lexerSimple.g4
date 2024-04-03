lexer grammar lexerSimple;

// Ignora espaços em branco e comentários (/ comentario /)
COMMENT: '//' ~[\r\n]* -> skip;
WS: [ \t\r\n]+ -> skip;

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
IF: 'IF';
THEN: 'THEN';
ELSE: 'ELSE';

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

ID: [a-zA-Z][a-zA-Z0-9]*;
CTE: [0-9]+;
CADEIA: '"' .*? '"' ;
NUMERO_INTEIRO: ('+' | '-')?[0-9]+;
NUMERO_REAL: ('+' | '-')?[0-9]+ '.' [0-9]+;

NOT: '~';