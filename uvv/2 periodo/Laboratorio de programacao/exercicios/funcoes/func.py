notas = []
def media(*nums):
    total = 0
    for num in nums:
        total += num
    total /= len(nums)
    print(f"Média do aluno: {total}")

while True:
    resposta = input("Quer adicionar nota (Digite: sim ou não): ")

    if resposta.lower() == 'sim':
        nota = float(input("Digite o valor da nota: "))
        notas.append(nota)
    elif resposta.lower() == 'não' or resposta.lower() == 'nao':
        if len(notas) > 0:
            media(*notas)
        break
    else:
        print("Resposta inválida")
