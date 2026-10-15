'''
Um evento disponibilizou 15 vagas para inscrições. A cada inscrição confirmada, o
sistema deve diminuir a quantidade de vagas disponíveis. Após quatro
confirmações, o programa deverá informar quantas vagas restam e se ainda existe
disponibilidade.
• Operador original: vagas = vagas - 1
• Operador equivalente: vagas -= 1
• Tarefa: inicie vagas com 15 e registre quatro inscrições, atualizando a
variável a cada confirmação.
• Desafio adicional: informe se ainda há vagas disponíveis.
'''
#para esste exercicio decidi utilizar uma função chamada random
#aqui posso decidir se toma o caminho de Operador original: vagas = vagas - 1 ou Operador equivalente: vagas -= 1
import random
#inicializo a variavel com 15
vagas = 15
#por motivos de formatação confirmadas precisa ser = 1
confirmadas = 0
while True:
    print()
    #peço valor para sN(sim ou nao)
    sN = input("Deseja confirmar sua vaga?(S = sim, N = nao e sair,fecha o programa): ")
    sN.upper()
    print()
    #se as vagas tiverem acabado fecho o programa
    if vagas == 0:
        print("Não temos mais vagas")
        exit()
    #se 4 vagas forem confirmadas a raiz condicional muda
    elif vagas <= 12:
           
    
            if sN == "s":
                if random.random() < 0.5:
                    vagas -= 1  # 50% de chance
                    confirmadas+=1
                    print("Vagas disponíveis(Método: vagas-=1): ", vagas)
                    print("Vagas confirmadas: ",confirmadas)
                    print()
                else:
                    vagas = vagas - 1  # 50% de chance
                    confirmadas = confirmadas + 1
                    print(f"Vagas disponíveis(Método: vagas = vagas - 1): {vagas}")
                    print("Vagas confirmadas: ",confirmadas)
                    
                    print()

            elif sN == "n":
                print(f"Vagas disponíveis {vagas}")
                print("Vagas confirmadas: ",confirmadas)
                
                break
            else:
                print("S ou N?")
    #caso contrário programa segue normalmente
    else:
            if sN == "s":
                #random vai de 0.0 a 1, então 0.5 garante que tem 50% de chance de um acontecer
                if random.random() < 0.5:
                    vagas -= 1  # 50% de chance
                    confirmadas+=1
                    print("Vagas disponíveis(Método: vagas-=1): ", vagas)
                    print("Vagas confirmadas: ",confirmadas)
                    
                    print()
                #caso contrário 50% do outro acontecer
                else:

                    vagas = vagas - 1  # 50% de chance
                    confirmadas = confirmadas + 1
                    print(f"Vagas disponíveis(Método: vagas = vagas - 1): {vagas}")
                    print("Vagas confirmadas: ",confirmadas)
                    
                    print()
            #caso deseje sair antes
            elif sN == "n":
                print(f"Vagas disponíveis {vagas}")
                print("Vagas confirmadas: ",confirmadas)
                
                break
            #valor invalido
            else:
                print("S ou N?")
         