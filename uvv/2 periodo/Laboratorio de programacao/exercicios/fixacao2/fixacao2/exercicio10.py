"""
Peça um número inteiro e calcule seu fatorial (ex: 5! = 5 × 4 × 3 × 2 × 1).
"""

numero = int(input("Digite um número inteiro: "))

fatorial = 1

for i in range(1, numero + 1):
    fatorial *= i

print(f"O fatorial de {numero} é {fatorial}")