
## Ponteiro

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

Nesse caso, `p` aponta para `numero`, então `*p = 50` altera o valor de `numero` para `50`.

### Ponteiro para ponteiro

Um **ponteiro para ponteiro** (ou ponteiro duplo) é uma variável que armazena o **endereço de memória de outro ponteiro**.

Enquanto um ponteiro simples guarda o endereço de uma variável comum, o ponteiro duplo guarda o endereço do "papel" onde o primeiro endereço foi anotado.


Exemplo:
``` c
int x = 10; 

int *p = &x; // 'p' guarda o endereço de 'x' int 

**q = &p; // 'q' guarda o endereço de 'p'

printf("Valor de x: %d\n", x); // Imprime 10 

printf("Via *p: %d\n", *p); // Desreferencia 'p' -> Imprime 10 

printf("Via **q: %d\n", **q); // Desreferencia 'q' duas vezes -> Imprime 10

```

#### **Visualização da Memória**

Para entender como a desreferenciação funciona na prática, imagine os endereços de memória:

| Variável | Endereço de Memória | Valor Armazenado | Significado         |
| -------- | ------------------- | ---------------- | ------------------- |
| **x**    | `0x100`             | `10`             | Valor inteiro comum |
| **p**    | `0x200`             | `0x100`          | Endereço de `x`     |
| **q**    | `0x300`             | `0x200`          | Endereço de `p`     |

- **q** resulta em `0x200` (o endereço de `p`).
- \*q acessa o conteúdo de `p`, que é `0x100` (o endereço de `x`).
- \**\*q acessa o conteúdo do endereço `0x100`, que é **10**.

#### **Para que serve na prática?**

Na linguagem C, você usará ponteiros duplos principalmente em **três cenários essenciais**:

1. **Modificar um ponteiro dentro de uma função (Passagem por Referência de Ponteiro):** Quando você precisa que uma função altere para onde um ponteiro aponta (por exemplo, ao **inserir um nó no início de uma Lista Encadeada** ou ao alocar memória dentro de uma função auxiliar).

``` c
void aloca_inteiro(int **ptr) {
    *ptr = (int *) malloc(sizeof(int)); // Modifica o ponteiro original na função chamadora
    **ptr = 42;                         // Atribui valor à memória alocada
}

```

2. **Matrizes Dinâmicas (Arrays Bidimensionais):** Alocação de um vetor de ponteiros, onde cada posição aponta para uma linha de elementos.

``` c
int **matriz = (int **) malloc(linhas * sizeof(int *));

```

3. **Vetor de Strings:** O parâmetro `char *argv[]` ou `char **argv` na função `main()` é um ponteiro para ponteiro, onde cada elemento é uma string (`char *`).

## Estrutura dinâmica

Uma **estrutura dinâmica** é uma estrutura de dados cujo **tamanho pode ser alterado durante a execução do programa**.

Diferente de estruturas estáticas, que possuem um tamanho definido previamente, as estruturas dinâmicas utilizam **memória alocada dinamicamente**, principalmente com `malloc()`, `calloc()`, `realloc()` e `free()`.

### Principais características

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

## TAD 

Um **TAD (Tipo Abstrato de Dados)** é um tipo definido pelo usuário que determina:

- **Quais dados** serão armazenados;
- **Quais operações** podem ser realizadas sobre esses dados.

A ideia principal é a **abstração**: o usuário sabe **o que pode fazer**, mas não precisa saber **como as operações são implementadas** (as operações são realizadas, mas o usuário não conhece os detalhes internos).

No desenvolvimento em C, dividimos o TAD em dois arquivos:

1. **Arquivo `.h` (Interface):** Define as operações públicas (o manual de uso do TAD).
2. **Arquivo `.c` (Implementação):** Contém a lógica interna de funcionamento das operações.

###  Arquivo `.h` — Interface

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

### Arquivo `.c` — Implementação

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

## *Complexidade de algoritmo*

A **complexidade de um algoritmo** analisa a quantidade de **recursos necessários** para executá-lo, principalmente:

- **Tempo:** quantidade de operações realizadas.
- **Espaço:** quantidade de memória utilizada.

A complexidade ajuda a **comparar algoritmos** e avaliar qual é mais eficiente para entradas grandes.

A análise pode considerar:

- **Melhor caso:** situação mais favorável.
- **Caso médio:** comportamento esperado para uma entrada comum.
- **Pior caso:** situação mais desfavorável.
### Anotação Big O

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


## Listas 

### Lista sequencial

Uma lista sequencial, ou ==lista contígua== é caracterizada por armazenar seus elementos em **posições adjacentes de memória**. É chamada de sequencial porque os elementos estão fisicamente dispostos em sequência direta na memória (um elemento imediatamente após o outro).

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

#### Como funciona a Inserção de Elementos

Para inserir um novo elemento em uma lista sequencial, precisamos garantir que há espaço disponível (`quantidade < TAMANHO_MAXIMO`). A lógica varia dependendo de **onde** o elemento será inserido:

