import random
nome1 = str(input("Digite o nome da primeira pessoa: "))
nome2 = str(input("Digite o nome da segunda pessoa: "))
nome3 = str(input("Digite o nome da terceira pessoa: "))
nome4 = str(input("Digite o nome da quarta pessoa: "))
lista = [nome1, nome2, nome3, nome4]
escolhido = random.choice(lista)
print ("O escolhido foi {}".format (escolhido))

from random import choice
nome1 = str(input("Digite o nome da primeira pessoa: "))
nome2 = str(input("Digite o nome da segunda pessoa: "))
nome3 = str(input("Digite o nome da terceira pessoa: "))
nome4 = str(input("Digite o nome da quarta pessoa: "))
lista = [nome1, nome2, nome3, nome4]
escolhido = choice(lista)
print ("O escolhido foi {}".format (escolhido))
