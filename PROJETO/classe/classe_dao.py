#Alunos: Bruno Lorenzo, Eduardo Peron, Enzo Salamão, Guilherme de Sá

import sqlite3
from classe import Usuario

class UsuarioDAO:
    def __init__(self, bd_path):
        self.bd_path = bd_path

    def inserir_usuario(self, usuario):         
        connection = sqlite3.connect(self.bd_path)
        cursor = connection.cursor()

        comando_sql = """
        INSERT INTO Usuarios (nome, idade, email, cpf, senha) 
        VALUES (?, ?, ?, ?, ?)
        """        
        cursor.execute(comando_sql, (usuario._nome, \
            usuario._idade, usuario._email, usuario._cpf, usuario._senha))
        connection.commit()
        connection.close()
        return True if cursor.lastrowid > 0 else False

    def buscar_cpf(self, cpf):

        connection = sqlite3.connect(self.bd_path)
        cursor = connection.cursor()
        
        comando_sql = """
        SELECT * FROM Usuarios WHERE cpf = ?
        """
        cursor.execute(comando_sql, [cpf])
        lista_cpf = cursor.fetchall()
        connection.close()

        if len(lista_cpf) > 0:
            
            cpfs = []
            for tupla in lista_cpf:
                usuario = Usuario(nome=tupla[1], idade=tupla[2], email=tupla[3], cpf=tupla[4], senha=tupla[5], id=tupla[0])
                cpfs.append(usuario)
            return cpfs, tupla

        else:
            return None

    def buscar_email(self, email):

        connection = sqlite3.connect(self.bd_path)
        cursor = connection.cursor()
        
        comando_sql = """
        SELECT * FROM Usuarios WHERE email = ?
        """
        cursor.execute(comando_sql, [email])
        lista_email = cursor.fetchall()
        connection.close()

        if len(lista_email) > 0:
            
            emails = []
            for tupla in lista_email:
                usuario = Usuario(nome=tupla[1], idade=tupla[2], email=tupla[3], cpf=tupla[4], senha=tupla[5], id=tupla[0])
                emails.append(usuario)
            return emails, tupla

        else:
            return None