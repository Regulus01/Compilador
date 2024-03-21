namespace Compilador.AnalisadorLexico.Token;

public class Token
{
    public TipoDoTokenEnum Tipo { get; private set; }
    public string Valor { get; private set; }
    public PosicaoDoToken Posicao { get; private set; }

    public Token(TipoDoTokenEnum tipo, string valor, PosicaoDoToken posicao)
    {
        Tipo = tipo;
        Valor = valor;
        Posicao = posicao;
    }
    
    public override string ToString()
    {
        var tipo = $"Token: Tipo: {Tipo}";
        var valor = $"Valor: {Valor}";
        var posicao = $"Posicao => Index: {Posicao.Indice}";
        var linha = $"Linha: {Posicao.Linha}";
        var coluna = $"Coluna: {Posicao.Coluna}";

        return $"{tipo}, {valor}, {posicao}, {linha}, {coluna}";
    }
}