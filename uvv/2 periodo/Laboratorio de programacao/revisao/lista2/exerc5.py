dias = int(input("Digite o valor de dias: "))
horas = int(input("Digite o valor de horas: "))
minutos = int(input("Digite o valor de minutos: "))
segundos = int(input("Digite o valor de segundos: "))

tempoTotal = (dias * 24 * 60 * 60) + (horas * 60 * 60) + (minutos * 60) + segundos
print(f"Tempo total em segundos: {tempoTotal:.2f}")