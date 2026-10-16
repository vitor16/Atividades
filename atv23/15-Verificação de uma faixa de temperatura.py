'''
Um equipamento industrial opera entre 10 °C e 40 °C, incluindo os extremos. O
sistema recebe uma medição e precisa indicar se a temperatura está dentro da
faixa permitida.
• Operador original: not (temperatura < 10 or temperatura > 40)
• Operador equivalente: temperatura >= 10 and temperatura <= 40
• Tarefa: leia a temperatura e informe se ela está dentro dos limites
operacionais.
• Desafio adicional: diferencie as situações de temperatura abaixo, dentro e
acima da faixa.
'''

# Solucao 1: a temperatura nao pode estar abaixo de 10 nem acima de 40.
temperatura = float(input("Digite a temperatura em graus Celsius: "))
dentro_da_faixa = not (temperatura < 10 or temperatura > 40)
print(f"Solucao 1: dentro da faixa? {dentro_da_faixa}")

# Solucao 2: compara explicitamente com os dois limites, que sao inclusivos.
dentro_da_faixa_equivalente = temperatura >= 10 and temperatura <= 40
print(f"Solucao 2: dentro da faixa? {dentro_da_faixa_equivalente}")
if temperatura < 10:
    print("Temperatura abaixo da faixa permitida.")
elif temperatura > 40:
    print("Temperatura acima da faixa permitida.")
else:
    print("Temperatura dentro da faixa permitida.")
