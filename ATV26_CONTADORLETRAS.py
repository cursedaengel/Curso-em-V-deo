frase = input("Vou contar quantas vezes a letra A apareceu na frase. Digite uma frase: ").upper()
contador = 0
for name in frase:
    if name == "A":
        contador += 1
print("***************ANALISANDO...")
print ("A letra A apareceu {} vezes. Sua primeira aparição foi na posição {} e a última na posição {}".format(contador, frase.find("A") +1, frase.rfind("A") + 1))
