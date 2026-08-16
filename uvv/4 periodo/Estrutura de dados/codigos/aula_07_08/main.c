#include <stdio.h>
#include "ponto.h"
#include "circunferencia.h"

int main()
{
    ponto *origem = cria_ponto(0,0);
    ponto *p = cria_ponto(0.5,0.3);
    ponto *q = cria_ponto(1,0);
    ponto *w = cria_ponto(1,1);
    ponto *v[3] = {p, q, w};
    circunferencia * c = cria_circunferencia(origem, 1);
    
    for (int i=0; i < 3; i++){
        if (pos_relativa_ponto(c, v[i]))
            printf("Fora\n");
        else
            printf("Dentro\n");
    }
    
    destroi_ponto(origem);
    destroi_ponto(p);
    destroi_ponto(q);
    destroi_ponto(w);
    destroi_circunferencia(c);

    return 0;
}