import math

a=float(input("Digite o valor de a:"))
b=float(input("Digite o valor de b:"))
c=float(input("Digite o valor de c:"))

delta=(b**2)-4*a*c
if delta < 0:
   print("Esta equação não possui raízes reais")
if delta == 0:
   X= (-b + math.sqrt(delta))/2*a
   Y= (-b - math.sqrt(delta))/2*a
   print("A raíz desta equação é", X)

if delta > 0:
   X= (-b + math.sqrt(delta))/2*a
   Y= (-b - math.sqrt(delta))/2*a
   if X>Y:
      print("As raízes desta equação são", Y, "e", X)
   else:
      print("As raízes desta equação", X, "e", Y)


   
