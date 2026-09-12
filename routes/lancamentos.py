import os
import sqlite3
from datetime import datetime
from flask import render_template, request, redirect, url_for, Blueprint
from database.connection import get_db_connection

#Criando uma Blueprint para organizar as rotas relacionadas à declaração
lancamentos_bp = Blueprint("lancamentos", __name__, url_prefix="/lancamentos")


# Rota para declarar/salvar lançamentos
@lancamentos_bp.route('/salvar', methods=['POST'])
def salvar_declaracao():
    tipo = request.form.get('tipo')
    nome = request.form.get('nome')
    valor = float(request.form.get('valor', 0))
    categoria = request.form.get('categoria')
    recorrente = 1 if request.form.get('recorrente') else 0
    pasta = request.form.get('obra_id')  # Obtendo o valor do campo "pasta" do formulário
    
    agora = datetime.now()
    data_hoje = agora.strftime('%Y-%m-%d')
    hora_atual = agora.strftime('%H:%M')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO transacoes (tipo, nome, valor, categoria, recorrente, data, hora, pasta) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        (tipo, nome, valor, categoria, recorrente, data_hoje, hora_atual, pasta)
    )
    conn.commit()
    conn.close()

    return redirect(url_for('site.index'))  # Redireciona para a página inicial após salvar a declaração