
"""
1) Converter as seguintes expressões para o interpretador Python:
(a) 10 +20×30
(b) 42 ÷30
(c) (94 +2) ×6−1
"""
# (a)
10 + 20 * 30

# (b)
42 / 30

# (c)
(94 + 2) * 6 - 1

"""
2) No interpretador Python (ou em um arquivo.py) resolva a expressão: 10%3 × 102
+ 1 −10×4/2. Resolva também usando apenas lápis e papel. O resultado a ser
encontrado é 81.0
"""
resultado = 10 % 3 * 10 ** 2 + 1 - 10 * 4 / 2
print(resultado)  
"""
3) Faça um programa que resolva a soma de três variáveis e imprima o resultado na
tela.
"""
a = 5
b = 10
c = 15
soma = a + b + c
print(f"A soma é:{soma}")


"""
4) Considerando um salário de R$ 750.00, determine numericamente um aumento
de 15%.
"""
salario = 750.00
aumento = salario * 0.15
print(f"Aumento: {aumento}")

"""
5) Escreva um programa que, a partir da entradas dos valores de dias, horas,
minutos
"""

dias = int(input("Digite os dias: "))
horas = int(input("Digite as horas: "))
minutos = int(input("Digite os minutos: "))
segundos = int(input("Digite os segundos: "))

total_segundos = dias * 86400 + horas * 3600 + minutos * 60 + segundos
print("Total em segundos:", total_segundos)

"""
6) Escreva um programa que pergunte três números para o usuário e que devolva
o maior numero entre eles
"""

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

maior = max(n1, n2, n3)
print("O maior número é:", maior)

"""
7) Escreva um programa em Python que verifique se um número é primo.
"""

num = int(input("Digite um número: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "não é primo")
            break
    else:
        print(num, "é primo")
else:
    print(num, "não é primo")