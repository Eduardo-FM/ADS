#include <stdio.h>
#include <stdlib.h>
#include "ponto.h"
#include "circunferencia.h"

struct circunferencia{
    ponto *centro;
    float raio;
};

circunferencia* cria_circunferencia(ponto *centro, float raio){
  circunferencia *c = NULL;
  
  if (raio) {
    c = malloc(sizeof(circunferencia));
    if (c)
      c->centro = cria_ponto(get_x(centro), get_y(centro));
      c->raio = raio;
  }
  return c;
}

void destroi_circunferencia(circunferencia *c){
    free(c->centro);
    free(c);
}

void exibe_circunferencia(circunferencia *c){
    
}

int pos_relativa_ponto(circunferencia *c, ponto *p){
    return distancia_ponto(c->centro, p) > c->raio;
}