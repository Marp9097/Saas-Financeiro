from flask import Flask, Blueprint, send_from_directory

download_bp = Blueprint('download', __name__)

@download_bp.route("/backup_db", methods=['GET'])
def download():
    arquivo_db= send_from_directory('.', 'sistema.db')

    return arquivo_db