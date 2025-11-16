import datetime

def registarDados() -> None:
    file = open("somas.txt", "at")

    data = datetime.datetime.now()

    if(file):
        with file as f:
            f.write(f"{data.strftime("%Y")}-{data.strftime("%m")}-{data.strftime("%d")} {data.strftime("%X")} {somar(num1, num2)}\n")
    else:
        print("Arquivo não existe")

    file.close()

def somar(num1: int, num2: int) -> str:
    return str(f"{num1} + {num2} = {num1 + num2}")

while True:
    num1: float = float(input("Digite o primeiro número: "))
    num2: float = float(input("Digite o segundo número: "))
    sum = somar(num1, num2)

    registarDados()


