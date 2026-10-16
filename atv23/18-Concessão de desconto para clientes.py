'''
Uma loja concede desconto especial para clientes que sejam estudantes ou
idosos. Basta que uma das condições seja verdadeira para que o desconto seja
concedido.
• Operador original: or
• Operador equivalente lógico em outras linguagens: ||
• Tarefa: crie as variáveis estudante e idoso e determine se o cliente tem
direito ao desconto.

• Desafio adicional: teste situações em que nenhuma, apenas uma ou
ambas as condições sejam verdadeiras.
Compare expressões equivalentes válidas, como estudante or idoso e not (not
estudante and not idoso). O operador || não é válido em Python.
'''

# Solucao 1: basta que estudante ou idoso seja verdadeiro.
print("Solucao 1 | Solucao 2")
for estudante in (False, True):
    for idoso in (False, True):
        tem_desconto = estudante or idoso

        # Solucao 2: De Morgan nega o caso em que nenhuma condicao vale.
        tem_desconto_equivalente = not (not estudante and not idoso)
        print(
            f"Estudante={estudante}, idoso={idoso}: "
            f"{tem_desconto} | {tem_desconto_equivalente}"
        )
