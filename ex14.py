#Exercicio 14

'''
Faça um programa que leia uma quantidade indeterminada de números positivos e
conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100].
A entrada de dados deverá terminar quando for lido um número negativo.
'''

Int1 = 0
Int2 = 0
Int3 = 0
Int4 = 0
while True:

    num = int(input("Diga um numero"))
    if num < 0 :
        break

    if num > 0 and num < 25:
        Int1 += 1

    elif num <= 50:
        Int2 += 1

    elif num <= 75:
        Int3 += 1

    elif num <= 100:
        Int4 += 1

print(f"{Int1}, {Int2}, {Int3}, {Int4}")
