import sqlite3
from functions.get_db_connection import get_db_connection
from flask import Flask
from flask import jsonify,  render_template, request, redirect, url_for, Blueprint
import functions.calculations_dashboard_painel as pegar

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

@add_categoria_bp.route('/dashboard_dados', methods=['GET'])
def categoria_pastas():
    pasta = request.args.get('obra_id')

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM transacoes WHERE pasta = ?    
    """,(pasta,))

    dados = cursor.fetchall()

    resp = jsonify({
        "saldo_painel": pegar.show_data_total() ,
         "saldo_credit": pegar.total_entradas(),
         "saldo_debit": pegar.total_saida(),
         "projecao_saldo": pegar.projetion_saldo(),}),200

    conn.close()

    return resp

@add_categoria_bp.route('/obra/listar_obras', methods=['GET'])
def lista_obras():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM categoria_obras
    """)
    categoria_obras = cursor.fetchall()

    conn.close()

    resp = jsonify([dict(item) for item in categoria_obras])
    return resp

@add_categoria_bp.route('/obra/adicionar_obra', methods=['POST'])
def add_categoria_obra():

    dados = request.get_json('nome_obra')

    obra_nome = dados.get('nome')

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO  categoria_obras (nome) VALUES (?)
    """,(obra_nome,))

    conn.commit()
    conn.close()

    

    return jsonify({"sucesso": True}), 200

@add_categoria_bp.route('/obra/deletar_obra/', methods=['DELETE'])
def deletar_categoria_obra():
    id = request.args.get('id')

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(""" 
    DELETE FROM categoria_obras WHERE id = (?)
    """,(id,))

    conn.commit()
    conn.close()


    return jsonify({'sucesso':'True'}), 200 

