"""
Solicite ao usuário 10 números inteiros e mostre a soma apenas dos números pares digitados.
"""

pares: int = 0
for num in range(0, 10):
    numero: str = int(input("Digite um número: "))
    if numero % 2 == 0:
        pares += numero


print(f"Soma dos pares: {pares}")