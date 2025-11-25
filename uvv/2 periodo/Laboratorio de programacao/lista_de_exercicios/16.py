matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

diagonalPrincipal = 0
diagonalSecundaria = 0

for i, linha in enumerate(matriz):
    diagonalPrincipal += matriz[i][i]
    diagonalSecundaria += matriz[i][((len(matriz) -1) - i)]

print(diagonalPrincipal)
print(diagonalSecundaria)
