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

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print ("Adição/Soma")

a = float (input ("Insira um número:"))

b = float (input ("Insira um número: "))

soma = a + b

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print ("Multiplicação")

a = float (input ("Insira um número: "))

b = float (input ("Insira um número: "))

multiplicação = a * b

print ("A multiplicação: ", multiplicação)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print ("Subtração")

a = float (input ("Insira um número: "))

b = float (input ("Insira um número: "))

subtração = a - b

print ("A subtração: ", subtração)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print ("Quem pode dirigir")

idade = int (input ("Insira sua idade: "))
habilitado = input ("Você tem uma habilitação? ")

if habilitado.lower() == "sim":
 habilitado = True
else:
  habilitado = False

if idade >= 18 and habilitado:
  print ("Pode dirigir!")
else:
  print ("Não pode dirigir")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print ("Quem pode votar?")

idade = int (input ("Insira sua idade: "))
titulo_eleitor = input ("Possui título de eleitor? ")

if titulo_eleitor.lower() == "sim":
    titulo_eleitor = True
else:
    titulo_eleitor = False

if idade >= 16 and titulo_eleitor:
    print ("Pode votar!")
else:
    print ("Não pode votar!")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print ("10% de desconto á vista")

pagamento = (input("Qual sua forma de pagamento? "))
valor = float(input("Insira o valor da compra: "))

if pagamento.lower() == "á vista":
 pagamento = True     
else:
 pagamento = False

if pagamento:
  print ("O valor com o desconto ficou:",valor - (valor * 0.10))
else:
  print ("O valor ficou:",valor)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("Bônus salarial")

salario = float(input("Insira o salario: "))
bonus = float(salario + (salario * 0.15))

if salario >= 2000:
  print("O salario com o bônus vale:", bonus)
else:
  print("O salario vale:", salario)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("INTERVALO")
intervalo = int(input("Insira um número: "))

if intervalo >= 10 and intervalo <= 50:
  print("Está dentro do intervalo")
else:
  print("Não está dentro do intervalo")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("CADASTRO")

cadastro = input("Cadastre a sua senha: ")
autenticacao = input("Faça o seu login: ")

if cadastro == autenticacao:
  print("Senha correta!")
else:
  print("Senha incorreta!")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("ENTRADA NO EVENTO")
idade = int(input("Insira a idade: "))
ingresso = input("Possui um ingresso: ")

if ingresso.lower() == "sim":
  ingresso = True
else:
  ingresso = False

if idade >= 18 and ingresso:
  print("Entrada permitida")
else:
  print("Entrada negada")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("<<CALCULADORA SIMPLES>>")
X = float(input("Digite o primeiro número: "))
Y = float(input("Digite o segundo número: "))
operacao = input("Digite o símbolo da operação desejada: ")

if operacao == "+":
  print(X,"+",Y,"=", X + Y)
elif operacao == "-":
  print(X,"-",Y,"=", X - Y)
elif operacao == "*":
  print(X,"*",Y,"=", X * Y)
elif operacao == "/":
  if X!= 0 and Y!= 0:
    print(X,"/",Y,"=", X / Y)
  else:
    print("A operação é inválida")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("<<PRÁTICA DE ESPORTES>>\n")
idade = int(input("Insira a idade: "))
autorizacao = input("Possui autorização para a prática? ")
if autorizacao.lower() == "sim":
  autorizacao = True
else:
  autorizacao = False
if idade >= 12 and idade <= 18 and autorizacao:
  print("Pode praicar")
else:
  print("Não pode praticar")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("---ESTÁ CHOVENDO---\n")
chovendo = input("Está chovendo?(sim/não) (yes?not)").lower()
if chovendo == "not" or chovendo == "não":
  print("Pode sair")
else:
  print("Não saia ou use seu guarda-chuva")

#professor:

print("---ESTÁ CHOVENDO---\n")
resposta = input("Está chovendo? (sim/não)(yes/not) ").lower()
chovendo = resposta 
if chovendo =="yes" or chovendo =="sim":
  print("Use guarda-chuva")
elif chovendo == resposta == "not" or "não":
  print("Saia tranquilo")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("DESCONTO PROGRESSIVO")
def main():
  compra = int(input("Insira o valor da compra: "))
  valorfinal = calculodesconto (compra)
  print("Valor total da compra: ",valorfinal)

def calculodesconto (compra):
  if compra >= 100 and compra < 300:
    return compra-(compra*0.10)
  elif compra >= 300 and compra < 500:
    return compra-(compra*0.15)
  elif compra >= 500:
    return compra-(compra*0.20)
  else:
    return compra
 
main()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("----TRIÂNGULO----")
lado_a = float(input("Insira o valor referente ao primeiro lado: "))
lado_b = float(input("Insira o valor referente ao segundo lado: "))
lado_c = float(input("Insira o valor referente ao terceiro lado: "))
if lado_a == lado_b and lado_a == lado_c:
  print("Triângulo equilátero")
elif (lado_a == lado_b and lado_a != lado_c) or (lado_a == lado_c and lado_a != lado_b) or (lado_b == lado_c and lado_b != lado_a):
  print("Triângulo isósceles")
else:
  print("Triângulo")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("---ESCOLHA DE PAGAMENTO---")

def main ():

  print("1 - Dinheiro")
  print("2 - Cartão de Crédito")
  print("3 - Cartão de Débito")
  print("4 - PIX")
  print("5 - Boleto")

  opcao = int (input ("Escolha a forma de pagamento: "))

  pagamento = escolhapagamento (opcao)

  print("Forma de pagamento escolhido: ",pagamento)

def escolhapagamento (opcao):

  match opcao:
    case 1:
      return "Dinheiro"
    case 2:
      return "Cartão de Crédito"
    case 3:
      return "Cartão de Débito"
    case 4:
      return "PIX"
    case 5:
      return "Boleto"
    case 6:
      return "Opção inválida"
  
main()
