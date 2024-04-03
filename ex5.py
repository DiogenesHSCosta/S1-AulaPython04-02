
num1 = int(input("Insira o primeiro numero: "))
num2 = int(input("Insira o segundo numero: "))

if num2 < num1:
    aux = num2
    num2 = num1
    num1 = aux

lim = num2 - num1
i = num1

while i < num2-1:
    i += 1
    print(i)

