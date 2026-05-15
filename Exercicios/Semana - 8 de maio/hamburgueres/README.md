# C. Hambúrgueres

**Link do Problema:** [Codeforces 371C](https://codeforces.com/problemset/problem/371/C)

---

## Enunciado

**Limite de tempo por teste:** 1 segundo  
**Limite de memória por teste:** 256 megabytes  

Polycarpus ama muito hambúrgueres. Ele adora especialmente os hambúrgueres que ele faz com suas próprias mãos. Polycarpus acha que existem apenas três ingredientes decentes para se fazer hambúrgueres: pão, salsicha e queijo. Ele anota a receita do seu favorito "Le Hamburger de Polycarpus" como uma string de letras `B` (pão), `S` (salsicha) e `C` (queijo). Os ingredientes na receita vão de baixo para cima, por exemplo, a receita "BSCBS" representa o hambúrguer onde os ingredientes vão de baixo para cima como pão, salsicha, queijo, pão e salsicha novamente.

Polycarpus tem `nb` pedaços de pão, `ns` pedaços de salsicha e `nc` pedaços de queijo na cozinha. Além disso, a loja próxima tem todos os três ingredientes, os preços são `pb` rublos por um pedaço de pão, `ps` por um pedaço de salsicha e `pc` por um pedaço de queijo.

Polycarpus tem `r` rublos e ele está pronto para fazer compras com eles. Qual o número máximo de hambúrgueres que ele pode cozinhar? Você pode assumir que Polycarpus não pode quebrar ou fatiar nenhum dos pedaços de pão, salsicha ou queijo. Além disso, a loja tem um número ilimitado de pedaços de cada ingrediente.

### Entrada

A primeira linha da entrada contém uma string não vazia que descreve a receita do "Le Hamburger de Polycarpus". O comprimento da string não excede 100, a string contém apenas as letras `B` (B maiúsculo), `S` (S maiúsculo) e `C` (C maiúsculo).

A segunda linha contém três inteiros `nb`, `ns`, `nc` (1 ≤ `nb`, `ns`, `nc` ≤ 100) — o número de pedaços de pão, salsicha e queijo na cozinha de Polycarpus. 

A terceira linha contém três inteiros `pb`, `ps`, `pc` (1 ≤ `pb`, `ps`, `pc` ≤ 100) — o preço de um pedaço de pão, salsicha e queijo na loja. 

Finalmente, a quarta linha contém o inteiro `r` (1 ≤ `r` ≤ 10¹²) — o número de rublos que Polycarpus tem.

> **Nota para C++:** Por favor, não escreva o especificador `%lld` para ler ou escrever inteiros de 64 bits. É preferível usar os fluxos `cin`, `cout` ou o especificador `%I64d`.

### 📤 Saída

Imprima o número máximo de hambúrgueres que Polycarpus pode fazer. Se ele não puder fazer nenhum hambúrguer, imprima `0`.

---

## Solução Guiada

* **A Estratégia Ideal:**  Nesse exercício, apesar de ter algumas formas diferentes de resolver, eu imagino que a mais a maneira mais fácil seja fazendo busca binária na resposta.
* **Como Funciona:** Busca binária na resposta é uma técnica em que 'chutamos' um valor que é a possível resposta do exercício, e verificamos se esse valor é uma resposta válida.
* **Importante!!!!!:** Só podemos utilizar essa técnica quando a função que descreve a resposta em relação aos valores de entrada é **monotônica** (ou seja, se eu consigo fazer 10 hambúrgueres, eu obrigatoriamente consigo fazer 9. Se eu não consigo fazer 11, não vou conseguir fazer 12).
