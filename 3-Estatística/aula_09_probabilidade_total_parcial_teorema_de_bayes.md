### Probabilidade Total
A probabilidade total é usada para calcular a probabilidade de um evento considerando todas as possíveis formas (ou caminhos) de ocorrer esse evento. Utiliza a ideia de eventos condicionais e a decomposição de um evento em eventos mutuamente exclusivos e exaustivos. A fórmula é:

\[ P(A) = \sum P(A \cap B_i) = \sum P(A | B_i) \cdot P(B_i) \]

Onde \( B_i \) são eventos que formam uma partição do espaço amostral.

### Probabilidade Condicional
A probabilidade condicional mede a probabilidade de um evento A ocorrer, dado que um evento B já ocorreu. É representada como \( P(A | B) \) e é calculada assim:

\[ P(A | B) = \frac{P(A \cap B)}{P(B)} \]

Se \( P(B) > 0 \).

### Teorema de Bayes
O Teorema de Bayes relaciona a probabilidade condicional de eventos. Ele permite atualizar a probabilidade de um evento com base em novas informações. A fórmula é:

\[ P(A | B) = \frac{P(B | A) \cdot P(A)}{P(B)} \]

Onde:
- \( P(A | B) \) é a probabilidade de A dado B.
- \( P(B | A) \) é a probabilidade de B dado A.
- \( P(A) \) e \( P(B) \) são as probabilidades de A e B ocorrerem independentemente.

### Exemplo Ilustrativo
Suponha que temos duas caixas de bolas. A Caixa 1 tem 3 bolas vermelhas e 2 azuis. A Caixa 2 tem 1 bola vermelha e 4 azuis. Queremos saber a probabilidade de pegar uma bola vermelha após escolher aleatoriamente uma das caixas.

1. **Probabilidade Total:**
   - \( P(Bola \ Vermelha) = P(Bola \ Vermelha \ | \ Caixa \ 1) \cdot P(Caixa \ 1) + P(Bola \ Vermelha \ | \ Caixa \ 2) \cdot P(Caixa \ 2) \)

2. **Probabilidade Condicional:**
   - \( P(Bola \ Vermelha \ | \ Caixa \ 1) = \frac{3}{5} \)
   - \( P(Bola \ Vermelha \ | \ Caixa \ 2) = \frac{1}{5} \)

3. **Teorema de Bayes:**
   - Queremos a probabilidade de ter escolhido a Caixa 1 dado que pegamos uma bola vermelha.
   - \( P(Caixa \ 1 | Bola \ Vermelha) = \frac{P(Bola \ Vermelha | Caixa \ 1) \cdot P(Caixa \ 1)}{P(Bola \ Vermelha)} \)

Usando essas fórmulas, podemos calcular as probabilidades relevantes de maneira sistemática.

Esses conceitos são fundamentais na teoria das probabilidades e têm aplicações em diversas áreas como estatística, ciência de dados, inteligência artificial, entre outras.