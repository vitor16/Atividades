'''Uma empresa precisa cadastrar os nomes de cinco pessoas que participarão de
um treinamento.
A lista deverá começar vazia. Cada nome informado deverá ser armazenado nela.
Estrutura que deve ser utilizada
Lista
A lista permite iniciar sem elementos e receber novos dados durante a execução
do programa.
O que desenvolver
1. Criar uma lista vazia.
2. Solicitar cinco nomes.
3. Adicionar cada nome à lista.
4. Apresentar os nomes cadastrados.
Resultado esperado
Exemplo:
Digite o nome: Ana
Digite o nome: Carlos
Digite o nome: Mariana
Digite o nome: Pedro
Digite o nome: João

Pessoas cadastradas:

Ana
Carlos
Mariana
Pedro
João'''
#lista vaszia

emp= []
#loop para pedir o nome 5 vezes

for i in range(5):
    nome = input(f"Digite o {i+1}º Nome: ")
    emp.append(nome)
print("======================")
print("Pessoas cadastradas: ")
for j in emp:
    print(j)

