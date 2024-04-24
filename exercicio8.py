hora = int(input("Quanto você ganha por hora? "))

mes = float(input("Quantas horas você trabalhou este mês? "))

salario = float(hora * mes)

print(f"Você ganhou {salario:.2f} este mês, trabalhando {mes:.2f} horas, ganhando {hora} por hora")
