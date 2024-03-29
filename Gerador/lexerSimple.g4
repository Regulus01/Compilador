lexer grammar lexerSimple;

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