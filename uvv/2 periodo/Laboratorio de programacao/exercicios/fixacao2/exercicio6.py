"""
Peça ao usuário uma lista de números (quantidade à escolha do usuário) e mostre o maior e o menor número digitado.
"""

qtd = int(input("Quantos números você deseja digitar? "))

numeros = []

for i in range(qtd):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

print(f"O maior número digitado foi: {max(numeros)}")
print(f"O menor número digitado foi: {min(numeros)}")