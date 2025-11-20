valorDaCompra = float(input("Digite o valor da compra: "))
opcaoDePagamento = input("Digite a opção de pagamento (A vista / 3x / 6x): ")

match opcaoDePagamento:
    case 'A vista':
        desconto = valorDaCompra * 0.10
        valorFinal = valorDaCompra - desconto
        print(f"Valor final: R${valorFinal:.2f}")
        print(f"Desconto aplicado: R${desconto:.2f}")

    case '3x':
        parcela = valorDaCompra / 3
        print(f"Valor total: R${valorDaCompra:.2f}")
        print(f"Valor de cada parcela: R${parcela:.2f}")

    case '6x':
        acrescimo = valorDaCompra * 0.05
        valorFinal = valorDaCompra + acrescimo
        parcela = valorFinal / 6
        print(f"Valor total com acréscimo: R${valorFinal:.2f}")
        print(f"Valor de cada parcela: R${parcela:.2f}")

    case _:
        print("Opção inválida!")
