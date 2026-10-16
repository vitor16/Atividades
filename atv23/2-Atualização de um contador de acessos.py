'''
Um contador de acessos começa em zero e deve ser atualizado três vezes.
• Solução 1: use contador = contador + 1.
• Solução 2: use contador += 1.
• Tarefa: apresente o total após cada atualização e confira o total final.
'''

# Solução 1: soma 1 explicitamente ao contador em cada acesso.
contador = 0
for acesso in range(1, 4):
    contador = contador + 1
    print(f"Solução 1 - acesso {acesso}: {contador}")
print(f"Total da solução 1: {contador}")

# Solução 2: += soma 1 e atualiza o contador na mesma operação.
contador_abreviado = 0
for acesso in range(1, 4):
    contador_abreviado += 1
    print(f"Solução 2 - acesso {acesso}: {contador_abreviado}")
print(f"Total da solução 2: {contador_abreviado}")
