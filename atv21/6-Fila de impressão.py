'''Uma empresa possui vários documentos aguardando impressão.
Os documentos devem ser impressos na ordem em que foram enviados para a
impressora. Um documento que chegou depois não pode ser impresso antes dos
documentos que já estavam aguardando.
Estrutura que deve ser utilizada
Fila
A fila representa corretamente o funcionamento de uma impressora, pois o
primeiro documento enviado deve ser processado primeiro.
O que desenvolver
Adicione os seguintes documentos:
Relatório
Contrato
Currículo
Nota Fiscal
Planilha
Depois, utilize um while para processar os documentos até que a fila fique vazia.
Resultado esperado
Imprimindo: Relatório
Imprimindo: Contrato
Imprimindo: Currículo
Imprimindo: Nota Fiscal
Imprimindo: Planilha

Todos os documentos foram impressos.'''

from time import sleep
pac= []
#loop para pedir o nome 5 vezes

for i in range(5):
    nome = input(f"Digite o Nome do {i+1}º item a ser impresso: ")
    pac.append(nome)
print("======================")
print("Items na fila de impressão: ")
#loop para mostrar todos os clientes
for a in pac:
    print(a)
#loop para mostrar regressão de fila
for j in range(5):
    if not pac:
        print("Lista vazia!")
        exit()
    atendido = pac.pop(0)
    sleep(2)
    print("======================")
    print("imprimindo:", atendido)
    print("======================")
    sleep(1)
    print("======================")
    if not pac:
        print("Tudo impresso(com certeza não foi ctrl + c ctrl + v da 5)!")
        exit()
         
    print("próximo:", pac[0])
    print("======================")
    sleep(2)
    if not pac:
            print("Tudo impresso(com certeza não foi ctrl + c ctrl + v da 5)!")
            exit()



