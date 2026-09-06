import sqlite3
from functions.get_db_connection import get_db_connection
from flask import Flask
from flask import jsonify,  render_template, request, redirect, url_for, Blueprint

add_categoria_bp = Blueprint("add_categoria", __name__, url_prefix="/categoria")



@add_categoria_bp.route('/deletar_categoria/<int:categoria_id>', methods=["DELETE"])
def apagar_categorias(categoria_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM categorias WHERE id = ?", (categoria_id,))
    conn.commit()
    conn.close()
    return jsonify({"sucesso": True}), 200


@add_categoria_bp.route('/listar_categorias', methods=["get"])
def listar_categorias():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM categorias")
    categorias = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jsonify(categorias), 200


@add_categoria_bp.route('/adicionar_categoria', methods=["POST"])
def salvar_categoria():
    dados = request.get_json()
    name = dados.get("nome")

    if not name:
        return jsonify({"error": "O nome da categoria é obrigatório."}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
         INSERT OR IGNORE INTO categorias (nome) VALUES (?)
    """, (name,))

    conn.commit()  
    conn.close()

    




    return jsonify({"sucesso": True}), 200

