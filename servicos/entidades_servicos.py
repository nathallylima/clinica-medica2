from config.db import criar_conexao
from datetime import datetime


def listar_medicos():
    conn = criar_conexao()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM clinica.medicos ORDER BY nome ASC")
        registros = cursor.fetchall()
        if not registros:
            print("Não há médicos cadastrados.")
        else:
            for medico in registros:
                print(f"ID: {medico[0]}, Nome: {medico[1]}, CRM: {medico[2]}, Telefone: {medico[3]}")
    except Exception as e:
        print(f"Erro ao listar médicos: {e}")
    finally:
        conn.close()


def cadastrar_medico():
    nome = input("Digite o nome do médico: ")
    crm = input("Digite o CRM do médico: ")
    telefone = input("Digite o telefone do médico: ")

    conn = criar_conexao()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO clinica.medicos (nome, crm, telefone)  VALUES (%s, %s, %s)", (nome, crm, telefone))
        conn.commit()
        print("Médico cadastrado com sucesso!")
    except Exception as e:
        print(f"Erro ao cadastrar médico: {e}")
    finally:
        conn.close()


def excluir_medico():
    listar_medicos()
    id_medico = input("Digite o ID do médico a ser excluído: ")
    
    conn = criar_conexao()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM clinica.medicos WHERE id = %s", (id_medico,))
        conn.commit()
        print("Médico excluído com sucesso!")
    except Exception as e:
        print(f"Erro ao excluir médico: {e}")
    finally:
        conn.close()


def listar_pacientes():
    conn = criar_conexao()
    cursor = conn.cursor()
    try:
        nome_busca = input("Digite o nome (ou parte do nome) do paciente para pesquisar: ").strip()
        if nome_busca: 
            cursor.execute("SELECT * FROM clinica.pacientes WHERE nome LIKE %s ORDER BY nome ASC", ('%' + nome_busca + '%',))
        else:
            cursor.execute("SELECT * FROM clinica.pacientes ORDER BY nome ASC")

        registros = cursor.fetchall()
        if not registros:
            print("Não há pacientes cadastrados com esse nome.")
        else:
            for paciente in registros:
                print(f"ID: {paciente[0]}, Nome: {paciente[1]}, Idade: {paciente[3]}, Telefone: {paciente[2]}")
    except Exception as e:
        print(f"Erro ao listar pacientes: {e}")
    finally:
        conn.close()


def cadastrar_paciente():
    nome = input("Digite o nome do paciente: ")
    idade = input("Digite a idade do paciente: ")
    telefone = input("Digite o telefone do paciente: ")
    endereco = input("Digite o endereço do paciente: ")

    conn = criar_conexao()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO clinica.pacientes (nome, telefone, idade, endereco) VALUES (%s, %s, %s, %s)", (nome, telefone, idade, endereco))
        conn.commit()
        print("Paciente cadastrado com sucesso!")
    except Exception as e:
        print(f"Erro ao cadastrar paciente: {e}")
    finally:
        conn.close()


def excluir_paciente():
    listar_pacientes()
    id_paciente = input("Digite o ID do paciente a ser excluído: ")
    conn = criar_conexao()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM clinica.pacientes WHERE id = %s", (id_paciente,))
        conn.commit()
        print("Paciente excluído com sucesso!")
    except Exception as e:
        print(f"Erro ao excluir paciente: {e}")
    finally:
        conn.close()


def listar_consultas():
    conn = criar_conexao()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT consultas.id, medicos.nome AS medico, pacientes.nome AS paciente, consultas.tipo, consultas.data 
            FROM clinica.consultas
            INNER JOIN clinica.medicos ON consultas.id_medico = medicos.id
            INNER JOIN clinica.pacientes ON consultas.id_paciente = pacientes.id
            ORDER BY consultas.data DESC
        """)
        registros = cursor.fetchall()
        if not registros:
            print("Não há consultas cadastradas.")
        else:
            for consulta in registros:
                print(f"Consulta ID: {consulta[0]}, Médico: {consulta[1]}, Paciente: {consulta[2]}, Tipo: {consulta[3]}, Data: {consulta[4]}")
    except Exception as e:
        print(f"Erro ao listar consultas: {e}")
    finally:
        conn.close()

def cadastrar_consulta():
    while True:
        try:
            id_medico = input("Digite o ID do médico: ")
            id_paciente = input("Digite o ID do paciente: ")
            tipo = input("Digite o tipo da consulta: ")

            while True:
                data = input("Digite a data da consulta (YYYY-MM-DD): ")
                try:
                    datetime.strptime(data, "%Y-%m-%d")
                    break
                except ValueError:
                    print("A data deve estar no formato YYYY-MM-DD. Tente novamente.")

            while True:
                horario = input("Digite o horário da consulta (HH:MM): ")
                try:
                    datetime.strptime(horario, "%H:%M")
                    break
                except ValueError:
                    print("O horário deve estar no formato HH:MM. Tente novamente.")

            conn = criar_conexao()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO clinica.consultas (id_medico, id_paciente, tipo, data, horario) VALUES (%s, %s, %s, %s, %s)", (id_medico, id_paciente, tipo, data, horario))
            conn.commit()
            print("Consulta cadastrada com sucesso!")
            break 

        except Exception as e:
            print(f"Erro ao cadastrar consulta: {e}")
            return
        finally:
            conn.close()


def atualizar_consulta():
    listar_consultas()

    id_consulta = input("Digite o ID da consulta a ser atualizada: ")
    novo_tipo = input("Digite o novo tipo da consulta: ")
    nova_data = input("Digite a nova data da consulta (YYYY-MM-DD): ")
    novo_horario = input("Digite o novo horário da consulta (HH:MM): ")

    conn = criar_conexao()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE clinica.consultas SET tipo = %s, data = %s, horario = %s WHERE id = %s", (novo_tipo, nova_data, novo_horario, id_consulta))
        conn.commit()
        print("Consulta atualizada com sucesso!")
    except Exception as e:
        print(f"Erro ao atualizar consulta: {e}")
    finally:
        conn.close()

def excluir_consulta():
    listar_consultas()

    id_consulta = input("Digite o ID da consulta a ser excluída: ")
    conn = criar_conexao()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM clinica.consultas WHERE id = %s", (id_consulta,))
        conn.commit()
        print("Consulta excluída com sucesso!")
    except Exception as e:
        print(f"Erro ao excluir consulta: {e}")
    finally:
        conn.close()
