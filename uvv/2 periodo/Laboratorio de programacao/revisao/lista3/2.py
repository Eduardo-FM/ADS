"""
2) Maior de três números
Peça três números inteiros ao usuário e use condicionais para exibir qual é o maior número.
"""

num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
num3 = int(input("Digite um número: "))

if num1 > num2 and num1 > num3:
    print("Número 1 é o maior: ")
elif num2 > num1 and num2 > num3:
    print("Número 2 é o maior: ")
elif num3 > num1 and num3 > num2:
    print("Número 3 é o maior: ")