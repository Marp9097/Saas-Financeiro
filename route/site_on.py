import sqlite3
from flask import render_template, Blueprint, request
from flask import app
from functions.get_db_connection import get_db_connection
from functions.calculations_dashboard_painel import show_data_total, total_entradas, total_saida,projetion_saldo
from functions.get_db_info import get_all_saidas, get_all_entradas



site_on_bp = Blueprint("site_on", __name__)


@site_on_bp.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Busca categorias apenas para preencher os selects do HTML se precisar
    cursor.execute("SELECT * FROM categorias ORDER BY nome ASC")
    categorias = cursor.fetchall()

    conn.close()

    return render_template('index.html', categorias=categorias,debitos=get_all_saidas('*'),creditos=get_all_entradas('*'))  # Inicializa saldo_painel como 0