# Consultas de entradas e saídas usadas pelo extrato/página inicial.

import sqlite3
from database.connection import get_db_connection


conn = get_db_connection()
cursor = conn.cursor()



def get_all_saidas(pasta):   
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM transacoes WHERE pasta = ? AND tipo = 'saida' ORDER BY data DESC, hora DESC
    """, (pasta,))
    todas_saidas = cursor.fetchall()

    conn.close()
 
    return todas_saidas

def get_all_entradas(pasta):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM transacoes WHERE pasta = ? AND tipo = 'entrada' ORDER BY data DESC, hora DESC
    """, (pasta,))
    todas_entradas = cursor.fetchall()

    conn.close()
 
    return todas_entradas
