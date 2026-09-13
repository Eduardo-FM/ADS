
## Aulas iniciais
### Ponteiro

Em C, **ponteiro é uma variável que guarda o endereço de memória de outra variável**.

``` c
int numero = 10;
int *p = &numero;
```

- `&` → pega o **endereço** de memória de uma variável.
- `*` na declaração → indica que a variável é um **ponteiro**.
- `*p` → acessa o **valor armazenado no endereço** para o qual `p` aponta.

Exemplo:
``` c
*p = 50;
```

### Estrutura dinâmica

Uma **estrutura dinâmica** é uma estrutura de dados cujo **tamanho pode ser alterado durante a execução do programa**.

Diferente de estruturas estáticas, que possuem um tamanho definido previamente, as estruturas dinâmicas utilizam **memória alocada dinamicamente**, principalmente com `malloc()`, `calloc()`, `realloc()` e `free()`.

#### Principais características

- O tamanho pode **aumentar ou diminuir** durante a execução.
- Utiliza **memória heap**.
- Geralmente utiliza **ponteiros** para controlar os dados.
- Permite utilizar a memória de forma mais **flexível e eficiente**.
- É necessário liberar a memória utilizada com `free()`.

Exemplo:

``` c
int *p = malloc(5 * sizeof(int));
```

Aqui, o programa solicita memória para armazenar **5 inteiros** durante a execução.

Depois de utilizar:
``` c
free(p);
```

==Estrutura dinâmica = estrutura cujo tamanho pode ser definido ou alterado durante a execução, utilizando alocação dinâmica de memória e ponteiros.==

### TAD 

Um **TAD (Tipo Abstrato de Dados)** é um tipo definido pelo usuário que determina:

- **Quais dados** serão armazenados;
- **Quais operações** podem ser realizadas sobre esses dados.

A ideia principal é a **abstração**: o usuário sabe **o que pode fazer**, mas não precisa saber **como as operações são implementadas** (as operações são realizadas, mas o usuário não conhece os detalhes internos).

No desenvolvimento em C, dividimos o TAD em dois arquivos:

1. **Arquivo `.h` (Interface):** Define as operações públicas (o manual de uso do TAD).
2. **Arquivo `.c` (Implementação):** Contém a lógica interna de funcionamento das operações.

####  Arquivo `.h` — Interface

``` c
#ifndef PONTO_H
#define PONTO_H

// Definicao opaca/abstrata do tipo Ponto para encapsulamento
typedef struct ponto Ponto;

// Funcoes (operacoes) disponibilizadas externamente
Ponto* ponto_criar(float x, float y);
void ponto_liberar(Ponto *p);
float ponto_obter_x(Ponto *p);
float ponto_obter_y(Ponto *p);
void ponto_atribuir(Ponto *p, float x, float y);

#endif // PONTO_H
```

#### Arquivo `.c` — Implementação

``` C
#include <stdlib.h>
#include "ponto.h"

// Definicao concreta da estrutura, oculta do usuario externo
struct ponto {
    float x;
    float y;
};

Ponto* ponto_criar(float x, float y) {
    Ponto *p = (Ponto*) malloc(sizeof(Ponto));
    if (p != NULL) {
        p->x = x;
        p->y = y;
    }
    return p;
}

void ponto_liberar(Ponto *p) {
    free(p);
}

float ponto_obter_x(Ponto *p) {
    if (p != NULL) return p->x;
    return 0.0;
}

float ponto_obter_y(Ponto *p) {
    if (p != NULL) return p->y;
    return 0.0;
}

void ponto_atribuir(Ponto *p, float x, float y) {
    if (p != NULL) {
        p->x = x;
        p->y = y;
    }
}
```
##### Para decorar

> **TAD = dados + operações + abstração.**  
> **`.h` = interface (o que pode ser usado).**  
> **`.c` = implementação (como funciona).**  
> **O usuário utiliza o TAD sem precisar conhecer sua implementação interna.**
## aula 10_08

### *Complexidade de algoritmo*

A **complexidade de um algoritmo** analisa a quantidade de **recursos necessários** para executá-lo, principalmente:

- **Tempo:** quantidade de operações realizadas.
- **Espaço:** quantidade de memória utilizada.

A complexidade ajuda a **comparar algoritmos** e avaliar qual é mais eficiente para entradas grandes.

A análise pode considerar:

- **Melhor caso:** situação mais favorável.
- **Caso médio:** comportamento esperado para uma entrada comum.
- **Pior caso:** situação mais desfavorável.
#### Anotação Big O

A **notação Big O** descreve como o custo de um algoritmo **cresce conforme o tamanho da entrada (`n`) aumenta**.

Ela normalmente é utilizada para representar o **pior caso**.

Exemplos:

