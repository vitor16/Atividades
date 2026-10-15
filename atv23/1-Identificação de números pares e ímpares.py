'''
Um sistema de controle de equipamentos utiliza números inteiros para identificar
cada item cadastrado. Para organizar os equipamentos, é necessário identificar
quais códigos são pares e quais são ímpares. O sistema deverá calcular o resto da
divisão do código por 2 e apresentar uma mensagem correspondente.
• Operador original: %
• Equivalência conceitual: mod
• Tarefa: leia um número inteiro, calcule o resto da divisão por 2 e informe se
o código é par ou ímpar.
• Desafio adicional: teste três números diferentes e compare os resultados.
'''

#como python não possui mod, utilizarei .fmod(resto para float)
#para isso preciso importar math
import math
#crio dois vetores para armazenar cada tipo
pAres = []
iMpares = []

#função para descobrir par ou impar utilizando %
def pArimp():
    global pAres
    global iMpares

    for i in range(3):    
        n1=int(input(f"Digite o {i+1}º numero para saber se é par ou ímpar utilizando o operador %: "))
        if n1 % 2 == 0:
            print(n1," É par")
            pAres.append(n1)
        else:
            print(n1," É ímpar")
            iMpares.append(n1)
   
    if not pAres:
        print("nenhum número par")
    elif not iMpares:
        print("nenhum número ímpar")
    else:
        print("Números pares: ", pAres)
        print("Números ímpares: ", iMpares)

          
#função para par ou impar utilizando math.fmod (a,b) a sendo o valor desejado e b sendo o divisor, e == 0  sendo o resto
def pArimp2(n2):

    
    if n2 <= 3:
        n=float(input(f"Digite o {n2} ºnumero para saber se é par ou ímpar utilizando o operador %: "))
        if  math.fmod (n,2) == 0.0:
            print(n," É par")
            pAres.append(n)
            pArimp2(n2 + 1)
        else:
            print(n," É ímpar")
            iMpares.append(n)
            pArimp2(n2 + 1)
    else:
        print("Números pares: ", pAres)
        print("Números ímpares: ", iMpares)
        
#menu principal
while True:
    print()
    print("========Menu========")
    #espaçamento
    print()
    print("1- verificar se seus 3 números são pares ou ímpares usando o operador %: ")
    print("2- verificar se seus 3 números são pares ou ímpares usando a função math: ")
    #espaçamento diferente
    print(f"\n0- sair")
    
    opcao = input(f"\ndigite a operação desejada: ")
    if opcao == "1":
        pArimp()
    elif opcao == "2":
        pArimp2(1)
    elif opcao == "0":
        print("Saindo...")
        exit()
    else:
        print("Tente novamente, opção incorreta!!")