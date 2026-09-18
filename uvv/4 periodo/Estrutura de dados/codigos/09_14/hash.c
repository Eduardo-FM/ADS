#include <stdio.h>
#include <stdlib.h>

#include "hash.h"

struct Hash
{
    int valor;
    struct Hash *proximo;
};

struct TADTabelaHash
{
    Hash *tabela[TAMANHO_HASH];
};

void inicializarHash(TADTabelaHash *hash)
{
    if (hash == NULL)
    {
        return;
    }

    for (int i = 0; i < TAMANHO_HASH; i++)
    {
        hash->tabela[i] = NULL;
    }
}


int funcaoHashing(int valor)
{
    return valor % TAMANHO_HASH;
}


void inserirHash(TADTabelaHash *hash, int valor)
{
    if (hash == NULL)
    {
        return;
    }

    int indice = funcaoHashing(valor);

    Hash *novo = malloc(sizeof(Hash));

    if (novo == NULL)
    {
        return;
    }

    novo->valor = valor;

    novo->proximo = hash->tabela[indice];

    hash->tabela[indice] = novo;
}


void mostrarHash(TADTabelaHash *hash)
{
    if (hash == NULL)
    {
        return;
    }

    for (int i = 0; i < TAMANHO_HASH; i++)
    {
        printf("[%d] -> ", i);

        Hash *atual = hash->tabela[i];

        while (atual != NULL)
        {
            printf("%d -> ", atual->valor);
            atual = atual->proximo;
        }

        printf("NULL\n");
    }
}


Hash *localizarHash(TADTabelaHash *hash, int valor)
{
    if (hash == NULL)
    {
        return NULL;
    }

    int indice = funcaoHashing(valor);

    Hash *atual = hash->tabela[indice];

    while (atual != NULL)
    {
        if (atual->valor == valor)
        {
            return atual;
        }

        atual = atual->proximo;
    }

    return NULL;
}


void excluirHash(TADTabelaHash *hash, int valor)
{
    if (hash == NULL)
    {
        return;
    }

    int indice = funcaoHashing(valor);

    Hash *atual = hash->tabela[indice];
    Hash *anterior = NULL;

    while (atual != NULL)
    {
        if (atual->valor == valor)
        {
            if (anterior == NULL)
            {
                // O elemento é o primeiro da lista
                hash->tabela[indice] = atual->proximo;
            }
            else
            {
                // O elemento está no meio ou no final
                anterior->proximo = atual->proximo;
            }

            free(atual);
            return;
        }

        anterior = atual;
        atual = atual->proximo;
    }
}


void liberarMemoria(TADTabelaHash *hash)
{
    if (hash == NULL)
    {
        return;
    }

    for (int i = 0; i < TAMANHO_HASH; i++)
    {
        Hash *atual = hash->tabela[i];

        while (atual != NULL)
        {
            Hash *proximo = atual->proximo;

            free(atual);

            atual = proximo;
        }

        hash->tabela[i] = NULL;
    }
}