- **Inserção no Final (**$O(1)$**):** É a operação mais rápida. O elemento é colocado diretamente na posição `quantidade` e o contador de elementos é incrementado.
- **Inserção no Início ou no Meio (**$O(n)$**):** Como os elementos devem permanecer contíguos sem "buracos", é necessário abrir espaço **deslocando todos os elementos subsequentes uma posição para a direita** (de trás para frente), antes de colocar o novo valor na posição desejada.

``` c
// Inserção em uma posição específica (pos)
int inserir(int v[], int *qtd, int tam_max, int elem, int pos) {
    if (*qtd >= tam_max) return 0;        // Falha: Lista cheia
    if (pos < 0 || pos > *qtd) return 0;  // Falha: Posição inválida

    // Desloca os elementos para a direita para abrir espaço
    for (int i = *qtd; i > pos; i--) {
        v[i] = v[i - 1];
    }

    v[pos] = elem; // Insere o novo elemento
    (*qtd)++;      // Incrementa a quantidade de elementos
    return 1;      // Sucesso
}
```

#### Como funciona a Remoção de Elementos

Para remover um elemento, a lista não pode estar vazia (`quantidade > 0`). A lógica também depende da posição do elemento a ser removido:

- **Remoção no Final (**$O(1)$**):** Basta decrementar a quantidade de elementos (`quantidade--`). O valor antigo permanece na memória, mas é considerado "lixo" inválido pela estrutura.
- **Remoção no Início ou no Meio (**$O(n)$**):** Ao remover um elemento do meio, fica uma lacuna ("buraco") na memória. Para manter a contiguidade física da lista, devemos **deslocar todos os elementos à direita uma posição para a esquerda** (da esquerda para a direita), preenchendo o espaço do elemento removido.

``` c
// Remoção em uma posição específica (pos)
int remover(int v[], int *qtd, int pos) {
    if (*qtd == 0) return 0;              // Falha: Lista vazia
    if (pos < 0 || pos >= *qtd) return 0; // Falha: Posição inválida

    // Desloca os elementos para a esquerda para cobrir a lacuna
    for (int i = pos; i < *qtd - 1; i++) {
        v[i] = v[i + 1];
    }

    (*qtd)--; // Decrementa a quantidade de elementos
    return 1; // Sucesso
}
```
#### Resumo da Complexidade Operacional

| Operação              | Início / Meio | Final  | Justificativa                                            |
| --------------------- | ------------- | ------ | -------------------------------------------------------- |
| **Acesso por Índice** | $O(1)$        | $O(1)$ | Cálculo direto via ponteiro base.                        |
| **Inserção**          | $O(n)$        | $O(1)$ | Exige deslocar elementos para a direita no início/meio.  |
| **Remoção**           | $O(n)$        | $O(1)$ | Exige deslocar elementos para a esquerda no início/meio. |

### Lista dinâmica

Na alocação dinâmica se utiliza o malloc.

```c
int *v;

v = malloc(n/*numero definido em tempo de execucao */* * sizeOf(int))

//para acessar 


free(v);
```

É possível mudar o tamanho da alocação dinâmica durante o código.

#### Código em C
###### estática

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

###### dinâmica

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

## Lista encadeada

Diferente das sequenciais, os elementos de uma lista encadeada **não ocupam posições adjacentes de memória**. Cada elemento (chamado de **nó**) armazena o valor desejado e também o endereço de memória do próximo elemento da lista.

- **Vantagens:** Grande flexibilidade para inserir ou remover elementos (especialmente entre duas posições intermediárias), pois basta ajustar os ponteiros envolvidos sem precisar mover todos os elementos seguintes na memória física.

### Tipos de Listas Encadeadas:

1. **Lista Simplesmente Encadeada:** Os nós apontam apenas em um sentido (para o próximo nó).
2. **Lista Duplamente Encadeada:** Cada nó guarda o endereço do próximo e também do nó anterior, permitindo navegação em ambos os sentidos.
3. **Lista Circular:** O último elemento aponta de volta para o primeiro, criando um ciclo.

### Estrutura de Nós e Cabeçalho

É uma excelente prática criar uma estrutura de **cabeçalho da lista** para armazenar metadados, tais como o tamanho da lista, ponteiro para o primeiro elemento e ponteiro para o último elemento. Isso otimiza operações de inserção e remoção no fim da lista para tempo constante ($O(1)$).

#### Exemplo de Estrutura para Lista Simplesmente Encadeada:

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

#### Exemplo de Estrutura para Lista Duplamente Encadeada:

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


## Pilha

A **Pilha** é uma estrutura de dados linear que segue estritamente o princípio **LIFO** (_Last-In, First-Out_ — **"O último que entra é o primeiro que sai"**), formada pelo "empilhamento" de elementos.

Analogia do mundo real: pense em uma pilha de pratos ou de livros. Você sempre coloca um novo elemento no topo e sempre remove o elemento que está no topo.

- **Base:** O primeiro elemento inserido na pilha (fica no fundo).
- **Topo:** A posição do último elemento inserido. **Toda e qualquer alteração ou consulta é realizada exclusivamente pelo topo.**


![[Pasted image 20260831213721.png]]

Existem duas operações obrigatórias em uma pilha:
- Push: p/ empilhar um elemento.
- Pop: p/ desempilhar 

