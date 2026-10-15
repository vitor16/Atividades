'''
Uma aplicação registra quantas vezes determinado usuário acessa uma
funcionalidade. O contador começa em zero e precisa ser atualizado a cada
acesso. Após três acessos, o programa deverá apresentar o total registrado.
• Operador original: contador = contador + 1
• Operador equivalente: contador += 1

• Tarefa: inicie contador com zero, incremente seu valor três vezes e exiba o
resultado após cada atualização.
• Desafio adicional: confira se o valor final corresponde à quantidade de
acessos registrados.
'''
contador = 0

#menu principal
while True:
    #condicional para contador
    if contador <= 2:
        print()
        print("========Menu========")
    #espaçamento
        print()
        print("1-fazer acesso a funcionalidade ")
        print("1-fazer acesso a funcionalidade tamém mas diferente ")
    #espaçamento diferente
        print(f"\n0- sair")
        opcao = input(f"\ndigite a operação desejada: ")
    
        if opcao == "1":
            contador += 1
            print("Acesso liberado, numero de acessos: ",contador)
        elif opcao == "2":
                    contador = contador + 1
                    print("Acesso liberado, numero de acessos registrados: ",contador)
        elif opcao == "0":
            print("Saindo...")
            exit()
        else:
            print("Tente novamente, opção incorreta!!")
    else:

        print("3 acessos, máximo atingido ")
        break