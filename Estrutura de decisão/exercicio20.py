
num = float(input("Escolha algum valor: "))

if num < 0:
    print(f"O valor {num:.2f} é negativo")
elif num > 0:
    print(f"O valor {num:.2f} é positivo")
else:
    print(f"O valor {num:.2f} é neutro")
