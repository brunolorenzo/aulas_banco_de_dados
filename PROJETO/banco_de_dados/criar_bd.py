#Alunos: Bruno Lorenzo, Eduardo Peron, Enzo Salamão, Guilherme de Sá

import sqlite3
import os

def criar_bd_usuario(bd_path): 
    if not os.path.exists(bd_path):

        connection = sqlite3.connect(bd_path)

        cursor = connection.cursor()

        cursor.execute("""
        CREATE TABLE Usuarios (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            idade INTEGER,
            email TEXT NOT NULL,
            cpf VARCHAR(15) NOT NULL,
            senha TEXT NOT NULL
        );
        """)

        print('\nBanco de dados criado')

        connection.close()

    else:
        print('\nBanco de dados ja existe')