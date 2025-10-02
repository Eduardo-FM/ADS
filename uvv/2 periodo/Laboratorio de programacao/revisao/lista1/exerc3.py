"""
3. Troca de Valores: Em um algoritmo de controle, dois valores foram digitados
incorretamente e precisam ser trocados.
Atividade:
● Leia dois números inteiros do usuário.
● Troque os valores entre as variáveis sem usar uma variável auxiliar.
● Exiba os valores após a troca.

"""

num1: int = int(input("Digite o primeiro valor: "))
num2: int = int(input("Digiete o segundo valor: "))
print(f"Valor 1 antes da troca: {num1}")
print(f"Valor 2 antes da troca: {num2}")
num1, num2 = num2, num1
print(f"Valor 1 depois da troca: {num1}")
print(f"Valor 2 depois da troca: {num2}")