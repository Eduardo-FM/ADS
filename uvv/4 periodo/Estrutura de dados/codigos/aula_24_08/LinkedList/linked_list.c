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

void insert_begin(linked_list *list, int number)
{
    if (list == NULL)
    {
        return;
    }

    node *new_node = malloc(sizeof(node));

    if (new_node == NULL)
    {
        return;
    }

    new_node->value = number;
    new_node->next = list->first;

    list->first = new_node;

    // Se a lista estava vazia,
    // o novo nó também será o último.
    if (list->last == NULL)
    {
        list->last = new_node;
    }

    list->size++;

    if (number > list->bigger)
    {
        list->bigger = number;
    }

    if (number < list->smaller)
    {
        list->smaller = number;
    }
}

void insert_end(linked_list *list, int number)
{
    if (list == NULL)
    {
        return;
    }

    node *new_node = malloc(sizeof(node));

    if (new_node == NULL)
    {
        return;
    }

    new_node->value = number;
    new_node->next = NULL;

    // Lista vazia
    if (list->first == NULL)
    {
        list->first = new_node;
        list->last = new_node;
    }
    else
    {
        list->last->next = new_node;
        list->last = new_node;
    }

    list->size++;

    if (number > list->bigger)
    {
        list->bigger = number;
    }

    if (number < list->smaller)
    {
        list->smaller = number;
    }
}

void remove_node(linked_list *list, node *no)
{
    if (list == NULL || no == NULL || list->first == NULL)
    {
        return;
    }

    node *current = list->first;
    node *previous = NULL;

    // Procura o nó e seu anterior
    while (current != NULL && current != no)
    {
        previous = current;
        current = current->next;
    }

    // O nó não pertence à lista
    if (current == NULL)
    {
        return;
    }

    // Removendo o primeiro nó
    if (previous == NULL)
    {
        list->first = current->next;
    }
    else
    {
        previous->next = current->next;
    }

    // Removendo o último nó
    if (current == list->last)
    {
        list->last = previous;
    }

    free(current);

    list->size--;

    // Se a lista ficou vazia
    if (list->size == 0)
    {
        list->first = NULL;
        list->last = NULL;
        list->bigger = INT_MIN;
        list->smaller = INT_MAX;
        return;
    }

    // Recalcula maior e menor
    list->bigger = list->first->value;
    list->smaller = list->first->value;

    current = list->first;

    while (current != NULL)
    {
        if (current->value > list->bigger)
        {
            list->bigger = current->value;
        }

        if (current->value < list->smaller)
        {
            list->smaller = current->value;
        }

        current = current->next;
    }
}

node* search(linked_list *list, int value)
{
    if (list == NULL)
    {
        return NULL;
    }

    node *current = list->first;

    while (current != NULL)
    {
        if (current->value == value)
        {
            return current;
        }

        current = current->next;
    }

    return NULL;
}