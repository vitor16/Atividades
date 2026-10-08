'''Contexto
Um sistema de controle de acesso precisa apresentar os andares de um prédio
para organizar uma sequência de visitas técnicas.
O prédio possui seis andares.
Proposta

Crie uma função recursiva chamada mostrar_andares() que apresente os andares
de 1 até o número informado.
Teste
mostrar_andares(6)
Resultado esperado
Andar 1
Andar 2
Andar 3
Andar 4
Andar 5
Andar 6
Para pensar
Como fazer o número do andar avançar a cada chamada?'''








n = int(input("Número de andares: "))
n2 = n
n = 1


def mostrar_andares(n):
    if n >= 1 and n <= n2:
        print("andar", n)
        mostrar_andares(n+1)
    else:
        print("Fim")
        exit()
mostrar_andares(n)