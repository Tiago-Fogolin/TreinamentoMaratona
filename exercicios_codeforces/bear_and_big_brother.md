Link: https://codeforces.com/problemset/problem/791/A

## A. Urso e o Irmão Mais Velho (Bear and Big Brother)

| Limite de Tempo | Limite de Memória |
| :--- | :--- |
| 1.0 segundo | 256 megabytes |

### Descrição do Problema

O urso Limak quer se tornar o maior de todos os ursos, ou pelo menos tornar-se maior que seu irmão Bob.

Atualmente, Limak e Bob pesam **$a$** e **$b$**, respectivamente. É garantido que o peso de Limak é menor ou igual ao peso de seu irmão.

Limak come muito e seu peso **triplica** a cada ano, enquanto o peso de Bob **dobra** a cada ano.



Depois de quantos anos inteiros Limak se tornará **estritamente maior** (estritamente mais pesado) que Bob?

### Entrada

A única linha da entrada contém dois inteiros **$a$** e **$b$** ($1 \le a \le b \le 10$) — o peso de Limak e o peso de Bob, respectivamente.

### Saída

Imprima um único inteiro, indicando o número de anos após os quais Limak se tornará estritamente maior que Bob.

### Exemplos

| Entrada (Input) | Saída (Output) |
| :--- | :--- |
| `4 7` | `2` |
| `4 9` | `3` |
| `1 1` | `1` |

---

### Notas dos Exemplos

1. **No primeiro exemplo:** Limak pesa 4 e Bob pesa 7 inicialmente. 
   - Após um ano, os pesos são: $4 \cdot 3 = 12$ e $7 \cdot 2 = 14$. Limak ainda não é maior que Bob.
   - Após o segundo ano, os pesos são: $12 \cdot 3 = 36$ e $14 \cdot 2 = 28$. 
   - Como 36 é maior que 28, Limak tornou-se maior que Bob após **2 anos**.

2. **No segundo exemplo:** Os pesos de Limak e Bob nos anos seguintes são:
   - Ano 1: 12 e 18.
   - Ano 2: 36 e 36.
   - Ano 3: 108 e 72. 
   - A resposta é **3**. Lembre-se que Limak quer ser estritamente maior, pesos iguais não o satisfazem.