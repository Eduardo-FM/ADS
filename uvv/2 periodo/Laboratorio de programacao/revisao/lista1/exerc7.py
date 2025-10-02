"""
7. Analisando Entrada: Um sistema precisa validar o que o usuário digita.
Atividade:
● Peça ao usuário que digite algo.
● Mostre na tela:
○ Se é numérico
○ Se é alfabético
○ Se está em maiúsculo ou minúsculo
Dica: Explorar métodos de string: .isnumeric(), .isalpha(), .islower(), .isupper().
"""

entrada = input("Digite algo: ")

print(f"É numérico: {entrada.isnumeric()}")
print(f"É alfabético: {entrada.isalpha()}")
print(f"É maiúsculo: {entrada.islower()}")
print(f"É minúsculo: {entrada.isupper()}")