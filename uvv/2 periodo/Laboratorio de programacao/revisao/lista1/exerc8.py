"""
8. Conversão Monetária: Um usuário precisa converter valores de dólar para real.
Atividade:
● Peça o valor em dólar e a cotação atual.
● Calcule e mostre o valor em reais
"""

dolar = float(input("Qual o valor em dólar: "))
cotacao = float(input("Digite a cotação atual: "))
real = dolar * cotacao
print(f"Valor em real: {real:.2f}")