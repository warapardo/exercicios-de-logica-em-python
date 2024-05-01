
num1 = float(input("Digite o primeiro número: "))

num2 = float(input("Digite o segundo número: "))

num3 = float(input("Digite o terceiro número: "))

if num1 > num2:
    if num2 > num3:
        print(f"O maior número é o {num1} e o menor é o {num3}")
    else:
        print(f"O maior número é o {num1} e o menor é o {num2}")
elif num2 > num3:
    if num3 > num1:
        print(f"O maior número é o {num2} e o menor é o {num1}")
    else:
        print(f"O maior número é o {num2} e o menor é o {num3}")

else:
    if num1 > num2:
        print(f"O maior número é o {num3} e o menor é o {num2}")
    else:
        print(f"O maior número é o {num3} e o menor é o {num1}")
