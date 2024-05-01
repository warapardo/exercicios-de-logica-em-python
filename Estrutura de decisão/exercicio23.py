
nota1 = float(input("Digite a primeira nota do aluno: "))

nota2 = float(input("Digite a segunda nota do aluno: "))

media = (nota1 + nota2) / 2

if 7 <= media <= 9.9:
    print("Aprovado")
elif media == 10:
    print("Aprovado com Distinção")
else:
    print("Reprovado")
