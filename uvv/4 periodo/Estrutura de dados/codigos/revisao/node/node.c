#include <stdlib.h>
#include <limits.h>

#include "node.h"

struct node
{
    int value;
    struct node* next;
};