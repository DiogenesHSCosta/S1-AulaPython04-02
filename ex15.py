#EXERCICIO 15

'''
- Em uma eleição presidencial existem quatro candidatos. Os votos são informados
por meio de código. Os códigos utilizados são:
1 , 2, 3, 4 - Votos para os respectivos candidatos
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. Para finalizar o
conjunto de votos tem-se o valor zero
'''

joao = 0
raimundo = 0
jorge = 0
joana = 0
nulo = 0
branco = 0
i = 0

while True:
    num = input("Diga seu voto: \n 1 - João \n 2 - Raimundo \n 3 - Jorge \n 4 - Joana \n 5 - Nulo \n 6 - branco \n 0 - sair")

    while num != "0" and num != "1" and num != "2" and num != "3" and num != "4" and num != "5" and num != "6":
        num = input("Diga seu voto: \n 1 - João \n 2 - Raimundo \n 3 - Jorge \n 4 - Joana \n 5 - Nulo \n 6 - branco \n 0 - sair")

    if num == '0':
        break
    elif num == '1':
        joao += 1

    elif num == '2':
        raimundo += 1

    elif num == '3':
        jorge += 1

    elif num == '4':
        joana += 1

    elif num == '5':
        nulo += 1

    elif num == '6':
        branco += 1
    i+=1


print(f"João: {joao}\n Raimundo: {raimundo}\n Jorge: {jorge} \n Joana: {joana} \n Nulos: {nulo/i:.2f} \n Brancos: {branco/i:.2f}")
