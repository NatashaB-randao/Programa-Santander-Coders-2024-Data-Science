Claro! Aqui está uma explicação clara e concisa sobre Análise Combinatória, incluindo o Princípio Fundamental da Contagem e os diferentes tipos de agrupamentos, formatada em Markdown:

---

## Análise Combinatória

A Análise Combinatória é uma área da matemática que estuda as maneiras de contar, agrupar e organizar objetos. 

### Princípio Fundamental da Contagem (PFC)

O Princípio Fundamental da Contagem é uma regra básica usada para calcular o número de maneiras de realizar uma sequência de eventos. 

**Regra:**

Se um evento pode ocorrer de \( n_1 \) maneiras, um segundo evento pode ocorrer de \( n_2 \) maneiras, e assim por diante, o número total de maneiras que a sequência de eventos pode ocorrer é:

```
n_1 \times n_2 \times n_3 \times \ldots \times n_k
```

**Exemplo:**

Se você tem 3 camisas e 2 calças, o número total de combinações de uma camisa e uma calça é:

```
3 \times 2 = 6
```

### Tipos de Agrupamentos

#### Arranjo

Arranjos são agrupamentos de elementos onde a ordem importa.

**Fórmula:**

Para arranjos de \( n \) elementos tomados \( p \) a \( p \):

```
A(n, p) = \frac{n!}{(n-p)!}
```

**Exemplo:**

Quantos arranjos diferentes podem ser feitos com 3 das 5 letras A, B, C, D, E?

```
A(5, 3) = \frac{5!}{(5-3)!} = \frac{5!}{2!} = \frac{120}{2} = 60
```

#### Permutação Simples

Permutações são agrupamentos de todos os elementos onde a ordem importa.

**Fórmula:**

Para permutações de \( n \) elementos:

```
P(n) = n!
```

**Exemplo:**

Quantas maneiras diferentes podemos ordenar 4 letras A, B, C, D?

```
P(4) = 4! = 24
```

#### Permutação com Repetição

Permutações de elementos onde alguns elementos podem se repetir.

**Fórmula:**

Para permutações de \( n \) elementos com repetições:

```
P(n; n_1, n_2, \ldots, n_k) = \frac{n!}{n_1! \times n_2! \times \ldots \times n_k!}
```

**Exemplo:**

Quantas maneiras diferentes podemos ordenar as letras da palavra "BANANA"?

```
P(6; 1, 3, 2) = \frac{6!}{1! \times 3! \times 2!} = \frac{720}{1 \times 6 \times 2} = \frac{720}{12} = 60
```

#### Combinação

Combinações são agrupamentos de elementos onde a ordem não importa.

**Fórmula:**

Para combinações de \( n \) elementos tomados \( p \) a \( p \):

```
C(n, p) = \frac{n!}{p! \times (n-p)!}
```

**Exemplo:**

Quantas combinações de 3 letras podem ser feitas a partir de 5 letras A, B, C, D, E?

```
C(5, 3) = \frac{5!}{3! \times (5-3)!} = \frac{120}{6 \times 2} = \frac{120}{12} = 10
```

### Resumo:

- **Princípio Fundamental da Contagem (PFC):** Multiplica as opções de cada evento.
- **Arranjo:** Ordem importa, usa parte dos elementos.
- **Permutação Simples:** Ordem importa, usa todos os elementos.
- **Permutação com Repetição:** Ordem importa, com elementos repetidos.
- **Combinação:** Ordem não importa.

---