import os
import sqlite3
from datetime import datetime
from flask import render_template, request, redirect, url_for, Blueprint
from functions.get_db_connection import get_db_connection

#Criando uma Blueprint para organizar as rotas relacionadas à declaração
actions_bp = Blueprint("actions", __name__, url_prefix="/actions")


# Rota para declarar/salvar lançamentos
@actions_bp.route('/salvar_declaracao', methods=['POST'])
def salvar_declaracao():
    tipo = request.form.get('tipo')
    nome = request.form.get('nome')
    valor = float(request.form.get('valor', 0))
    categoria = request.form.get('categoria')
    recorrente = 1 if request.form.get('recorrente') else 0
    
    agora = datetime.now()
    data_hoje = agora.strftime('%Y-%m-%d')
    hora_atual = agora.strftime('%H:%M')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO transacoes (tipo, nome, valor, categoria, recorrente, data, hora) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (tipo, nome, valor, categoria, recorrente, data_hoje, hora_atual)
    )
    conn.commit()
    conn.close()

    return redirect(url_for('site_on.index'))  # Redireciona para a página inicial após salvar a declaração