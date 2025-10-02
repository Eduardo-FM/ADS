"""
Peça ao usuário um número N e imprima todos os números da sequência de Fibonacci menores ou iguais a N.
"""

n = int(input("Digite um número: "))

a, b = 0,1

while a <= n:
    print(a, end=", ")
    a, b = b, a + b