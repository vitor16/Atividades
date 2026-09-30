'''Um sistema precisa cadastrar 5 participantes de uma atividade.
Utilize um laço for para solicitar o nome de cada participante.
Ao final do cadastro, apresente os nomes informados.'''
#para isso crio um vetor chamado nomes
nOmes = []
#loop de for 5 vezes
for i in range(1, 6):
    nOme = input(f"Digite o nome do {i} participante: ")
    #guardo o a string nome no array nomes um de cada vez
    nOmes.append(nOme)
#nesse ponto eu queria mostrar os nomes em ordem usando o valor de i denovo
#porém i agora é 5, então tiro 4
i -= 4

print("Participantes cadastrados:")
#mostra os nomes guardados no array "nomes"
for nOme in nOmes:
    
    print(f"{i}º {nOme}")
    i = i + 1