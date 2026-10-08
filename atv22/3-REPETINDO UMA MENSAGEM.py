'''Contexto
Um sistema de comunicação precisa apresentar uma mensagem de aviso
algumas vezes para garantir que ela seja visualizada pelo usuário.
Por exemplo:
Atenção!
Atenção!
Atenção!
Proposta
Crie uma função recursiva chamada mostrar_mensagem() que receba uma
mensagem e a quantidade de vezes que ela deverá ser apresentada.
Teste
mostrar_mensagem("Atenção!", 3)
Resultado esperado
Atenção!
Atenção!
Atenção!
Para pensar
A cada chamada da função, a quantidade de repetições deverá aumentar ou
diminuir?diminuir'''
#importa a função sleep
from time import sleep
#pego os dois valores
mEn = input("Qual mensagem deseja mostrar?: ")
n = int(input("Quantas vezes?: "))
#declaro função
def mostrar_mensagem(mEn , n):
    #dorme 1 seg
    sleep(1)
    #enquanto o numero de vezes for maior que 0 chama a funçaõ
    if n > 0:
        print(mEn)
        n -= 1
        mostrar_mensagem(mEn , n)
    else:
        print("Fim")
        exit()
mostrar_mensagem(mEn, n)