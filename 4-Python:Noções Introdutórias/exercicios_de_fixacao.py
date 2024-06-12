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
float(input("Digite um número a seguir: "))

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
print(num == x*y, num*y == x*y, y > x + num)

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
not (((not True) or int(z) % 7 == 0) and ((str(int(x*y)) == z) and (type(x) !=

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
"O maior número entre os três informados é par?", (ou seja, o programa exibe, através de um booleano, se o maior entre os três números informados é par).
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

###

#Exercícios de fixação II


# Questão 1
# Em Python é possível utilizar expressões condicionais para o direcionamento de fluxo do código. Considere o trecho de código a seguir:
# x = int(input("Digite um número inteiro: "))

# if XXX:
#     resp1 = "negativo"
# else:
#     resp1 = "positivo"
    
# if ***:
#     resp2 = "par"
# else:
#     resp2 = "impar"
    

# print("
# O número {} é {} e {}.".format(x, resp1, resp2))
# O código acima informa se o número inteiro informado pelo usuário (e armazenado na variável x) é positivo ou negativo e par ou ímpar. Por exemplo, caso o usuário digite o número -42, o output esperado é:
# O número -42 é negativo e par.
# Para que este output seja possível, pelo que devemos substituir XXX e *** no código acima, respectivamente?

""""
Resposta: d) x < 0 e x % 2 == 0

x = int(input("Digite um número inteiro: "))

if x < 0:
    resp1 = "negativo"
else:
    resp1 = "positivo"
    
if x % 2 == 0:
    resp2 = "par"
else:
    resp2 = "ímpar"

print("O número {} é {} e {}.".format(x, resp1, resp2))


"""



# Questão 2
# É muito frequente o uso de programação para a automação de tarefas repetitivas, sendo possível devido às estruturas de repetição. Em python, uma dessas estruturas é o laço while, que determina que um bloco de código seja repetido enquanto uma dada condição for verdadeira. Observe o código a seguir:
# cont = 0
# resultado = 0
# n = 1000

# while cont != n:

#     resultado = resultado + 1/(2**cont)

#     cont = cont + 1

# print(resultado)
# Ao ser executado, o que o trecho de código acima mostra na tela?


""""
Resposta: b) A soma dos n (no caso, n = 1000) primeiros termos da série 1, 1/2, 1/4, 1/8,...

"""



# Questão 3
# Além do laço de repetição while, muitas vezes utilizamos o operador for em Python para implementarmos laços de repetição. Embora isso seja possível, o for é mais do que meramente um laço de repetição: este operador é utilizado para percorrer alguma estrutura iterável.
# for _ in range(10):

#    print("Olá, mundo!") 
# Quando queremos utilizar o for explicitamente como um laço de repetição, é muito comum utilizarmos a estrutura acima, com o auxílio do iterador range(). No entanto, o mesmo comportamento é possível se nos aproveitarmos do fato de que o for percorre qualquer iterável. Sabendo disso, das alternativas a seguir, qual é a única que NÃO reproduz o mesmo resultado que o trecho acima?

""""
Resposta: d) for _ in [10]: print("Olá, mundo!")

"""

# Questão 4
# Utilizamos listas para armazenar em um único objeto uma coleção de valores. Muitas vezes, desejamos criar uma nova lista a partir de uma lista original. Observe o código abaixo:
# lista_inicial = [10, 5, -7, 6, -42, 63, -8, -5, 13]

# lista_final = []

# for item in lista_inicial:

#     if item % 2 == 0:

#         if item < 0:

#             lista_final.append(A)
    
#         else:

#             lista_final.append(B)
#     else:

#         if item < 0:
            
#             lista_final.append(C)
    
#         else:

#             lista_final.append(D)
# Qual deve ser o valor de A, B, C e D, respectivamente, para que o código acima gere a seguinte lista_final: [10, 10, 14, 6, 42, 126, 8, 10, 26]?

""""
Resposta: b) -item, item, -2*item, 2*item

"""

# Questão 5
# Algumas funções podem nos ajudar a trabalhar com listas. Observe o código abaixo e o respectivo output desejado:
# animais = ['gato', 'coelho', 'macaco', 'girafa']

# animais.função1('gato')
# print(animais)
# print(função2(animais))
# print(animais.função3('coelho'))
# Output desejado:
# > ['coelho', 'macaco', 'girafa']
# > 3
# > 0
# Respectivamente, por quais funções devemos substituir função1, função2 e função3 no código acima, para obter o output desejado?


""""
Resposta: remove, len, index

"""