'Exercicio 4'


i = 0
lim = 10
soma = 0

while i < lim:
    num = int(input(f"insira o {i+1}° numero: "))
    soma += num
    i += 1

print(f"a soma dos numeros é {soma} e a média é {soma/lim}")
