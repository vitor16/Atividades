'''
Um sistema de atendimento classifica solicitações como prioritárias quando o
nível informado é 1 ou 2. Os demais níveis são tratados como solicitações
comuns.
• Operador original: nivel == 1 or nivel == 2
• Operador equivalente: nivel in (1, 2)
• Tarefa: leia um número que represente o nível de prioridade e informe a
classificação.
• Desafio adicional: teste os níveis 1, 2, 3 e 4.
'''

# Solução 1: considera prioritários os níveis 1 e 2 usando or.
nivel = int(input("Digite o nível de prioridade (1 a 4): "))
prioritaria = nivel == 1 or nivel == 2
print(f"Solução 1: solicitação prioritária? {prioritaria}")

# Solução 2: in verifica se o nível pertence à tupla de prioridades.
prioritaria_equivalente = nivel in (1, 2)
print(f"Solução 2: solicitação prioritária? {prioritaria_equivalente}")

# Exibe a classificação para os quatro níveis do desafio.
for nivel_teste in (1, 2, 3, 4):
    classificacao = "prioritária" if nivel_teste in (1, 2) else "comum"
    print(f"Nível {nivel_teste}: solicitação {classificacao}.")