Outras operações são possíveis:
- peek: consulta o elemento do topo da pilha sem remover o elemento.
- pilha-vazia: verifica se a pilha está vazia.

### Operações Principais e Cenários de Uso

**A. Inserção (****Push** **— Empilhar)**

Adiciona um novo elemento sobre o topo atual da pilha.

- **Complexidade:** $O(1)$ — Tempo constante.
- **Cenários e Cuidados:**
    - **Overflow (Pilha Cheia):** Na **Pilha Sequencial**, deve-se verificar se a capacidade máxima do array foi atingida (`topo == TAMANHO_MAXIMO - 1`) antes de inserir.
    - **Falha de Memória:** Na **Pilha Dinâmica**, deve-se verificar se a alocação de memória via `malloc()` retornou `NULL`.

**B. Remoção (****Pop** **— Desempilhar)**

Remove e retorna o elemento que está no topo da pilha.

- **Complexidade:** $O(1)$ — Tempo constante.
- **Cenários e Cuidados:**
    - **Underflow (Pilha Vazia):** Antes de desempilhar, é obrigatório checar se a pilha possui ao menos um elemento (`topo == -1` ou `topo == NULL`). Tentar desempilhar uma pilha vazia gera erro de execução.
    - **Liberação de Memória:** Na **Pilha Dinâmica**, o nó removido deve ter sua memória liberada explicitamente com `free()`.

**C. Consulta e Busca de Elementos**

- **Consulta ao Topo (****Peek** **ou** **Top****):** Retorna o valor contido no topo **sem removê-lo**.
    - **Complexidade:** $O(1)$.
- **Busca por um Elemento Qualquer:** Como não há acesso aleatório direto aos elementos do meio ou da base, para buscar um elemento específico sob as regras puras de uma pilha, é necessário desempilhar os elementos um a um até encontrá-lo (armazenando-os em uma pilha auxiliar para depois restaurar a pilha original).
    - **Complexidade:** $O(n)$ — Tempo linear.
### Implementações

1) Pilha sequencial. 
	Alocação sequencial semelhante à lista sequencial.
	Utiliza um vetor contíguo de tamanho fixo e uma variável inteira `topo` que guarda o índice do elemento do topo (inicializada em `-1` para indicar pilha vazia).

``` c
#define TAM_MAX 100 

typedef struct { 
	int itens[TAM_MAX]; 
	int topo; 
} PilhaSequencial; 

void inicializar(PilhaSequencial *p) { 
	p->topo = -1; 
} 

int push(PilhaSequencial *p, int valor) { 
	if (p->topo == TAM_MAX - 1) return 0; // Erro: Overflow (Pilha cheia) 
	
	p->topo++; 
	p->itens[p->topo] = valor; 
	return 1; // Sucesso 
} 

int pop(PilhaSequencial *p, int *valor) { 
	if (p->topo == -1) return 0; // Erro: Underflow (Pilha vazia) 
	*valor = p->itens[p->topo]; 
	p->topo--; 
	return 1; // Sucesso 
}
```

2) Pila dinâmica
	Semelhante à alocação dinâmica, os elementos da pilha são alocados em tempo de execução em endereços aleatórios. 
	Cada elemento é um nó alocado na memória heap contendo o dado e um ponteiro para o nó abaixo dele. O topo é representado por um ponteiro para o primeiro nó da lista.

``` c


typedef struct No { 
	int dado; 
	struct No *proximo; 
} No; 

typedef struct { 
	No *topo; 
} PilhaDinamica;

void inicializar(PilhaDinamica *p) { 
	p->topo = NULL; 
} 

int push(PilhaDinamica *p, int valor) { 
	No *novo = (No *) malloc(sizeof(No)); 
	if (novo == NULL) return 0; // Falha na alocação 
	
	novo->dado = valor; 
	novo->proximo = p->topo; // O novo nó aponta para o antigo topo 
	p->topo = novo; // O topo passa a ser o novo nó 
	return 1; 
} 

int pop(PilhaDinamica *p, int *valor) { 
	if (p->topo == NULL) return 0; // Erro: Underflow (Pilha vazia) 
	
	No *temp = p->topo; 
	*valor = temp->dado; 
	p->topo = p->topo->proximo; // Atualiza o topo para o nó de baixo 
	free(temp); // Libera a memória do nó removido 
	return 1; 
}
```

### Problema da celebridade 

Em uma festa com $n$ pessoas, existe a hipótese de haver uma **celebridade**. Uma pessoa é considerada celebridade se cumpre duas condições rigorosas:

1. **Não conhece ninguém** na festa.
2. **É conhecida por todas** as outras pessoas da festa.

Temos à disposição uma função de consulta `conhece(A, B)` que retorna `true` se a pessoa $A$ conhece a pessoa $B$, e `false` caso contrário.

**Por que usar uma Pilha?**

- **Abordagem Bruta (Sem Pilha):** Testar todas as combinações de pessoas resulta em complexidade $O(n^2)$.
- **Abordagem Eficiente (Com Pilha):** Permite eliminar candidatos a cada comparação e resolver o problema em tempo **linear** $O(n)$.

