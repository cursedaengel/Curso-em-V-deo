frase = str(input("Digite a sua frase: ")).strip()
print ("A sua frase em maiúscula é: {}".format(frase.upper()))
print ("A sua frase em minúscula é: {}".format(frase.lower()))
#para contar sem os espaços - .strip() e depois -frase.count
print ("A sua frase têm {} letras".format(len(frase)-frase.count(" ")))
print ("Sua primeira frase têm {} letras".format(frase.find (" ")))
