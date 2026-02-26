Link: https://codeforces.com/problemset/problem/236/A

## A. Garoto ou Garota (Boy or Girl)

| Limite de Tempo | Limite de Memória |
| :--- | :--- |
| 1.0 segundo | 256 megabytes |

### Descrição do Problema

Hoje em dia, muitos garotos usam fotos de garotas bonitas como avatares em fóruns. Por isso, é muito difícil determinar o gênero de um usuário à primeira vista. No ano passado, nosso herói entrou em um fórum e teve uma conversa agradável com uma beldade (ou assim ele pensou). Depois disso, eles conversaram com frequência e acabaram se tornando um casal na rede.

Mas ontem, ele foi encontrar "ela" no mundo real e descobriu que "ela" é, na verdade, um homem muito forte! Nosso herói está muito triste e cansado demais para amar novamente. Então, ele inventou uma maneira de reconhecer o gênero dos usuários por seus nomes de usuário.

**O método dele é o seguinte:**
* Se o número de **caracteres distintos** no nome de usuário for **ímpar**, então o usuário é um **homem**.
* Se o número de **caracteres distintos** for **par**, então o usuário é uma **mulher**.



Você recebeu a string que denota o nome de usuário. Ajude nosso herói a determinar o gênero deste usuário usando o método dele.

### Entrada

A primeira linha contém uma string não vazia composta apenas por letras latinas minúsculas — o nome de usuário. Esta string contém, no máximo, 100 letras.

### Saída

* Se for uma mulher pelo método do nosso herói, imprima **"CHAT WITH HER!"** (sem as aspas).
* Caso contrário, imprima **"IGNORE HIM!"** (sem as aspas).

### Exemplos

| Entrada (Input) | Saída (Output) |
| :--- | :--- |
| `wjmzbmr` | `CHAT WITH HER!` |
| `xiaodao` | `IGNORE HIM!` |
| `sevenkplus` | `CHAT WITH HER!` |

---

### Notas

No primeiro exemplo (`wjmzbmr`), existem **6** caracteres distintos: "w", "j", "m", "z", "b" e "r". Como 6 é um número par, o usuário é considerado uma mulher.