#Exercicio 10

'''
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo
usuário. Ex.: 5!=5.4.3.2.1=120
'''

num = input("insira o numero: ")

while not num.isnumeric():
    num = print("insira um numero")

num = int(num)
fatorial = num
fatorialPrint = f'{num}! = '

while num > 1:
    fatorialPrint += f"{num}*"
    num-=1
    fatorial *=num

fatorialPrint += "1"
print(f"{fatorialPrint} = {fatorial}")

