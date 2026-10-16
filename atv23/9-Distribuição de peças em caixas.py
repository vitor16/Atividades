'''
Um depósito precisa organizar 47 peças em caixas com seis unidades. O sistema
deverá informar quantas caixas completas podem ser preenchidas e quantas
peças permanecerão fora das caixas completas.
• Solução 1: use caixas = pecas // 6 e sobras = pecas % 6.
• Solução 2: use caixas //= 6 e sobras %= 6 em cópias da quantidade inicial.
• Tarefa: calcule quantas caixas completas podem ser preenchidas e quantas
peças sobram.
• Desafio adicional: apresente os dois resultados em uma única mensagem.
'''
# Solucao 1: // informa caixas completas e % informa as pecas que sobram.
pecas = 47
caixas = pecas // 6
sobras = pecas % 6
print(f"Solucao 1: {caixas} caixas completas e {sobras} pecas restantes.")

# Solucao 2: os operadores //= e %= atualizam as quantidades diretamente.
caixas_abreviadas = pecas
sobras_abreviadas = pecas
caixas_abreviadas //= 6
sobras_abreviadas %= 6
print(
    f"Solucao 2: {caixas_abreviadas} caixas completas e "
    f"{sobras_abreviadas} pecas restantes."
)