'exercicio 1'

while True:
    valor = input("Insira um numero entre 0 e 10: ")
    if valor.isnumeric():
        valor = int(valor)
        if valor >= 0 and valor <=10:
            print("PARABENS!!! vc escreveu um numero")
            break
        else:
            print("deve ser entre 0 e 10")
    else:
        print("insira um numero")

