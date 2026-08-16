#ifndef CIRCUNFERENCIA_H
#define CIRCUNFERENCIA_H

typedef struct circunferencia circunferencia;

circunferencia* cria_circunferencia(ponto *centro, float raio);
void destroi_circunferencia(circunferencia *c);

void exibe_circunferencia(circunferencia *c);
int pos_relativa_ponto(circunferencia *c, ponto *p);

#endif