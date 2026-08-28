#include <stdlib.h>
#include <limits.h>

#include "linked_list.h"

struct node
{
    int value;
    struct node* next;
};

struct linked_list
{
    int bigger;
    int smaller; 
    int size;
    struct node *first;
    struct node *last;
};

linked_list* create() 
{
    linked_list *list = malloc(sizeof(linked_list));

    if (list == NULL)
    {
        return NULL;
    }

    list->bigger = INT_MIN;
    list->smaller = INT_MAX;
    list->size = 0;
    list->first = NULL;
    list->last = NULL;

    
    return list;
    
}

void destroy(linked_list *linked_list)
{
    if (linked_list == NULL)
    {
        return;
    }
    
    struct node *current = linked_list->first;

    while (current != NULL)
    {
        struct node *next = current->next;
        
        free(current);
        current = next;
    }
    
    
    free(linked_list);
}

void insert_begin(linked_list *list,int number)
{
    if (list == NULL)
    {
        return;
    }
    
    
}

void insert_end(linked_list *list, int number)
{

}

void remove_node(linked_list *list, node *node)
{
    
}

node* search(linked_list *list, int value)
{

}