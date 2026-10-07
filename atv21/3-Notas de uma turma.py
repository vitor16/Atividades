'''Um sistema escolar precisa armazenar as notas de cinco alunos.
Depois de armazenar as notas, o sistema deverá percorrer os valores e calcular a
soma e a média da turma.
Estrutura que deve ser utilizada
Lista
A lista permite armazenar diversas notas em uma única estrutura e percorrer
todos os valores.
O que desenvolver
1. Criar uma lista com cinco notas.
2. Percorrer as notas utilizando for.
3. Calcular a soma.
4. Calcular a média.
5. Apresentar os resultados.
Resultado esperado
Considerando as notas:
7
8
6
9
10
O sistema deverá apresentar algo semelhante a:
Notas:
7
8
6
9
10

Soma: 40

Média: 8.0'''

#define a lista

nOtas = []
#uma variavel para somar
soma = 0

for i in range(5):
    #pede 5 notas
    nota= int(input(f"Digite a {i+1}º nota: "))
    #soma todas elas
    soma += nota
    nOtas.append(nota)
#calcula a media
media = soma/5
print("====================")
print("Notas dos alunos: ")
print("====================")
#mostra todas
for i in nOtas:
    print(i)
# mostra a soma e a media
print("A soma de todas as notas é: ", soma )
print("A méda da sala é: ", media)