'''Contexto
Um sistema de controle de um elevador precisa informar os andares durante a
descida. O elevador está no quinto andar e deverá informar cada andar até chegar
ao térreo.

A sequência será:
5
4
3
2
1
0
Proposta
Crie uma função recursiva chamada descer_elevador() que receba o andar atual e
faça a contagem regressiva até o térreo.
Teste
descer_elevador(5)
Resultado esperado
5
4
3
2
1
0
Térreo
Para pensar
Qual deve ser o caso base dessa função?'''
#importa a funçaõ 
from time import sleep
#variavel para saber o numero de andares percorridos
n=int(input("Digite o andar atual: "))
#função
def descer_elevador(n):
    #enquanto n for maior ou igual a zero ele mostra o andar e diminui 1 de n
    if n>=0:
        sleep(2)
        print("Andar ",n)
        descer_elevador(n-1)
    else:
        #na verdade exi() não era necessário aqui, ele simplesmente acaba se não tiver mais nada
        print("Térreo")

descer_elevador(n)