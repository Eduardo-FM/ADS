"""
Peça um número ao usuário e verifique se ele é primo.
"""

num = int(input())

if num <= 1:
    print("Não é primo")
else:
    primo = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            primo = False
            break

    if primo:
        print("É primo")
    else:
        print("Não é primo")