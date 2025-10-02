"""
Operações com Strings: Um formulário pede nome completo do usuário.
Atividade:
● Solicite o nome completo do usuário.
● Mostre:
1. O nome em letras maiúsculas.
2. O nome em letras minúsculas.
3. Quantos caracteres possui sem contar espaços.
"""

nome = input("Digite seu nome completo: ")
print(f"O nome em letras maiúsculas: {nome.upper()}")
print(f"O nome em letras minúsculas: {nome.lower()}")
print(f"Quantos caracteres possui sem contar espaços: {len(nome.replace(" ", ""))}")

