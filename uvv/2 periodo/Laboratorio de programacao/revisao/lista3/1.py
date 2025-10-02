"""
1) Verificação de idade para votar
Peça ao usuário para digitar sua idade e exiba:
"Voto obrigatório" se a idade for entre 18 e 70 anos;
"Voto facultativo" se for entre 16 e 17 anos ou acima de 70;
"Não pode votar" se for menor de 16 anos.
"""

idade = int(input("Digite sua idade: "))

if  18 <= idade <= 70 :
    print("Voto obrigatório")
elif idade < 18 or idade > 70:
    print("Voto facultativo")
else:
    print("Não pode voltar")