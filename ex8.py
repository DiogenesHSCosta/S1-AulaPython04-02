
num = input("Insira um termo da sequencia de fibonacci: ")

while not num.isnumeric():
    num = input("Insira um termo da sequencia de fibonacci: ")

num = int(num)

i = 0
termo1 = 1
termo2 = 1
while i < num:
    termo3 = termo1+termo2

    termo1 = termo1
    termo2 = termo3


