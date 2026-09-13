import sqlite3
from flask import Flask, Blueprint, jsonify, request
from database.connection import get_db_connection

servicos_bp = Blueprint('servicos', __name__,  url_prefix=("/servicos"))

@servicos_bp.route('/orcamentos/servicos/adicionar', methods=['POST'])
def adicionar_servicos():
    conn = get_db_connection()
    cursor = conn.cursor()

    requisicao = request.get_json()


    nome = requisicao.get("nome")
    preco = requisicao.get("preco")
    categoria = requisicao.get("categoria")
    formula = requisicao.get("calculo")

    cursor.execute("""
    INSERT OR IGNORE INTO servicos  (nome, preco, categoria, formula) VALUES (?, ?, ?, ?)
    """,(nome, preco, categoria, formula))

    conn.commit()
    conn.close()

    return jsonify({"sucesso":"Formula Cadastrada"}), 200

@servicos_bp.route('/orcamentos/listar_servicos', methods=['GET'])
def listar_servicos():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM servicos
    """)

    dados = cursor.fetchall()

    json_to_send = [dict(item) for item in dados]

    conn.commit()
    conn.close()

    return  jsonify(json_to_send,{"sucesso":"Envia Realizado"}), 200
