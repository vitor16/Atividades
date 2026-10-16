'''
Uma plataforma de cursos libera uma avaliação quando o estudante está
matriculado e possui o cadastro ativo. Se qualquer uma dessas condições não for
atendida, o acesso deverá ser negado.
• Operador original: and
• Operador equivalente lógico em outras linguagens: &&
• Tarefa: crie as variáveis matriculado e cadastro_ativo e verifique se o
acesso pode ser liberado.
• Desafio adicional: teste as quatro combinações possíveis de valores
booleanos.
Para comparar as duas formas em Python, utilize and nas duas versões e altere a
organização da expressão, por exemplo, usando parênteses: matriculado and
cadastro_ativo e (matriculado) and (cadastro_ativo). O operador && não é válido
em Python.
'''

# Solucao 1: o acesso exige matricula e cadastro ativo ao mesmo tempo.
print("Solucao 1 | Solucao 2")
for matriculado in (False, True):
    for cadastro_ativo in (False, True):
        libera = matriculado and cadastro_ativo

        # Solucao 2: os parenteses deixam explicita a ordem sem alterar o and.
        libera_equivalente = (matriculado) and (cadastro_ativo)
        print(
            f"Matriculado={matriculado}, cadastro ativo={cadastro_ativo}: "
            f"{libera} | {libera_equivalente}"
        )
