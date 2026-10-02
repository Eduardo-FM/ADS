#include <stdio.h>
#include <stdlib.h>

#include "list.h"

struct head
{
    int count;
    struct node *first;
    struct node *last;
};

struct node
{
    int val;
    struct node *prev;
    struct node *next;
    
};

List *insert_last(List *Lista, int x)
{

    if (Lista == NULL)
    {
        return NULL;
    }
    
    node *novo = malloc(sizeof(node));

    if(novo == NULL) return NULL;

    novo->val = x;
    novo->next = NULL;

    //Lista vazia
    if (Lista->count == 0)
    {
        novo->prev = NULL;

        Lista->first = novo;
        Lista->last = novo;
    }
    
    //lista com elemento
    else 
    {
        novo->prev = Lista->last;
        Lista->last->next = novo;
        Lista->last = novo;
    }

    Lista->count++;
    return Lista;
}

