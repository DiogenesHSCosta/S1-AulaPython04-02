'''exercicio 1

Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem
caso o valor seja inválido e continue pedindo até que o usuário informe um valor
válido'''

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

