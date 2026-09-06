import sqlite3
from functions.get_db_connection import get_db_connection


conn = get_db_connection()
cursor = conn.cursor()



def get_all_saidas():   
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM transacoes WHERE tipo = 'saida' ORDER BY data DESC, hora DESC
    """)
    todas_saidas = cursor.fetchall()

    conn.close()
 
    return todas_saidas

def get_all_entradas():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM transacoes WHERE tipo = 'entrada' ORDER BY data DESC, hora DESC
    """)
    todas_entradas = cursor.fetchall()

    conn.close()
 
    return todas_entradas
