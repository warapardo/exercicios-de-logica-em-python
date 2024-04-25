import math

valor_litro = 80.00
lata_tinta = 18
metros_quadrados = float(input("Quantos metros quadrados irão ser pintados? "))
cobertura = (metros_quadrados / 3)
qtd_latas_necessarias = math.ceil(cobertura / lata_tinta)
preco_total = qtd_latas_necessarias * valor_litro


print(f"Para essa cobertura que irá ser pintada você precisará de:\n"
      f"{qtd_latas_necessarias} de latas de tinta\n"
      f"e terá que pagar R${preco_total:.2f}")
