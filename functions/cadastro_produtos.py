import sqlite3

from flask import jsonify
import get_db_connection

def cadastro_produtos(nome_produto, preco, medida,categoria):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO produtos (nome, preco, medida, categoria) VALUES (?, ?, ?, ?)
    """, (nome_produto, preco, medida, categoria))
    conn.commit()
    conn.close()

    return jsonify({'sucesso': True, 'mensagem': 'Produto cadastrado com sucesso!'}), 200