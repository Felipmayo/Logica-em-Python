print("BOLETIM DE NOTAS")

nome = input ("Nome: ")
curso = input ("Curso: ")
semestre = input ("Semestre: ")
disciplina = input ("Disciplina: ")
nota1 = float (input ("Nota 1: "))
nota2 = float (input ("Nota 2: "))

#MÉDIA

media = ((nota1 + nota2) / 2)

if media >= 60 and media <= 100:
    print ("APROVADO!")

elif media <= 20:
    print ("REPROVADO!")

if media >= 20 and media <= 60:
    print ("RECUPERAÇÃO!")

if media > 100:
    print ("ERRO DE LANÇAMENTO")

print ("NOME: ",nome)
print ("CURSO: ",curso)
print ("SEMESTRE: ",semestre)
print ("DISCIPLINA: ",disciplina)
print ("MÉDIA: ",media)