==ponteiro==

==estrutura dinâmica==

- TAD 
Tipo abstrato de dados (tipo definido pelo usuário, aonde se define o conjunto de elementos e as operações que atuam sobre esses elementos).
É feito as operações, mas o usuário não sabe como é feito.

No C, o arquivo .c implementa as operações, e o arquivo .h define as operações. 

O TAD então sãos as bibliotecas do C e o arquivo .h

==arquivo .c e .h==

# aula 10_08

*Complexidade de algoritmo*

A complexidade de algoritmo serve para medir a qualidade de algoritmo.

Para fazer essa análise se utiliza a análise do pior caso, melhor caso e caso médio.

##### ==Anotação Big O==

# 14_08

## Listas 

### Lista sequencial

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

### Lista dinamica

Na alocação dinâmica se utiliza o malloc.

```c
int *v;

v = malloc(n/*numero definido em tempo de execucao */* * sizeOf(int))

//para acessar 


free(v);
```

É possivel mudar o tamnho da alocacao dinamica durante o código.

#### Código em C
##### estatica

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


##### dinamica

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


### lista encadeada 

Ela tem a seguinte forma, precisa guardar o valor que vc quer guardar e guardar o endereço do próximo elemento. 

### lista duplamente encadeada 

Guarda o endereço do próximo e do anterior. 


# aula 21_08

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


# Aula 24_08



