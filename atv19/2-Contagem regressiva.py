'''Um sistema está sendo utilizado para controlar o início de uma atividade.
Crie um programa que apresente uma contagem regressiva de 10 até 1 utilizando
um laço for.
Ao finalizar a contagem, apresente uma mensagem informando que a atividade foi
iniciada.'''

import time

for i in range(10, 0, -1):
    time.sleep(1)
    print(i)
print("contagem concluida! atividade foi iniciada.")