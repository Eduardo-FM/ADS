numeros = []
pares = []
impares = []
while True:
    num = int(input("Digite um número(0 para parar): "))

    if num == 0:
        break

    numeros.append(num)

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print(f"Quantidade de número digitados: {len(numeros)}")
print(f"Média dos valores: {sum(numeros) / len(numeros)}")
print(f"Quantidade de pares: {len(pares)}")
print(f"Quantidade de impáres: {len(impares)}")
