/**
 * IDENTIFICAÇÃO DO ESTUDANTE:
 * Preencha seus dados e leia a declaração de honestidade abaixo. NÃO APAGUE
 * nenhuma linha deste comentário de seu código!
 *
 *    Nome completo:
 *    Matrícula:
 *    Turma:
 *    Email:
 *
 * DECLARAÇÃO DE HONESTIDADE ACADÊMICA:
 * Eu afirmo que o código abaixo foi de minha autoria. Também afirmo que não
 * pratiquei nenhuma forma de "cola" ou "plágio" na elaboração do programa,
 * e que não violei nenhuma das normas de integridade acadêmica da disciplina.
 * Estou ciente de que todo código enviado será verificado automaticamente
 * contra plágio e que caso eu tenha praticado qualquer atividade proibida
 * conforme as normas da disciplina, estou sujeito à penalidades conforme
 * definidas pelo professor da disciplina e/ou instituição.
 */


/**
 * Inclusão de bibliotecas:
 */
#include <cs50.h>
#include <stdio.h>

/**
 * Função main
 */
int main(void)
{
    // Solicita o valor da comida:
    float comida;
    do
    {
        comida = get_float("Valor da comida: ");
    }
    while (comida < 10.00 || comida > 999.99);
    
    // Solicita o percentual de impostos:
    float impostos;
    do
    {
        impostos = get_float("Porcentagem de impostos: ");
    }
    while (impostos < 0.00 || impostos > 100.00);
    
    // Solicita o percentual de gorjeta:
    int gorjeta;
    do
    {
        gorjeta = get_int("Porcentagem da gorjeta: ");
    }
    while (gorjeta < 0 || gorjeta > 100);
    
    // TODO: coloque aqui seu código para o cálculo do valor da conta.
    // Não se esqueça de imprimir o valor final conforme especificado na
    // descrição do exercício.
    
    float valor_imposto = comida * (impostos/100.0);

    float subtotal = comida + valor_imposto;
    
    float valor_gorjeta = subtotal * ((float)gorjeta/100.0);

    float total = subtotal + valor_gorjeta;

    float metade = total / 2.0;

    printf("Cada um pagará R$ %.2f!\n", metade);
    
    // Termina o programa:
    return 0;
}

