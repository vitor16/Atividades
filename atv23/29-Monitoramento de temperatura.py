'''
Um equipamento só pode operar quando a temperatura estiver entre 10 °C e 40
°C, inclusive. O sistema deve detectar medições fora da faixa e emitir um aviso
quando a temperatura estiver abaixo ou acima dos limites.
• Operador original: not (temperatura < 10 or temperatura > 40)
• Operador equivalente: temperatura >= 10 and temperatura <= 40
• Tarefa: leia a temperatura e informe se o equipamento está em condição
operacional.
• Desafio adicional: apresente mensagens diferentes para temperatura
abaixo do mínimo, dentro da faixa e acima do máximo.
'''

# Solução 1: a temperatura está fora da faixa se ultrapassar qualquer limite.
temperatura = float(input("Digite a temperatura em graus Celsius: "))
operacional = not (temperatura < 10 or temperatura > 40)
print(f"Solução 1: equipamento em condição operacional? {operacional}")

# Solução 2: verifica explicitamente que a medição respeita ambos os limites.
operacional_equivalente = temperatura >= 10 and temperatura <= 40
print(f"Solução 2: equipamento em condição operacional? {operacional_equivalente}")

# Diferencia temperaturas abaixo, dentro e acima da faixa de operação.
if temperatura < 10:
    print("Aviso: temperatura abaixo do mínimo de 10 °C.")
elif temperatura > 40:
    print("Aviso: temperatura acima do máximo de 40 °C.")
else:
    print("Temperatura dentro da faixa de operação.")
