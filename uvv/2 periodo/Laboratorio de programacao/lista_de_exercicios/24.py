import csv

arquivo = "vendas.csv"

totais_por_produto = {}
total_geral = 0

with open(arquivo, "r", encoding="utf-8") as f:
    leitor = csv.reader(f)
    next(leitor)

    for produto, quantidade, preco in leitor:
        quantidade = int(quantidade)
        preco = float(preco)

        total_item = quantidade * preco
        total_geral += total_item

        if produto in totais_por_produto:
            totais_por_produto[produto] += total_item
        else:
            totais_por_produto[produto] = total_item

print("\n=== RELATÓRIO DE VENDAS ===")
for produto, total in totais_por_produto.items():
    print(f"{produto}: R$ {total:.2f}")

print("\nTotal geral: R$ {:.2f}".format(total_geral))
