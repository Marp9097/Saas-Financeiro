import sqlite3
from database.connection import get_db_connection
from flask import jsonify,  render_template, request, redirect, url_for, Blueprint
import functions.dashboard as dashboard

categorias_bp = Blueprint("categorias", __name__, url_prefix="/categorias")



@categorias_bp.route('/deletar/<int:categoria_id>', methods=["DELETE"])
def apagar_categorias(categoria_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM categorias WHERE id = ?", (categoria_id,))
    conn.commit()
    conn.close()
    return jsonify({"sucesso": True}), 200


@categorias_bp.route('/listar', methods=["get"])
def listar_categorias():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM categorias")
    categorias = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jsonify(categorias), 200


@categorias_bp.route('/adicionar', methods=["POST"])
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

@categorias_bp.route('/dashboard/dados', methods=['GET'])
def categoria_pastas():
    pasta = request.args.get('obra_id')

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM transacoes WHERE pasta = ?    
    """,(pasta,))

    dados = cursor.fetchall()

    saldo_painel = dashboard.show_data_total()
    saldo_credit = dashboard.total_entradas()
    saldo_debit = dashboard.total_saida()
    projecao_saldo = dashboard.projecao_saldo()

    resp = jsonify({
        "saldo_painel": saldo_painel ,
         "saldo_credit":saldo_credit,
         "saldo_debit":saldo_debit,
         "projecao_saldo":projecao_saldo}),200

    conn.close()

    return resp

@categorias_bp.route('/obras/listar', methods=['GET'])
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

@categorias_bp.route('/obras/adicionar', methods=['POST'])
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

@categorias_bp.route('/obras/deletar/', methods=['DELETE'])
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

