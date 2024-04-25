
peso_peixes = float(input("Quantos quilos de peixe você pescou hoje? "))

excesso = peso_peixes - 50

multa = float(excesso * 4)

print(f"O excesso de pesca hoje foi de {excesso:.2f}kg e você terá que pagar R${multa:.2f} de multa")