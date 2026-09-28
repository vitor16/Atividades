'''Crie uma função chamada saudar() que receba o nome de uma pessoa.
A função deverá apresentar uma mensagem de boas-vindas utilizando o nome
recebido.
No programa principal, solicite o nome ao usuário e utilize a função criada.'''
#definit função saudar
def saudar(nome):
    print(f"Olá, {nome}! Seja bem-vindo!")
#pedir um valor para nome
nome = input("Digite seu nome: ")
#chamo a função saudar agora com um valor dentro
saudar(nome)
#sair porque estava executando duas vezes por algum motivo
exit
