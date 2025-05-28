#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // FOR
    string nome = get_string("Qual o seu nome?\n");

    for (int i = 0; i < 10; i++)
    {
        printf("Olá, %s!\n", nome);
    }

    // WHILE
    int numero = get_int("Digite um número:\n");
    while (numero < 10)
    {
        printf("Número: %d\n", numero);
        numero++;
    }

    // DO WHILE
    int tabuada = get_int("Digite um número para a tabuada:\n");
    int i = 1;
    do
    {
        printf("%d x %d = %d\n", tabuada, i, tabuada * i);
        i++;
    } while (i <= 10);

    

    return 0;
}
 
