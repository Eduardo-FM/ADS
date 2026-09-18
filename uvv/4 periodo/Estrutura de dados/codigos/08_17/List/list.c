#include "list.h"
#include <stdio.h>
#include <stdlib.h>

struct list
{
    int capacity;
    int last_element;
    int *elements;
};


list* create_list(int capacity) 
{
    if (capacity <= 0)
    {
        return NULL;
    }

    list *l = malloc(sizeof(list));

    if (l == NULL) 
    {
        return NULL;
    }

    l->elements = malloc(capacity * sizeof(int));

    if (l-> elements == NULL) 
    {
        free(l);
        return NULL;
    }

    l->capacity = capacity;
    l->last_element = 0;

    return l;
    
}

void destroy_list(list *l) 
{
    if (l == NULL) 
    {
        return;
    }

    free(l->elements);
    free(l);
}

int insert_list(list *l, int element) 
{
    if (l == NULL) {
        return 0;
    }

    if(l->last_element >= l->capacity)
    {
        return 0;
    }

    l->elements[l->last_element] = element;
    l->last_element++;

    return 1;
}

int remove_list(list *l, int position) 
{
    if (l == NULL)
    {
        return 0;
    }

    if (position < 0 || position >= l->last_element)
    {
        return 0;
    }

    for (int i = position; i < l->last_element - 1; i++)
    {
        l->elements[i] = l->elements[i + 1];
    }
    
    l->last_element--;

    return 1;
}

int search_list(list *l, int element)
{
    if (l == NULL)
    {
        return -1;
    }

    for (int i = 0; i < l->last_element; i++)
    {
        if (l->elements[i] == element)
        {
            return i;
        }
        
    }

    return-1;
}

void show_list(list *l)
{
    for (int i = 0; i < l->last_element; i++)
    {
        printf("%d", l->elements[i]);

        if (i < l->last_element - 1)
        {
            printf(", ");
        }
    }

    printf("\n");
}