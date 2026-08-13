programa {
  funcao inicio() {
  
  escreva("BOLETIM DE NOTAS")

   cadeia nome
   cadeia curso
   cadeia semestre
   cadeia disciplina
   real nota1
   real nota2
   real media

    escreva("\nNome: ")
    leia (nome)

    escreva("\nCurso: ")
    leia(curso)

    escreva("\nSemestre: ")
    leia(semestre)

    escreva("\nDisciplina: ")
    leia(disciplina)

    escreva("\nPrimeira nota: ")
    leia(nota1)

    escreva("\nSegunda nota: ")
    leia(nota2)

   media = ((nota1 + nota2) / 2)

  escreva("\nNome: ",nome)
  escreva("\nCurso: ",curso)
  escreva("\nSemestre: ",semestre)
  escreva("\nDisciplina: ",disciplina)
  escreva("\n média é: ",media)

    se (media >= 60)
    {
      escreva("\nAPROVADO!")
    }
    senao se (media >= 40 e media < 60)
    {
         escreva("\nEXAME!")
    }
    senao se (media > 100)
    {
      escreva("nota invalida")
    }
    senao
    {
     escreva("\nREPROVADO!")
    } 
    }
  } 
}