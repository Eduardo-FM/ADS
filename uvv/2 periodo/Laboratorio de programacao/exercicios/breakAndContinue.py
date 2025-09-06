while True:
    string_digitada = input("Digite uma palavra: ")
    if string_digitada.lower() == "sair":
        print("Fim!")
        break
    if len(string_digitada) < 2:
        print("String muito pequena")
        continue
    print("Tente digitar \"sair\"")