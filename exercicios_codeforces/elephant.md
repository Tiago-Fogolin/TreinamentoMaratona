Link: https://codeforces.com/problemset/problem/617/A

## A. Elefante (Elephant)

| Limite de Tempo | Limite de Memória |
| :--- | :--- |
| 1.0 segundo | 256 megabytes |

### Descrição do Problema

Um elefante decidiu visitar seu amigo. Acontece que a casa do elefante está localizada no ponto **0** e a casa de seu amigo está localizada no ponto **$x$** ($x > 0$) de uma linha coordenada.

Em um passo, o elefante pode se mover **1, 2, 3, 4 ou 5** posições para frente. Determine qual é o número mínimo de passos que ele precisa dar para chegar à casa de seu amigo.



### Entrada

A primeira linha da entrada contém um inteiro **$x$** ($1 \le x \le 1.000.000$) — a coordenada da casa do amigo.

### Saída

Imprima o número mínimo de passos que o elefante precisa dar para ir do ponto 0 ao ponto $x$.

### Exemplos

| Entrada (Input) | Saída (Output) |
| :--- | :--- |
| `5` | `1` |
| `12` | `3` |

---

### Notas dos Exemplos

1. **No primeiro exemplo:** O elefante só precisa dar um passo de comprimento 5 para chegar ao ponto $x$.
2. **No segundo exemplo:** O elefante pode chegar ao ponto $x$ se ele se mover, por exemplo, 3, 5 e 4 posições. Existem outras formas de obter a resposta ideal, mas o elefante não consegue chegar em $x$ com menos de três movimentos.