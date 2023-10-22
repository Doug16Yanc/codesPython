import math
x1=int(input("Digite a abscissa do primeiro ponto:"))
y1=int(input("Digite a ordenada do primeiro ponto:"))
x2=int(input("Digite a abscissa do segundo ponto:"))
y2=int(input("Digite a ordenada do segundo ponto:"))

distância=math.sqrt((x2-x1)**2 + (y2-y1)**2)

if distância < 10:
   print("perto")
else:
    print("longe")