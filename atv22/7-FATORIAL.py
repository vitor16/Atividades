'''Contexto
Um sistema matemático precisa calcular o fatorial de um número.
O fatorial representa a multiplicação de um número por todos os números
positivos anteriores.
Por exemplo:
5! = 5 × 4 × 3 × 2 × 1
Portanto:
5! = 120
A ideia pode ser dividida em problemas menores:
5! = 5 × 4!
4! = 4 × 3!
3! = 3 × 2!
2! = 2 × 1!
A função deve continuar até chegar ao caso base.
Proposta
Crie uma função recursiva chamada fatorial() que receba um número e retorne
seu fatorial.

Teste
print(fatorial(5))
Resultado esperado
120
Outros testes
fatorial(3) → 6
fatorial(4) → 24
fatorial(6) → 720'''

# A função recursiva calcula o fatorial de um número.
# O caso base é quando n for 0 ou 1, porque 0! e 1! valem 1.
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    # Reduz o problema: n! = n * (n - 1)!
    return n * fatorial(n - 1)


# Pede ao usuário um número e mostra o fatorial dele.
numero = int(input("Digite um número: "))
print(f"O fatorial de {numero} é: {fatorial(numero)}")

