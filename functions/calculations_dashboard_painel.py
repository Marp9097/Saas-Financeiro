import sqlite3
from functions.get_db_connection import get_db_connection


def show_data_total():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM transacoes WHERE tipo = 'entrada'
    """)
    entradas = sum(item[3] for item in cursor.fetchall() if item[3] is not None  )

    cursor.execute("""
        SELECT * FROM transacoes WHERE tipo = 'saida'
    """)

    saidas = sum(item[3] for item in cursor.fetchall() if item[3] is not None  )

    
    saldo_format = entradas - saidas
    saldo = f"{saldo_format:,.2f}".replace(',','.')
    conn.close()

    return(saldo)

def total_entradas():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM transacoes WHERE tipo = 'entrada'
    """)
    somando  = sum(item[3] for item in cursor.fetchall() if item[3] is not None  )
    conn.close()

    total_entradas = f"{somando:,.2f}".replace(',','.')


    return total_entradas

def total_saida():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM transacoes WHERE tipo = 'saida'
    """)
    calculando = sum(item[3] for item in cursor.fetchall() if item[3] is not None  )
    conn.close()

    saida = f"{calculando:,.2f}".replace(',','.')

    return saida

def projetion_saldo():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM transacoes WHERE tipo = 'entrada'
    """)
    entradas = sum(item[3] for item in cursor.fetchall() if item[3] is not None  )
    conn.close()

    percent = entradas * (5/100)
    somando = entradas + percent

    projetion = f"{somando:,.2f}".replace(',','.')

    return projetion