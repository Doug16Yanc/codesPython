notas = False
r = a = af = 0
while (not notas):
     n= float(input("Digite um número, ou o zero para terminar:"))
     if n == 0:
        notas = True
     else: 
       if n <= 3.0:
         r = r + 1
       else:
          a = a + 1
          if n >= 3.1 and n <= 4.9:
            af = af + 1
ap = a - af
print("A quantidade de alunos reprovados foi igual a", r)
print("A quantidade de alunos que não reprovados foi igual a", a)
print("A quantidade de alunos convocados para avaliação final foi igual a", af)
print("A quantidade de alunos aprovados automaticamente foi igual a", ap)
