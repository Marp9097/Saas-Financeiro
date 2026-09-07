import sqlite3
from flask import request, Blueprint, render_template, jsonify
from functions.filter import filter

filter_bp = Blueprint('filter', __name__)

@filter_bp.route('/filtra_mes', methods=['GET'])
def filtrar():
    month = request.args.get('mes')
    year = request.args.get('ano')
    category = request.args.get('categoria')
    pasta = request.args.get('select_obra_filtro')  # Obtendo o valor do campo "pasta" do formulário

    if category == 'todas':
        category = '%'

    if  pasta== 'todas':
        pasta = '%'

    result = filter(year=year, month=month, category=category, pasta=pasta)


    return  jsonify([dict(item) for item in result ])