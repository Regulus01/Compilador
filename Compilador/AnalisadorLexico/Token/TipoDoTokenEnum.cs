namespace Compilador.AnalisadorLexico.Token;

public enum TipoDoTokenEnum
{
    EOF = -1,
    OPAD, // MAIS, MENOS
    OPMULT, // VEZES E DIV
    OPLOG, // OR E AND
    OPNEG, // NEGAÇÃO
    OPREL, // MENOR, MAIOR ETC
    
    //Simbolos
    PVIG, // ;
    PONTO, // .
    DPONTOS, // :
    VIG,   // ,
    ABPAR, // (
    FPAR,  // )
    ATRIB, // :=
    
    
    NUM
    
}