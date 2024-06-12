# Conversão de Tipos em Python

# Em Python, você pode converter um tipo de dado em outro utilizando funções específicas ou construtores de tipos.

# 1. Conversão de Inteiro para String:
# Utilize a função str() para converter um inteiro em uma string.
exemplo_int_para_str = str(10)  # Resultado será uma string '10'

# 2. Conversão de String para Inteiro:
# Utilize a função int() para converter uma string em um inteiro.
exemplo_str_para_int = int("20")  # Resultado será o inteiro 20

# 3. Conversão de String para Float:
# Utilize a função float() para converter uma string em um número de ponto flutuante.
exemplo_str_para_float = float("3.14")  # Resultado será o número de ponto flutuante 3.14

# 4. Conversão de Float para Inteiro:
# Utilize a função int() para converter um número de ponto flutuante em um inteiro.
exemplo_float_para_int = int(3.9)  # Resultado será o inteiro 3 (parte inteira de 3.9)

# 5. Conversão de Inteiro para Float:
# A conversão de inteiro para float é implícita ao realizar operações com números de ponto flutuante.
exemplo_int_para_float = 10 / 2  # Resultado será o número de ponto flutuante 5.0

# 6. Conversão de Booleano para Inteiro:
# Utilize a função int() para converter um valor booleano em 0 (False) ou 1 (True).
exemplo_bool_para_int = int(True)  # Resultado será o inteiro 1

# 7. Conversão de Inteiro para Booleano:
# Qualquer número inteiro diferente de zero é considerado True quando convertido para booleano.
exemplo_int_para_bool = bool(10)  # Resultado será True

# 8. Conversão de String para Booleano:
# Utilize expressões condicionais para converter uma string em um valor booleano.
exemplo_str_para_bool = bool("True")  # Resultado será True (considerando qualquer string não vazia como True)

# 9. Conversão de Lista para String:
# Utilize a função join() para converter uma lista em uma única string.
exemplo_lista_para_str = ", ".join(["apple", "banana", "cherry"])  # Resultado será a string 'apple, banana, cherry'

# 10. Conversão de String para Lista:
# Utilize o método split() para dividir uma string em uma lista de substrings.
exemplo_str_para_lista = "apple, banana, cherry".split(", ")  # Resultado será a lista ['apple', 'banana', 'cherry']
