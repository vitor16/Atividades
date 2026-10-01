'''Desenvolva um programa que apresente o seguinte menu:
=========================
SISTEMA ESCOLA
=========================

1 - Cadastrar aluno
2 - Consultar alunos
3 - Registrar nota
4 - Exibir quantidade de alunos
0 - Encerrar sistema
O programa deverá permanecer em execução até que o usuário escolha a opção
0.
Para cada opção, apresente uma mensagem correspondente.
Exemplo:
Opção 1 selecionada.
Cadastro de aluno.
O programa deverá utilizar um laço de repetição para manter o menu funcionando.
Requisito adicional
Ao escolher a opção 0, apresente:
Sistema encerrado.

Desafio extra
Analise os três cenários abaixo e determine qual estrutura de repetição você
utilizaria em cada situação:
Situação A
Um sistema precisa executar uma tarefa exatamente 10 vezes.
Estrutura escolhida: _______For_______________
Situação B
Um sistema precisa continuar solicitando uma senha enquanto o usuário não
informar a senha correta.
Estrutura escolhida: _________While_____________
Situação C
Um sistema precisa solicitar uma informação pelo menos uma vez e continuar
solicitando enquanto o valor informado for inválido.
Estrutura escolhida: _________While True_____________'''
#vetor para armazenar os nomes dos alunos e outro para armazenar as notas
alunos = []
notas = []

#funções para cada operação do sistema
def cad_Aluno():
    print("Opção 1 selecionada.")
    print("Cadastro de aluno.")
    nome = input("Digite o nome do aluno: ")
    #se o nome ja estiver na lista de alunos, ele nao vai cadastrar e vai mostrar uma mensagem
    if nome in alunos:
        print(f"Aluno {nome} já está cadastrado.")
    else:
        #se o nome nao estiver na lista de alunos, ele vai cadastrar e adicionar a nota 0
        alunos.append(nome)
        notas.append(0)
        print(f"Aluno {nome} cadastrado com sucesso.")

#definição da função para consultar alunos
def con_Aluno():
    print("Opção 2 selecionada.")
    print("Consulta de alunos.")
    #se o lenght( que significa quantidade de elementos) for igual a 0,
    #  significa que nao ha alunos cadastrados
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
    else:
        nome = input("Digite o nome do aluno para consultar: ")
        #se o nome estiver na lista de alunos, ele vai pegar a posicao do nome e mostrar a nota
        if nome in alunos:
            posicao = alunos.index(nome)
            print(f"Aluno {nome} encontrado.")
            print(f"Nota atual: {notas[posicao]}")
        else:
            #se o nome nao estiver na lista de alunos, ele vai mostrar uma mensagem de erro
            print(f"Aluno {nome} não encontrado.")

#definição da função para registrar nota
def reg_Nota():
    print("Opção 3 selecionada.")
    print("Registro de nota.")
#se o lenght( que significa quantidade de elementos) for igual a 0,
#  significa que nao ha alunos cadastrados, entao nao pode registrar nota
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado. Cadastre um aluno antes de registrar a nota.")
    else:
        #pega o nome do aluno para registrar a nota
        nome = input("Digite o nome do aluno para registrar a nota: ")
        #se o nome estiver na lista de alunos, ele vai pegar a posicao do nome e registrar a nota
        if nome in alunos:
            #pega a posicao do nome na lista de alunos
            #index() retorna a posição do elemento na lista, que é 
            # usada para acessar a nota correspondente na lista de notas
            posicao = alunos.index(nome)
            nota = input(f"Digite a nota do aluno {nome}: ")
            #substitui a vírgula por ponto para permitir a entrada de números decimais
            nota = nota.replace(",", ".")
            #verifica se a nota é um número válido entre 0 e 10
            #JA QUE tive problema com o float, eu usei o replace para substituir a vírgula por ponto
            if nota.replace(".", "").isdigit() and float(nota) >= 0 and float(nota) <= 10:
                notas[posicao] = float(nota)
                print(f"Nota {nota} registrada para o aluno {nome}.")
            else:
                #se a nota nao for valida, ele vai mostrar uma mensagem de erro
                print("Nota inválida. Digite uma nota entre 0 e 10.")
        else:
            #esse else é para quando o nome do aluno nao estiver na lista de alunos, 
            # ele vai mostrar uma mensagem de erro
            print(f"Aluno {nome} não encontrado. Não é possível registrar a nota.")

#definição da função para exibir a quantidade de alunos cadastrados
def qtd_Alunos():
    print("Opção 4 selecionada.")
    print("Exibição da quantidade de alunos.")
    #uso o len() para contar a quantidade de elementos no array alunos e mostrar na tela
    print(f"Quantidade de alunos cadastrados: {len(alunos)}")

#programa principal
while True:
    print("=========================")
    print("SISTEMA ESCOLA")
    print("=========================")
    print("1 - Cadastrar aluno")
    print("2 - Consultar alunos")
    print("3 - Registrar nota")
    print("4 - Exibir quantidade de alunos")
    print("0 - Encerrar sistema")
# loop para manter o menu ativo até que o usuário escolha sair (break) que faz while 
# parar de executar fazendo ser False
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cad_Aluno()
    elif opcao == "2":
        con_Aluno()
    elif opcao == "3":
        reg_Nota()
    elif opcao == "4":
        qtd_Alunos()
    elif opcao == "0":
        print("Sistema encerrado.")
        break
    else:
        print("Opção inválida. Tente novamente.")