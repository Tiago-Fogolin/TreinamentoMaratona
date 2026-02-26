Link: https://codeforces.com/problemset/problem/263/A

## A. Matriz Bonita (Beautiful Matrix)

| Limite de Tempo | Limite de Memória |
| :--- | :--- |
| 2.0 segundos | 256 megabytes |

### Descrição do Problema

Você recebeu uma matriz de $5 \times 5$, composta por 24 zeros e um único número um. Vamos indexar as linhas da matriz por números de 1 a 5, de cima para baixo, e as colunas da matriz por números de 1 a 5, da esquerda para a direita.

Em um movimento, você tem permissão para aplicar uma das duas transformações a seguir na matriz:
1. Trocar duas linhas adjacentes da matriz, ou seja, linhas com índices $i$ e $i + 1$ para algum inteiro $i$ ($1 \le i < 5$).
2. Trocar duas colunas adjacentes da matriz, ou seja, colunas com índices $j$ e $j + 1$ para algum inteiro $j$ ($1 \le j < 5$).

Você considera que uma matriz parece **bonita** se o único número um da matriz estiver localizado exatamente no seu centro (na célula que está na interseção da terceira linha e da terceira coluna). Calcule o número mínimo de movimentos necessários para tornar a matriz bonita.



### Entrada

A entrada consiste em cinco linhas, cada uma contendo cinco inteiros: o $j$-ésimo inteiro na $i$-ésima linha da entrada representa o elemento da matriz que está localizado na interseção da $i$-ésima linha e da $j$-ésima coluna. É garantido que a matriz consiste em 24 zeros e um único número um.

### Saída

Imprima um único inteiro — o número mínimo de movimentos necessários para tornar a matriz bonita.

### Exemplos

| Entrada (Input) | Saída (Output) |
| :--- | :--- |
| `0 0 0 0 0` <br> `0 0 0 0 1` <br> `0 0 0 0 0` <br> `0 0 0 0 0` <br> `0 0 0 0 0` | `3` |
| `0 0 0 0 0` <br> `0 0 0 0 0` <br> `0 1 0 0 0` <br> `0 0 0 0 0` <br> `0 0 0 0 0` | `1` |