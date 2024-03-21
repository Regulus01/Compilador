using System.Text.RegularExpressions;

namespace Compilador.AnalisadorLexico.Token;

public class DefinicaoDoToken
{
    public TipoDoTokenEnum Tipo { get; private set; }
    public Regex Regex { get; private set; }
    public bool IsIgnored { get; private set; }

    public DefinicaoDoToken(Regex regex, TipoDoTokenEnum tipo, bool isIgnored)
    {
        Tipo = tipo;
        Regex = regex;
        IsIgnored = isIgnored;
    }

    public static class Factory
    {
        public static DefinicaoDoToken Criar (
            Regex regex,
            TipoDoTokenEnum tipo,
            bool isIgnored = false
        )
        {
            return new DefinicaoDoToken(regex, tipo, isIgnored);
        }
    }
}