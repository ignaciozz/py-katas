dados = {}
dados ["nome"] = input("Digite seu nome: ")

while True:
    try:
        dados["idade"] = int(input("Digite a sua idade: "))
        break
    except ValueError:
        print("Idade deve ser preenchida em formato numérico!")

print(dados["nome"])
print(dados["idade"])
