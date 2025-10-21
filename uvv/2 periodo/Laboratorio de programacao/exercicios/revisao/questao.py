notas = []
boas = []
ruins = []

for i in range(0, 5):
    num = float(input("Digite sua nota: "))
    notas.append(num)

for n in notas:
    if n >= 7:
        boas.append(n)
    elif n < 7:
        ruins.append(n)

print(f"Notas boas: {boas}")
print(f"Notas ruins: {ruins}")