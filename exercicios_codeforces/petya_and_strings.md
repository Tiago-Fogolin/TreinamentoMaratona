Link: https://codeforces.com/problemset/problem/112/A

## A. Petya e Strings (Petya and Strings)

| Limite de Tempo | Limite de Memória |
| :--- | :--- |
| 2.0 segundos | 256 megabytes |

### Descrição do Problema

O pequeno Petya adora presentes. Sua mãe comprou para ele duas strings do mesmo tamanho em seu aniversário. As strings consistem em letras latinas maiúsculas e minúsculas. Agora Petya quer comparar essas duas strings **lexicograficamente**.

A diferença entre maiúsculas e minúsculas não importa, ou seja, uma letra maiúscula é considerada equivalente à letra minúscula correspondente. Ajude Petya a realizar a comparação.

### Entrada

Cada uma das duas primeiras linhas contém uma string. Os comprimentos das strings variam de 1 a 100 caracteres, inclusive. É garantido que as strings tenham o mesmo comprimento e que consistam apenas em letras latinas maiúsculas e minúsculas.

### Saída

- Se a primeira string for **menor** que a segunda, imprima **"-1"**.
- Se a segunda string for **menor** que a primeira, imprima **"1"**.
- Se as strings forem **iguais**, imprima **"0"**.

Lembre-se: o caso das letras (maiúsculo/minúsculo) deve ser ignorado na comparação.

### Exemplos

| Entrada (Input) | Saída (Output) |
| :--- | :--- |
| `aaaa` <br> `aaaA` | `0` |
| `abs` <br> `Abz` | `-1` |
| `abcdefg` <br> `AbCdEfF` | `1` |

---

### Notas

Para entender mais o que é a ordem lexicográfica, acesse: https://pt.wikipedia.org/wiki/Ordem_lexicogr%C3%A1fica