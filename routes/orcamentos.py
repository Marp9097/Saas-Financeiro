from flask import Flask, Blueprint, request,  jsonify
import sqlite3
from functions.salvar_orcamentos import salvar_orcamento 

orcamento_bp = Blueprint("orcamento", __name__ , url_prefix='/orcamentos')

@orcamento_bp.route('/salvar_orcamento', methods=['POST'])
def salvar_orcamentos():

    json = request.get_json()

    obra_id = json.get('obra_id')
    categoria = json.get('categoria')
    nome = json.get('nome')
    valor = json.get('valor')
    data = json.get('data')

    print(json)

    resposta = salvar_orcamento(nome_orcamento=nome, data=data, obra=obra_id, valor_total=valor, categoria_orcamento=categoria)

    return jsonify(resposta)