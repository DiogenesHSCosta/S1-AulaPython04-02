#Exercicio13

'''
Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se
que:
1. Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
2. Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
3. A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao
dobro do percentual do ano anterior. Faça um programa que determine o
salário atual desse funcionário. Após concluir isto, altere o programa
permitindo que o usuário digite o salário inicial do funcionário.
'''

anoFinal = 2000
salario = 1000
taxa = 0.015
anoInicio = 1995

while anoInicio < anoFinal:
    salario *= (1+taxa)
    taxa *= 2
    anoInicio += 1
print(salario)
