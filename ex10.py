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

