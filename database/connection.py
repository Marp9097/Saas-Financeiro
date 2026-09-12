# Conexão central com o banco SQLite.
# As outras partes do sistema importam esta função em vez de abrir conexões diferentes.

    
import sqlite3

def get_db_connection():
    conn = sqlite3.connect('sistema.db')
    conn.row_factory = sqlite3.Row
    return conn