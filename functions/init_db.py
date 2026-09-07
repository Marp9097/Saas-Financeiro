

from functions.get_db_connection import get_db_connection


def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo TEXT NOT NULL,
            nome TEXT NOT NULL,
            valor REAL NOT NULL,
            categoria TEXT NOT NULL,
            recorrente INTEGER DEFAULT 0,
            data TEXT NOT NULL,
            hora TEXT NOT NULL,
            pasta text NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS arquivos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_arquivo TEXT NOT NULL,
            caminho TEXT NOT NULL,
            data_envio TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS categorias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL UNIQUE
        )
    ''')
    
    # Inserir categorias padrão caso a tabela esteja vazia
    cursor.execute("SELECT COUNT(*) FROM categorias")
    if cursor.fetchone()[0] == 0:
        categorias_padrao = [('alimentacao',), ('infraestrutura',), ('transporte',), ('lazer',), ('outros',)]
        cursor.executemany("INSERT INTO categorias (nome) VALUES (?)", categorias_padrao)

    conn.commit()
    conn.close()