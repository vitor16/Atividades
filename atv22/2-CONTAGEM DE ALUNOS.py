'''Contexto
Durante uma atividade em sala, o instrutor deseja apresentar uma contagem
crescente para organizar a entrada dos alunos em uma atividade.
Por exemplo, para uma turma com cinco alunos:
Aluno 1
Aluno 2
Aluno 3
Aluno 4
Aluno 5
Proposta
Crie uma função recursiva chamada contar_alunos() que receba a quantidade de
alunos e apresente a numeração de 1 até o valor informado.
Teste
contar_alunos(5)
Resultado esperado
Aluno 1
Aluno 2
Aluno 3
Aluno 4

Aluno 5
Para pensar
O que deve acontecer quando a contagem chegar ao número informado?'''

#importa a funçaõ time
from time import sleep
#pede um valor
n1 = int(input("Digite a quantidade de alunos: "))
#uso esse n para controlar o if
n = 1

#funcao para contar
def contar_alunos(n):
    #doorme um segundo para parecer uma contagem real    
    #quando n não for menor que n1 else sai do programa

    if n <= n1:
        print("Aluno", n)
        sleep(1)
        contar_alunos(n+1)
    else:
        print("Fim")
        exit()

    
contar_alunos(n)