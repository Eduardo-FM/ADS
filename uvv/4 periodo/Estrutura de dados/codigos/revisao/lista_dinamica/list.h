#ifndef LIST_H
#define LIST_H

typedef struct list list;

list* create(int capacity);

void destroy(list *l);

int insert(list *l, int element);

int remove(list *l, int position);

int search(list *l, int element);

void show(list *l);

#endif