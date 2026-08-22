#include <stdio.h>

#include "list.h"

int main() {

    list *l = create_list(5);

    if(l == NULL)
        printf("Erro ao criar a lista");

    printf("Lista criada");
    

    return 0;
}