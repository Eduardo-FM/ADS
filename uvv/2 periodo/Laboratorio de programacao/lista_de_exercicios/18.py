import random

sorteio = random.sample(range(1, 61), 6)
sorteio.sort()

usuario = []
print("Digite 6 números entre 1 e 60:")

while len(usuario) < 6:
    n = int(input(f"Número {len(usuario) + 1}: "))

    if n < 1 or n > 60:
        print("Número fora do intervalo! Digite entre 1 e 60.")
    elif n in usuario:
        print("Número repetido! Digite outro.")
    else:
        usuario.append(n)

usuario.sort()

acertos = set(sorteio) & set(usuario)
quantidade_acertos = len(acertos)

print("\nNúmeros sorteados:", sorteio)
print("Seus números:", usuario)
print(f"Acertos ({quantidade_acertos}):", sorted(acertos))