|Big O|Nome|Exemplo|
|---|---|---|
|`O(1)`|Constante|Acessar uma posição de um vetor|
|`O(log n)`|Logarítmica|Busca binária|
|`O(n)`|Linear|Percorrer um vetor|
|`O(n log n)`|Linearítmica|Merge Sort|
|`O(n²)`|Quadrática|Bubble Sort|
|`O(2ⁿ)`|Exponencial|Alguns algoritmos recursivos|

> **Big O mostra como o número de operações cresce em relação ao tamanho da entrada.**

Por exemplo, em:

``` c
for (int i = 0; i < n; i++)
{
    printf("%d\n", i);
}
```

O `for` executa aproximadamente `n` vezes. Portanto:

**Complexidade = `O(n)`**

Se tivermos dois `for` aninhados:

``` c
for (int i = 0; i < n; i++)
{
    for (int j = 0; j < n; j++)
    {
        printf("%d %d\n", i, j);
    }
}
```

Temos aproximadamente `n × n` operações:

**Complexidade = `O(n²)`**

##### Para decorar

> **`n` = tamanho da entrada**  
> **Big O = crescimento do custo do algoritmo**  
> **`O(1)` → não depende de `n`**  
> **`O(n)` → cresce proporcionalmente a `n`**  
> **`O(n²)` → cresce proporcionalmente a `n²`**
## Aula 14_08

### Listas 

#### Lista sequencial

Uma lista sequencial é caracterizada por armazenar seus elementos em **posições adjacentes de memória**. É chamada de sequencial porque os elementos estão fisicamente dispostos em sequência direta na memória (um elemento imediatamente após o outro).

- **Busca e Acesso:** O acesso a qualquer posição é direto ($O(1)$) porque podemos calcular a posição exata de um elemento sabendo o endereço de início (endereço base) através da fórmula: $$\text{Endereço} = \text{Endereço Base} + (\text{Índice} \times \text{Tamanho do Elemento})$$ _(Exemplo: um inteiro (`int`) normalmente ocupa **4 bytes** na memória)._

Existem dois formatos principais de lista sequencial:

1. **Com Alocação Estática:** O tamanho máximo do array é definido previamente em tempo de compilação.
2. **Com Alocação Dinâmica:** O tamanho inicial pode ser definido em tempo de execução via `malloc()` e redimensionado dinamicamente com `realloc()`.

A lista sequencial é ordenado. Porque o segundo vem depois do primeiro (tem uma posição especifica de endereço de memória)

para declarar:
```c
// estática
int v[3];

//para acessar 
v[0];
v[1];
v[2];

//para alterar o valor:
v[o] == 1;
```

para acessar um elemento o acesso é direto, então se dá a posição do elemento é você já consegue acessa-la.

#### Lista dinamica

Na alocação dinâmica se utiliza o malloc.

```c
int *v;

v = malloc(n/*numero definido em tempo de execucao */* * sizeOf(int))

//para acessar 


free(v);
```

É possivel mudar o tamnho da alocacao dinamica durante o código.

##### Código em C
###### estatica

```c
int main()
{
	float nota[5] = {8.5, 9.6, 7.9, 8.9, 10.0};
	
	for(int i = 0; i < 5; i++)
	{
		printf("Notas %d: %.2f\n", i+1, nota[i]);
	}
	
	return 0;
}

```

###### dinamica

```c
int main()
{
    float *notas = malloc(5 * sizeof(float));
    
    for(int i = 0; i < 5; i++)
    {
        printf("Digite a nota %d: ", i + 1);
        scanf("%f", &notas[i]);
    }

    for(int i = 0; i < 5; i++)
    {
        printf("Nota %d: %.2f\n", i + 1, notas[i]);
    }

    free(notas);

    return 0;
}

```

## Aula 21_08

### Lista encadeada

Diferente das sequenciais, os elementos de uma lista encadeada **não ocupam posições adjacentes de memória**. Cada elemento (chamado de **nó**) armazena o valor desejado e também o endereço de memória do próximo elemento da lista.

- **Vantagens:** Grande flexibilidade para inserir ou remover elementos (especialmente entre duas posições intermediárias), pois basta ajustar os ponteiros envolvidos sem precisar mover todos os elementos seguintes na memória física.

#### Tipos de Listas Encadeadas:

1. **Lista Simplesmente Encadeada:** Os nós apontam apenas em um sentido (para o próximo nó).
2. **Lista Duplamente Encadeada:** Cada nó guarda o endereço do próximo e também do nó anterior, permitindo navegação em ambos os sentidos.
3. **Lista Circular:** O último elemento aponta de volta para o primeiro, criando um ciclo.

#### Estrutura de Nós e Cabeçalho

É uma excelente prática criar uma estrutura de **cabeçalho da lista** para armazenar metadados, tais como o tamanho da lista, ponteiro para o primeiro elemento e ponteiro para o último elemento. Isso otimiza operações de inserção e remoção no fim da lista para tempo constante ($O(1)$).

##### Exemplo de Estrutura para Lista Simplesmente Encadeada:

