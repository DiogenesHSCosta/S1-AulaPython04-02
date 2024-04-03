'exercicio 2'

populacaoA = 80000

populacaoB = 200000

anos = 0

while populacaoA <= populacaoB:
    anos+=1

    populacaoA += (populacaoA/100)*3
    print(f"populacaoA = {populacaoA}")

    populacaoB += (populacaoB/100)*1.5
    print(f"populacaoB = {populacaoB}")


print(f"foram necessario {anos} para a população A igualar a população B")
