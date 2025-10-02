"""
2)Solicite ao usuário 10 números inteiros e mostre a soma apenas dos números pares digitados.
"""
soma = 0

for i in range(0, 10):
    numero = int(input("Digite um numero: "))
    if numero % 2 == 0:
        soma+=numero


print(soma)