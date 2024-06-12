# Exercícios de fixação I

"""
Muitas vezes é requerido o armazenamento de algum valor ou o resultado de alguma operação, para que os dados possam ser utilizados em outras partes do programa. Para que isso seja possível, o Python permite a criação de variáveis. Sabendo disso, considere o trecho de código a seguir:

"""
# var1 = 12

# var2 = 30

# var3 = var1 XXX var2

# print(var3)

# var3 = var3 YYY 2

# print(var3)

# --------

# Definindo as variáveis var1 e var2
var1 = 12
var2 = 30

# Realizando a operação matemática para obter o valor desejado em var3
var3 = var1 + var2

# Exibindo o valor atual de var3
print(var3)  # Resultado será 42

# Realizando outra operação para alterar o valor de var3
var3 = var3 / 2

# Exibindo o novo valor de var3
print(var3)  # Resultado será 21.0


""""
A instrução print(var3) exibe na tela o valor armazenado na variável var3, em cada uma das duas vezes que a instrução aparece no script acima. Para que os valores exibidos na tela sejam, nessa ordem, 42 e 21.0, quais operadores matemáticos devem substituir 'XXX' e 'YYY' no trecho de código, respectivamente?

Resposta
+ e /

"""


""""
Questão 2
Algumas situações requerem que os dados sejam recebidos diretamente pelo usuário como parte da execução do programa. Isso pode ser feito com a função input(). No entanto, esta função sempre retorna os valores em string. Assim, se os dados esperados do usuário forem numéricos, é importante realizar a conversão dos tipos de dados para que eles possam ser processados. Considere o trecho abaixo:

"""

# num1 = XXX

# dobro = 2*num1

# print("O dobro do número digitado é:", dobro)


# -----

# Questão 2: Conversão de Tipos

# Solicitando ao usuário um número e convertendo para inteiro
num1 = int(input("Digite um número a seguir: "))

# Dobrando o número inserido pelo usuário
dobro = 2 * num1

# Exibindo o dobro do número digitado pelo usuário
print("O dobro do número digitado é:", dobro)


""""
Levando em consideração que o usuário pode entregar qualquer número como input, o 'XXX' no código acima deve ser substituído por qual elemento?

Resposta:
int(input("Digite um número a seguir: "))

"""

""""
Questão 3
Para a construção de programas flexíveis e mais complexos, é necessário que haja a realização de comparações. Isso é possível com o uso de operadores lógicos de comparação (em python: ==, !=, <, <=, >, >=), como mostra o código:

"""
x = 10
y = 4.2

num = float(input("Digite um número a seguir: "))

print(num > x*y, num <= x + y, num*y != x*y)

""""
Suponha que na execução do script acima, o usuário digitou o valor 10, quando solicitado pelo input. Qual das alternativas a seguir produz o mesmo output que o script acima?

Resposta:
print(False, True, True)

"""

"""
Questão 4
Em muitos programas é necessário que mais de uma expressão lógica seja avaliada, de maneira composta. É possível realizar a composição lógica através dos operadores and e or do Python. Além disso, o operador not é utilizado para inverter o valor lógico de um booleano ou expressão lógica como um todo.


"""

x = 4.2

y = 10

z = "42"

not (((x * y == z) and not (x < y)) or y % 2 == 0)

#---

# Questão 4: Expressões Lógicas

# Definindo os valores de x, y e z
x = 4.2
y = 10
z = "42"

# Avaliando a expressão lógica e exibindo o resultado
print(not (((x * y == z) and not (x < y)) or y % 2 == 0))



""""
Qual das seguintes alternativas contém uma expressão que resulta no mesmo valor lógico (True ou False) que a última linha do código acima?

Resposta:
not ((x == y or True) and ((int(z) < x*y) and (type(y) == type(int(z)))))

"""


""""
Questão 5
Um dos principais usos destinados aos operadores lógicos é a construção de expressões condicionais, que são utilizadas para (re)direcionar o fluxo de um programa. Isso é possível com as expressões if, elif e else em Python.

"""

# a = int(input("Digite o primeiro número inteiro: "))
# b = int(input("Digite o segundo número inteiro: "))
# c = int(input("Digite o terceiro número inteiro: "))

# if a > b and a > c:
#     resposta = a % 2 == 0

# elif b > a and b > c:
#     resposta = b % 2 == 0

# else:
#     resposta = c % 2 == 0

# print(XXX, resposta)

""""
"O maior entre os três números informados é:" (ou seja, o programa exibe qual é o maior entre os três números informados).

"""

# Questão 5: Expressões Condicionais

# Solicitando ao usuário três números inteiros
a = int(input("Digite o primeiro número inteiro: "))
b = int(input("Digite o segundo número inteiro: "))
c = int(input("Digite o terceiro número inteiro: "))

# Verificando qual é o maior número entre os três
if a > b and a > c:
    resposta = "O maior número entre os três informados é: " + str(a)
elif b > a and b > c:
    resposta = "O maior número entre os três informados é: " + str(b)
else:
    resposta = "O maior número entre os três informados é: " + str(c)

# Exibindo a resposta
print(resposta)
