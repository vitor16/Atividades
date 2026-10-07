'''Uma empresa de alimentação possui pedidos aguardando preparação.

Os pedidos precisam ser preparados na ordem em que foram recebidos para
evitar que um pedido mais recente seja processado antes de outro que está
esperando há mais tempo.
Estrutura que deve ser utilizada
Fila
A fila permite processar os pedidos seguindo a ordem de chegada.
O que desenvolver
Cadastre cinco pedidos e depois processe todos utilizando um while.
Resultado esperado
Pedidos aguardando:

Pedido 1
Pedido 2
Pedido 3
Pedido 4
Pedido 5

Processando Pedido 1
Processando Pedido 2
Processando Pedido 3
Processando Pedido 4
Processando Pedido 5

Todos os pedidos foram processados.'''
from time import sleep
#listas
pedd = []
lixeira = []

#funcoes para as opcoes
def cad():
    for a in range(5):
        ped = input(f" {a+1}º pedido: ")
        pedd.append(ped)

def proc():
    if not pedd:
        print("cadastre algo primeiro")
        return
    else:
        for i in range(len(pedd)):
            sleep(1)
            print(f"Processando {pedd[0]} ")
            sleep(1)
            lixeira = pedd.pop(0)
            sleep(1)
    print("todos os pedidos foram processados")

#loop principal
        
while True:
    print("============menu============")
    print("1-cadastrar pedido")
    print("2-Processar pedidos")
    print("0-Sair")
    opcao = input("Oque deseja fazer hoje?: ")

    if opcao == "1":
        cad()
    elif opcao == "2":
        proc()
    elif opcao == "0":
        print("saindo...........")
        exit()
    else:
        print("valor não válido(inválido)")