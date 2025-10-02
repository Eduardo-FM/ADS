"""
7) Ler do teclado uma lista com 5 inteiros e imprimir o menor valor.
"""
numbers = []

for i in range(0, 5):
    num = int(input(f"Digite o número {i + 1}: "))
    numbers.append(num)

print(f"O maior número é: {max(numbers)}")
