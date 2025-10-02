"""
Peça uma palavra ao usuário e informe se ela é um palíndromo (lida de trás para frente é igual).
"""

palavra = input("Digite uma palavra: ")

if palavra == palavra[::-1]:
    print("É palíndromo")
else:
    print("não é")