from flask import Flask, Blueprint, send_from_directory

download_bp = Blueprint('download', __name__, url_prefix='/sistema')

@download_bp.route("/backup", methods=['GET'])
def download():
    arquivo_db= send_from_directory('.', 'sistema.db')

    return arquivo_db