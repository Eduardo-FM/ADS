/* IDENTIFICAÇÃO DO ESTUDANTE:
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

// Comece aqui seu programa.
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int num = get_int("Você quer a tabuada de qual número? ");
    for (int i = 0; i <= 10; i++)
    {
        printf("%d x %d = %d\n", num, i, num * i);
    }
}