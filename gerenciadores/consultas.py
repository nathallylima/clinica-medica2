from servicos.entidades_servicos import *

def gerenciar_consultas():
    while True:
        try:
            print('\n --- Gerenciador de Consultas ---')
            print("[1] - Listar Consultas")
            print("[2] - Cadastrar Consulta")
            print("[3] - Atualizar Consulta")
            print("[4] - Excluir Consulta")
            print("[5] - Voltar ao Menu Principal")
            
            opcao = input("Digite a opção desejada: ")
            
            if opcao == "1":
                listar_consultas()
                input('Pressione Enter para voltar ao menu...')
            elif opcao == "2":
                cadastrar_consulta()
            elif opcao == "3":
                atualizar_consulta()
            elif opcao == "4":
                excluir_consulta()
            elif opcao == "5":
                break
            else:
                print("Opção inválida! Tente novamente.")
        except ValueError:
            print('Digite uma opção válida.')