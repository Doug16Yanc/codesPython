jogo=0
def computador_escolhe_jogada(n, m):
   if n <= m:
     return n
   else: 
      numero = n % (m+1)
      if numero > 0:
         return numero
      else:
         return m
def usuario_escolhe_jogada(n, m):
    jogada = 0
    while jogada == 0:
        jogada=int(input("Quantas peças você vai tirar?"))
        if jogada > n or jogada < 1 or jogada > m:
          print("Oops! Jogada Inválida! Tente de novo.")
          jogada = 0
    return jogada

def partida():
   n = int(input("Quantas peças?"))
   m = int(input("Limite de peças por jogada?"))
   
   time_computer = False 
   print("O computador começa!")
   if n % (m+1) != 0:
      time_computer = True
   else:
      print("Você começa!")

   while n > 0:
      if time_computer:
          jogada = computador_escolhe_jogada(n, m)
          time_computer = False
          print("Computador tirou {} peças.".format(jogada))
      else:
          jogada = usuario_escolhe_jogada(n, m)
          time_computer = True
          print("Você tirou {} peças.".format(jogada))
      n= n - jogada 
      print("Agora restam {} peças no tabuleiro.\n".format(n))
   if time_computer:
     print("Você ganhou!")
     return 1
   else:
     print("Fim de jogo! O computador ganhou!")
     return 0
          
def campeonato():
   usuario = 0
   computador = 0
   for _ in range(3):
      vencedor = partida()
      if vencedor == 1:
        usuario = usuario + 1
      else:
        computador = computador + 1
        print("Final do campeonato!")
        print("Placar: Você {} x {} Computador".format(usuario, computador))

while jogo == 0:
   print("Bem vindo ao jogo do NIM! Escolha:")
   print(" ")
   print("1 - para jogar uma partida.")
   print("2 - para jogar um campeonato.")


   jogo = int(input("Sua opção:"))
   print(" ")

   if jogo == 1:
      partida()
      break
   if jogo == 2:
      campeonato()
      break
   else:
      print("Opção inválida!")
      jogo = 0
      
