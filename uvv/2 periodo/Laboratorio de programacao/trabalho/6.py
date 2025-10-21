idade = int(input("Idade: "))
if idade < 18:
    print("Menor de idade")
elif idade >= 18 and idade < 60: #No final desta condicão não havia os (:) dois pontos
    print("Maior de idade")
else:
    print("Idoso")