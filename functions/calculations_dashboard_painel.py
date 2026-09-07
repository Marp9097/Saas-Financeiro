import sqlite3
from functions.get_db_connection import get_db_connection


def show_data_total(select_pasta):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM transacoes WHERE pasta LIKE ? AND tipo = 'entrada'
    """,(select_pasta,))
    entradas = sum(item[3] for item in cursor.fetchall() if item[3] is not None  )

    cursor.execute("""
        SELECT * FROM transacoes WHERE tipo = 'saida'
    """)

    saidas = sum(item[3] for item in cursor.fetchall() if item[3] is not None  )

    
    saldo_format = entradas - saidas
    saldo = f"{saldo_format:,.2f}".replace(',','.')
    conn.close()

    return(saldo)

def total_entradas(select_pasta):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM transacoes WHERE pasta LIKE ? AND tipo = 'entrada'
    """,(select_pasta,))
    somando  = sum(item[3] for item in cursor.fetchall() if item[3] is not None  )
    conn.close()

    total_entradas = f"{somando:,.2f}".replace(',','.')


    return total_entradas

def total_saida(select_pasta):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM transacoes WHERE pasta LIKE ? AND tipo = 'saida'
    """,(select_pasta,))
    calculando = sum(item[3] for item in cursor.fetchall() if item[3] is not None  )
    conn.close()

    saida = f"{calculando:,.2f}".replace(',','.')

    return saida

def projetion_saldo(select_pasta):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM transacoes WHERE pasta LIKE ? AND tipo = 'entrada'
    """,(select_pasta,))
    entradas = sum(item[3] for item in cursor.fetchall() if item[3] is not None  )
    conn.close()

    percent = entradas * (5/100)
    somando = entradas + percent

    projetion = f"{somando:,.2f}".replace(',','.')

    return projetion