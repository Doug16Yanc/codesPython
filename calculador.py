#Programa em Python a fim de que se faça cálculos aritméticos com a utilização de um programa computacional.

print("Digite três dígitos diferentes e farei os cálculos relativos.")
a=int(input("Digite o primeiro inteiro:"))
b=int(input("Digite o segundo inteiro:"))
c=int(input("Digite o terceiro inteiro:"))

if(a==b or a==c or b==c or a==b==c):
   print("Identifiquei pelo menos dois números iguais, por favor, atente-se à primeira regra.")
else:
    soma = (a+b+c)
    média = (a+b+c)/3
    produto = a*b*c
    
    print("A soma é", soma)
    print("A média aritmética entre eles é", média)
    print("O produto é", produto)
