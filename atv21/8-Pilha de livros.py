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
livros = ["livro 1","livro 2","livro 3","livro 4","livro 5"]

#mostra lista de livros

print("Livros:", livros)

# loop de for para esvaziar a lista
for i in livros:

    if not livros:
        print("Lista Vazia")
        exit()
    while len(livros) > 0:
        retirado = livros.pop(0)
        print("livro retirado:", retirado)
        print("pilha de livros após retirada:", livros)

    if not livros:
        print("Lista Vazia")
        exit()



