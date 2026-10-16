'''
Uma escola recebeu 53 materiais para montar kits com quatro unidades cada. O
sistema precisa calcular quantos kits completos podem ser montados e quantos
materiais sobrarão.
• Operador original: quantidade = quantidade // divisor
• Operador equivalente: quantidade //= divisor
• Tarefa: utilize a divisão inteira para calcular os kits completos e o operador
% para calcular as sobras.
• Desafio adicional: confirme se a soma dos materiais utilizados nos kits
com as sobras corresponde ao total recebido.
'''
# Solucao 1: // calcula kits completos e % calcula os materiais restantes.
materiais = 53
kits = materiais // 4
sobras = materiais % 4
print(f"Solucao 1: {kits} kits completos e {sobras} materiais restantes.")
print(f"Conferencia: {kits} * 4 + {sobras} = {kits * 4 + sobras}.")

# Solucao 2: //= e %= atualizam as variaveis com os mesmos resultados.
quantidade_para_kits = materiais
quantidade_para_sobras = materiais
quantidade_para_kits //= 4
quantidade_para_sobras %= 4
print(
    f"Solucao 2: {quantidade_para_kits} kits completos e "
    f"{quantidade_para_sobras} materiais restantes."
)