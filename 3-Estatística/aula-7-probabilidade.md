## O que é Probabilidade?

Probabilidade é a medida da chance de que um evento ocorra. Ela varia de 0 a 1, onde 0 significa que o evento não pode acontecer, e 1 significa que o evento certamente acontecerá.

### Conceitos Básicos:

1. **Experimento Aleatório:**
   - Um experimento cujo resultado não pode ser previsto com certeza. Exemplo: jogar uma moeda.

2. **Evento:**
   - Um possível resultado ou um conjunto de resultados de um experimento aleatório. Exemplo: obter "cara" ao jogar uma moeda.

3. **Espaço Amostral (S):**
   - O conjunto de todos os resultados possíveis de um experimento aleatório. Exemplo: ao jogar uma moeda, o espaço amostral é {cara, coroa}.

### Calculando a Probabilidade:

A probabilidade de um evento é calculada usando a fórmula:

```
Probabilidade (P) = Número de resultados favoráveis / Número total de resultados possíveis
```

### Exemplos:

1. **Moeda:**
   - Jogando uma moeda, a probabilidade de obter "cara" é:

```
P(cara) = 1/2 = 0.5
```

2. **Dado:**
   - Jogando um dado de seis faces, a probabilidade de obter um "4" é:

```
P(4) = 1/6
```

### Definições de Probabilidade

#### Definição Clássica

A definição clássica de probabilidade é baseada em resultados igualmente prováveis. Foi proposta pelo matemático francês Pierre-Simon Laplace no século XVIII. Esta definição é adequada quando todos os resultados possíveis de um experimento são igualmente prováveis.

**Fórmula:**

```
Probabilidade (P) = Número de resultados favoráveis / Número total de resultados possíveis
```

**Exemplo:**

1. **Moeda:**
   - Jogando uma moeda, a probabilidade de obter "cara" é:
   
   ```
   P(cara) = 1/2 = 0.5
   ```

2. **Dado:**
   - Jogando um dado de seis faces, a probabilidade de obter um "4" é:
   
   ```
   P(4) = 1/6
   ```

#### Definição Frequentista

A definição frequentista de probabilidade é baseada na frequência relativa de um evento à medida que o número de experimentos se aproxima do infinito. Esta definição é útil em situações em que os eventos não são necessariamente igualmente prováveis e é amplamente utilizada na inferência estatística.

**Fórmula:**

```
Probabilidade (P) = Limite da frequência relativa conforme o número de experimentos tende ao infinito
```

**Exemplo:**

1. **Lançamento de Moeda:**
   - Se você jogar uma moeda 100 vezes e obtiver "cara" 55 vezes, a probabilidade empírica de obter "cara" é:
   
   ```
   P(cara) = 55/100 = 0.55
   ```

2. **Qualquer Experimento Aleatório:**
   - A probabilidade de um evento E após n tentativas é:
   
   ```
   P(E) = (Número de vezes que E ocorreu) / n
   ```

#### Definição Axiomática

A definição axiomática de probabilidade foi introduzida pelo matemático russo Andrey Kolmogorov em 1933. Ela se baseia em um conjunto de axiomas (regras fundamentais) que formam a base para a teoria da probabilidade.

Os três axiomas de Kolmogorov são:

1. **Axioma da Não-Negatividade:**
   - Para qualquer evento \(A\), a probabilidade de \(A\) é um número não-negativo.
   ```
   P(A) \geq 0
   ```

2. **Axioma da Unidade:**
   - A probabilidade do espaço amostral \(S\) é 1.
   ```
   P(S) = 1
   ```

3. **Axioma da Aditividade:**
   - Para quaisquer dois eventos mutuamente exclusivos \(A\) e \(B\),
   ```
   P(A \cup B) = P(A) + P(B)
   ```

**Exemplo:**

1. **Eventos Mutuamente Exclusivos:**
   - Se você tem um baralho de cartas e seleciona uma carta, a probabilidade de escolher um ás ou um rei (considerando que não podem ser escolhidos simultaneamente) é:
   ```
   P(\text{ás} \cup \text{rei}) = P(\text{ás}) + P(\text{rei}) = \frac{4}{52} + \frac{4}{52} = \frac{8}{52} = \frac{2}{13}
   ```

### Conceitos Adicionais:

1. **Eventos Independentes:**
   - Dois eventos são independentes se a ocorrência de um não afeta a ocorrência do outro. Exemplo: Jogar duas moedas.

2. **Eventos Mutuamente Exclusivos:**
   - Dois eventos são mutuamente exclusivos se não podem acontecer ao mesmo tempo. Exemplo: Obter "cara" e "coroa" no mesmo lançamento de uma moeda.

### Resumo:

- **Definição Clássica:** Baseada em resultados igualmente prováveis, adequada para situações com um número finito de resultados igualmente prováveis.
  
- **Definição Frequentista:** Baseada na frequência relativa de um evento, adequada para grandes conjuntos de dados e experimentos repetitivos.

- **Definição Axiomática:** Baseada em um conjunto de axiomas fundamentais, fornece uma base rigorosa e generalizada para a teoria da probabilidade.

Probabilidade é uma ferramenta matemática que mede a chance de eventos ocorrerem. Usamos frações ou porcentagens para expressar essa chance, baseando-nos em espaços amostrais e resultados favoráveis.

---