print("Digite uma sequência crescente de notas de alunos terminada por dez.")
nota=0
contadorA = 0
contadorRec = 0

for i in range(10):
    
    valor=float(input("Digite uma nota de um aluno:"))

    if valor >= 7:
        contadorA += 1
    else:
        if valor > 4:
            contadorRec += 1

print(f"O número de alunos aprovados é {contadorA}")
print(f"O número de alunos de recuperação é {contadorRec}")
print(f"O número de alunos de alunos aprovados é {10 - (contadorA + contadorRec)}")
  