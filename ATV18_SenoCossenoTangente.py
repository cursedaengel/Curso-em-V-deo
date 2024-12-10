import math
angulo = int(input("Digite o valor do seu ângulo: "))
seno = math.sin(math.radians(angulo))
print ("O ângulo {} tem seno igual a {:.2f}".format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print ("O ângulo {} tem cosseno igual a {:.2f}".format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print ("O ângulo {} tem tangente igual a {:.2f}".format(angulo, tangente))

from math import radians, sin, cos, tan 
angulo = int(input("Digite o valor do seu ângulo: "))
seno = sin(radians(angulo))
print ("O ângulo {} tem seno igual a {:.2f}".format(angulo, seno))
cosseno = cos(radians(angulo))
print ("O ângulo {} tem cosseno igual a {:.2f}".format(angulo, cosseno))
tangente = tan(radians(angulo))
print ("O ângulo {} tem tangente igual a {:.2f}".format(angulo, tangente))
