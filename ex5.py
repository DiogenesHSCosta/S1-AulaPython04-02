#Exercicio 5
'''
Faça um programa que receba dois números inteiros e gere os números inteiros
que estão no intervalo compreendido por eles
'''
num1 = int(input("Insira o primeiro numero: "))
num2 = int(input("Insira o segundo numero: "))

if num2 < num1:
    aux = num2
    num2 = num1
    num1 = aux

i = num1

while i < num2 - 1:
    i += 1
    print(i)

