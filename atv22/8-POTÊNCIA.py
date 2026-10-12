'''Contexto
Um sistema de cálculos precisa calcular uma potência.
Uma potência pode ser representada por multiplicações sucessivas.
Por exemplo:
23 = 2 × 2 × 2
Resultado:
8
O problema pode ser reduzido da seguinte forma:
23 = 2 × 22
22 = 2 × 21
21 = 2 × 20
Quando o expoente chega a 0, temos:
20 = 1
Proposta
Crie uma função recursiva chamada potencia() que receba a base e o expoente.
Não utilize:
**
nem:

pow()
Teste
print(potencia(2, 3))
Resultado esperado
8
Outros testes
potencia(5, 2) → 25
potencia(3, 3) → 27
potencia(10, 2) → 100'''

# Função recursiva para calcular a potência de uma base.
# Caso base: qualquer número elevado a 0 resulta em 1.
def potencia(base, expoente):
    if expoente == 0:
        return 1
    # Reduz o problema: base^expoente = base * base^(expoente - 1)
    return base * potencia(base, expoente - 1)


# Pede a base e o expoente ao usuário e mostra o resultado.
base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))
print(f"{base}^{expoente} = {potencia(base, expoente)}")

