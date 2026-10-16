'''
Um técnico precisa calcular a área de dois terrenos quadrados, um com lado de 8
metros e outro com lado de 12 metros. A área de cada terreno corresponde ao
lado elevado ao quadrado. Ao final, o programa deverá apresentar a área total dos
terrenos.
• Operador original: area = lado ** 2
• Operador equivalente: area **= 2, após atribuir o valor do lado à variável
area
• Tarefa: calcule as duas áreas e some os resultados.
• Desafio adicional: apresente a área individual de cada terreno e a área total
em metros quadrados.
'''

# Solucao 1: calcula a area usando a potencia em uma expressao.
lado_a = 8
lado_b = 12
area_a = lado_a ** 2
area_b = lado_b ** 2
print(f"Solucao 1: terreno 1 = {area_a} m²; terreno 2 = {area_b} m².")
print(f"Area total: {area_a + area_b} m².")

# Solucao 2: **= eleva a variavel ao quadrado e guarda o resultado nela.
area_a_abreviada = lado_a
area_b_abreviada = lado_b
area_a_abreviada **= 2
area_b_abreviada **= 2
print(
    f"Solucao 2: terreno 1 = {area_a_abreviada} m²; "
    f"terreno 2 = {area_b_abreviada} m²."
)
print(f"Area total: {area_a_abreviada + area_b_abreviada} m².")
