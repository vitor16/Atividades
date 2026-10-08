'''Contexto
Você está desenvolvendo um sistema para uma máquina que precisa realizar uma
contagem antes de iniciar seu funcionamento. A contagem deve começar em um
número informado e diminuir até chegar a 1.
Poposta
Crie uma função recursiva chamada contagem_regressiva() que receba um
número e mostre os valores em ordem decrescente.
Teste
contagem_regressiva(5)
Resultado esperado
5
4

3
2
1
Para pensar
Identifique:
• Qual é o caso base?
• Qual é a chamada recursiva?
• O que muda a cada chamada?'''

#importa a funçaõ time
from time import sleep
n = int(input("Digite o numero: "))
#funcao para contar
def contagem_regressiva(n):
    #doorme um segundo para parecer uma contagem real
    sleep(1)
    if n > 0:
        print(n)
        contagem_regressiva(n-1)
    else:
        #quando n for 0 acaba
        print("Fim")
        exit()
    
contagem_regressiva(n)