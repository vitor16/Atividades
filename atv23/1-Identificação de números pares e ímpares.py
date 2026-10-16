'''
Um sistema precisa identificar se três códigos inteiros são pares ou ímpares.
Um número é par quando o resto da divisão por 2 é zero.
• Solução 1: use o operador % para calcular o resto.
• Solução 2: use math.fmod para calcular o resto.
• Tarefa: leia três números e informe a classificação em cada solução.
• Desafio adicional: compare os resultados das duas formas.
'''

import math

# Lê três valores para testar as duas formas de calcular o resto.
for indice in range(1, 4):
    numero = int(input(f"Digite o {indice}º número inteiro: "))

    # Solução 1: o operador % retorna zero para números pares.
    resto_percentual = numero % 2
    classificacao_percentual = "par" if resto_percentual == 0 else "ímpar"

    # Solução 2: math.fmod calcula o resto da divisão como número real.
    resto_fmod = math.fmod(numero, 2)
    classificacao_fmod = "par" if resto_fmod == 0 else "ímpar"

    print(f"Solução 1 (%): {numero} é {classificacao_percentual}.")
    print(f"Solução 2 (math.fmod): {numero} é {classificacao_fmod}.")
