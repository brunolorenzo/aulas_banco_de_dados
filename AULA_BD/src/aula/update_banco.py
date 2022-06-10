import sqlite3
from datetime import datetime

if __name__ == '__main__':

    conn = sqlite3.connect('clientes.db')

    cursor = conn.cursor()

    data = datetime.now()
    updatesql_nome = """
    UPDATE clientes SET nome = ? WHERE id = ?
    """
    updatesql_cpf = """
    UPDATE clientes SET cpf = ? WHERE id = ?
    """
    updatesql_idade = """
    UPDATE clientes SET idade = ? WHERE id = ?
    """
    updatesql_email = """
    UPDATE clientes SET email = ? WHERE id = ?
    """
    updatesql_data = """
    UPDATE clientes SET criado_em = ? WHERE id = ?
    """

    cursor.execute(updatesql_nome, ('Rosileide Thomaz', 2))
    cursor.execute(updatesql_cpf, ('031.310.869-20', 2))
    cursor.execute(updatesql_email, ('leidi.thomaz@hotmail.com', 2))
    cursor.execute(updatesql_idade, (41, 2))
    cursor.execute(updatesql_data, (data, 2))

    conn.commit()
    print('Updates feito com sucesso!')

    conn.close()
