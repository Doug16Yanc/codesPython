primo = True
n=int(input("Digite um número inteiro:"))

divisor = 2

while divisor < n and primo:
  if n % divisor == 0:
    primo = False
  divisor += 1

if primo and n != 1:
  print("primo")
else:
  print("não primo")
      
