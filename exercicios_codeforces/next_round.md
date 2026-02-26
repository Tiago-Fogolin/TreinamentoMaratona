Link: https://codeforces.com/problemset/problem/158/A

## A. Próxima Rodada (Next Round)

| Limite de Tempo | Limite de Memória |
| :--- | :--- |
| 3.0 segundos | 256 megabytes |

### Descrição do Problema

"O competidor que obtiver uma pontuação igual ou maior que a pontuação do competidor que ficou em $k$-ésimo lugar avançará para a próxima rodada, desde que o competidor obtenha uma pontuação positiva..." — um trecho das regras do concurso.

Um total de $n$ participantes participaram do concurso ($n \ge k$), e você já conhece as suas pontuações. Calcule quantos participantes avançarão para a próxima rodada.

### Entrada

A primeira linha da entrada contém dois inteiros $n$ e $k$ ($1 \le k \le n \le 50$) separados por um único espaço.

A segunda linha contém $n$ inteiros separados por espaços $a_1, a_2, ..., a_n$ ($0 \le a_i \le 100$), onde $a_i$ é a pontuação obtida pelo participante que ficou em $i$-ésimo lugar. A sequência fornecida é **não-crescente** (ou seja, para todo $i$ de $1$ a $n-1$, a condição $a_i \ge a_{i+1}$ é satisfeita).

### Saída

Imprima o número de participantes que avançarão para a próxima rodada.

### Exemplos

| Entrada (Input) | Saída (Output) |
| :--- | :--- |
| `8 5` <br> `10 9 8 7 7 7 5 5` | `6` |
| `4 2` <br> `0 0 0 0` | `0` |

---

### Notas dos Exemplos

No **primeiro exemplo**, o participante em 5º lugar obteve 7 pontos. Como o participante em 6º lugar também obteve 7 pontos, existem 6 classificados.

No **segundo exemplo**, ninguém obteve uma pontuação positiva (maior que zero).