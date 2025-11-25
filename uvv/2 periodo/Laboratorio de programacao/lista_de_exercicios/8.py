pedidos = []
valorTotal = 0

while True:
    pedido: str= input("Qual pedido deseja registar(digite 'fim' para sair): ")

    if pedido.lower() == "fim".lower():
        break

    pedidos.append(pedido)
    valor = float(input("Digite o valor do pedido: "))
    valorTotal += valor

print(f"Quantidade de pratos pedidos: {len(pedidos)}")
print(f"Valor total da conta: R$ {valorTotal:.2f}")