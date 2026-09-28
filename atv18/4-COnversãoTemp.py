'''Crie uma função chamada converter_temperatura() que receba uma temperatura
em Celsius.
Utilize a fórmula:
fahrenheit = (celsius * 9 / 5) + 32
A função deverá retornar a temperatura convertida.'''
#definir função para converter temperatura de celcius para fahrenheit
def converter_temperatura(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    print(fahrenheit)
#como celcius começa como uma variável vazia peço um valor
celsius = int(input("Digite a temperatura em Celsius: "))

#chamo a função diretamente 
converter_temperatura(celsius)