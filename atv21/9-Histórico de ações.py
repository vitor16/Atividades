'''Um sistema possui uma funcionalidade para desfazer as últimas ações realizadas
pelo usuário.
Por exemplo, o usuário realizou cinco ações. Ao selecionar a opção "Desfazer", a
última ação realizada deverá ser desfeita primeiro.
Estrutura que deve ser utilizada

Pilha
A pilha é adequada porque a última ação realizada deve ser a primeira a ser
desfeita.
O que desenvolver
Adicione as seguintes ações:
Digitou o nome
Alterou o endereço
Adicionou um produto
Alterou o telefone
Excluiu um produto
Depois, utilize uma pilha para desfazer as ações.
Resultado esperado
Desfazendo: Excluiu um produto
Desfazendo: Alterou o telefone
Desfazendo: Adicionou um produto
Desfazendo: Alterou o endereço
Desfazendo: Digitou o nome
Observe que a ordem de saída é inversa da ordem de entrada.'''

#lista de credenciais
creden = []

#pedi as variaveis que o enunciado pediu
nome = input("Digite seu Nome: ")
creden.append(nome)
eNd = input("Digite seu endereço: ")
creden.append(eNd)
pRod = input("Digite o produto: ")
creden.append(pRod)
tEl = input("Digite seu numero de telefone: ")
creden.append(tEl)
#num é apenas para mostrar em ordem

num = 3




for i in range(4):
    #printa os que estao sendo disfeitos em ordem de ultimo que entrou primeiro a sair
    print(f"\n Desfazendo: ",creden[num])
    creden.pop()
    num -=1
    print("Lista atual: ",creden)
    if not creden:
        print("Lista agora vazia!")
    
    