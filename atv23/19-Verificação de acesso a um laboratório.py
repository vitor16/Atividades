'''
Um laboratório permite a entrada somente quando a sala não está bloqueada. O
sistema possui uma variável que informa se existe bloqueio e precisa verificar se o
acesso está liberado.
• Operador original: not
• Operador equivalente lógico em outras linguagens: !
• Tarefa: crie a variável sala_bloqueada e mostre se o acesso está liberado.
• Desafio adicional: teste os valores True e False.
Compare not sala_bloqueada com sala_bloqueada == False. O operador ! não é
válido em Python para essa finalidade.
'''

# Solucao 1: o acesso esta livre quando nao existe bloqueio.
print("Solucao 1 | Solucao 2")
for sala_bloqueada in (False, True):
    acesso_liberado = not sala_bloqueada

    # Solucao 2: verificar se o bloqueio e exatamente False e equivalente.
    acesso_equivalente = sala_bloqueada == False
    print(
        f"Sala bloqueada={sala_bloqueada}: "
        f"{acesso_liberado} | {acesso_equivalente}"
    )
