import math
x = 1
while x >= 0:
    x = int(input("Digite um número:"))
    fatorial = 1
    while x > 1:
        fatorial = fatorial * x
        x = x - 1
    print (fatorial)
