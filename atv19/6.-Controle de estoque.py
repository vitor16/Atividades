'''Uma empresa precisa registrar a quantidade de produtos armazenados.
O sistema deverá solicitar ao usuário a quantidade disponível em estoque.
Enquanto a quantidade informada for menor ou igual a zero, o sistema deverá
solicitar novamente uma quantidade válida.
Utilize while para realizar essa validação.'''

#peço um valor para a quantidade
qUantidade=int(input("Digite a quantidade de produtos: "))
#enquanto for zero ou menor que zero pedira novamente
while qUantidade <= 0:
        print("====Tente novamente====")
        print()
        qUantidade=int(input("Digite a quantidade de produtos ( deve ser maior que zero (0) ) : "))
#quando a condicional do while for quebrada, exibe uma meensagem de sucesso
print(f"Registro completo, {qUantidade} produto(s)")