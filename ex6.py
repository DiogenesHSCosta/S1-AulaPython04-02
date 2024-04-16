'Exercicio 6'
'''
Faça um programa que leia um nome de usuário e a sua senha e não aceite a 
senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a 
pedir as informações
'''
usuario = input("insira o nome de usuario: ")


senha = input("insira a senha: ")

while usuario == senha:
    senha = input("escreva uma senha diferente do usuario: ")

