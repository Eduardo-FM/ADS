#include <stdio.h>
#include <cs50.h>

int main(void)
{
    //OR e AND
    char letra = get_char("Você concorda com o nosso pacto? (S/N)");

    if (letra == 'S' || letra == 's')
    {
        printf("Sua alma é minha!!!\n");
    }
    else if (letra == 'N' || letra == 'n')
    {
        printf("SNIF, SNIF, você é do time de Jesus\n");
    } else
    {
        printf("Não sei o que você quer!\n");
    }
    
}