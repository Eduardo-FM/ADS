#include <stdlib.h>

#include "queue.h"

struct queue
{
    int capacity;
    int quantity;
    int first;
    int last;
    int elements; 
};

queue* create(int cap)
{
    queue queue[cap];

    if(queue == NULL) 
    {
        return NULL;
    }

    queue->capacity = cap;
    queue->quantity = 0;
    queue->first = 0;
    queue->last = 0;
}