# Laços de Repetição "For" em Python

# O laço de repetição for é usado para iterar sobre uma sequência (como uma lista, tupla, string ou intervalo de números).

# 1. Estrutura Básica do Laço For:
# O laço for percorre cada item em uma sequência e executa o bloco de código para cada item.
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print("Número é:", numero)

# 2. Laços For com Strings:
# Você pode iterar sobre cada caractere em uma string.
palavra = "Python"
for letra in palavra:
    print("Letra é:", letra)

# 3. Usando a Função Range:
# A função range() é usada para gerar uma sequência de números.
# Exemplo com um intervalo de 0 a 4:
for i in range(5):
    print("Valor de i é:", i)

# Exemplo com um intervalo de 2 a 6:
for i in range(2, 7):
    print("Valor de i é:", i)

# Exemplo com um intervalo de 0 a 10 com passo 2:
for i in range(0, 11, 2):
    print("Valor de i com passo 2 é:", i)

# 4. Laços For com Listas:
# Você pode iterar sobre uma lista e realizar operações em cada item.
frutas = ["maçã", "banana", "cereja"]
for fruta in frutas:
    print("Fruta é:", fruta)

# 5. Usando Enumerate:
# A função enumerate() permite iterar sobre uma lista e ter acesso ao índice e ao valor ao mesmo tempo.
for indice, fruta in enumerate(frutas):
    print(f"Índice: {indice}, Fruta: {fruta}")

# 6. Laços For com Listas Aninhadas:
# Você pode usar laços for aninhados para iterar sobre listas de listas (ou listas bidimensionais).
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for linha in matriz:
    for elemento in linha:
        print("Elemento é:", elemento)

# 7. Usando Break em Laços For:
# A instrução break pode ser usada para sair do laço antes que ele termine normalmente.
for numero in numeros:
    if numero == 3:
        break  # Sai do laço quando numero for igual a 3
    print("Número é:", numero)

# 8. Usando Continue em Laços For:
# A instrução continue pode ser usada para pular o restante do bloco de código na iteração atual e continuar com a próxima iteração.
for numero in numeros:
    if numero % 2 == 0:
        continue  # Pula a iteração se numero for par
    print("Número ímpar é:", numero)

# Os laços for são úteis para iterar sobre sequências e realizar operações repetitivas em cada item da sequência.
