from servicos.entidades_servicos import *

def gerenciar_medicos():
    while True:
        try:
            print('\n --- Gerenciador de Médicos ---')
            print("[1] - Listar Médicos")
            print("[2] - Cadastrar Médico")
            print("[3] - Excluir Médico")
            print("[4] - Voltar ao Menu Principal")
            
            opcao = input("Digite a opção desejada: ")
            
            if opcao == "1":
                listar_medicos()
                input('Pressione Enter para voltar ao menu...')
            elif opcao == "2":
                cadastrar_medico()
            elif opcao == "3":
                excluir_medico()
            elif opcao == "4":
                break
            else:
                print("Opção inválida! Tente novamente.")
        except ValueError:
            print('Digite uma opção válida.')