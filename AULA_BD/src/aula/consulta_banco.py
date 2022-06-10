import sqlite3

if __name__ == '__main__':

    conn = sqlite3.connect('clientes.db')

    cursor = conn.cursor()

    #cursor.execute("""SELECT * FROM clientes """)
    #cursor.execute("""SELECT nome, idade FROM clientes """)
    #cursor.execute("""SELECT * FROM clientes WHERE idade = 27""")
    #cursor.execute("""SELECT * FROM clientes WHERE nome = 'Mariana Tassan'""")
    comando_recuperarsql = """
    SELECT * FROM clientes WHERE id = ?
    """
    cursor.execute(comando_recuperarsql, [4])

    clientes = cursor.fetchall()
    #fetone() = retorna só um.

    for cliente in clientes:
        print(cliente)

    
    campo_pesquisa = 'id'
    comando_recuperarsql2 = f'SELECT * FROM clientes WHERE {campo_pesquisa} = ?'
    cursor.execute(comando_recuperarsql2, [2])

    clientes = cursor.fetchall()
    #fetone() = retorna só um.

    for cliente in clientes:
        print(cliente)

    conn.close()