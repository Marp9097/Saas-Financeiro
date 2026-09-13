"""Rotas de produtos.

Este módulo está reservado para o cadastro de produtos do sistema.
A implementação atual não foi alterada para evitar criar funcionalidades
que não existiam no código original.
"""

from flask import Blueprint, render_template, request, jsonify
import sqlite3
import json
from database.connection import get_db_connection

produtos_bp = Blueprint('produtos', __name__, url_prefix='/produtos')

@produtos_bp.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar_produto():
    produto = request.get_json()

    conn = get_db_connection()
    cursor = conn.cursor()



    nome = produto.get("nome")
    preco = produto.get("preco")
    unidade = produto.get("unidade")
    categoria = produto.get("categoria")

    cursor.execute("""
    INSERT OR IGNORE INTO produtos (nome, preco, uni_medida, categoria) VALUES (?,?,?,?)
    """,(nome, preco, unidade, categoria))

    conn.commit()
    conn.close()

    return jsonify({'sucesso':'Cadastrado com Sucesso '}), 200


@produtos_bp.route('/listar', methods=['GET'])
def listar():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM produtos
    """)

    produtos = cursor.fetchall()

    conn.close()

    json_return = [dict(item) for item in produtos]
    return  jsonify(json_return, {"sucesso": "pedido entregue "}), 200
