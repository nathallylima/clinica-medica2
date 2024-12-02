from .medicos import gerenciar_medicos
from. pacientes import gerenciar_pacientes
from. consultas import gerenciar_consultas

def menu():
    while True:
        try:
            print(f"\n--- GERENCIADOR CLÍNICA MÉDICA ---")
            print("[1] - Gerenciar Médicos")
            print("[2] - Gerenciar Pacientes")
            print("[3] - Gerenciar Consultas")
            print("[4] - Sair")

            opcao = input("Digite a opção desejada: ")
            
            if opcao == "1":
                gerenciar_medicos()
            elif opcao == "2":
                gerenciar_pacientes()
            elif opcao == "3":
                gerenciar_consultas()
            elif opcao == "4":
                print("Encerrando o programa...")
                exit()
            else:
                print("Opção inválida! Tente novamente.")
        except ValueError:
            print('Digite uma opção válida.')