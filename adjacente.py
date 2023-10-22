n=int(input("Digite um número:"))
adjacente=False
i=0

while n>0:
    fir=n%10
    n=n//10
    i=n%10
    if fir==i:
        adjacente=True
if adjacente:
  print("sim")
else:
  print("não")
    
    


