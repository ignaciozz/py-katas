senha = "Senha123!"

while True:
    tentativa_senha = input("Digite sua senha: ")
    if tentativa_senha == senha:
        print("Acesso permitido.")
        break
    else:
        print("Acesso negado. Tente novamente.")
        