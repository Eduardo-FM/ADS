total = 0

arquivo = open("produtos.txt", "r")
for linha in arquivo:
    linha = linha.strip()

    if linha == "":
        continue

    nome, preco = linha.split(",")
    preco = float(preco)

    total += preco

print(f"Total do estoque: R$ {total:.2f}")