``` c
#include <stdlib.h>

// 1. Struct para o No da Lista
typedef struct no {
    int valor;
    struct no *proximo;
} No;

// 2. Struct para o Cabecalho da Lista
typedef struct {
    No *inicio;
    No *fim;
    int tamanho;
} ListaEncadeada;

// Inicializacao da lista
void inicializar_lista_encadeada(ListaEncadeada *l) {
    l->inicio = NULL;
    l->fim = NULL;
    l->tamanho = 0;
}
```

##### Exemplo de Estrutura para Lista Duplamente Encadeada:

``` c
typedef struct no_duplo {
    int valor;
    struct no_duplo *anterior;
    struct no_duplo *proximo;
} NoDuplo;

typedef struct {
    NoDuplo *inicio;
    NoDuplo *fim;
    int tamanho;
} ListaDuplamenteEncadeada;
```

###  Análise de Complexidade de Operações em Listas

Para listas lineares comuns, o custo computacional das operações fundamentais varia conforme o cenário:

- **Inserção:**
    - Se realizada em posições controladas com ponteiros diretos (por exemplo, sempre no início ou no fim com o uso de um cabeçalho), a inserção tem tempo constante: **$O(1)$**.
- **Remoção:**
    - **Melhor Caso:** Remoção no início da lista (ajuste simples de ponteiros diretos) -> **$O(1)$**.
    - **Pior Caso:** Remoção de um elemento no final ou no meio da lista (exige percorrer toda a lista para encontrar o elemento ou atualizar o penúltimo elemento no caso de simplesmente encadeada) -> **$O(n)$**.
- **Busca:**
    - **Melhor Caso:** O elemento procurado é o primeiro da lista -> **$O(1)$**.
    - **Pior Caso:** O elemento está na última posição ou não pertence à lista -> **$O(n)$**.

## Aula 31_08 

### Pilha

Estrutura linear formada pelo "empilhamento" de elementos.

![[Pasted image 20260831213721.png]]

A posiçao na base se chama base, e a posição em cima se chama topo.

Só consegue mexer no elemento do topo, seja para inserir como para excluir. 

Os elementos são inseridos e removidos no topo  da pilha.

Existem duas operações obrigatórias em uma pilha:
- Push: p/ empilhar um elemento.
- Pop: p/ desempilhar 

Outras operações são possíveis:
- peek: consulta o elemento do topo da pilha sem remover o elemento.
- pilha-vazia: verifica se a pulha está vazia.

#### Implementações

1) Pilha sequencial. 
		Alocação sequencial semelhante à lista sequencial.

2) Pila dinâmica
		semelhante à alocação dinâmica, os elementos da pilha são alocados em tempo de execução em endereços aleatórios. 


#### Problema da celebridade 

Vai ter uma festa, e uma celebridade vai para a essa festa. Nos temos como conhecer quem ta na festa, e quem conhece quem. E queremos saber se tem ou não uma celebridade na festa, e quem é. Uma celebridade é uma pessoa que não conhece ninguém, e todo mundo conhece ele.



## Fila

Enquanto pilhas usam a política LiFo(Last in, first Out), as filas seguem o princípio FiFo (First in, First out).

Isso significa que quando retiramos um elemento da fila, retiramos o elemento que está há mais tempo armazenado. 

Na prática, os elementos são inseridos no im e retirados no começo.

### Operações

Duas operações são necessárias:
1) "Enqueue": insere no final da fila
2) "dequeue": retira no início da fila

![[Pasted image 20260911212524.png]]


### Implementação 

- Array

- Lista


---

Fila tem um inicio e um fim.

Tem duas operacoes: enqueu (enfilerar), dequeu (defilerar)

Temos alguns tipos de filas que podemos implementar:
- Simples 
- circular
- De prioridade

Para implementar ela pode se usar um array, e cada elemento está na fila, ou pode ser usar uma fila (simplesmente encadeada, duplamente ..., depende de como for implementar)

Para implementar uma fila com um array é preciso:
- ter duas variaveis, para marcar o inicio da fila, e aonde termina a fila
- pode marcar a ultima posicao ocupada como fim ou a primeira posicao livre. 
- Apontando para a primeira posicao livre, voce terá um array vazio, e o fim será o elemento [0] do array. Inseriu um elemento dentro, a primeira posicao livre anda. O problema é quando acaba as posiçoes livres do array. Para resolver esse problema se utiliza um array circular e quando o elemento fim estiver fora do array coloca ele como elemento 0. Para isso se utiliza a formula (F = (F + 1) % tamanho da lista)
- E para saber se a lista anterior está cheia se faz: tem que comparar a quantidade de elementos que você tem, com o tamanho da lista. Para isso precisa de um cabeçalho (inicio, fim, quantidade de elementos, capacidade da lista) se a quantidade for igual a capacidade entao ele está cheia.

---
