Link: https://codeforces.com/problemset/problem/231/A

## A. Equipe (Team)

| Limite de Tempo | Limite de Memória |
| :--- | :--- |
| 2.0 segundos | 256 megabytes |

### Descrição do Problema

Um dia, três melhores amigos — Petya, Vasya e Tonya — decidiram formar uma equipe e participar de concursos de programação. Geralmente, vários problemas são oferecidos aos participantes durante esses eventos. Muito antes do início, os amigos decidiram que implementarão um problema se **pelo menos dois deles** estiverem certos da solução. Caso contrário, eles não escreverão a solução do problema.

Este concurso oferece $n$ problemas aos participantes. Para cada problema, sabemos qual amigo tem certeza sobre a solução. Ajude os amigos a encontrar o número de problemas para os quais eles escreverão uma solução.

### Entrada

A primeira linha da entrada contém um único inteiro $n$ ($1 \le n \le 1000$) — o número de problemas no concurso. 

Em seguida, seguem $n$ linhas, cada uma contendo três inteiros. Cada inteiro é **0** ou **1**:
- Se o primeiro número da linha for **1**, Petya tem certeza sobre a solução; caso contrário, ele não tem.
- O segundo número mostra a visão de Vasya.
- O terceiro número mostra a visão de Tonya.

Os números nas linhas são separados por espaços.

### Saída

Imprima um único inteiro — o número de problemas que os amigos irão implementar no concurso.

### Exemplos

| Entrada (Input) | Saída (Output) |
| :--- | :--- |
| `3` <br> `1 1 0` <br> `1 1 1` <br> `1 0 0` | `2` |
| `2` <br> `1 0 0` <br> `0 1 1` | `1` |

---

### Notas dos Exemplos

No **primeiro exemplo**, Petya e Vasya têm certeza sobre o primeiro problema, e todos os três sabem resolver o segundo. Isso significa que eles escreverão soluções para esses dois problemas. Apenas Petya tem certeza sobre o terceiro, o que não é suficiente.

No **segundo exemplo**, os amigos implementarão apenas o segundo problema, pois Vasya e Tonya estão certos da solução.