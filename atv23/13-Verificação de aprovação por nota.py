'''
Uma instituição considera aprovado o estudante que obtiver nota igual ou
superior a 7. O programa deverá receber a nota e informar se o estudante foi
aprovado ou se precisará realizar recuperação.
• Operador original: nota >= 7
• Operador equivalente: nota > 7 or nota == 7
• Tarefa: leia uma nota e verifique se atende ao critério de aprovação.
• Desafio adicional: teste as notas 6.9, 7 e 8.5.
'''

# Solucao 1: nota igual ou maior que 7 garante a aprovacao.
nota = float(input("Digite a nota do estudante: "))
aprovado = nota >= 7
print(f"Solucao 1: aprovado? {aprovado}")

# Solucao 2: >= equivale a ser maior que 7 ou exatamente igual a 7.
aprovado_equivalente = nota > 7 or nota == 7
print(f"Solucao 2: aprovado? {aprovado_equivalente}")

# Casos de teste pedidos no desafio, incluindo a nota-limite.
for nota_teste in (6.9, 7, 8.5):
    print(
        f"Nota {nota_teste}: "
        f"{nota_teste >= 7} / {nota_teste > 7 or nota_teste == 7}"
    )
