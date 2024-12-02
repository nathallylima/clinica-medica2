import bcrypt
from config.db import criar_conexao

def criptografar(password):
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed

def checar_password(password, hashed):
    password_bytes = password.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hashed)

def inserir_usuario(email, password):
    try:
        conn = criar_conexao()
        cursor = conn.cursor()

        sql_verificar = "SELECT * FROM clinica.usuarios WHERE email = %s"
        cursor.execute(sql_verificar, [email])
        usuario_existente = cursor.fetchone()

        if usuario_existente:
            print("Este e-mail já está cadastrado!")
            return  

        hashed_password = criptografar(password).decode('utf-8')

        sql_inserir = "INSERT INTO clinica.usuarios (email, password) VALUES (%s, %s)"
        cursor.execute(sql_inserir, [email, hashed_password])
        conn.commit()
        print("Usuário criado com sucesso!")
    except Exception as e:
        print(f"Erro ao criar usuário: {e}")
    finally:
        conn.close()


def login(email, password):
    try:
        conn = criar_conexao()
        cursor = conn.cursor()

        sql = "SELECT * FROM clinica.usuarios WHERE email = %s"
        cursor.execute(sql, [email])
        usuario = cursor.fetchone()

        if usuario:
            hashed_password = usuario[2].encode('utf-8')  
            if checar_password(password, hashed_password):
                return usuario 
        return None  
    except Exception as e:
        print(f"Erro ao realizar login: {e}")
        return None
    finally:
        conn.close()

