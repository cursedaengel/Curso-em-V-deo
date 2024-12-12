cidade = input("Irei reconhecer se a sua cidade inicia com Santo ou não. Qual a sua cidade? ").upper()
if cidade[0:5] == "SANTO":
    print(True)
else:
    print(False)
