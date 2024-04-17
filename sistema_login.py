def cadastro_usuario(usuarios):
    while True:
        email = input("Digite um email: ")
        if "gmail" in email or "@hotmail" in email:
            senha = input("Digite uma senha: ")
            if len(senha) >= 6:
                # criando uma biblioteca para armazenar todos os usuarios
                usuarios[email] = senha

                print("Cadastro feito com sucesso")
                print("-"*20)
                return email, senha
            else:
                print("Senha muito pequena, tente novamente. ")
        else:
            print("Digite um email válido")


def login(email_cadastro, senha_cadastro):
    while True:
        email_login = input("Digite seu email: ")
        senha_login = input("Digite sua senha: ")
        if email_login == email_cadastro and senha_login == senha_cadastro:
            print("Login feito com sucesso.")
            print("-"*20)
            return True
        else:
            print("Email ou senha inválidos, tente novamente")


def main():
    usuarios = {}
    while True:
        print("==== Sistema de Login ====")
        email, senha = cadastro_usuario(usuarios)
        if login(email, senha):
            print(usuarios)
            opcao = input("Deseja cadastrar outro usuário? (s/n): ")
            print("-"*20)
            if opcao.upper() != "S":
                break


if __name__ == "__main__"
main()
