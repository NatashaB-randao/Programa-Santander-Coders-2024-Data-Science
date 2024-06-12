# Métodos e Funções de Listas em Python

# Listas em Python vêm com vários métodos e funções integradas que permitem realizar operações comuns.

# 1. append():
# Adiciona um elemento ao final da lista.
frutas = ["maçã", "banana", "cereja"]
frutas.append("manga")
print("Após append:", frutas)

# 2. insert():
# Insere um elemento em uma posição específica.
frutas.insert(1, "abacaxi")
print("Após insert:", frutas)

# 3. remove():
# Remove a primeira ocorrência de um elemento específico.
frutas.remove("banana")
print("Após remove:", frutas)

# 4. pop():
# Remove e retorna o elemento em uma posição específica (ou o último elemento se nenhum índice for especificado).
ultima_fruta = frutas.pop()
print("Após pop:", frutas)
print("Fruta removida:", ultima_fruta)

# 5. clear():
# Remove todos os elementos da lista.
frutas.clear()
print("Após clear:", frutas)

# 6. index():
# Retorna o índice da primeira ocorrência de um elemento específico.
frutas = ["maçã", "banana", "cereja"]
indice_cereja = frutas.index("cereja")
print("Índice de 'cereja':", indice_cereja)

# 7. count():
# Retorna o número de vezes que um elemento aparece na lista.
contagem_banana = frutas.count("banana")
print("Contagem de 'banana':", contagem_banana)

# 8. sort():
# Ordena os elementos da lista em ordem crescente (ou decrescente, se especificado).
numeros = [5, 2, 9, 1, 5, 6]
numeros.sort()
print("Após sort crescente:", numeros)
numeros.sort(reverse=True)
print("Após sort decrescente:", numeros)

# 9. reverse():
# Inverte a ordem dos elementos na lista.
numeros.reverse()
print("Após reverse:", numeros)

# 10. copy():
# Retorna uma cópia superficial da lista.
copia_frutas = frutas.copy()
print("Cópia da lista de frutas:", copia_frutas)

# Funções úteis com listas:

# 11. len():
# Retorna o número de elementos na lista.
tamanho = len(frutas)
print("Tamanho da lista de frutas:", tamanho)

# 12. sum():
# Retorna a soma dos elementos na lista (funciona com listas de números).
soma_numeros = sum(numeros)
print("Soma dos números:", soma_numeros)

# 13. max():
# Retorna o maior elemento da lista.
max_numero = max(numeros)
print("Maior número:", max_numero)

# 14. min():
# Retorna o menor elemento da lista.
min_numero = min(numeros)
print("Menor número:", min_numero)

# 15. list():
# Converte um iterável (como uma string ou tupla) em uma lista.
tupla = (1, 2, 3)
lista_tupla = list(tupla)
print("Lista convertida de tupla:", lista_tupla)

# Estes métodos e funções facilitam a manipulação de listas em Python, permitindo adicionar, remover, ordenar, e realizar outras operações comuns de maneira eficiente.
