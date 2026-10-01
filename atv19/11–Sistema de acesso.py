'''Desenvolva um sistema que solicite:
Usuário:
Senha:
O sistema deverá permitir no máximo 3 tentativas de acesso.
Caso o usuário e a senha estejam corretos, apresente:
Acesso autorizado.
Caso sejam realizadas três tentativas incorretas, apresente:
Acesso bloqueado.
Utilize um laço de repetição para controlar as tentativas.'''
#definir variaveis
uSr = "default"
pSwrd = 1234
tEntativas = 0

while True:
    #loop sempre testa se tentativas ja sao 3
    if tEntativas == 3:

        print("====bloqueado====")
        exit()
    else:
        uSr = input("qual o nome de usuario?:")
        pSwrd = int(input("qual a senha: "))
    #confere se semha e usuario estao certos simultaneamente
    if uSr != "default" or pSwrd != 1234:
        print(f"usuario ou senha incorretos, { 2 - tEntativas} tentativas sobrando")
        tEntativas += 1
    else:
        break
        
print("acesso concedido, abretesesamo(ou algo do tipo)")