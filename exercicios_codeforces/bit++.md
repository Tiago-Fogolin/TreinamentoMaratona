Link: https://codeforces.com/problemset/problem/282/A

## A. Bit++

| Limite de Tempo | Limite de Memória |
| :--- | :--- |
| 1.0 segundo | 256 megabytes |

### Descrição do Problema

A linguagem de programação clássica de Bitland é o Bit++. Esta linguagem é muito peculiar e complicada.

A linguagem é tão peculiar que possui exatamente uma variável, chamada **$x$**. Além disso, existem duas operações:
1.  A operação **++** aumenta o valor da variável $x$ em 1.
2.  A operação **--** diminui o valor da variável $x$ em 1.

Uma instrução na linguagem Bit++ é uma sequência que consiste em exatamente uma operação e uma variável $x$. A instrução é escrita sem espaços, ou seja, pode conter apenas os caracteres "+", "-" e "X". Executar uma instrução significa aplicar a operação que ela contém.

Um programa em Bit++ é uma sequência de instruções, e cada uma delas precisa ser executada. Executar um programa significa executar todas as instruções contidas nele.

Você recebeu um programa na linguagem Bit++. O valor inicial de $x$ é **0**. Execute o programa e encontre seu valor final (o valor da variável após a execução de todas as instruções).

### Entrada

A primeira linha contém um único inteiro $n$ ($1 \le n \le 150$) — o número de instruções no programa.

As próximas $n$ linhas contêm uma instrução cada. Cada instrução contém exatamente uma operação (**++** ou **--**) e exatamente uma variável **x** (representada pela letra "X"). Portanto, não existem instruções vazias. A operação e a variável podem ser escritas em qualquer ordem (ex: `++X`, `X++`, `--X`, `X--`).

### Saída

Imprima um único inteiro — o valor final de **$x$**.

### Exemplos

| Entrada (Input) | Saída (Output) |
| :--- | :--- |
| `1` <br> `++X` | `1` |
| `2` <br> `X++` <br> `--X` | `0` |