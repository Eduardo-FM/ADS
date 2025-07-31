/**
 * IDENTIFICAÇÃO DO ESTUDANTE:
 * Preencha seus dados e leia a declaração de honestidade abaixo. NÃO APAGUE
 * nenhuma linha deste comentário de seu código!
 *
 *    Nome completo: Eduardo Freitas Machado
 *    Matrícula: 202525460
 *    Turma: AN1tN
 *    Email: eduardo.freitas.machado@gmail.com
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

double calcularImc(double peso, double altura);
void classificacao(double imc);
/**
 * Função main
 */
int main(void)
{
    // TODO: escreva aqui o código que solicita o peso da pessoa (em kg).
    // Seu código só deve aceitar valores válidos entre 40,0 e 200,0 kg
    // (inclusive). Se o peso informado não estiver nessa faixa ou se o usuário
    // informar um dado inválido, seu programa deve continuar a solicitar o peso
    // até que ele informe um peso válido.
    double peso = 0;
    while (peso < 40.0 || peso > 200.0)
    {
        peso = get_double("Informe seu peso (kg): ");
    }
    // TODO: escreva aqui o código que solicita a altura da pessoa (em m)
    // Seu código só deve aceitar valores válidos entre 1,40 e 2,50 m
    // (inclusive). Se a altura informada não estiver nessa faixa ou se o
    // usuário informar um dado inválido, seu programa deve continuar a
    // solicitar a altura até que ele informe uma altura válida.
    double altura = 0;
    while (altura < 1.40 || altura > 2.50)
    {
        altura = get_double("Informe sua altura (m): ");
    }
    // TODO: escreva aqui o código que calcula o IMC e imprime a classificação
    // da obesidade no terminal, conforme as especificações do exercício.
    double imc = calcularImc(peso, altura);
    classificacao(imc);
    // Termina o programa:
    return 0;
}

double calcularImc(double peso, double altura)
{
    double calculo = peso / (altura * altura);
    return calculo;
    
}

void classificacao(double imc)
{
    printf("IMC: %.2f; ", imc);
    if (imc < 16.0)
    {
        printf("Classificação: Magreza grau III.\n");
    }
    else if (imc < 17.0)
    {
        printf("Classificação: Magreza grau II.\n");
    }
    else if (imc < 18.5)
    {
        printf("Classificação: Magreza grau I.\n");
    }
    else if (imc < 25.0)
    {
        printf("Classificação: Peso adequado.\n");
    }
    else if (imc < 30.0)
    {
        printf("Classificação: Pré-obeso.\n");
    }
    else if (imc < 35.0)
    {
        printf("Classificação: Obesidade grau I.\n");
    }
    else if (imc < 40)
    {
        printf("Classificação: Obesidade grau II.\n");
    }
    else
    {
        printf("Classificação: Obesidade grau III.\n");
    }
}
