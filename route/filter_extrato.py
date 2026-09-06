import sqlite3
from flask import request, Blueprint, render_template, jsonify
from functions.filter import filter

filter_bp = Blueprint('filter', __name__)

@filter_bp.route('/filtra_mes', methods=['GET'])
def filtrar():
    month = request.args.get('mes')
    year = request.args.get('ano')
    category = request.args.get('categoria')

    if category == 'todas':
        category = '%'

    result = filter(year, month, category)


    return  jsonify([dict(item) for item in result ])