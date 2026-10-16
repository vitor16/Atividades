'''
Uma sala pode ser utilizada quando estiver disponível e não estiver em
manutenção. O sistema deverá verificar as duas condições antes de autorizar o
uso.
• Operador original: disponivel and not em_manutencao
• Operador equivalente: not (not disponivel or em_manutencao)

• Tarefa: crie as variáveis disponivel e em_manutencao e informe se a sala
pode ser utilizada.
• Desafio adicional: teste todas as combinações possíveis das duas
variáveis.
'''

# Solucao 1: a sala precisa estar disponivel e fora de manutencao.
print("Solucao 1 | Solucao 2")
for disponivel in (False, True):
    for em_manutencao in (False, True):
        pode_utilizar = disponivel and not em_manutencao

        # Solucao 2: nega a situacao em que falta disponibilidade ou ha manutencao.
        pode_utilizar_equivalente = not (not disponivel or em_manutencao)
        print(
            f"Disponivel={disponivel}, manutencao={em_manutencao}: "
            f"{pode_utilizar} | {pode_utilizar_equivalente}"
        )
