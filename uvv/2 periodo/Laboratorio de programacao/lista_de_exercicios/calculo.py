def calcular_media(notas):
    return sum(notas) / len(notas)

def situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"
