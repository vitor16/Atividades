'''Um sistema está sendo utilizado para controlar o início de uma atividade.
Crie um programa que apresente uma contagem regressiva de 10 até 1 utilizando
um laço for.
Ao finalizar a contagem, apresente uma mensagem informando que a atividade foi
iniciada.'''

#chamo a função time
import time

#loop de for, de 10 a 0 com intervalos de -1
for i in range(10, 0 , -1):
    #a cada 1 segundo o programa dorme temporariamente e depois imprime i
    time.sleep(1)
    # para simular uma contagem real
    print(i)
print("contagem concluida! atividade foi iniciada.")