'''
Um programa de inscrição permite a participação de pessoas com até 18 anos. O
sistema deverá verificar se a idade informada está dentro do limite estabelecido.
• Operador original: idade <= 18
• Operador equivalente: idade < 18 or idade == 18
• Tarefa: leia a idade e informe se a pessoa atende ao critério.
• Desafio adicional: teste uma idade abaixo do limite, uma igual ao limite e
outra acima dele.
'''

# Solucao 1: o limite de participacao inclui quem tem exatamente 18 anos.
idade = int(input("Digite a idade: "))
dentro_do_limite = idade <= 18
print(f"Solucao 1: atende ao criterio? {dentro_do_limite}")

# Solucao 2: <= equivale a ser menor que 18 ou igual a 18.
dentro_do_limite_equivalente = idade < 18 or idade == 18
print(f"Solucao 2: atende ao criterio? {dentro_do_limite_equivalente}")

# Testes abaixo, exatamente no limite e acima dele.
for idade_teste in (17, 18, 19):
    print(
        f"Idade {idade_teste}: "
        f"{idade_teste <= 18} / "
        f"{idade_teste < 18 or idade_teste == 18}"
    )
