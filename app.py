import os
import sqlite3
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
from flask import Blueprint
from route.declarar import actions_bp
from route.categoria import add_categoria_bp
from route.site_on import site_on_bp
from functions.init_db import init_db
from functions.get_db_connection import get_db_connection
from route.filter_extrato import filter_bp



app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['DATABASE'] = 'sistema.db'
app.register_blueprint(add_categoria_bp)
app.register_blueprint(actions_bp)
app.register_blueprint(site_on_bp)
app.register_blueprint(filter_bp)

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


#__________________________________________________________________________________ ______
#________________________________________________________________________________________
#                           INICIALIZAÇÃO DO BANCO DE DADOS
init_db()
#________________________________________________________________________________________
#________________________________________________________________________________________



if __name__ == '__main__':
    print("Servidor ON em http://localhost:5000")
    app.run(host="0.0.0.0", port=9097)