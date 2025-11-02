"""
2 -
Uma loja tem duas listas:
produtos = ["Mouse", "Teclado", "Monitor", "Headset", "Webcam"]
quantidades = [15, 8, 10, 4, 6]
Faça um script que: Solicite o nome de um produto e verifique se há no estoque;
Caso exista, permita retirar uma quantidade e atualize a lista;
 Exiba os produtos com quantidade abaixo de 5 (alerta de reposição).
"""
#produtos = {"Mouse": 15, "Teclado": 8, "Monitor" : 10 , "Headset" : 4, "Webcam" : 6}
produtosLista = ["Mouse", "Teclado", "Monitor", "Headset", "Webcam"]
quantidadesLista = [15, 8, 10, 4, 6]


produtos = dict(zip(produtosLista, quantidadesLista))
nomeProduto = input("Qual produto quer saber se há no estoque: ")

def retirarProduto(retirar: int, total: int) -> int:
    return total - retirar

if produtos[nomeProduto.capitalize()] > 0:
    print("Há produto em estoque")
    retirarProdutoBoolean = input("Deseja retirar uma quantidade do estoque? ")
    if retirarProdutoBoolean.lower() == "sim".lower():
        qtdeRetirar = int(input("Quantidade a ser retira: "))
        produtos[nomeProduto.capitalize()] = retirarProduto(qtdeRetirar, produtos[nomeProduto.capitalize()])
        print(produtos)
else:
    print("Não há produto em estoque")

print("\n--- ALERTA DE REPOSIÇÃO ---")
for nome, quantidade in produtos.items():
    if quantidade < 5:
        print(f"{nome} - {quantidade} unidades restantes")
