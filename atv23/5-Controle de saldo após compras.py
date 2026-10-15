'''
Uma carteira digital possui saldo inicial de R$ 500,00. O usuário realiza uma
compra de R$ 125,00 e outra de R$ 89,00. O programa deve descontar os valores e
apresentar o saldo restante após cada transação.
• Operador original: saldo = saldo - valor
• Operador equivalente: saldo -= valor
• Tarefa: inicie saldo com 500 e realize os dois descontos.

• Desafio adicional: verifique se o saldo restante seria suficiente para uma
terceira compra de R$ 200,00.
'''

from time import sleep

capital = 500.00
shopee = 125.00
meli = 89.00
print(f"temos R$ {capital} de saldo inicial")
sleep(3)
capital -= shopee
print(f"compra na shopee no valor de R$ {shopee}, ficando com {capital}")
sleep(4)
print("Ah sim..")
capital = capital - meli
sleep(1)
print(f"E ainda por cima você gastou no mercado livre, ficando com {capital}")
sleep(3)
print("Você gastou: ", 500 - capital)
sleep(2)
print("Espero que tenha valido a pena")
sleep(1)
if capital >= 200:
    print("Seu saldo é de ", capital," ou seja ainda tem dinheiro para uma compra de R$ 200")
    sleep(2)
    print("mas ficaria com R$ ", capital - 200)

