lar=int(input("Digite a largura:"))
alt=int(input("Digite a altura:"))


row=1

while row<=alt:
     print("#",end="")
     column=2
     while column<lar:
          if row==1 or row==alt or column==lar:
               print("#",end="")
          else:
               print(end=" ")
          column=column+1
     print("#")
     row=row+1
