#include <stdio.h>

#include "linked_list.h"

int main() {

    linked_list *l = create();

    destroy(l);   

    return 0;
}