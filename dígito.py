número_inteiro=input("Digite um número inteiro:")
temp=float(número_inteiro)
unidade=(temp)%10
número=(temp-unidade)/10
dezena=(número)%10
print("O dígito das dezenas é", dezena)