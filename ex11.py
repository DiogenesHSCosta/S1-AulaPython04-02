num = input("insira o numero: ")
while not num.isnumeric():
    num = print("insira um numero")

num = int(num)
i = 2
#só precisamos testar até a raiz de um numero
while i < num**0.5:
    print(f'{num}%{i} = {num%i}')
    if num % i == 0:
        print(f"o numero {num} não é primo")
        break
    i+=1

if i == num**0.5:
    print(f"o numero {num} é primo")

