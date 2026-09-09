from flask import Blueprint, render_template, request
from functions.cadastro_produtos import cadastro_produtos

cadastro_produtos_bp = Blueprint('cadastra_produtos',__name__)

@cadastro_produtos_bp.route('/orcamento/produtos/adicionar', methods=['POST'])
def adionar_produtos():
    nome_produto = request.form.get('nome_produto')
    preco = float(request.form.get('preco'))
    medida = request.form.get('medida')
    categoria = request.form.get('categoria')
    return cadastro_produtos(nome_produto, preco, medida, categoria)