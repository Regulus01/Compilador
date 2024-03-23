grammar Simple;

programa:
    declaracao*
    comando*
    EOF;

declaracao:
    tipo ID ';'
    | 'var' ID ':' tipo ';';

tipo:
    'inteiro'
    | 'real'
    | 'texto';

comando:
    atribuicao ';'
    | comandoLeitura
    | comandoEscrita
    | comandoCondicional
    | comandoRepeticao;

atribuicao:
    ID '=' expressao;

expressao:
    termo
    | expressao '+' termo
    | expressao '-' termo;

termo:
    fator
    | termo '*' fator
    | termo '/' fator;

fator:
    ID
    | NUMERO_INTEIRO
    | NUMERO_REAL
    | '(' expressao ')';

comandoLeitura:
    'leia' '(' ID ')' ';';

comandoEscrita:
    'escreva' '(' expressao ')' ';';

comandoCondicional:
    'se' expressao 'entao' comando* 'senao' comando* 'fimse';

comandoRepeticao:
    'para' ID 'de' expressao 'ate' expressao 'faca' comando* 'fimpara';

// Regras para tokens

ID: [a-zA-Z]+;
NUMERO_INTEIRO: [0-9]+;
NUMERO_REAL: [0-9]+'.'[0-9]+;

// Ignorar espaços em branco e comentários

WS: [ \t\r\n]+ -> skip;
COMMENT: '//' .* -> skip;