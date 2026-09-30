'''Uma aplicação possui o seguinte menu:
1 - Cadastrar usuário
2 - Consultar usuário
3 - Alterar usuário
4 - Excluir usuário
0 - Sair
Crie um programa que apresente o menu ao usuário.
O menu deverá continuar sendo apresentado enquanto o usuário não escolher a
opção 0.
Utilize while para controlar a repetição.
Para cada opção escolhida, apresente uma mensagem informando a operação
selecionada.'''

#definindo as funções para cada operação do sistema
#começo com um array para armazenar todos os nomes
nomes = []
# duas vari
nome = ""
nomeCad = "" 
def cad_Usr():
    nome = input("Digite o nome do usuário: ")
    nomes.append(nome)
    print(f"Usuário {nome} cadastrado com sucesso!")
    nomeCad = nome
def con_Usr():
    nome= input("Digite o nome do usuário que deseja consultar: ")
    if nome in nomes:
        print(f"usuário {nome} encontrado!")
    else:
        print("usuário não cadastrado!")
def altr_Usr():
    global nome
    print("usuarios cadastrados: ", ", ".join(nomes))
    nomeCad = input("Escolher usuário: ")
    nome = nomeCad
def del_Usr():
    nome = input("Digite o nome do usuário para excluir: ")
    nomes.remove(nome)
    print("usuário {nome} foi removido!")

#programa principal
print("Bem-vindo ao sistema de atendimento da empresa!")
print("Escolha uma opção do menu")

#loop para manter o menu ativo até que o usuário escolha sair (break) que faz while parar de executar fazendo ser False


while True:
    print()
    print()
    
    if nome in nomes:
        print(f"usuário atual: {nome}")
    else:
        print("nenhum usuário logado atualmente!")
    print("1 - Cadastrar usuário")
    print("2 - Consultar usuário")
    print("3 - Alterar usuário")
    print("4 - Excluir usuário")
    print("0 - Sair")
    opcao = input("Digite a opção desejada: ")
    if opcao == "1":
        cad_Usr()
    elif opcao == "2":
        con_Usr()
    elif opcao == "3":
        altr_Usr()
    elif opcao == "4":
        del_Usr()
    elif opcao == "0":
        break
    else:
        print("Opção inválida. Tente novamente.")   


print("saindo...")