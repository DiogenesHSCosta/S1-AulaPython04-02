#exercicio7

'''
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número
inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a
tabuada. A saída deve ser conforme o exemplo abaixo:
'''

j = 1
while j < 10:
    i = 1
    while i <= 10:
        print(f"{j} x {i} = {j*i}")
        i+=1

    j += 1
    print(' ')