**Passo a Passo da Solução com Pilha:**

1. **Empilhar todos os convidados:** Empilhe todas as $n$ pessoas (de $0$ a $n-1$).
2. **Fase de Eliminação:** Enquanto houver **mais de 1 pessoa na pilha**:
    - Desempilhe duas pessoas, $A$ e $B$.
    - Pergunte: `conhece(A, B)`?
        - **Se** $A$ **conhece** $B$**:** $A$ **não** pode ser a celebridade (pois uma celebridade não conhece ninguém). Descarte $A$ e **re-empilhe** $B$.
        - **Se** $A$ **NÃO conhece** $B$**:** $B$ **não** pode ser a celebridade (pois a celebridade é conhecida por todos). Descarte $B$ e **re-empilhe** $A$.
3. **Fase de Verificação Final:** Restará apenas **1 candidato** no topo da pilha. Desempilhe-o e faça uma checagem final:
    - Confirme se o candidato não conhece ninguém da festa.
    - Confirme se todas as outras pessoas conhecem o candidato.
    - Se passar nos dois testes, ele é a celebridade; caso contrário, não há celebridades na festa.

## Fila

A **Fila** é uma estrutura de dados linear que segue rigorosamente o princípio **FIFO** (_First-In, First-Out_ — **"O primeiro que entra é o primeiro que sai"**).

Analogia do mundo real: pense em uma fila de banco ou do caixa do supermercado. A primeira pessoa que entra na fila é a primeira a ser atendida e sair.

- **Início (Front / Head):** A posição de onde os elementos são removidos (atendidos).
- **Fim (Rear / Tail):** A posição onde novos elementos entram na fila.

### Operações


![[Pasted image 20260911212524.png]]

**A. Inserção (****Enqueue** **— Enfileirar)**

Adiciona um novo elemento exclusivamente no **fim** da fila.

- **Complexidade:** $O(1)$ — Tempo constante.
- **Cenários e Cuidados:**
    - **Overflow (Fila Cheia):** Na **Fila Sequencial (Array)**, é obrigatório checar se a quantidade de elementos atingiu a capacidade máxima (`quantidade == capacidade`) antes de inserir.
    - **Falha de Memória:** Na **Fila Dinâmica**, deve-se verificar se a alocação do novo nó via `malloc()` retornou `NULL`.

**B. Remoção (****Dequeue** **— Desenfileirar)**

Remove e retorna o elemento localizado no **início** da fila.

- **Complexidade:** $O(1)$ — Tempo constante.
- **Cenários e Cuidados:**
    - **Underflow (Fila Vazia):** Antes de desenfileirar, é obrigatório checar se a fila possui elementos (`quantidade == 0` ou `inicio == NULL`). Tentar desenfileirar uma fila vazia provoca erro de execução.
    - **Ajuste do Início:** Na fila circular, o ponteiro/índice de início deve avançar usando o operador módulo. Na fila dinâmica, o nó removido deve ter sua memória liberada com `free()`.

**C. Consulta e Busca de Elementos**

- **Consulta ao Início (****Peek** **ou** **Front****):** Retorna o valor do primeiro elemento da fila **sem removê-lo**.
    - **Complexidade:** $O(1)$.
- **Busca por um Elemento Qualquer:** Como a regra da fila exige inserção no fim e remoção no início, para buscar um elemento no meio/fim sob as regras estritas da estrutura, é necessário desenfileirar os elementos um a um até encontrá-lo (armazenando-os em uma fila auxiliar para depois recompor a fila original).
    - **Complexidade:** $O(n)$ — Tempo linear.

### Tipos de Filas

1. **Fila Simples:** Estrutura direta com inserção no fim e remoção no início.
2. **Fila Circular:** Utiliza um array de forma contínua em anel, reaproveitando as posições que ficaram vagas após remoções.
3. **Fila de Prioridade (Priority Queue):** Os elementos possuem prioridades atribuídas. O elemento de maior prioridade é sempre o primeiro a ser removido, independentemente da ordem de chegada (geralmente implementada com a estrutura _Heap_).


### Implementação 

**1) Fila Sequencial Circular (Com Array / Alocação Estática ou Dinâmica)**

**O Problema do Array Simples:**

Se apenas incrementarmos o índice de início a cada `dequeue`, o espaço no começo do array fica inutilizado, fazendo a fila parecer "cheia" mesmo com poucas posições ocupadas. Deslocar todos os elementos para a esquerda a cada remoção tornaria a operação lenta ($O(n)$).

**A Solução Circular:**

Tratamos o vetor como um círculo. Quando o ponteiro `fim` chega ao último índice do array e há posições livres no início, ele "volta" para o índice `0` utilizando o **operador de módulo (****%****)**: $$\text{Fim} = (\text{Fim} + 1) \pmod{\text{Capacidade}}$$

Para controlar com precisão os estados de cheia e vazia, utilizamos uma **estrutura de cabeçalho** com 4 campos: `inicio`, `fim`, `quantidade` e `capacidade`.

