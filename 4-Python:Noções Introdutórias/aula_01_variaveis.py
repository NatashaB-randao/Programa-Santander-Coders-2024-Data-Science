'''
Variáveis em Python são como contêineres que armazenam dados, como números, textos ou objetos. Elas têm um nome que as identifica e um valor que representa o dado armazenado. Aqui está uma explicação passo a passo:

'''



# Declaração de variáveis
idade = 25
nome = "João"

# Tipos de dados
# Python permite diferentes tipos de dados em variáveis
# como números inteiros (int), números de ponto flutuante (float),
# strings (str), listas (list), entre outros.

# Atribuição e reatribuição
# Você pode atribuir um valor a uma variável usando o operador de atribuição =
# e também reatribuir um novo valor a ela.
idade = 30

# Uso das variáveis
# Depois de declaradas, você pode usar as variáveis em expressões e instruções
# para realizar operações ou exibir informações.
print(nome + " tem " + str(idade) + " anos.")

# Escopo das variáveis
# O escopo de uma variável é onde ela é acessível.
# Se uma variável é definida dentro de uma função, ela pode não ser acessível fora dela.
def minha_funcao():
    x = 10  # variável x só é acessível dentro desta função

minha_funcao()
# A seguinte linha geraria um erro, pois x não é definido aqui
# print(x)


