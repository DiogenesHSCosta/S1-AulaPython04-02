#Exercicio 4
''' Faça um programa que leia 5 números e informe a soma e a média dos números'''

i = 0
lim = 10
soma = 0

while i < lim:
    num = input(f"insira o {i+1}° numero: ")
    while not num.isnumeric():
        print("deve ser um numero")
        num = input(f"insira o {i+1}° numero: ")

    num = int(num)
    soma += num
    i += 1

print(f"a soma dos numeros é {soma} e a média é {soma/lim}")
