from servicos.entidades_servicos import *

def gerenciar_pacientes():
    while True:
        try:
            print('\n --- Gerenciador de Pacientes ---')
            print("[1] - Listar Pacientes")
            print("[2] - Cadastrar Paciente")
            print("[3] - Excluir Paciente")
            print("[4] - Voltar ao Menu Principal")
            
            opcao = input("Digite a opção desejada: ")
            
            if opcao == "1":
                listar_pacientes()
                input('Pressione Enter para voltar ao menu...')
            elif opcao == "2":
                cadastrar_paciente()
            elif opcao == "3":
                excluir_paciente()
            elif opcao == "4":
                break
            else:
                print("Opção inválida! Tente novamente.")
        except ValueError:
            print('Digite uma opção válida.')