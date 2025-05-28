#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // int linhas = get_int("Quantas linhas? \n");
    // int colunas = get_int("Quantas colunas? \n");

    // for (int l = 1; l <= linhas; l++)
    // {
        
    //     for (int c = 1; c <= colunas; c++)
    //     {
    //         printf("#");
    //     }
    //     printf("\n");
    // }

    int linhas = get_int("Quantas linhas? \n");
    for (int l = 1; l <= linhas; l++)
    {
        for (int c = 0; c <= l; c++)
        {
            printf("#");
        }
        printf("\n");
        
    }
    
}