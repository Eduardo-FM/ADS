#include <stdio.h>
#include <cs50.h>

int potencia(int base, int expoente); //PROTÓTIPO DAS FUNCOES

int main(void)
{
    printf("Valor: %d \n", potencia(3, 2));
    return 0;
}

int potencia(int base, int expoente)
{
    int valor = 1;

    for (int i = 1; i <= expoente; i++)
    {
        valor *= base;
    }
    
    return valor;
}
