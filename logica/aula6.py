usuarios = {
    "admin": "Admin123",
    "joao": "Joao2024"
}

def senha_valida(senha):
    tem_maiuscula = any(c.isupper() for c in senha)
    tem_numero = any(c.isdigit() for c in senha)
    tamanho_ok = len(senha) >= 8
    return tem_maiuscula and tem_numero and tamanho_ok

def fazer_login():
    tentativas = 3

    while tentativas > 0:
        usuario = input("Usuário: ")
        senha = input("Senha: ")

        if usuario in usuarios and usuarios[usuario] == senha:
            print(f"Bem-vindo(a), {usuario}!")
            return
        else:
            tentativas -= 1
            print(f"Login inválido. Tentativas restantes: {tentativas}")

    print("Número de tentativas excedido. Acesso bloqueado.")

def cadastrar_usuario():
    novo_usuario = input("Novo nome de usuário: ")

    if novo_usuario in usuarios:
            print("Usuário já existe.")
            return

    nova_senha = input("Nova senha: ")

    if senha_valida(nova_senha):
        usuarios[novo_usuario] = nova_senha
        print("Usuário cadastrado com sucesso!")
    else:
        print("Senha inválida. Use ao menos 8 caracteres, uma letra maiúscula e um número.")

while True:
    print("\n=== MENU ===")
    print("1 - Login")
    print("2 - Cadastrar novo usuário")
    print("3 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        fazer_login()
    elif opcao == "2":
        cadastrar_usuario()
    elif opcao == "3":
        print("Encerrando o sistema.")
        break
    else:
        print("Opção inválida.")
