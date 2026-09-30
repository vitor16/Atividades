'''Um sistema possui uma senha de acesso.
O usuário deverá informar a senha até acertar.
Enquanto a senha estiver incorreta, o programa deverá solicitar uma nova
tentativa.
Utilize while para implementar essa situação.
Quando a senha estiver correta, apresente uma mensagem informando que o
acesso foi liberado.'''

senhaCorreta = "2077"
senhaV = "samurai"
senhaJohnny = "chippin"
senhaAdam = "smasher"
senhaSaburo = "arasaka"

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

senha = input("Digite sua senha de acesso(corp newbies: 2077): ")

while (
    senha != senhaV
    and senha != senhaJohnny
    and senha != senhaAdam
    and senha != senhaSaburo
    and senha != senhaCorreta
):
    print("❌ Senha incorreta.")
    senha = input("Digite a senha novamente: ")

print()

if senha == senhaCorreta:
    print("◈ ACESSO LIBERADO ◈")
    print("Bem-vindo, Operador Novato.")
    print("4651651 atividades em aberto.")
    print("Tempo estimado para término 72h e 48 minutos(excluindo idas ao banheiro e outras necessidades básicas)")

elif senha == senhaV:
    print("◈ ACESSO LIBERADO ◈")
    print("Bem-vindo, V.")
    print("Night City ainda tem trabalho para você, mercenário.")

elif senha == senhaJohnny:
    print("◈ ACESSO LIBERADO ◈")
    print("Bem-vindo, Johnny Silverhand.")
    print("Wake the fuck up, Samurai. Temos uma cidade para incendiar.")

elif senha == senhaAdam:
    print("◈ ACESSO LIBERADO ◈")
    print("Bem-vindo, Adam Smasher.")
    print("Unidade de combate reconhecida. Sistemas Arasaka liberados.")

elif senha == senhaSaburo:
    print("◈ ACESSO MÁXIMO LIBERADO ◈")
    print("Bem-vindo, Saburo Arasaka.")
    print("Todos os sistemas corporativos estão à sua disposição.")