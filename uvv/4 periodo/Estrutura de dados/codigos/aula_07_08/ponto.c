#include "ponto.h"
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct ponto{
    float x, y;
};

ponto* cria_ponto(float x, float y) {
    ponto *p = NULL;
    
    if (p = malloc (sizeof(ponto))) {
        p->x = x;
        p->y = y;
    }
    
    return p;
}

void destroi_ponto(ponto *p){
    free(p);
}

ponto* soma_ponto(ponto *p, ponto *q) {
    ponto *r = NULL;
    
    if (r = malloc (sizeof(ponto))) {
        r->x = p->x + q->x;
        r->y = p->y + q->y;
    }
    
    return r;
}

void exibe_ponto(ponto *p) {
    printf("(%f, %f)", p->x, p->y);
}

float distancia_ponto(ponto *p, ponto *q){
    float deltax = p->x - q->x;
    float deltay = p->y - q->y;
    
    return sqrt(deltax*deltax + deltay*deltay);
}

float get_x(ponto *p){
    return p->x;
}

float get_y(ponto *p){
    return p->y;
}

void set_x(ponto *p, float x){
    p->x = x;
}

void set_y(ponto *p, float y){
    p->y = y;
}

