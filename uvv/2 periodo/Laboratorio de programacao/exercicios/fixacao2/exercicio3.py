"""
Peça uma palavra ao usuário e informe se ela é um palíndromo (lida de trás para frente é igual).
"""

palavra: str = input("Digite uma palavra: ")

if palavra == palavra[::-1]:
    print(f"A Palavra: {palavra} é um palíndromo")