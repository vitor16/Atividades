'''
Uma equipe de desenvolvimento possui um orçamento inicial de R$ 2.500,00.
Durante o planejamento, recebe R$ 750,00 adicionais para adquirir equipamentos
e mais R$ 300,00 para materiais de consumo. O sistema precisa atualizar o
orçamento acumulado após cada acréscimo.
• Operador original: orcamento = orcamento + valor
• Operador equivalente: orcamento += valor
• Tarefa: inicie orcamento com 2500 e adicione os dois valores
separadamente.
• Desafio adicional: mostre o orçamento após cada operação e o aumento
total em relação ao valor inicial.
'''
from time import sleep

capital = 2500.00
equipamentos = 750.00
materiais = 300.00
print(f"temos R$ {capital} de orçamento inicial")
sleep(3)
capital += equipamentos
print(f"acrescentamos R$ {equipamentos} para os equipamentos, ficando com {capital}")
sleep(4)
print("Ah sim..")
capital = capital + materiais
sleep(1)
print(f"E pra fechar com chave de latão, acrescentaremos R$ 300 para materiais de consumo, ficando com {capital}")
sleep(3)
print("A relação ao valor inicial é de: ", capital - 2500)

