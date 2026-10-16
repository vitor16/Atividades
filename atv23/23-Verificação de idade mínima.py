'''
Um sistema exige idade mínima de 18 anos para permitir a criação de
determinado tipo de conta. O programa deverá identificar os usuários que ainda
não atingiram essa idade.
• Operador original: not (idade >= 18)
• Operador equivalente: idade < 18
• Tarefa: leia a idade e informe se o usuário está abaixo da idade mínima.
• Desafio adicional: teste as idades 16, 18 e 21.
'''

# Solucao 1: identifica quem ainda nao atingiu a idade minima.
idade = int(input("Digite a idade: "))
abaixo_da_idade_minima = not (idade >= 18)
print(f"Solucao 1: abaixo da idade minima? {abaixo_da_idade_minima}")

# Solucao 2: negar idade >= 18 equivale a idade < 18.
abaixo_equivalente = idade < 18
print(f"Solucao 2: abaixo da idade minima? {abaixo_equivalente}")

# Testes do desafio: menor de idade, idade minima e adulto.
for idade_teste in (16, 18, 21):
    print(
        f"Idade {idade_teste}: "
        f"{not (idade_teste >= 18)} | {idade_teste < 18}"
    )
