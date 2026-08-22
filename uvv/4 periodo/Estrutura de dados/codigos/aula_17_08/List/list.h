#ifndef LIST_H
#define LIST_H

typedef struct list list;

list* create_list(int capacity);

void destroy_list(list *l);

int insert_list(list *l, int element);

int remove_list(list *l, int position);

int search_list(list *l, int element);

#endif



