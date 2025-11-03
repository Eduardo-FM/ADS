"""
7 - Uma padaria recebe uma lista de pedidos e seus respectivos status: pedidos = [["Pão de queijo", "Entregue"], ["Café", "Pendente"], ["Bolo", "Entregue"], ["Suco", "Pendente"]]Crie um programa que: Conte quantos pedidos estão “Pendentes” e quantos “Entregues”; Liste apenas os pedidos pendentes; Atualize o status de um pedido para “Entregue”.
"""

pedidos = [
    ["Pão de queijo", "Entregue"],
    ["Café", "Pendente"],
    ["Bolo", "Entregue"],
    ["Suco", "Pendente"]
]

pendentes = sum(1 for p in pedidos if p[1] == "Pendente")
entregues = sum(1 for p in pedidos if p[1] == "Entregue")

print(f"Pedidos pendentes: {pendentes}")
print(f"Pedidos entregues: {entregues}")

print("\nPedidos pendentes:")
for nome, status in pedidos:
    if status == "Pendente":
        print("-", nome)

pedido_nome = input("\nDigite o nome do pedido que foi entregue: ")

atualizado = False
for pedido in pedidos:
    if pedido[0].lower() == pedido_nome.lower():
        pedido[1] = "Entregue"
        atualizado = True
        break

if atualizado:
    print(f"O pedido '{pedido_nome}' foi marcado como 'Entregue'.")
else:
    print("Pedido não encontrado.")

print("\nLista atualizada de pedidos:")
for nome, status in pedidos:
    print(f"- {nome}: {status}")
