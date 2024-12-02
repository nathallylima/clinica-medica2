import getpass
from servicos.usuario_servicos import inserir_usuario, login
from gerenciadores.menu import menu

while True:
    try:
        print("1 - Cadastrar Usuario  2 - Login")
        opcao = input("Digite a opcao desejada: ")

        if opcao == "1":
            email = input("Digite o email: ")
            password = input("Digite a senha: ")
            inserir_usuario(email, password)

        elif opcao == "2":
            email = input("Digite o email: ")
            password = getpass.getpass("Digite a senha: ")
            usuario_autenticado = login(email, password)
            if usuario_autenticado:
                menu()
            else:
                print("Usuário ou senha inválidos!")
        else:
            print("Opção inválida! Por favor, escolha 1 ou 2.")
    except ValueError:
        print('Digite uma opção válida.')
