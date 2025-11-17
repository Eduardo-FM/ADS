produto = float(input("Digite o valor do produto: "))
desconto = float(input("Digite a porcentagem de desconto: "))

desconto = produto * (desconto/100)

print(f"Valor final: {produto - desconto}")
print(f"Valor do desconto: {desconto:.2f}")