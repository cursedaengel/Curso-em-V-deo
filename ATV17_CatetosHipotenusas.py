import math
cateto1 = float(input("Digite o valor do cateto oposto: "))
cateto2 = float(input("Digite o valor do cateto adjacente: "))
hipotenusa = math.hypot(cateto1, cateto2)
print ("O valor da hipotenusa é {:.2f}".format(hipotenusa))

from math import hypot
cateto1 = float(input("Digite o valor do cateto oposto: "))
cateto2 = float(input("Digite o valor do cateto adjacente: "))
hipotenusa = hypot(cateto1, cateto2)
print ("O valor da hipotenusa é {:.2f}".format(hipotenusa))
