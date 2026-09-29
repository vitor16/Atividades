'''Uma escola deseja automatizar o cálculo do resultado final dos estudantes. Além
das notas, a frequência também deverá ser considerada para determinar a
situação do aluno.
Desenvolva um programa que solicite:
• Nome do estudante;
• Primeira nota;
• Segunda nota;
• Terceira nota;
• Percentual de frequência.
Calcule a média:
media = (nota1 + nota2 + nota3) / 3
Utilize as seguintes regras:
• Se a frequência for menor que 75%, o estudante estará reprovado por
frequência;

• Se a frequência for igual ou superior a 75% e a média for igual ou superior a
7, estará aprovado;
• Se a média for igual ou superior a 5 e menor que 7, estará em recuperação;
• Se a média for menor que 5, estará reprovado por nota.
O programa deverá apresentar:
• Nome do estudante;
• Média final;
• Frequência;
• Situação final.
Também verifique se as notas estão entre 0 e 10. Caso alguma nota seja inválida,hk
apresente uma mensagem de erro.'''
#pede os dados do estudante
nome = input("Digite o nome do estudante: ")
nota1 = float(input("Digite a primeira nota (0 a 10): "))
nota2 = float(input("Digite a segunda nota (0 a 10): "))
nota3 = float(input("Digite a terceira nota (0 a 10): "))
frequencia = int(input("Digite o percentual de frequência (0 a 100): "))
#se as notas e a frequência forem válidas, calcula a média e determina a situação do estudante
if nota1 < 0 or nota1 > 10:
    print("Erro: A primeira nota deve estar entre 0 e 10.")
    exit()
elif nota2 < 0 or nota2 > 10:
    print("Erro: A segunda nota deve estar entre 0 e 10.")
    exit()
elif nota3 < 0 or nota3 > 10:
    print("Erro: A terceira nota deve estar entre 0 e 10.")
    exit()
elif frequencia < 0 or frequencia > 100:
    print("Erro: A frequência deve estar entre 0 e 100.")
    exit()
media = (nota1 + nota2 + nota3) / 3
if frequencia < 75:
    situacao = "Reprovado por frequência"
elif media >= 7:
    situacao = "Aprovado"
elif media >= 5:
    situacao = "Recuperação"    
else:
    situacao = "Reprovado por nota"
    #exibe o resultado final do estudante
print("Nome do estudante: ", nome)
print("Média final: ", media)
print("Frequência: ", frequencia)
print("Situação final: ", situacao)