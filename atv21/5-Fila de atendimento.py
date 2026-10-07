'''Uma clínica precisa controlar o atendimento dos pacientes.
Os pacientes devem ser atendidos na mesma ordem em que chegaram. O
primeiro paciente que chegou deve ser o primeiro a ser atendido.
Estrutura que deve ser utilizada
Fila
A fila é adequada porque utiliza o princípio FIFO — First In, First Out.
O que desenvolver
1. Criar uma fila.
2. Adicionar cinco pacientes.
3. Apresentar a fila.
4. Atender os pacientes um por vez.
5. Retirar o primeiro paciente da fila a cada atendimento.
Resultado esperado
Fila de atendimento:
Ana
Carlos
Mariana
Pedro
João

Atendendo: Ana
Atendendo: Carlos
Atendendo: Mariana
Atendendo: Pedro
Atendendo: João'''

#lista vaszia
from time import sleep
pac= []
#loop para pedir o nome 5 vezes

for i in range(5):
    nome = input(f"Digite o Nome do {i+1}º paciente: ")
    pac.append(nome)
print("======================")
print("Pacientes: ")
#loop para mostrar todos os clientes
for a in pac:
    print(a)
#loop para mostrar regressão de fila
for j in range(5):
    if not pac:
        print("Lista vazia!")
        exit()
    atendido = pac.pop(0)
    sleep(2)
    print("======================")
    print("Pessoa atendida:", atendido)
    print("======================")
    sleep(1)
    print("======================")
    print("Fila após atendimento:", pac)
    print("======================")
    sleep(2)
    if not pac:
            print("Lista vazia!")
            exit()




