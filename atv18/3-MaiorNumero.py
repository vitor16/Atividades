'''Crie uma função chamada maior_numero() que receba dois números.
A função deverá verificar qual dos dois números possui o maior valor.
Caso os valores sejam iguais, deverá informar que os números são iguais.'''
#definir função para descobrir maior numero
def maior_numero(num1, num2):
    if num1 > num2:
        print(num1)
    else:
        print(num2)

# Solicita os dois números ao usuário
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
# Chama a função maior_numero com os números fornecidos
maior_numero(num1,num2)