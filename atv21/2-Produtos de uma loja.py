'''Uma loja precisa apresentar os produtos disponíveis em seu sistema.
Os produtos estão armazenados em uma estrutura e o sistema deverá percorrer
todos os elementos para apresentá-los na tela.
Estrutura que deve ser utilizada
Lista
A lista é adequada para armazenar os diversos produtos e permitir que eles sejam
percorridos.
O que desenvolver
1. Criar uma lista com cinco produtos.
2. Utilizar um for para percorrer a lista.
3. Apresentar cada produto na tela.
Resultado esperado
Produtos disponíveis:

Teclado
Mouse
Monitor
Impressora
Webcam'''
#importa a função sleep
from time import sleep

#estoque inicial
estoque= ["Teclado", "Mouse" , "Monitor" , "Impressora" , "Webcam"]
print("Items disponíveis: ")
#percorre o estoque
for i in estoque:
    print(i)
#loop de menu principal
while True:
    print("======Menu Principal======")
    print("1-Adicionar mais items a lista")
    print("2-Remover items da lista")
    print("3-Listar items da lista")
    print("4-auto DESTRUIÇÃO(Apaga Tudo E Guarda Sua alma EM um CHIP)")
    print("5-Sair   ")
    opcao = input("Digite a opção desejada: ")
    if opcao == "1":
        #opção de adicionar mais items
        item = input("Digite o item que deseja adicionar: ")
        estoque.append(item)
        print(f"{item} adicionado com sucesso!")
    elif opcao == "2":
        #remove item da lista
        item = input("Digite o item que deseja remover: ")
        if item in estoque:
            estoque.remove(item)
            print(f"{item} removido com sucesso!")
        else:
            print(f"{item} não encontrado na lista.")
        #mostra lista atualizada
    elif opcao == "3":
        print("Items disponíveis: ")
        for i in estoque:
            print(i)
        # Guarda sua personalidade e ideais em um chip como punição de um crime
    elif opcao == "4":
        estoque.clear()
        print("Lista limpa com sucesso!")
        print("Todos os items foram apagados e sua alma foi guardada em um chip.")
        sleep(2)
        print("A lista está vazia ", end="")
        sleep(1)
        print("...")
        sleep(2)
        print("Espero que tenha valido a pena, sua alma está guardada em um chip e a lista foi apagada...")
        sleep(2)
        print("no happy endings in cybercity")
        print("                       ⣀⣀⣤⣤⣤⣤⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("                 ⢀⣠⣶⣾⡿⠿⢛⣛⣛⣛⡛⠻⠿⣿⣷⣦⡀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀     ⢀⣴⣿⡿⠛⠁⠀⣴⣿⣿⣿⣿⣿⣷⡄⠀⠉⠻⣿⣷⡀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀  ⢀⣿⡿⢁⣠⣤⣤⣤⣈⢿⣿⣿⣿⣿⣿⣿⠇⣠⣤⣤⣤⣀⠹⣿⣧⠀")
        print("⠀⠀⠀       ⣿⣿⠘⣿⣿⣿⣿⣿⣿⣿⡀⢸⣿⣿⠀⣸⣿⣿⣿⣿⣿⣿⡿⢹⣿⡇")
        print("⠀⠀⠀⠀⠀⠀   ⢿⣿⡄⠈⠙⠛⠟⠛⠙⢿⣿⣾⣿⣿⣾⣿⠟⠙⠛⠟⠛⠉⠀⣸⣿⠁")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠘⢿⣷⣄⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀⠀⠀⠀⠀⢀⣴⣿⠟⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⠈⠻⣿⣷⣄⡀⠀⠀⠀⢸⣿⣿⠀⠀⠀⠀⢀⣴⣿⡿⠃⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⠈⠙⠿⣿⣷⣶⣤⣼⣛⣻⣤⣤⣶⣾⡿⠟⠋⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀      ⠀⠉⠉⠛⠛⠛⠛⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀")
    #Sai do programa
    elif opcao == "5":
        print("Saindo do programa...")
        break
    #aceita somente respostas corretas
    else:
        print("Opção inválida. Por favor, digite uma opção válida.")