#Exercicio 8
'''
A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,... Faça um
programa capaz de gerar a série até o n−ésimo termo.
'''

num = input("Insira um termo da sequencia de fibonacci: ")

while not num.isnumeric():
    num = input("Insira um termo da sequencia de fibonacci: ")

num = int(num)

i = 1
termo1 = 1
termo2 = 1

print(f"o {i}° termo é: {termo1}")
while i < num:
    termo3 = termo1+termo2
    termo1 = termo2
    termo2 = termo3
    i +=1
    print(f"o {i}° termo é: {termo1}")

