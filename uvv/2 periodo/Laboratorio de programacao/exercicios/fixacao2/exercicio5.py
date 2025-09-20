"""
Peça um número ao usuário e verifique se ele é primo.
"""

primo: bool = True

numero = int(input("Digite um número: "))

if numero <= 1:
    primo = False
else:
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            primo = False
            break

if primo:
    print(f"{numero} é primo.")
else:
    print(f"{numero} não é primo.")