'''Contexto
Um sistema de análise matemática precisa gerar valores da Sequência de
Fibonacci.
Na sequência de Fibonacci, cada número é obtido pela soma dos dois números
anteriores.
Observe:
0 1 1 2 3 5 8 13 21
Veja como os valores são formados:
0 + 1 = 1
1 + 1 = 2
1 + 2 = 3
2 + 3 = 5
3 + 5 = 8
5 + 8 = 13
A regra pode ser representada por:
F(n) = F(n - 1) + F(n - 2)
Os dois primeiros valores são os casos base:
F(0) = 0

F(1) = 1
Por exemplo:
F(5) = 5
porque:
F(5) = F(4) + F(3)
F(4) = F(3) + F(2)
F(3) = F(2) + F(1)
Até chegar aos casos base.
Proposta
Crie uma função recursiva chamada fibonacci() que receba uma posição e retorne
o valor correspondente da sequência.
Teste
print(fibonacci(5))
Resultado esperado
5
Outros testes
fibonacci(0) → 0
fibonacci(1) → 1
fibonacci(6) → 8
fibonacci(7) → 13'''

