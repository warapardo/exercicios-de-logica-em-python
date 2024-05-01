
num1 = float(input("Digite o primeiro número: "))

num2 = float(input("Digite o segundo número: "))

num3 = float(input("Digite o terceiro número: "))

if num1 > num2 and num1 > num3:
    print(f"O maior número entre os três é o {num1:.2f}")
elif num2 > num1 and num2 > num3:
    print(f"O maior número entre os três é o {num2:.2f}")
else:
    print(f"O maior número entre os três é o {num3:.2f}")