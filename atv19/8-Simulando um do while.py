'''Uma aplicação precisa solicitar ao usuário uma idade.
A idade deverá ser maior ou igual a 18.
O programa deverá primeiro solicitar a idade pelo menos uma vez e, caso o
valor seja inválido, deverá solicitar novamente até que uma idade válida seja
informada.
Implemente essa situação utilizando while, simulando o comportamento de um
do while.'''

#variavel iDade para receber o valor inicial
iDade = int(input("Digite sua idade: "))

while True:
    # se a idade for maior ou igual a 18 quebra o loop
    if iDade >= 18:
        print("Hora de trabalhar!")
        break
    #se não ela so pode ser menor, e se for menor não quebra o loop
    else:
        print("Idade inválida, deve ser maior de 18 anos ou ter 18 anos ")
        iDade = int(input("Digite sua idade: "))