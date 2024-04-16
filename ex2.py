'exercicio 2'

'nome'
nome = input("Informe seu nome: ")
while len(nome) <= 3:
    nome = input("Informe seu nome(com mais de 3 letras")


'idade'

idade = input("Informe uma idade entre 0 e 150: ")
while True:
    if idade.isnumeric():
        idade = int(idade)
        if idade > 0 or idade < 150:
            break

    idade = input("Informe uma idade entre 0 e 150: ")



#salario
salario = input("Informe seu salario: ")

#verifica se todos os caracteres são numericos. Simbolos como - e + fazem o isnumeric dar false
while not salario.isnumeric():
    salario = input("Informe sua salario(numeros): ")

salario = int(salario)


'sexo'
sexo = input("informe seu sexo (f ou m): ")

while sexo!= "f" and sexo!="m":
    sexo = input("informe seu sexo (f ou m): ")



'Estado Civil'

estadoCivil = input("Informe o seu estado civil ( 's', 'c', 'v' ou 'd): ")
while estadoCivil != 's' and estadoCivil != 'c' and estadoCivil != 'v' and estadoCivil != 'd':
    estadoCivil = input("Informe o seu estado civil corretamente ( 's', 'c', 'v' ou 'd): ")


print(f"{nome}, {idade}, {salario}, {sexo}, {estadoCivil}")
