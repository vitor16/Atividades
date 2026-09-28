'''Crie uma função chamada calcular_media() que receba três notas.
A função deverá calcular e retornar a média das notas.

No programa principal, solicite as três notas, utilize a função e apresente a média
calculada.  '''

#definindo a função calcular_media para .... calcular a média
def calcular_media(nota1, nota2, nota3):
    #calcula a média das três notas recebidas como parâmetros
    #inicialmente variaveis vazias
    media = (nota1 + nota2 + nota3) / 3
    return media
#agora peço o valor das variaveis utilizadas pela função
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

#chamo a função calcular_media com os valores das notas e exibo o resultado

print(f"A média das notas é: {calcular_media(nota1, nota2, nota3)}")