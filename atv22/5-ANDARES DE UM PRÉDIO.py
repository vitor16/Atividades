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








# Lê a quantidade total de andares informada pelo usuário.
n = int(input("Número de andares: "))
# Guarda o limite final antes de usar n como contador do andar atual.
n2 = n
# A contagem começa no primeiro andar.
n = 1


def mostrar_andares(n):
    # Enquanto o andar atual estiver dentro do limite, mostra esse andar.
    if n >= 1 and n <= n2:
        print("andar", n)
        # Chama a função novamente para mostrar o próximo andar.
        mostrar_andares(n+1)
    else:
        # Caso base: todos os andares já foram apresentados.
        print("Fim")
        exit()


# Inicia a contagem dos andares a partir do primeiro.
mostrar_andares(n)