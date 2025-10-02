"""
. Calculadora de IMC: Uma clínica médica quer calcular o IMC dos pacientes.
Atividade:
● Solicite peso (kg) e altura (m).
● Calcule o IMC: IMC = peso / (altura ** 2).
● Mostre o resultado com duas casas decimais.
"""

peso: float = float(input("Digite seu peso: "))
altura: float = float(input("Digite sua altura em metros: "))
imc: float = peso / (altura**2)
print(f"Imc: {imc:.2f}")