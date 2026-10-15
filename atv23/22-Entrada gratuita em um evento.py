'''
Um evento permite entrada gratuita para menores de 12 anos acompanhados de
um responsável ou para pessoas que possuem ingresso VIP. O sistema deve
combinar as condições corretamente para decidir se a entrada gratuita está
autorizada.
• Operador original: (idade < 12 and acompanhado) or ingresso_vip
• Operador equivalente: not (not (idade < 12 and acompanhado) and not
ingresso_vip)
• Tarefa: crie as variáveis idade, acompanhado e ingresso_vip e verifique se a
entrada está autorizada.
• Desafio adicional: teste uma criança acompanhada sem ingresso VIP, uma
pessoa sem acompanhante com ingresso VIP e outra que não atende a
nenhuma condição.
'''
