'''Crie um programa que possua as seguintes funções:
somar()
subtrair()
multiplicar()
dividir()
Cada função deverá receber dois números e realizar a 
operação correspondente.
Crie um menu para que o usuário possa escolher 
qual operação deseja realizar.'''
#definição de funções para as operações
def somar(num1, num2):
    print (num1 + num2)
def subtrair(num1,num2):
    print(num1-num2)
def multiplicar(num1,num2):
    print(num1*num2)
def dividir(num1,num2):
    if num2 == 0 or num1 == 0:
        print("Não é possível dividir por zero.")
    else:
        print(num1/num2)
#peço o valor das variáveis e a operação desejada
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
operacao= input("Digite a operação desejada (somar, subtrair, multiplicar, dividir): ").upper()
while operacao != "SOMAR" and operacao != "SUBTRAIR" and operacao != "MULTIPLICAR" and operacao != "DIVIDIR":
    print("Operação inválida. Por favor, escolha uma operação válida.")
    operacao= input("Digite a operação desejada (somar, subtrair, multiplicar, dividir): ").upper()
#se a operação for igual a SOMAR, SUBTRAIR, MULTIPLICAR ou DIVIDIR, chame a função correspondente
if operacao == "SOMAR":
    somar(num1,num2)
elif operacao == "SUBTRAIR":
    subtrair(num1,num2)
elif operacao == "MULTIPLICAR":
    multiplicar(num1,num2)
elif operacao == "DIVIDIR":
    dividir(num1,num2)
#se não ,mostra um código de erro, assim somente as opções validas serão aceitas
else :
    print("Operação inválida. Por favor, escolha uma operação válida.")



