'''Uma aplicação precisa calcular a soma dos números de 1 até 100.
Desenvolva um programa utilizando for para realizar a soma.
Ao final, apresente o resultado da soma.'''
#valor inicial para o numero
num = 0
#for de um a cem
for i in range(1,101):
    #para ser mais facil de vizualizar  adicionei a conta sendo feita
    print (num," + ",i," = ", num + i)
    #porem o print nao guarda valor algum, entao abaixo eu guardo sempre a soma de
    #seja la oque o numero atualmente é de 1 a 100
    num = num + i

print("ou seja, resultado final é: ",num)