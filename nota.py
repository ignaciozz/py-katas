aluno = input("Digite seu nome: ")
print(f"Olá aluno {aluno}! Como vai?")

nota = float(input("Digite a sua nota: "))

if nota == 10:
    print(f"Incrível {aluno}, você é um gênio!")
elif nota >= 7:
    print(f"Parabéns {aluno}, você foi aprovado!")
else:
    print(f"Uma pena {aluno}, você está reprovado :(")
