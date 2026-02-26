Link: https://codeforces.com/problemset/problem/339/A

## A. Matemática Útil (Helpful Maths)

| Limite de Tempo | Limite de Memória |
| :--- | :--- |
| 2.0 segundos | 256 megabytes |

### Descrição do Problema

Xenia, a matemática iniciante, é uma estudante do terceiro ano da escola primária. Ela agora está aprendendo a operação de adição.

O professor escreveu a soma de vários números. Os alunos devem calcular essa soma. Para facilitar o cálculo, a soma contém apenas os números **1, 2 e 3**. No entanto, isso ainda não é suficiente para Xenia. Como ela está apenas começando a contar, ela só consegue calcular uma soma se os termos estiverem organizados em **ordem não decrescente**. 

Por exemplo, ela não consegue calcular a soma `1+3+2+1`, mas consegue calcular as somas `1+1+2` e `3+3`.



Você recebeu a soma que foi escrita no quadro. Reorganize os termos e imprima a soma de tal forma que Xenia consiga calculá-la.

### Entrada

A primeira linha contém uma string não vazia $s$ — a soma que Xenia precisa contar. A string $s$ não contém espaços, apenas dígitos e o caractere "+". Além disso, $s$ é uma soma correta dos números 1, 2 e 3. A string tem no máximo 100 caracteres.

### Saída

Imprima a nova soma de forma que Xenia consiga calcular (com os números em ordem não decrescente).

### Exemplos

| Entrada (Input) | Saída (Output) |
| :--- | :--- |
| `3+2+1` | `1+2+3` |
| `1+1+3+1+3` | `1+1+1+3+3` |
| `2` | `2` |