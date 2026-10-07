'''Uma biblioteca possui uma pilha de livros sobre uma mesa.
Um novo livro é colocado sempre sobre o último livro que foi colocado. Quando
um livro precisa ser retirado, o livro que está no topo deve sair primeiro.

Estrutura que deve ser utilizada
Pilha
A pilha utiliza o princípio LIFO — Last In, First Out, em que o último elemento
inserido é o primeiro a ser retirado.
O que desenvolver
1. Criar uma pilha.
2. Adicionar cinco livros.
3. Retirar os livros utilizando pop().
4. Utilizar while até que a pilha fique vazia.
Resultado esperado
Se os livros forem adicionados nesta ordem:
Livro 1
Livro 2
Livro 3
Livro 4
Livro 5
A retirada deverá ocorrer assim:
Retirando: Livro 5
Retirando: Livro 4
Retirando: Livro 3
Retirando: Livro 2
Retirando: Livro 1'''

#define a lista
livros = []

livros.append("livro 1")
livros.append("livro 2")
livros.append("livro 3")
livros.append("livro 4")
livros.append("livro 5")

print("Livros:", livros)

retirado = livros.pop()

for i in range
print("livro retirado:", retirado)
print("pilha de livros após retirada:", livros)
