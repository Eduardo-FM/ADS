"""
8) Ler do teclado uma lista com 5 inteiros e imprimir True se a lista estiver ordenada de forma crescente ou False caso contrário.
"""

numbers = []

for i in range(0, 5):
    num = int(input(f"Digite o número {i + 1}: "))
    numbers.append(num)

if numbers == sorted(numbers):
    print(True)
else:
    print(False)