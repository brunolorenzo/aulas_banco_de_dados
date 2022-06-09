import sqlite3

if __name__ == '__main__':

    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE clientes (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER,
        cpf VARCHAR(15) NOT NULL,
        email TEXT NOT NULL,
        criado_em DATE NOT NULL
    );
    """)

    conn.close()
