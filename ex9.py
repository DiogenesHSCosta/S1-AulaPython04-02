i = 0
pares = 0

while i<10:
    num = input(f"Diga o {i+1}° numero: ")

    while not num.isnumeric():
        input("insira um numero")
        num = input(f"Diga o {i+1}° numero: ")

    num = int(num)

    if num % 2 == 0:
        pares +=1

    i+=1
print(f"Pares = {pares} impares = {10-pares}")
