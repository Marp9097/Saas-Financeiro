import os
import sqlite3
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
from flask import Blueprint
from routes.lancamentos import lancamentos_bp
from routes.categorias import categorias_bp
from routes.site import site_bp
from database.init import init_db
from database.connection import get_db_connection
from routes.extrato import extrato_bp
from routes.download import download_bp
from routes.produtos import produtos_bp



app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['DATABASE'] = 'sistema.db'
app.register_blueprint(categorias_bp)
app.register_blueprint(lancamentos_bp)
app.register_blueprint(site_bp)
app.register_blueprint(extrato_bp)
app.register_blueprint(download_bp)
app.register_blueprint(produtos_bp)
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