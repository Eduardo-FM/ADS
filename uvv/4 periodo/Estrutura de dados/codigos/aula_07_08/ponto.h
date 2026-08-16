#ifndef PONTO_H
#define PONTO_H

typedef struct ponto ponto;

ponto* cria_ponto(float x, float y);
void destroi_ponto(ponto *p);

ponto* soma_ponto(ponto *p, ponto *q);
void exibe_ponto(ponto *p);
float distancia_ponto(ponto *p, ponto *q);
float get_x(ponto *p);
float get_y(ponto *p);
void set_x(ponto *p, float x);
void set_y(ponto *p, float y);

#endif