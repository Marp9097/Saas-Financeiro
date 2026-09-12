"""Rotas de produtos.

Este módulo está reservado para o cadastro de produtos do sistema.
A implementação atual não foi alterada para evitar criar funcionalidades
que não existiam no código original.
"""

from flask import Blueprint, render_template, request, jsonify
import sqlite3
from database.connection import get_db_connection

produtos_bp = Blueprint('produtos', __name__, url_prefix='/produtos')

@produtos_bp.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar_produto():
    produto = request.get_json()

    print([print(item[1])for item in produto])




    return jsonify({'sucesso':'Cadastrado com Sucesso '}), 200


@produtos_bp.route('/cadastrar', methods=['GET'])
def listar():
    produto = request.get_json()

  




    return jsonify({'sucesso':'Cadastrado com Sucesso '}), 200
