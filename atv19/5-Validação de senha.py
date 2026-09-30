'''Um sistema possui uma senha de acesso.
O usuário deverá informar a senha até acertar.
Enquanto a senha estiver incorreta, o programa deverá solicitar uma nova
tentativa.
Utilize while para implementar essa situação.
Quando a senha estiver correta, apresente uma mensagem informando que o
acesso foi liberado.'''

#senhas inspiradas em cyberpunk 2077
senhaCorreta = "2077"
senhaV = "samurai"
senhaJohnny = "chippin"
senhaAdam = "smasher"
senhaSaburo = "arasaka"

#arte de ascii que achei na internet e usei muito tempo no meu terminal kitty
print("◈ Bem-vindo ao seu primeiro dia na ARASAKA CORP ◈")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀       ⣀⣤⣴⣶⡶⣶⣶⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀            ⢀⣴⡾⠛⠉⢠⣶⣿⣿⣶⣄⠉⠛⢿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀      ")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⠋⠀⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀⠀⠙⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⢣⣴⣶⣶⣦⡹⢿⣿⣿⡿⢏⣴⣶⣶⣦⡜⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡏⣿⣿⣿⣿⣿⣿⠀⣿⡿⠀⣿⣿⣿⣿⣿⣿⢸⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡇⠻⣿⣿⣿⣿⣿⡀⣽⣿⢀⣽⣿⣿⣿⣿⠟⢸⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⡀⠈⠉⠉⠉⠻⣿⣿⣿⣾⠟⠁⠉⠉⠁⠀⣾⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⡀⠀⠀⠀⠀⠈⣿⣿⠁⠀⠀⠀⠀⢀⣾⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣦⣄⠀⠀⠀⣽⣷⠀⠀⠀⣠⣴⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⢷⣶⣾⣷⣶⡶⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⣀⣀⡀⠀⠀⣀⣀⣀⣀⣀⣀⠀⠀⠀⣀⣀⣀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⣀⣀⡀⠀⢀⣀⡀⠀⢀⣀⣀⣀⣀⣀⡀⠀⠀")
print("⠀⠀⣴⣿⠟⠛⢿⣦⡀⣿⡟⠛⠛⠛⣿⣷⣰⣿⠟⠛⢿⣷⡄⢠⣠⣤⡻⠻⠗⠀⣴⣿⠟⠛⢿⣦⣸⣿⣧⣾⡿⢛⣿⡿⠟⠻⣿⣦⠀")
print("⠀⠀⣿⡇⠀⠀⠀⣿⡇⣿⣷⣄⡀⠀⠉⠁⣿⣇⠀⠀⠀⣿⡇⣀⡉⠻⢿⣶⣄⡰⣿⣇⠀⠀⠀⣿⡿⣿⣿⣅⡀⢸⣿⡀⠀⠀⢸⣿⠀")
print("⠀⠀⠙⠿⣷⣶⣦⣿⡇⠛⠋⠛⢿⣷⣤⡀⠙⠿⣷⣶⡦⣿⡇⢿⣷⣶⣶⣿⣿⣿⠙⠿⣷⣶⡆⣿⡟⠛⠋⠻⢿⣶⣿⣿⣷⣶⣼⣿⡁")

#peço o input do usuario para ter um valor em senha
senha = input("Digite sua senha de acesso(corp newbies: 2077): ")

#loop para que a senha seja alguma ja existente
#tratei o parêntesis como se fosse colchetes em css para ver se funciona

#funcionou
while (
    senha != senhaV
    and senha != senhaJohnny
    and senha != senhaAdam
    and senha != senhaSaburo
    and senha != senhaCorreta
):
    #caso a senha não seja uma das senhas existentes mostra codigo de erro
    print("❌ Senha incorreta.")
    senha = input("Digite a senha novamente: ")
#print vazio para dar espaço
print()
# se a senha for uma das existentes cada uma terá uma mensagem específica
if senha == senhaCorreta:
    print("◈ ACESSO LIBERADO ◈")
    print("Bem-vindo, Operador Novato.")
    print("4651651 atividades em aberto.")
    print("Tempo estimado para término 72h e 48 minutos(excluindo idas ao banheiro e outras necessidades básicas)")
    print()
    print()
    print()
elif senha == senhaV:
    print("◈ ACESSO LIBERADO ◈")
    print("Bem-vindo, V.")
    print("Night City ainda tem trabalho para você, mercenário.")
    print()
    print()
    print()
elif senha == senhaJohnny:
    print("◈ ACESSO LIBERADO ◈")
    print("Bem-vindo, Johnny Silverhand.")
    print("Wake the fuck up, Samurai. Temos uma cidade para incendiar.")
    print()
    print()
    print()
elif senha == senhaAdam:
    print("◈ ACESSO LIBERADO ◈")
    print("Bem-vindo, Adam Smasher.")
    print("Unidade de combate reconhecida. Sistemas Arasaka liberados.")
    print()
    print()
    print()

elif senha == senhaSaburo:
    print("◈ ACESSO MÁXIMO LIBERADO ◈")
    print("Bem-vindo, Saburo Arasaka.")
    print("Todos os sistemas corporativos estão à sua disposição.")
    print()
    print()
    print()