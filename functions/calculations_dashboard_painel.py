import sqlite3
from flask import request
from functions.get_db_connection import get_db_connection


def show_data_total():
    select_pasta = request.args.get('obra_id')
    
    if select_pasta == 'todas':
        select_pasta = '%'


    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM transacoes WHERE pasta LIKE ? AND tipo = 'entrada'
    """,(select_pasta,))
    entradas = sum(item[3] for item in cursor.fetchall() if item[3] is not None  )

    cursor.execute("""
        SELECT * FROM transacoes WHERE pasta LIKE ? AND tipo = 'saida'
    """,(select_pasta,))

    saidas = sum(item[3] for item in cursor.fetchall() if item[3] is not None  )

    
    saldo_format = entradas - saidas
    saldo = saldo_format
    conn.close()

    return(saldo)

def total_entradas():
    select_pasta = request.args.get('obra_id')
    if select_pasta == None:
        select_pasta = '%'
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM transacoes WHERE pasta LIKE ? AND tipo = 'entrada'
    """,(select_pasta,))
    somando  = sum(item[3] for item in cursor.fetchall() if item[3] is not None  )
    conn.close()

    total_entradas = somando


    return total_entradas

def total_saida():
    select_pasta = request.args.get('obra_id')
    if select_pasta == None:
        select_pasta = '%'
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM transacoes WHERE pasta LIKE ? AND tipo = 'saida'
    """,(select_pasta,))
    calculando = sum(item[3] for item in cursor.fetchall() if item[3] is not None  )
    conn.close()

    saida = calculando

    return saida

def projetion_saldo():
    select_pasta = request.args.get('obra_id')
    if select_pasta == None:
        select_pasta = '%'
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM transacoes WHERE pasta LIKE ? AND tipo = 'entrada'
    """,(select_pasta,))
    entradas = sum(item[3] for item in cursor.fetchall() if item[3] is not None  )
    conn.close()

    percent = entradas * (5/100)
    somando = entradas + percent

    projetion = somando

    return projetion