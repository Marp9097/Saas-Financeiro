from flask import Blueprint, request, jsonify
from functions.salvar_orcamentos import salvar_orcamento
from database.connection import get_db_connection

orcamento_bp = Blueprint("orcamento", __name__ , url_prefix='/orcamentos')

@orcamento_bp.route('/salvar_orcamento', methods=['POST'])
def salvar_orcamentos():
    dados = request.get_json(silent=True) or {}

    resposta = salvar_orcamento(
        nome_orcamento=dados.get('nome'),
        data=dados.get('data'),
        obra=dados.get('obra_id'),
        valor_total=dados.get('valor'),
        categoria_orcamento=dados.get('categoria'),
        itens=dados.get('itens', [])
    )

    status = 200 if resposta.get('sucesso') else 400
    return jsonify(resposta), status


@orcamento_bp.route('/listar_orcamentos', methods=['GET'])
def listar_orcamentos():
    """Retorna cada orçamento com seu cabeçalho e seus itens."""
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            SELECT
                o.id,
                o.nome,
                o.data,
                o.obra AS obra_id,
                COALESCE(ob.nome, CAST(o.obra AS TEXT)) AS obra_nome,
                o.categoria_orcamento AS categoria,
                o.valor_total AS valor
            FROM orcamentos AS o
            LEFT JOIN categoria_obras AS ob ON ob.id = o.obra
            ORDER BY o.data DESC, o.id DESC
        """)
        orcamentos = [dict(linha) for linha in cursor.fetchall()]

        for orcamento in orcamentos:
            cursor.execute("""
                SELECT
                    id, orcamento_id, tipo, catalogo_id, nome, categoria,
                    calculo, fator, preco, total, formula,
                    medida_1, medida_2, medida_3, unidade
                FROM orcamento_itens
                WHERE orcamento_id = ?
                ORDER BY id
            """, (orcamento['id'],))
            orcamento['itens'] = [dict(linha) for linha in cursor.fetchall()]

        return jsonify(orcamentos), 200
    finally:
        conn.close()
