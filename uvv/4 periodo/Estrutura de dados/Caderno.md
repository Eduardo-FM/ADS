
## Aulas iniciais
### ponteiro

Em C, **ponteiro é uma variável que guarda o endereço de memória de outra variável**.

``` c
int numero = 10;
int *p = &numero;
```

- `&` → pega o **endereço** de uma variável.
- `*` na declaração → indica que a variável é um **ponteiro**.
- `*p` → acessa o **valor armazenado no endereço** para o qual `p` aponta.

Exemplo:
``` c
*p = 50;
```

### estrutura dinâmica

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

Tipo abstrato de dados (tipo definido pelo usuário, aonde se define o conjunto de elementos e as operações que atuam sobre esses elementos).

É feito as operações, mas o usuário não sabe como é feito.

No C, o arquivo .c implementa as operações, e o arquivo .h define as operações. 

**O TAD é o **conceito/interface + implementação** que permite usar um tipo sem precisar conhecer seus detalhes internos. O `.h` normalmente representa a **interface pública**, enquanto o `.c` contém a **implementação**.

Um **TAD (Tipo Abstrato de Dados)** é um tipo definido pelo usuário que determina:

- **quais dados** serão armazenados;
- **quais operações** podem ser realizadas sobre esses dados.

A ideia principal é a **abstração**: o usuário sabe **o que pode fazer**, mas não precisa saber **como as operações são implementadas**.

####  Arquivo `.h` — Interface

O arquivo `.h` contém as **declarações** que serão disponibilizadas para quem utilizar o TAD, como:

- funções;
- tipos;
- constantes;
- estruturas que precisam ser conhecidas externamente.

Exemplo:

``` c
void inserir(int valor);
void remover(void);
```

É como um **manual de uso** do TAD.

#### Arquivo `.c` — Implementação

O arquivo `.c` contém o **código das funções declaradas no `.h`**.

É onde fica a lógica de **como as operações realmente funcionam**.

``` c
void inserir(int valor)
{
    // implementação
}
```

É como a **parte interna** do TAD.

### 🔗 Relação entre eles

```
.h → O QUE o TAD oferece
.c → COMO o TAD funciona
```

Normalmente:

```
programa.c
    ↓
inclui
    ↓
TAD.h
    ↓
utiliza as funções
    ↓
TAD.c
    ↓
implementa as funções
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

há dois tipos de listas sequenciais:
- com alocaçao estática
- com alocacao dinâmica

A lista é sequencial pq cada elemento de sua lista não há um endereco de memoria disponivel.

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

para acessar um elemento o acesso é direto, entao se dá a posiçao do elemento é você já consegue acessa-la.

Para saber a posiçao do elemento: a base do array é o elemento na primeira posição, para achar outro elemento ele pega o endereço base + indexe * o tamanho do elemento (ex: int tem 4 bites).

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


#### lista encadeada 

Ela tem a seguinte forma, precisa guardar o valor que vc quer guardar e guardar o endereço do próximo elemento. 

#### lista duplamente encadeada 

Guarda o endereço do próximo e do anterior. 


## aula 21_08

A operação de inserir tem sempre tempo constante (O(1)).

A operação de remoção, há uma análise de melhor caso e de pior caso. No melhor caso a uma operação O(1), no pior caso é O(n).

A operacao de busca, há uma análise de melhor caso e de pior caso. no melhor caso a operacao O(1), no pior caso é O(n).

### Lista encadeada

Como na lista encadeada os elementos nao tem posiçoes adjacentes de memórias, é mais fácil para inserir novos elementos. 

Também tem a flexibilidade para inserir um elemento entre dois elementos.

Existe vários tipos de lista encadeada:
- Lista simplesmente encadeada (anda em apenas um sentido)
- Lista duplamente encadeada (o elemento aponta para o anterior e o posterior)
- lista circular (o primeiro aponta para o ultimo, o ultimo aponta para o primeiro)

É possivel criar um cabeçalho da lista armazenando informaçoes como: tamanho, ultimo, primeiro. Para facilitar operacoes de inserçao, remoção,, ...


Para implementar tem que ter no cabeçalho:
- struct para o nó da lista;
- struct para a lista;




