'''
Um sistema recebe o código informado pelo usuário e compara esse valor com o
código registrado no cadastro. Se os códigos forem iguais, deverá informar que o
registro foi localizado. Caso contrário, deverá indicar que os valores não
correspondem.
• Operador original: codigo1 == codigo2
• Operador equivalente: not (codigo1 != codigo2)
• Tarefa: leia dois códigos inteiros e verifique se são iguais.
• Desafio adicional: teste com códigos iguais e diferentes.
'''

# Solucao 1: compara diretamente os dois codigos com ==.
codigo1 = int(input("Digite o primeiro codigo: "))
codigo2 = int(input("Digite o segundo codigo: "))
iguais = codigo1 == codigo2
print(f"Solucao 1: os codigos sao iguais? {iguais}")

# Solucao 2: a negacao de 'diferentes' produz o mesmo resultado.
iguais_equivalente = not (codigo1 != codigo2)
print(f"Solucao 2: os codigos sao iguais? {iguais_equivalente}")

# Exemplos do desafio: um par igual e outro diferente.
for primeiro, segundo in [(123, 123), (123, 456)]:
    print(
        f"Teste ({primeiro}, {segundo}): "
        f"{primeiro == segundo} / {not (primeiro != segundo)}"
    )
