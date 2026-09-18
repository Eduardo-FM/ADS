#ifndef LINKED_LIST_H
#define LINKED_LIST_H

typedef struct linked_list linked_list;
typedef struct node node;

linked_list* create();

void destroy(linked_list *linked_list);

void insert_begin(linked_list *list, int number);

void insert_end(linked_list *list,int number);

void remove_node(linked_list *list, node *node);

node* search(linked_list *list, int value);


#endif