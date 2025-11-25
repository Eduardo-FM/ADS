import random

matriz = [[] for _ in range(5)]
pares = 0
maiorNumero = 0

for i in range(5):
    for j in range(5):
        matriz[i].append(random.randint(1, 100))

for c, coluna in enumerate(matriz):
    for l, linha in enumerate(coluna):
        if matriz[c][l] % 2 == 0:
            pares += matriz[c][l]
        if matriz[c][l] > maiorNumero:
            maiorNumero = matriz[c][l]
            
print(matriz)
print(pares)
print(maiorNumero)