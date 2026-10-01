'''Uma escola precisa registrar as notas de 5 estudantes.
Para cada estudante, o sistema deverá solicitar uma nota e, ao final, apresentar:
• a quantidade de estudantes aprovados;
• a quantidade de estudantes em recuperação;
• a quantidade de estudantes reprovados.
Considere:
• Nota maior ou igual a 7 → Aprovado
• Nota entre 5 e 6.9 → Recuperação
• Nota menor que 5 → Reprovado
Utilize for para controlar a quantidade de estudantes.'''

#primeiro um array para todas as notas
nOtas = []
#depois 3 contadores com valores inicialmente vazios
aProvados = 0
rEprovados = 0
rEcuperados = 0

#por 5 vezes guardarei "nota" no array "notas"
for i in range (1,6):
    print()
    nota = float(input(f"digite a {i} nota(1-10): "))
    nOtas.append(nota)
    print()

#criei esses ifs para testar cada uma das posicoes do vetor notas
# assim se a nota estiver no parametro aprovado por exemplo, 
# adiciona o incremento de 1 em "aprovados"

#posicao 0, sendo a primeira nota digitada
if nOtas[0] >= 7:
    print("primeiro aluno aprovado!")
    aProvados += 1
elif nOtas[0] >= 5 and nOtas[0] <= 6.9:
    print("primeiro aluno de recuperacao!")
    rEcuperados += 1
elif nOtas[0] <5:
    print("primeiro aluno de reprovado!")
    rEprovados += 1


#posicao 1 sendo a segunda
if nOtas[1] >= 7:
    print("Segundo aluno aprovado!")
    aProvados += 1
elif nOtas[1] >= 5 and nOtas[1] <= 6.9:
    print("Segundo aluno de recuperacao!")
    rEcuperados += 1
elif nOtas[1] < 5:
    print("Segundo aluno de reprovado!")
    rEprovados += 1

#posicao 2 sendo a terceira
if nOtas[2] >= 7:
    print("terceiro aluno aprovado!")
    
    aProvados += 1
elif nOtas[2] >= 5 and nOtas[2] <= 6.9:
    print("terceiro aluno de recuperacao!")
    rEcuperados += 1
elif nOtas[2] < 5:
    print("terceiro aluno de reprovado!")
    rEprovados += 1

#posicao 3 sendo a quarta
if nOtas[3] >= 7:
    print("quarto aluno aprovado!")
    aProvados += 1
elif nOtas[3] >= 5 and nOtas[3] <= 6.9:
    print("quarto aluno de recuperacao!")
    rEcuperados += 1
elif nOtas[3] < 5:
    print("quarto aluno de reprovado!")
    rEprovados += 1

#e por fim posicao 4 sendo a quinta
if nOtas[4] >= 7:
    print("quinto aluno aprovado!")
    aProvados += 1
elif nOtas[4] >= 5 and nOtas[4] <= 6.9:
    print("quinto aluno de recuperacao!")
    rEcuperados += 1
elif nOtas[4] < 5:
    print("quinto aluno de reprovado!")
    rEprovados += 1


#o sumario pega entao esses contadores agora com valores ou nao

print("========sumario========")
print()
print(f"Alunos aprovados: {aProvados}")
print()
print(f"Alunos reprovados: {rEprovados}")
print()
print(f"Alunos de recuperacao: {rEcuperados}")
