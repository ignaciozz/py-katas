frutas = []

entrada = input("Digite uma fruta à sua lista: ")
frutas.append(entrada)

while True:
    lista = input("Digite uma fruta à sua lista ou digite 'Ver lista' para ver como sua lista está: ")

    if lista.lower() == "ver lista":
        print(frutas)
        break
    else:
        frutas.append(lista)
