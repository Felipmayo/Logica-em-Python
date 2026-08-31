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

