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

