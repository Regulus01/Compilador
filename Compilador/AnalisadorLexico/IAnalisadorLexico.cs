using Compilador.AnalisadorLexico.Token;

namespace Compilador.AnalisadorLexico;

public interface IAnalisadorLexico
{
    IEnumerable<Token.Token> CriarToken(string source);
    void AdicionarDefinicao(DefinicaoDoToken definicaoDoToken);
}