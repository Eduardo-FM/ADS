#include <stdio.h>

#include "list.h"

int main() {

    list *l = create_list(5);
    insert_list(l,1);
    //insert_list(l, 2);
    //insert_list(l, 3);
    //insert_list(l, 4);
    //insert_list(l, 5);
    show_list(l);
    destroy_list(l);

    return 0;
}