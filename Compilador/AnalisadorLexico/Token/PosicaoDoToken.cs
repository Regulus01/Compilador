namespace Compilador.AnalisadorLexico.Token;

public class PosicaoDoToken
{
    public int Linha { get; private set; }
    public int Indice { get; private set; }
    public int Coluna { get; private set; }

    public PosicaoDoToken(int linha, int indice, int coluna)
    {
        Linha = linha;
        Indice = indice;
        Coluna = coluna;
    }
}