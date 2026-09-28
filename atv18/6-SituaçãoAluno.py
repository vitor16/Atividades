'''Crie uma função chamada verificar_situacao() que receba a média de um aluno.
A função deverá retornar uma das seguintes situações:
Aprovado

Recuperacao
Reprovado
Considere:
• Média maior ou igual a 7: Aprovado
• Média entre 5 e 6.9: Recuperação
• Média abaixo de 5: Reprovado'''
# definir função verificar_situacao() que recebe a média do aluno e retorna a situação correspondente
def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif 5 <= media < 7:
        return "Recuperacao"
    else:
        return "Reprovado"
#pede as notas do aluno e calcula a média
nota1 = float(input("Digite a nota do primeiro trimestre: "))
nota2 = float(input("Digite a nota do segundo trimestre: "))
nota3 = float(input("Digite a nota do terceiro trimestre: ")) 

media = (nota1 + nota2 + nota3) / 3
#declara a variavel situação para fazer o codigo mais simples de entender
situacao = verificar_situacao(media)
print(f"Situação do aluno: {situacao}") 