num = []
pares = []
for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    num.append(numero)

for numero in num:
    if numero % 2== 0:
        pares.append(numero)

print(f"Lista original: {num}")
print(f"Lista filtrada: {pares}")