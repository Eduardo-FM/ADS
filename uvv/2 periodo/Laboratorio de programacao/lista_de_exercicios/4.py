distancia: float = float(input("Escreva a distância percorrida: "))

frete = int(distancia) * 2.50

print(f"Valor total da entrega: R$ {(frete + 10):.2f}")