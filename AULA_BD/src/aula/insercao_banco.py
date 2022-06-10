import sqlite3
from datetime import datetime

if __name__ == '__main__':

    conn = sqlite3.connect('clientes.db')

    cursor = conn.cursor()

    #cursor.execute("""
    #INSERT INTO clientes (nome, idade, cpf, email, criado_em)
    #VALUES('Bruno Lorenzo Thomaz', 20, '140.627.707-09', 'bruno.lorenzo.thomaz@gmail.com', '2022-06-10')
    #'''""")
    comando = """
    INSERT INTO clientes (nome, idade, cpf, email, criado_em)
    VALUES(?, ?, ?, ?, ?)
    """

    data = datetime.now()

    #cursor.execute(comando, ('Mariana Tassan', 19, \
        #'190.698.777-20', 'marianatassan19@gmail.com', data))

    clientes = [
        ('Rafael Thomaz', 11, \
        '150.665.730-20', 'rafaelthomaz@gmail.com', data),
        ('Fernando Thomaz', 27, \
        '456.215.429-60', 'fernando_nathan@gmail.com', data),
    ]

    cursor.executemany(comando, clientes)
    print('Dados inseridos com sucesso!.')
    conn.commit()
    conn.close()