``` C
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int *dados;
    int inicio;
    int fim;
    int quantidade;
    int capacidade;
} FilaCircular;

FilaCircular* criar_fila(int capacidade) {
    FilaCircular *f = (FilaCircular*) malloc(sizeof(FilaCircular));
    f->dados = (int*) malloc(capacidade * sizeof(int));
    f->inicio = 0;
    f->fim = 0; // Aponta para a primeira posição livre
    f->quantidade = 0;
    f->capacidade = capacidade;
    return f;
}

int enqueue(FilaCircular *f, int valor) {
    if (f->quantidade == f->capacidade) return 0; // Erro: Overflow (Fila Cheia)

    f->dados[f->fim] = valor;
    f->fim = (f->fim + 1) % f->capacidade; // Avança circularmente
    f->quantidade++;
    return 1; // Sucesso
}

int dequeue(FilaCircular *f, int *valor) {
    if (f->quantidade == 0) return 0; // Erro: Underflow (Fila Vazia)

    *valor = f->dados[f->inicio];
    f->inicio = (f->inicio + 1) % f->capacidade; // Avança circularmente
    f->quantidade--;
    return 1; // Sucesso
}
```

---

**2) Fila Dinâmica (Com Lista Encadeada)**

Utiliza nós encadeados em memória heap. A estrutura armazena dois ponteiros: um para o `inicio` (primeiro nó a sair) e um para o `fim` (último nó inserido).

``` C
typedef struct No {
    int dado;
    struct No *proximo;
} No;

typedef struct {
    No *inicio;
    No *fim;
    int quantidade;
} FilaDinamica;

void inicializar(FilaDinamica *f) {
    f->inicio = NULL;
    f->fim = NULL;
    f->quantidade = 0;
}

int enqueue(FilaDinamica *f, int valor) {
    No *novo = (No*) malloc(sizeof(No));
    if (novo == NULL) return 0; // Falha na alocação

    novo->dado = valor;
    novo->proximo = NULL;

    if (f->quantidade == 0) {
        f->inicio = novo; // Se vazia, início também aponta para o novo nó
    } else {
        f->fim->proximo = novo; // O nó antigo do fim aponta para o novo
    }

    f->fim = novo; // Atualiza o ponteiro de fim
    f->quantidade++;
    return 1;
}

int dequeue(FilaDinamica *f, int *valor) {
    if (f->quantidade == 0) return 0; // Erro: Underflow (Fila Vazia)

    No *temp = f->inicio;
    *valor = temp->dado;

    f->inicio = f->inicio->proximo; // O início passa para o próximo nó
    if (f->inicio == NULL) {
        f->fim = NULL; // Se a fila ficou vazia, ajusta o fim para NULL
    }

    free(temp); // Libera o nó removido
    f->quantidade--;
    return 1;
}
```

### Comparativo de Operações

|Operação|Complexidade|Condição de Erro / Borda|
|---|---|---|
|**Enqueue** **(Inserir)**|$O(1)$|**Overflow:** Fila Cheia (`quantidade == capacidade` ou erro no `malloc`).|
|**Dequeue** **(Remover)**|$O(1)$|**Underflow:** Fila Vazia (`quantidade == 0`).|
|**Peek** **(Consultar)**|$O(1)$|Fila Vazia (`quantidade == 0`).|
|**Busca por Posição/Valor**|$O(n)$|Exige desenfileirar elementos para inspeção.|

## **Tabela Hash (Tabela de Dispersão)**

### Conceito e Modelo Ideal vs. Aplicação Real

Diferente das listas (cujo tempo médio de acesso é \(T = n/2\)), a **Tabela Hash** busca implementar um modelo ideal de acesso direto em **tempo constante \(O(1)\)** por meio da transformação chave-índice. Em aplicações reais, esse comportamento ideal é aproximado.

A estrutura é organizada por dois componentes centrais:

1. **Tabela de Hashing:** Um vetor de tamanho finito composto por \(b\) entradas ou depósitos.
2. **Função de Hashing (\(h(C)\)):** Uma regra de cálculo que mapeia uma chave \(C\) para um índice numérico válido no intervalo da tabela.

##### **Propriedades Importantes:**

- **Ausência de Ordem:** Não existe ordem física entre os elementos; quem determina a posição de cada dado é exclusivamente a função Hash. Por essa razão, a tabela hash não permite imprimir os dados em ordem de chave nem buscar facilmente o elemento com maior ou menor chave.
- **Colisão:** Ocorre quando a função hash gera exatamente a mesma posição na tabela para duas ou mais chaves diferentes ($h(C_1) = h(C_2)$).
- **Fator de Carga (**$\alpha$**)**: É a razão entre o número de elementos armazenados e a capacidade total da tabela ($\alpha = \frac{n}{b \cdot s}$). Manter o fator de carga controlado (como em torno de 0,75) garante que existam posições livres para manter a eficiência do sistema e evitar a degradação do tempo de acesso.

---

### Hashing Aberto (Encadeado / Chaining)

No **Hashing Aberto**, a tabela hash consiste em um vetor onde cada posição armazena a **cabeça de uma lista encadeada**. Quando ocorre uma colisão, os novos elementos são simplesmente encadeados no mesmo índice.

