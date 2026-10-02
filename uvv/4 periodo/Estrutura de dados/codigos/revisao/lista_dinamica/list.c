#include "list.h"
#include <stdio.h>
#include <stdlib.h>

struct list
{
    int capacity;
    int last_element;
    int *elements;
};

list* create (int capacity)
{
    //se a capacidade for 0, retorna null
    if (capacity <= 0) return NULL;

    list  *l = malloc(sizeof(list));

    // se não criar a lista, retorna null
    if(l == NULL) return NULL;

    l->elements = malloc(sizeof(int) * capacity);

    //se nao criar os elementos, retorna null
    if(l->elements == NULL)
    {
        free(l);
        return NULL;
    }

    l->capacity = capacity;
    l->last_element = 0;

    return l;
}

void destroy(list *l)
{
    
    if (l == NULL) return;

    free(l->elements);    
    free(l);
}

int insert(list *l, int element)
{
    if (l == NULL) return 0;

    if(l->last_element >= l->capacity) return 0;
  
    l->elements[l->last_element] = element;
    l->last_element++;

    return 1;
}

int remove(list *l, int position)
{
    if (l == NULL) return 0;

    if(position < 0 || position >= l->last_element) return 0;

    for (int i = position; i < l->last_element -1 ; i++)
    {
        l->elements[i] = l->elements[i + 1];
    }

    l->last_element--;

    return ;
}

int search(list *l, int element)
{
    if (l == NULL) return -1;

    for (int i = 0; i < l->last_element; i++)
    {
        if (l->elements[i] == element)
        {
            return i;
        } 
    }
    
    return -1;
}

void show(list *l)
{
    if (l == NULL) return;

    for (int i = 0; i < l->last_element; i++)
    {
        printf("%d", l->elements[i]);

        if (i < l->last_element -1)
        {
            printf(", ");
        }
        
    }

    printf("\n");
    
}