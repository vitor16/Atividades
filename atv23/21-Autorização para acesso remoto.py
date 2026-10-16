'''
Uma empresa permite que funcionários solicitem acesso remoto quando
estiverem em regime de plantão ou possuírem autorização especial. O programa
deverá analisar as duas possibilidades antes de liberar a solicitação.
• Operador original: plantao or autorizacao_especial
• Operador equivalente: not (not plantao and not autorizacao_especial)

• Tarefa: crie as variáveis plantao e autorizacao_especial e determine se o
acesso pode ser solicitado.
• Desafio adicional: teste as quatro combinações possíveis das duas
variáveis.
'''

# Solucao 1: plantao ou autorizacao especial permite solicitar o acesso.
print("Solucao 1 | Solucao 2")
for plantao in (False, True):
    for autorizacao_especial in (False, True):
        pode_solicitar = plantao or autorizacao_especial

        # Solucao 2: De Morgan equivale a negar que ambas as opcoes falhem.
        pode_solicitar_equivalente = not (
            not plantao and not autorizacao_especial
        )
        print(
            f"Plantao={plantao}, autorizacao especial={autorizacao_especial}: "
            f"{pode_solicitar} | {pode_solicitar_equivalente}"
        )
