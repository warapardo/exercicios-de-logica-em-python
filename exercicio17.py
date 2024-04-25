import math

metros_pintados = float(input("Quantos metros quadrados irão ser pintados? "))

galoes_maiores = math.ceil(metros_pintados / 108)
galoes_menores = math.ceil(metros_pintados / 21.6)

valor_galoes_maiores = galoes_maiores * 80
valor_galoes_menores = galoes_menores * 25

print(f"Se você comprar galões de 18l irá ter que comprar {galoes_maiores} e gastará R${valor_galoes_maiores}\n"
      f"Mas se comprar galões de 3,6l irá ter que comprar {galoes_menores} e gastará {valor_galoes_menores}")
