num = input("insira o numero: ")
while not num.isnumeric():
    num = print("insira um numero")

num = int(num)
i = 2

while i < num:
    print(f'{num}%{i} = {num%i}')
    if num % i == 0:
        print(f"o numero {num} não é primo")
        break
    i+=1

if i == num:
    print(f"o numero {num} é primo")

