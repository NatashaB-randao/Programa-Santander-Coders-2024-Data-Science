"""
O que são Funções em Python?
Em Python, uma função é um bloco de código reutilizável que realiza uma tarefa específica. 
Ela recebe entrada (argumentos), executa operações definidas dentro dela e pode retornar um resultado.

Estrutura Básica de uma Função:
python
Copiar código
def nome_da_funcao(argumentos):
    # Corpo da função
    # Operações realizadas pela função
    return resultado  # Opcional, se a função retorna algum valor
Explicação Passo a Passo:
Definição da Função (def): Começa com a palavra-chave def, seguida pelo nome da função e parênteses (). 
Se a função aceitar argumentos, eles são especificados dentro dos parênteses.

Exemplo:

python
Copiar código
def saudacao(nome):
Corpo da Função: É o bloco de código indentado que contém as operações que a função executa quando é chamada. 
Todas as linhas indentadas após a definição pertencem ao corpo da função.

Exemplo:

python
Copiar código
def saudacao(nome):
    mensagem = f"Olá, {nome}!"
    print(mensagem)
Argumentos: São valores que podem ser passados para a função quando ela é chamada. Eles são opcionais, dependendo da função.

Exemplo:

python
Copiar código
def saudacao(nome):
Retorno (opcional): Algumas funções retornam um resultado após a execução. 
O valor retornado pode ser utilizado onde a função foi chamada.

Exemplo:

python
Copiar código
def soma(a, b):
    return a + b
Chamando uma Função:
Depois de definida, uma função pode ser chamada (ou "invocada") em qualquer parte do código.

Exemplo:

python
Copiar código
# Chamada da função saudacao
saudacao("Maria")
Neste exemplo, "Maria" é passado como argumento para a função saudacao. 
A função então executa suas operações (criando e imprimindo uma mensagem de saudação).

Benefícios das Funções:
Reutilização de Código: Evita repetição de código ao encapsular operações em funções.
Organização: Divide o programa em partes menores e mais gerenciáveis.
Legibilidade: Facilita a compreensão do código ao nomear e agrupar funcionalidades relacionadas.
Em resumo, funções são blocos de construção fundamentais em Python e em muitas outras linguagens de programação, 
permitindo modularidade, reutilização e organização eficiente do código.
"""

# Definição da função saudacao
def saudacao(nome):
    mensagem = f"Olá, {nome}!"
    print(mensagem)

# Exemplo de chamada da função
saudacao("Maria")

# Esta função imprime "Olá, Maria!" quando executada.