##### **Cenários de Operação:**

- **Inserção (\(O(1)\) constante):**
    
    1. Calcula-se a posição usando a função hash: \(pos = h(C)\) (por exemplo, via resto da divisão: \(C \bmod b\)).
    2. Aloca-se dinamicamente um novo nó com `malloc()`.
    3. O novo nó é inserido no início da lista encadeada daquela posição (`novo->prox = tabela[pos]; tabela[pos] = novo;`).
- **Busca (\(O(1)\) médio, \(O(n)\) pior caso):**
    
    1. Calcula-se o índice correspondente: \(pos = h(C)\).
    2. Acessa-se a cabeça da lista contida em `tabela[pos]`.
    3. Percorre-se a lista encadeada de forma sequencial até encontrar o elemento com a chave desejada ou atingir o fim (`NULL`).
- **Remoção (\(O(1)\) médio, \(O(n)\) pior caso):**
    
    1. Calcula-se a posição \(pos = h(C)\).
    2. Se a chave estiver no primeiro nó da lista (`tabela[pos]`), atualiza-se a cabeça da lista para o próximo nó (`tabela[pos] = tabela[pos]->prox`) e libera-se a memória com `free()`.
    3. Caso esteja no meio/fim da lista, percorre-se a estrutura mantendo um ponteiro para o nó anterior (`ant`). Ao localizar o nó, ajusta-se o encadeamento (`ant->prox = aux->prox`) e libera-se a memória.

#### **Implementação Prática em C (Hashing Aberto):**

``` c
#define numEntradas 8

typedef struct _Hash {
    int chave;
    struct _Hash *prox;
} Hash;

typedef Hash* Tabela[numEntradas];

int funcaoHashing(int num) {
    return num % numEntradas;
}

// Inserção
void inserirHash(Tabela tabela, int n) {
    int pos = funcaoHashing(n);
    Hash* novo = (Hash *) malloc(sizeof(Hash));
    novo->chave = n;
    novo->prox = tabela[pos];
    tabela[pos] = novo;
}

// Busca
Hash* localizarHash(Tabela tabela, int num) {
    int pos = funcaoHashing(num);
    Hash* aux;
    if (tabela[pos] != NULL) {
        if (tabela[pos]->chave == num) return tabela[pos];
        else {
            aux = tabela[pos]->prox;
            while (aux != NULL && aux->chave != num)
                aux = aux->prox;
            return aux;
        }
    }
    return NULL;
}

// Remoção
void excluirHash(Tabela tabela, int num) {
    int pos = funcaoHashing(num);
    Hash* aux;
    if (tabela[pos] != NULL) {
        if (tabela[pos]->chave == num) {
            aux = tabela[pos];
            tabela[pos] = tabela[pos]->prox;
            free(aux);
        } else {
            Hash* ant = tabela[pos];
            aux = tabela[pos]->prox;
            while (aux != NULL && aux->chave != num) {
                ant = aux;
                aux = aux->prox;
            }
            if (aux != NULL) {
                ant->prox = aux->prox;
                free(aux);
            } else {
                printf("\nNumero nao encontrado");
            }
        }
    } else {
        printf("\nNumero nao encontrado");
    }
}
```

---

### Hashing Fechado (Endereçamento Aberto / Open Addressing)

No **Hashing Fechado**, todos os elementos são armazenados no **próprio vetor da tabela**, sem a necessidade de ponteiros ou estruturas encadeadas adicionais. Quando ocorre uma colisão, procura-se por outra posição livre dentro da própria tabela.

#### **Os Estados das Posições (Slots):**

Como o espaço no vetor é reutilizado, a remoção em endereçamento aberto **não pode simplesmente apagar o valor do vetor**, pois isso quebraria a sequência de sondagem e faria buscas posteriores falharem. Cada posição da tabela deve ser marcada com um estado:

- **Livre ('L'):** A posição nunca foi utilizada.
- **Ocupado ('O'):** A posição contém uma chave válida ativa.
- **Removido ('R'):** A posição continha uma chave que foi excluída. Permite continuar a busca de elementos que colidiram após ela.

#### **Técnicas de Sondagem para Solução de Colisões:**

