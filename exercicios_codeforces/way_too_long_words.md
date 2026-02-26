Link: https://codeforces.com/problemset/problem/71/A

## A. Palavras Muito Longas (Way Too Long Words)

| Limite de Tempo | Limite de Memória |
| :--- | :--- |
| 1.0 segundo | 256 megabytes |

### Descrição do Problema

Às vezes, algumas palavras como "localization" ou "internationalization" são tão longas que escrevê-las muitas vezes em um texto se torna cansativo.

Vamos considerar uma palavra **muito longa** se o seu comprimento for **estritamente maior que 10 caracteres**. Todas as palavras muito longas devem ser substituídas por uma abreviação especial.

A abreviação é feita da seguinte forma:
1. Escrevemos a primeira letra da palavra.
2. Entre a primeira e a última letra, escrevemos o número de letras que existem entre elas.
3. Escrevemos a última letra da palavra.

Dessa forma, "localization" vira "l10n" (pois tem 10 letras entre o 'l' e o 'n'), e "internationalization" vira "i18n".

Sua tarefa é automatizar esse processo. Todas as palavras muito longas devem ser substituídas pela abreviação, enquanto as palavras que não são muito longas devem permanecer inalteradas.

### Entrada

A primeira linha contém um inteiro $n$ ($1 \le n \le 100$). Cada uma das $n$ linhas seguintes contém uma palavra. Todas as palavras consistem em letras latinas minúsculas e têm comprimentos de 1 a 100 caracteres.

### Saída

Imprima $n$ linhas. A $i$-ésima linha deve conter o resultado da substituição da $i$-ésima palavra da entrada.

### Exemplos

| Entrada (Input) | Saída (Output) |
| :--- | :--- |
| `4` | |
| `word` | `word` |
| `localization` | `l10n` |
| `internationalization` | `i18n` |
| `pneumonoultramicroscopicsilicovolcanoconiosis` | `p43s` |

