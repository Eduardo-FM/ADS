#ifndef HASH_H
#define HASH_H

#define TAMANHO_HASH 10

typedef struct Hash Hash;

typedef struct TADTabelaHash TADTabelaHash;

void inicializarHash(TADTabelaHash *hash);

int funcaoHashing(int valor);

void inserirHash(TADTabelaHash *hash, int valor);

void mostrarHash(TADTabelaHash *hash);

Hash *localizarHash(TADTabelaHash *hash, int valor);

void excluirHash(TADTabelaHash *hash, int valor);

void liberarMemoria(TADTabelaHash *hash);

#endif