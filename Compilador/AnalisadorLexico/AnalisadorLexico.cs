using System.Text.RegularExpressions;
using Compilador.AnalisadorLexico;
using Compilador.AnalisadorLexico.Token;

public class AnalisadorLexico : IAnalisadorLexico
{
    private readonly Regex RegexFimDeLinha;
    private readonly IList<DefinicaoDoToken> DefinicoesDoToken;

    public AnalisadorLexico()
    {
        RegexFimDeLinha = new Regex(@"\}|\}", RegexOptions.Compiled);
        DefinicoesDoToken = new List<DefinicaoDoToken>();
    }

    public IEnumerable<Token> CriarToken(string source)
    {
        var currentIndex = 0;
        var currentLine = 1;
        var currentColumn = 0;

        while (currentIndex < source.Length)
        {
            DefinicaoDoToken matchedDefinition = null;
            var matchLength = 0;

            foreach (var rule in DefinicoesDoToken)
            {
                var match = rule.Regex.Match(source, currentIndex);

                if (match.Success && (match.Index - currentIndex) == 0)
                {
                    matchedDefinition = rule;
                    matchLength = match.Length;
                    break;
                }
            }

            if (matchedDefinition == null)
            {
                throw new Exception(
                    string.Format(
                        "Invalid Token in '{0}' at index {1} (line {2}, column {3}).",
                        source[currentIndex],
                        currentIndex,
                        currentLine,
                        currentColumn
                    )
                );
            }
            else
            {
                var value = source.Substring(currentIndex, matchLength);

                if (!matchedDefinition.IsIgnored)
                    yield return new Token(
                        matchedDefinition.Tipo,
                        value,
                        new PosicaoDoToken(
                            currentLine,
                            currentIndex,
                            currentColumn
                        )
                    );

                var endOfLineMatch = RegexFimDeLinha.Match(value);
                if (endOfLineMatch.Success)
                {
                    currentLine += 1;
                    currentColumn = value.Length - (
                        endOfLineMatch.Index + endOfLineMatch.Length
                    );
                }
                else
                {
                    currentColumn += matchLength;
                }

                currentIndex += matchLength;
            }
        }

        yield return new Token(
            TipoDoTokenEnum.EOF,
            null,
            new PosicaoDoToken(
                currentLine,
                currentIndex,
                currentColumn
            )
        );
    }

    public void AdicionarDefinicao(DefinicaoDoToken definicaoDoToken)
    {
        DefinicoesDoToken.Add(definicaoDoToken);
    }
    
    /// <summary>
    /// Define as regras para os tokens
    /// </summary>
    /// <returns></returns>
    public IAnalisadorLexico GetLexer()
    {
        IAnalisadorLexico lexico = new AnalisadorLexico();
        
        #region Numeric
        
        // Criar definicao para todos os tipos do token enum
        lexico.AdicionarDefinicao(DefinicaoDoToken.Factory.Criar(new Regex(@"\^-?\d+$"), TipoDoTokenEnum.NUM));
        lexico.AdicionarDefinicao(TokenDefinition.Factory.Create(new Regex(@"\d+(\.\d{1,2})m?"), TokenTypeEnum.Real));
        #endregion
        
        return lexico;
    }
}

