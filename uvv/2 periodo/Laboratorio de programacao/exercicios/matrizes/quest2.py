"""
2 -
Uma loja tem duas listas:
produtos = ["Mouse", "Teclado", "Monitor", "Headset", "Webcam"]
quantidades = [15, 8, 10, 4, 6]
Faça um script que: Solicite o nome de um produto e verifique se há no estoque;
Caso exista, permita retirar uma quantidade e atualize a lista;
 Exiba os produtos com quantidade abaixo de 5 (alerta de reposição).
"""
produtos = ["Mouse", "Teclado", "Monitor", "Headset", "Webcam"]
quantidades = [15, 8, 10, 4, 6]


listProdutos: dict = dict(zip(produtos, quantidades))
print(listProdutos)

nomeProduto = input("Qual produto quer saber se há no estoque: ")

if nomeProduto in listProdutos.keys():
    print(nomeProduto)