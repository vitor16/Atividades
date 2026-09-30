'''Um sistema precisa receber vários valores digitados pelo usuário.
O programa deverá continuar solicitando números enquanto o usuário desejar
continuar informando valores.

Quando o usuário informar 0, a entrada deverá ser encerrada.
Ao final, apresente a soma de todos os valores informados, desconsiderando o
zero utilizado para finalizar.
Utilize while.'''
#declaro uma variavel para ser somada e guardar o valor do loop,
#porque a variavel numero (sem s), vai mudar a cada loop.
nUmeros = 0
#loop do while
while True:
    #mostrar opções disponíveis
    print("====Escolha uma das opções abaixo====")
    print()
    print("1- Digitar um número")
    print("2- Ver a soma dos números")
    print("0- Sair")
    #peço a opção e logo em seguida a condicional checa qual 
    #ramificação do código seguir
    oPcao=input("Oque deseja fazer hoje?: ")
    if oPcao == "1":
        nUmero = int(input("Digite um número: "))

        nUmeros = nUmero + nUmeros
        
        
    elif oPcao == "2":
        print(f" A soma dos números é {nUmeros}")
    elif oPcao == "0":
        break
    else:
        print("Erro, valor inválido")
        print()
        print()
#quando escolher 0, break=quebrar e não freiar, break quebra o loop
print("Saindo...")

print ("⠀⠀⠀ ⣤⣴⣾⣿⣿⣿⣿⣿⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡄")
print ("⠀  ⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⢰⣦⣄⣀⣀⣠⣴⣾⣿⠃")
print ("⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⠀")
print ("⠀⠀⣼⣿⡿⠿⠛⠻⠿⣿⣿⡇⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀")
print ("⠀⠀⠉⠀⠀⠀⢀⠀⠀⠀⠈⠁⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀")
print ("⠀⠀⣠⣴⣶⣿⣿⣿⣷⣶⣤⠀⠀⠀⠈⠉⠛⠛⠛⠉⠉⠀⠀⠀")
print ("⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⣶⣦⣄⣀⣀⣀⣤⣤⣶⠀⠀")
print ("⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀")
print ("⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀")
print ("⢠⣿⡿⠿⠛⠉⠉⠉⠛⠿⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀")
print ("⠘⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⢿⣿⣿⣿⣿⣿⠿⠛⠀⠀⠀")

