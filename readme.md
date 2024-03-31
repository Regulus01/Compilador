# Gerador de código lexico/sintatico com Antrl4

![img.png](img.png)

## O que é?

O **ANTLR4** (Another Tool for Language Recognition) é um gerador de parsers poderoso usado para ler, processar, 
executar ou traduzir arquivos de texto estruturado ou binário.
Ele é bastante utilizado na construção de linguagens, ferramentas e frameworks.

Para mais informações acesse a documentação em https://www.antlr.org/.

## Como instalar?
1. Abra algum terminal na pasta do arquivo
2. Utilize pip install -r requirements.txt.

### Gerando novos arquivos do compilador .py a partir do Simple.g4
1. No windows utilize -> **Cd Gerador**
2. Execute o seguinte comando -> **java -jar antlr4-4.13.1.jar -Dlanguage=Python3 Simple.g4**
3. Coloque o código desejado no arquivo **CodigoTeste.txt** 

## Observações
* É necessário ter algum SDK do java instalado