import sqlite3
from flask import request, jsonify
from database.connection import get_db_connection



def salvar_orcamento(nome_orcamento, data,  obra, categoria_orcamento, valor_total):
    conn = get_db_connection()
    cursor = conn.cursor()

    json_recive = request.get_json()

    cursor.execute("""
        INSERT INTO orcamentos (nome,data,obra,categoria_orcamento,valor_total) VALUES (?,?,?,?,?)
        """,('nome_orcamento', 'data', 'obra', 'categoria_orcamento', 'valor_total'))


    conn.commit()
    conn.close()

    return 'sucesso','orcamento salvo com sucesso'