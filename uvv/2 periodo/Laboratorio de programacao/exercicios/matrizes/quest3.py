"""
3 - Uma empresa armazena suas vendas diárias em uma lista: vendas = [250, 300, 150, 400, 500, 600, 350] Desenvolva um programa que:
Mostre o total e a média de vendas semanais; Exiba o dia com maior e menor venda; Indique se a meta semanal de R$ 2.500 foi atingida.
"""
vendas = [250, 300, 150, 400, 500, 600, 350]

print(f"Total de vendas semanais: {sum(vendas)}")
print(f"Média de vendas semanais: {(sum(vendas) / len(vendas)):.2f}")
print(f"Dia com maior venda: {max(vendas)}")
print(f"Dia com menor venda: {min(vendas)}")

if sum(vendas) >= 2500:
    print("Meta semana batida!")
else:
    print("Meta semanal não foi batida")