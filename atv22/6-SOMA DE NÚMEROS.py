'''Contexto
Uma aplicação precisa calcular o total de uma sequência de números.
Por exemplo:
1 + 2 + 3 + 4 + 5
O resultado será:
15
A ideia é fazer com que a função resolva uma pequena parte do problema a cada
chamada.
Por exemplo:
5 + soma(4)
Depois:
4 + soma(3)
Até chegar ao caso base.
Proposta

Crie uma função recursiva chamada somar() que receba um número e retorne a
soma de 1 até esse número.
Teste
print(somar(5))
Resultado esperado
15
Outros testes
somar(3) → 6
somar(4) → 10
somar(10) → 55'''

# Função recursiva: soma todos os números de 1 até n.
# Caso base: quando n for 0, a soma é 0.
def somar(n):
    if n == 0:
        return 0
    # A função resolve uma parte do problema e chama a si mesma com n - 1.
    return n + somar(n - 1)


# Pede ao usuário um número e mostra a soma dos números de 1 até ele.
numero = int(input("Digite um número: "))
print(f"A soma de 1 até {numero} é: {somar(numero)}")

