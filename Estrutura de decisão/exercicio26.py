
produto1 = float(input("Digite o valor do primeiro produto: "))

produto2 = float(input("Digite o valor do segundo produto: "))

produto3 = float(input("Digite o valor do terceiro produto: "))

if produto1 < produto2 and produto1 < produto3:
    print(f"O produto mais barato é o primeiro e custa R${produto1:.2f}")
elif produto2 < produto1 and produto2 < produto3:
    print(f"O produto mais barato é o segundo e custa R${produto2:.2f}")
else:
    print(f"O produto mais barato é o terceiro e custa R${produto3:.2f}")
