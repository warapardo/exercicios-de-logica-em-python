
salario_hora = float(input("Quanto você ganha por cada hora trabalhada? "))

horas_mes = int(input("Quantas horas você trabalhou nesse mês? "))

salario_bruto = salario_hora * horas_mes

imposto_renda = salario_bruto * 0.11

inss = salario_bruto * 0.08

sindicato = salario_bruto * 0.05

salario_liquido = (((salario_bruto - imposto_renda) - inss) - sindicato)

print(f"+ Salario bruto: R${salario_bruto}\n"
      f"- IR (11%): R${imposto_renda}\n"
      f"- INSS (8%): R${inss}\n"
      f"- Sindicato (5%): R${sindicato}\n"
      f"= Salario líquido = R${salario_liquido}")
