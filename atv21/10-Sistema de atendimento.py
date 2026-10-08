'''Uma empresa precisa desenvolver um pequeno sistema para controlar o
atendimento de clientes.
O sistema deverá permitir que clientes sejam adicionados à fila e atendidos na
ordem em que chegaram.
Enquanto houver clientes aguardando, o sistema deverá continuar realizando os
atendimentos.
Estrutura que deve ser utilizada
Fila
A fila deve ser utilizada porque o atendimento precisa respeitar a ordem de
chegada dos clientes.

O que desenvolver
O sistema deverá:
1. Criar uma fila vazia.
2. Adicionar cinco clientes.
3. Exibir os clientes aguardando.
4. Atender o primeiro cliente.
5. Remover o cliente atendido.
6. Exibir quantos clientes ainda aguardam.
7. Continuar o atendimento utilizando while.
8. Encerrar quando a fila estiver vazia.
Resultado esperado
Clientes aguardando:

Ana
Carlos
Mariana
Pedro
João

Atendendo: Ana
Clientes restantes: 4

Atendendo: Carlos
Clientes restantes: 3

Atendendo: Mariana
Clientes restantes: 2

Atendendo: Pedro
Clientes restantes: 1

Atendendo: João
Clientes restantes: 0

Fila vazia.
Todos os clientes foram atendidos.'''
#importa função sleep
from time import sleep
#cria lista vazia
fila = []
#funçoes
def add():
    #pede 4 nomes
    for i in range(4):
        nome= input("Digite o nome do cliente:")
        fila.append(nome)

def show():
    #mostra a fila
    for i in fila:
        print(i)

def atend():
    #remove items da fila
    for i in range(len(fila)):
            if not fila:
                print("Ninguem cadastrado!")
            else:
                sleep(1)
                print(f"Atendendo {fila[0]} ")
                sleep(1)
                lixeira = fila.pop(0)
                print("Clientes na fila:", fila)
                sleep(1)
    print("todos os clientes foram atendidos")

#loop principal
while True:
    print("======MENU======")
    print("1-Adicionar clientes(nomes)")
    print("2-Exibir fila")
    print("3-Atender em ordem")
    print("4-sair")
    opcao = input("Oque  deseja hoje kk: ")
    if opcao == "1":
         add()
    elif opcao == "2":
             show()
    elif opcao == "3":
             atend()
    elif opcao == "4":
             print("Saindo......")
             exit()
    


