"""
2. Conversor de Temperatura: Um meteorologista precisa converter temperaturas de
Celsius para Fahrenheit.
Atividade:
● Peça ao usuário a temperatura em graus Celsius.
● Converta para Fahrenheit usando a fórmula: F = (C * 9/5) + 32.
● Mostre o resultado formatado.
"""

celsius: float = float(input("Digite a temperatura em graus Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print(f"Temperatura em fahrenheit: {fahrenheit:.2f}")