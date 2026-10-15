'''
Um depósito precisa organizar 47 peças em caixas com seis unidades. O sistema
deverá informar quantas caixas completas podem ser preenchidas e quantas
peças permanecerão fora das caixas completas.
• Operador original: resto = numero % divisor
• Operador equivalente: resto = numero seguido de resto %= divisor
• Tarefa: calcule o resto da divisão de 47 por 6 e determine a quantidade de
caixas completas.
• Desafio adicional: apresente os dois resultados em uma única mensagem.
'''
pecas=pecas2=47
caixas = pecas // 6
print("Com ",pecas," peças é possível fazer ",caixas," caixas")
enter = input("Aperte ENTER para continuar para o método 2(resto %= numero)")



print("Com", materiais," Materiais é possível fazer ",kits," kits")
print("desafio:")
print("com esses materiais somados temos: ",kits*4," e sobra ",materiais2-kits*4,"pois é necessário 4 por kit")