# Laços de Repetição "While" em Python

# O laço de repetição while permite executar repetidamente um bloco de código enquanto uma condição é verdadeira.

# 1. Estrutura Básica do Laço While:
# O laço while continua executando o bloco de código enquanto a condição especificada for verdadeira.
contador = 0
while contador < 5:
    print("Contador é:", contador)
    contador += 1  # Incrementa o contador

# 2. Usando o Laço While para Iterar Até uma Condição Ser Falsa:
# A condição é avaliada antes de cada iteração do laço. Se a condição for falsa, o laço é encerrado.
numero = 10
while numero > 0:
    print("Número é:", numero)
    numero -= 1  # Decrementa o número

# 3. Laços While com Condição de Parada Baseada em Entrada do Usuário:
# O laço pode continuar executando até que uma condição de parada seja atendida, como a entrada do usuário.
entrada = ""
while entrada != "sair":
    entrada = input("Digite algo (ou 'sair' para parar): ")
    print("Você digitou:", entrada)

# 4. Laços While Infinitos:
# Um laço while sem uma condição de término se torna um laço infinito. Use com cuidado e sempre forneça uma maneira de sair do laço.
# while True:
#     print("Este é um laço infinito.")
#     # Normalmente, você inclui uma instrução break para sair do laço em algum momento.

# 5. Usando Break para Sair do Laço While:
# A instrução break pode ser usada para sair do laço antes que a condição se torne falsa.
contador = 0
while contador < 10:
    if contador == 5:
        break  # Sai do laço quando contador for igual a 5
    print("Contador é:", contador)
    contador += 1

# 6. Usando Continue para Pular uma Iteração:
# A instrução continue pode ser usada para pular o restante do bloco de código na iteração atual e continuar com a próxima iteração.
contador = 0
while contador < 10:
    contador += 1
    if contador % 2 == 0:
        continue  # Pula para a próxima iteração se contador for par
    print("Contador é ímpar:", contador)

# Os laços while são úteis para executar um bloco de código repetidamente enquanto uma condição específica for verdadeira.
