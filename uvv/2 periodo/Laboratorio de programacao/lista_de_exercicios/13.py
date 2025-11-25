frase = input("Digite uma frase: ")

palavras = frase.lower().split()

unicas = set(palavras)

contador = {}

for palavra in palavras:
    if palavra in contador:
        contador[palavra] += 1
    else:
        contador[palavra] = 1

print("\nPalavras únicas:")
for p in unicas:
    print(p)

print("\nContagem de ocorrências:")
for p, qtd in contador.items():
    print(f"{p}: {qtd}")
