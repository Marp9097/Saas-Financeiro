import sqlite3
from flask import request, Blueprint, render_template, jsonify
from functions.transaction_filter import filter

extrato_bp = Blueprint('extrato', __name__, url_prefix='/extrato')

@extrato_bp.route('/filtrar', methods=['GET'])
def filtrar():
    month = request.args.get('mes')
    year = request.args.get('ano')
    category = request.args.get('categoria')
    pasta = request.args.get('obra_id')  # Obtendo o valor do campo "pasta" do formulário

    if category == 'todas':
        category = '%'

    if  pasta == 'todas':
        pasta = '%'

    result = filter(year=year, month=month, category=category, pasta=pasta)


    return  jsonify([dict(item) for item in result ])