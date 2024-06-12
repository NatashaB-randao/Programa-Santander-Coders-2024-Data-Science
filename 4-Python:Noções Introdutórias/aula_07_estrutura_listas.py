# Estrutura de Listas em Python

# Listas são uma estrutura de dados que permitem armazenar múltiplos itens em uma única variável.
# Em Python, as listas são definidas usando colchetes [].

# 1. Criando uma Lista:
# Você pode criar uma lista com valores iniciais.
frutas = ["maçã", "banana", "cereja"]
print("Lista de frutas:", frutas)

# 2. Acessando Elementos da Lista:
# Os elementos da lista podem ser acessados usando índices. O índice começa em 0.
primeira_fruta = frutas[0]
print("Primeira fruta:", primeira_fruta)

# 3. Modificando Elementos da Lista:
# Você pode modificar um elemento da lista atribuindo um novo valor ao índice correspondente.
frutas[1] = "laranja"
print("Lista modificada:", frutas)

# 4. Adicionando Elementos à Lista:
# Use a função append() para adicionar um elemento ao final da lista.
frutas.append("manga")
print("Lista após adicionar manga:", frutas)

# 5. Inserindo Elementos em uma Posição Específica:
# Use a função insert() para adicionar um elemento em uma posição específica.
frutas.insert(1, "abacaxi")
print("Lista após inserir abacaxi na posição 1:", frutas)

# 6. Removendo Elementos da Lista:
# Use a função remove() para remover a primeira ocorrência de um elemento específico.
frutas.remove("cereja")
print("Lista após remover cereja:", frutas)

# Use a função pop() para remover um elemento pelo índice. Se nenhum índice for especificado, o último elemento é removido.
ultima_fruta = frutas.pop()
print("Lista após remover a última fruta:", frutas)
print("Última fruta removida:", ultima_fruta)

# 7. Comprimento da Lista:
# Use a função len() para obter o número de elementos na lista.
comprimento = len(frutas)
print("Comprimento da lista de frutas:", comprimento)

# 8. Iterando sobre uma Lista:
# Use um laço for para iterar sobre os elementos de uma lista.
for fruta in frutas:
    print("Fruta:", fruta)

# 9. Verificando a Presença de um Elemento na Lista:
# Use o operador in para verificar se um elemento está presente na lista.
tem_banana = "banana" in frutas
print("Tem banana na lista?", tem_banana)

# 10. Listas Aninhadas:
# Listas podem conter outras listas, criando listas aninhadas.
listas_aninhadas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Listas aninhadas:", listas_aninhadas)

# Acessando elementos em listas aninhadas:
elemento = listas_aninhadas[1][2]
print("Elemento na segunda lista, terceira posição:", elemento)

# 11. Fatiamento de Listas:
# Você pode obter uma sublista usando fatiamento (slice).
sublista = frutas[1:3]
print("Sublista de frutas:", sublista)

# Listas são uma estrutura de dados flexível e poderosa em Python, permitindo armazenar e manipular coleções de itens de forma eficiente.
