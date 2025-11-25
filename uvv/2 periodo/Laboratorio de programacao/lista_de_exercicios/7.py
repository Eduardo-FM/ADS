tipo: str = input("Digite o tipo do cliente: ")
consumo: int = int(input("Digite o consumo do cliente em kWh/mês: "))

if tipo.lower() == "residencial".lower():
    if consumo <= 300:
        print("Categoria: Baixo consumo")
    elif consumo > 300 and consumo <= 600:
        print("Categoria: Médio consumo")
    else:
        print("Categoria: Alto consumo")
elif tipo.lower() == "Industrial".lower():
    if consumo <= 1000:
        print("Categoria: Normal")
    else:
        print("Categoria: Elevado")