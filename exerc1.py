habilitado = str(input("Você tem uma habilitação? "))
if (habilitado == "sim"):
    print("Você pode dirigir")
elif (habilitado == "não"):
    print("Você não pode dirigir")
else:
    print("erro, responda com sim ou não")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

pagamento = str(input("Qual sua forma de pagamento? "))
valor = float
desconto = float
valor = 1000

if(pagamento == "a vista"):
    print("O valor com o desconto ficou:",valor - (valor * 0.1),"reais")
else:
    print("O valor ficou:", valor,"reais")
