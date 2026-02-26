Link: https://codeforces.com/problemset/problem/50/A

## A. Empilhamento de Dominós (Domino Piling)

| Limite de Tempo | Limite de Memória |
| :--- | :--- |
| 2.0 segundos | 256 megabytes |

### Descrição do Problema

Você recebeu um tabuleiro retangular de $M \times N$ quadrados. Além disso, você tem um número ilimitado de peças de dominó padrão de $2 \times 1$ quadrados. Você pode rotacionar as peças. Sua tarefa é colocar o maior número possível de dominós no tabuleiro respeitando as seguintes condições:

1. Cada dominó cobre completamente dois quadrados.
2. Dois dominós não podem se sobrepor.
3. Cada dominó deve estar inteiramente dentro do tabuleiro. É permitido tocar as bordas do tabuleiro.

Encontre o número máximo de dominós que podem ser colocados sob essas restrições.

### Entrada

Em uma única linha, são fornecidos dois inteiros $M$ e $N$ — as dimensões do tabuleiro em quadrados ($1 \le M \le N \le 16$).

### Saída

Imprima um único número — o número máximo de dominós que podem ser colocados.

### Exemplos

| Entrada (Input) | Saída (Output) |
| :--- | :--- |
| `2 4` | `4` |
| `3 3` | `4` |