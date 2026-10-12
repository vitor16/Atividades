'''Contexto
Você está desenvolvendo um pequeno sistema que precisa realizar uma operação
em várias etapas. A cada etapa, o sistema deverá informar que está processando.
Quando todas as etapas forem concluídas, o sistema deverá apresentar uma
mensagem informando o término do processo.
Proposta

Crie uma função recursiva chamada processar() que receba um número indicando
a quantidade de etapas.
A cada chamada, apresente:
Processando...
Quando todas as etapas forem concluídas, apresente:
Processamento concluído!
Teste
processar(3)
Resultado esperado
Processando...
Processando...
Processando...
Processamento concluído!
Para pensar
Identifique:
• Qual é o caso base?
• Qual é a chamada recursiva?
• Qual valor deve ser alterado a cada chamada?
• O que aconteceria se a função nunca chegasse ao caso base?'''

# Função recursiva para simular o processamento de várias etapas.
# Caso base: quando a quantidade de etapas for 0, o processamento termina.
def processar(etapas):
    if etapas == 0:
        print("Processamento concluído!")
        return
    # Em cada chamada, informa que a etapa está sendo processada.
    print("Processando...")
    # Reduz a quantidade de etapas até chegar ao caso base.
    processar(etapas - 1)


# Pede ao usuário a quantidade de etapas a serem processadas.
quantidade = int(input("Digite a quantidade de etapas: "))
processar(quantidade)


