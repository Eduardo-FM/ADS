"""
1. Cálculo de Desconto: Uma loja está oferecendo desconto de 10% para
pagamentos à vista.
Atividade:
● Solicite ao usuário o valor da compra.
● Calcule o valor final com desconto e exiba o resultado
"""

preco = float(input('Digite o valor do produto: '))

desconto = preco * 0.1
valorFinal = preco - desconto

print(f"Valor do desconto: {desconto:.2f}")
print(f"Valor do produto: {valorFinal:.2f}")