#include <cs50.h>
#include <stdio.h>

int main (void)
{
    string nome = get_string("Qaul seu nome? ");
    int idade = get_int("Sua idade é: ");
    double numero = get_double("Qual seu número favorito? ");


    printf ("Olá, %s, você tem %d anos! \n", nome, idade);
    printf("Seu número favorito é %.2f.\n", numero);
}