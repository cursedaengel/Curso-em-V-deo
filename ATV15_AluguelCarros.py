# o carro custa 60 por dia e 0,15 por km
dias = int(input("Por quantos dias o carro foi alugado? "))
km = float(input("Quantos km foram rodados? "))
valor = (dias*60)+(km*0.15)
print ("O valor a ser pago por {} dias alugado é {:.2f}".format(dias, valor))
