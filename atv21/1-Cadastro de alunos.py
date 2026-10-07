'''Uma escola precisa desenvolver uma pequena funcionalidade para armazenar os
nomes dos alunos de uma turma.
Os nomes precisam ficar armazenados para que o sistema possa apresentar
todos os alunos cadastrados e também acessar alunos de posições específicas.
O sistema deverá inicialmente possuir cinco alunos. Depois, um novo aluno
deverá ser adicionado.
Estrutura que deve ser utilizada
Lista
A lista é adequada porque os alunos precisam ser armazenados em uma
sequência e podem ser acessados por suas posições.
O que desenvolver
1. Criar uma lista com cinco nomes.
2. Exibir todos os alunos.
3. Exibir o primeiro aluno.
4. Exibir o último aluno.
5. Adicionar um novo aluno.
6. Exibir a lista atualizada.
Resultado esperado
Alunos cadastrados:
Ana
Carlos
Mariana
Pedro
João

Primeiro aluno: Ana
Último aluno: João

Lista atualizada:

Ana
Carlos
Mariana
Pedro
João
Lucas'''

# Criar uma lista com cinco nomes

alunos = ["Ana", "Carlos", "Mariana", "Pedro", "João"]

#numcont é só pra fazer a contagem dos nomes
numCont = 1
print(f"\n =====Lista de ALUNOS=====")
#percorre a lista
for i in alunos:
    # o primeiro sendo 1
    print(f"{numCont}º {i}")
    # o próximo 2 e etc
    numCont += 1
    #mostra primeiro e ultimo aluno
print(f"\n===============================")
print(f"Primeiro Aluno: {alunos[0]}")
print(f"Ultimo Aluno: {alunos[4]}")
print("===============================")
#pede o nome do novo aluno
nOval = input("Digite o nome do novato: ")
#guarda em alunos
alunos.append(nOval)

print(f"\n =====Lista de ALUNOS=====")
#como nessa parte ja seria 6, eu tiro então 5
numCont -= 5
for i in alunos:
    print(f"{numCont}º {i}")
    numCont += 1
print(f"\n===============================")
print(f"Primeiro Aluno: {alunos[0]}")
print(f"Ultimo Aluno: {alunos[5]}")
print("===============================")