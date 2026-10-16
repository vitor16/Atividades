'''
Uma plataforma educacional aceita notas entre 5 e 10, incluindo os extremos,
para determinada classificação. O programa deverá verificar se a nota informada
está dentro dessa faixa.
• Operador original: nota >= 5 and nota <= 10
• Operador equivalente: 5 <= nota <= 10

• Tarefa: leia a nota e informe se ela pertence ao intervalo permitido.
• Desafio adicional: teste valores abaixo de 5, entre 5 e 10 e acima de 10.
'''

# Solução 1: compara a nota separadamente com os limites inclusivos.
nota = float(input("Digite a nota: "))
nota_valida = nota >= 5 and nota <= 10
print(f"Solução 1: nota dentro da faixa? {nota_valida}")

# Solução 2: a comparação encadeada verifica os mesmos dois limites.
nota_equivalente = 5 <= nota <= 10
print(f"Solução 2: nota dentro da faixa? {nota_equivalente}")

# Testa um valor abaixo, um dentro e outro acima do intervalo.
for nota_teste in (4, 7.5, 10.5):
    print(
        f"Nota {nota_teste}: "
        f"{nota_teste >= 5 and nota_teste <= 10} | "
        f"{5 <= nota_teste <= 10}"
    )