1. **Tentativa Linear (Linear Probing):**
    
    - **Fórmula:** \\(h'(x, j) = $$h'(x, j) = (h(x) + j) \bmod m \quad \text{para } 1 \le j \le m-1$$ _Onde_ $h(x) = x \bmod m$ _é a função hash inicial,_ $j$ _é a tentativa de salto e_ $m$ _é a capacidade da tabela
    - **Funcionamento:** Avança sequencialmente de $1$ em $1$ posição ($h(x)+1, h(x)+2, h(x)+3, \dots$) a partir do índice de colisão até encontrar um slot vago.
-
    - **Problema:** Gera **agrupamentos primários (clusters primários)**, onde longas sequências de posições ocupadas se formam, aumentando progressivamente o tempo de busca.
2. **Tentativa Quadrática (Quadratic Probing):**

- **Fórmula Recorrente:** $$ \begin{cases} h'(x, 0) = h(x) \\ h'(x, k) = \big(h'(x, k-1) + k\big) \bmod m \quad \text{para } 1 \le k \le m-1 \end{cases} $$ *Onde* $k$ *representa a* $k$-ésima tentativa de colisão.
- **Funcionamento:** O tamanho dos saltos cresce a cada tentativa ($+1, +2, +3, \dots$), gerando uma sequência acumulada quadrática ($h(x)+1, h(x)+3, h(x)+6, h(x)+10, \dots$) que afasta a busca rapidamente da zona de colisão3.
- **Vantagem:** Mitiga o agrupamento primário e reduz a degradação de desempenho, gerando apenas **agrupamento secundário** (quando chaves diferentes compartilham o mesmo $h(x)$ inicial)2.

#### **Cenários de Operação no Endereçamento Aberto:**

- **Inserção:**
    
    1. Calcula-se a posição inicial \(pos = h(n)\).
    2. Percorre-se a sequência de sondagem (linear ou quadrática) enquanto as posições estiverem ocupadas ('O').
    3. Insere-se a chave na primeira posição encontrada com estado **'L' (livre)** ou **'R' (removido)** e altera-se o estado para **'O'**.
    4. Se percorrer toda a tabela sem encontrar 'L' ou 'R', indica-se que a tabela está cheia.
- **Busca:**
    
    1. Calcula-se o índice inicial \(pos = h(n)\).
    2. Avança-se na sequência de sondagem enquanto a posição não for **'L' (livre)** e a chave armazenada for diferente da procurada. As posições marcadas como **'R' são ignoradas/ultrapassadas** para continuar a busca.
    3. Se a chave for localizada em um slot marcado com estado **'O'**, retorna-se o índice correspondente. Se encontrar um slot 'L' ou percorrer toda a tabela, conclui-se que o elemento não está presente.
- **Remoção:**
    
    1. Executa-se a função de busca para obter o índice da chave.
    2. Se encontrada, altera-se apenas o estado da posição para **'R' (removido)**.

---

#### **Implementação Prática em C (Tentativa Linear):**

``` c
#define tam 8

typedef struct {
    int chave;
    char livre; // 'L' = livre, 'O' = ocupado, 'R' = removido
} Hash;

typedef Hash Tabela[tam];

int funcaoHashing(int num) {
    return num % tam;
}

// Inserção com Tentativa Linear
void inserir(Tabela tabela, int n) {
    int i = 0;
    int pos = funcaoHashing(n);
    while (i < tam && tabela[(pos + i) % tam].livre != 'L' && tabela[(pos + i) % tam].livre != 'R') {
        i = i + 1;
    }
    if (i < tam) {
        tabela[(pos + i) % tam].chave = n;
        tabela[(pos + i) % tam].livre = 'O';
    } else {
        printf("\nTabela cheia!");
    }
}

// Busca com Tentativa Linear
int buscar(Tabela tabela, int n) {
    int i = 0;
    int pos = funcaoHashing(n);
    while (i < tam && tabela[(pos + i) % tam].livre != 'L' && tabela[(pos + i) % tam].chave != n) {
        i = i + 1;
    }
    if (tabela[(pos + i) % tam].chave == n && tabela[(pos + i) % tam].livre == 'O') {
        return (pos + i) % tam;
    } else {
        return tam; // Não encontrado
    }
}

// Remoção
void remover(Tabela tabela, int n) {
    int posicao = buscar(tabela, n);
    if (posicao < tam) {
        tabela[posicao].livre = 'R';
    } else {
        printf("\nElemento nao esta presente.");
    }
}
```

#### **Implementação Prática em C (Tentativa Quadrática):**

``` c
// Inserção com Tentativa Quadrática
void inserirChave(Tabela tabela, int n) {
    int pos = funcaoHashing(n);
    int k = 1;
    while (k < tam && tabela[pos].livre != 'L' && tabela[pos].livre != 'R') {
        pos = (pos + k) % tam;
        k = k + 1;
    }
    if (k < tam) {
        tabela[pos].chave = n;
        tabela[pos].livre = 'O';
    } else {
        printf("\nTabela cheia ou em loop!");
    }
}

// Busca com Tentativa Quadrática
int buscarChave(Tabela tabela, int n) {
    int pos = funcaoHashing(n);
    int k = 1;
    while (k <= tam && tabela[pos].livre != 'L' && tabela[pos].chave != n) {
        pos = (pos + k) % tam;
        k = k + 1;
    }
    if (tabela[pos].chave == n && tabela[pos].livre == 'O') {
        return pos;
    } else {
        return tam; // Não encontrado
    }
}

// Remoção
void removerChave(Tabela tabela, int n) {
    int posicao = buscarChave(tabela, n);
    if (posicao < tam) {
        tabela[posicao].livre = 'R';
    } else {
        printf("\nElemento nao estah presente.");
    }
}
```


### Resumo Comparativo das Estruturas

|Aspecto|Hashing Aberto (Encadeado)|Hashing Fechado (Endereçamento Aberto)|
|:--|:--|:--|
|**Armazenamento**|Vetor de ponteiros + Listas Encadeadas fora do vetor.|Tudo armazenado dentro do próprio vetor de \(m\) posições.|
|**Alocação de Memória**|Dinâmica em runtime via `malloc()`.|Fixa no array.|
|**Tratamento de Remoção**|Libera o nó da lista encadeada com `free()`.|Exige marcar a posição como Removido ('R') para não quebrar a sondagem.|
|**Limite de Capacidade**|Suporta mais elementos que o número de entradas do vetor.|Limitado à capacidade total do vetor (\(m\)).|
|**Resolução de Colisão**|Encadeamento sequencial na lista.|Sondagem Linear (\(h(x)+j\)) ou Quadrática (\(h(x)+k\)).|

### **Nomenclatura Formal e Parâmetros Numéricos**

A literatura técnica define a Tabela Hash através de parâmetros formais de capacidade e preenchimento:

- $n$**:** Número total de elementos armazenados.
- $b$**:** Número de depósitos / entradas na tabela (tamanho do vetor).
- $s$**:** Capacidade de cada depósito (aplicável ao hashing fechado).
- $T$**:** Cardinalidade do domínio das chaves (total de chaves possíveis no universo).
- $\frac{n}{T}$ **(Densidade Identificadora):** Razão entre elementos armazenados e chaves possíveis.
- $\alpha = \frac{n}{b \cdot s}$ **(Densidade de Carga / Fator de Carga):** Mede o nível de preenchimento da tabela.

---

###  **Técnicas Avançadas de Funções Hash**

Para evitar a degeneração no pior caso (onde todas as chaves colidem no mesmo índice), a função hash deve garantir **distribuição uniforme**. _(Exemplo de função ruim: usar a "primeira letra do nome", pois letras do alfabeto não são distribuídas uniformemente na população)._

As principais técnicas para construir funções de dispersão são:

- **Método do Resto da Divisão:** $h(C) = C \bmod b$ (o método clássico e mais utilizado).
- **Meio do Quadrado (Mid-Square):** Eleva-se a chave ao quadrado e extraem-se os bits/dígitos centrais do resultado. Como o centro do quadrado depende de todos os dígitos da chave, a distribuição melhora.
- **Desdobramento (Folding):** Utilizado para cadeias de caracteres (strings). A string é dividida em pedaços e seus códigos ASCII são somados:
    - **Shift Folding:** Soma simples dos blocos de caracteres.
    - **Limit Folding:** Inverte os dígitos a cada segundo caractere antes de realizar a soma (como uma sanfona).
- **Análise de Frequência:** Analisa uma amostra das chaves e escolhe os dígitos/caracteres que apresentam a variação mais uniforme.

### Limitações e Comparativo (Hash vs. Listas vs. Árvores)

O material estabelece um comparativo direto entre as estruturas de dados:

| Estrutura       | Tempo Médio de Acesso | Vantagens                                                       | Limitações Principais                                                                                            |
| --------------- | --------------------- | --------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **Listas**      | $T = \frac{n}{2}$     | Simplicidade de implementação.                                  | Lenta para grande volume de dados (ex: 100.000 dados exigem centenas de milhares de acessos).                    |
| **Tabela Hash** | $T \approx O(1)$      | Desempenho excelente para buscas diretas e alta escalabilidade. | **Não permite imprimir dados em ordem**, realizar buscas por faixa/intervalo, nem encontrar a menor/maior chave. |

## Arvore binária 

Uma árvore pode ser um nulo (vazio), se nao for vazio é dividida em nós e subárvore.

Ela é binária porque cada nó tem no máximo dos filhos. 

O nó que nao tem nenhum pai, se chama de raiz (raiz da árvore). Também tem as raizes das subarvores. Quem nao tem filho,, tem o nome de folha. 

O caminho de um nó em uma árvore binária ==é a sequência de nós percorrida desde a [nó raiz](https://concursos.estrategia.com/portal/percursos-arvores-binarias/) até o nó desejado==. Nao pode subir, apenas desce pela árvore. 

Longitude: e quantos santos se da em um caminho. 

altura de um nó: maior longitude de um nó, até as folhas. Tem que pegar a maior longitudade

altura de uma árvore: é a altura da raiz. Maior valor da raiz, até as folhas.

Nivel de um nó: longitude da raiz até ele. 

O ultimo nivel de uma árvore é a altura dela. 


- árvore completa 
todos os nós, ou nao tem filhos, ou tem dois 

- árvore cheia
é uma árvore completa e todas as folhas estão no mesmo nível . 


fórmula para saber a altura máxima de nó (n -1)

Para saber a altura mínima (Log(n + 1) -1)

- Caminhamento:
Pode se percorrer uma arvore de cima para baixa (percorrendo em profundidade). Tem 3 maneiras de se fazer: pré-ordem, em ordem, pós ordem.
1) pré-ordem: visita a raiz da árvore, depois a sub-arvore esquerda e depois a direita
2) em ordem visita a sub-arvore esquerda, raiz e direita
3) esquerda, direita, raiz
==visita a sub-arvore a direita ou a esquerda e nao o nó==


Ou de esquerda para a direita (percorrendo em largura). Percorrendo em nivel