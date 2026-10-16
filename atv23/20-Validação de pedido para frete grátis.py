'''
Uma loja concede frete grátis para pedidos de pelo menos R$ 200,00 realizados
por clientes cadastrados. O programa deve verificar o valor do pedido e a situação
cadastral antes de conceder o benefício.
• Operador original: and
• Operador equivalente: not (not (valor_pedido >= 200) or not
cliente_cadastrado)
• Tarefa: leia o valor do pedido e a situação cadastral e verifique se as duas
condições são atendidas.
• Desafio adicional: teste um pedido acima do limite com cadastro inativo e
outro abaixo do limite com cadastro ativo.
'''

# Solucao 1: frete gratis requer valor suficiente e cadastro ativo.
valor_pedido = float(input("Digite o valor do pedido em reais: "))
resposta_cadastro = input("Cliente cadastrado? (s/n): ").strip().lower()
cliente_cadastrado = resposta_cadastro == "s"
frete_gratis = valor_pedido >= 200 and cliente_cadastrado
print(f"Solucao 1: frete gratis? {frete_gratis}")

# Solucao 2: nega o caso em que ao menos um requisito nao e atendido.
frete_gratis_equivalente = not (not (valor_pedido >= 200) or not cliente_cadastrado)
print(f"Solucao 2: frete gratis? {frete_gratis_equivalente}")

# Exemplos: acima do limite sem cadastro e abaixo do limite com cadastro.
for valor_teste, cadastrado_teste in ((250, False), (150, True)):
    print(
        f"Pedido R$ {valor_teste:.2f}, cadastrado={cadastrado_teste}: "
        f"{valor_teste >= 200 and cadastrado_teste} | "
        f"{not (not (valor_teste >= 200) or not cadastrado_teste)}"
    )
