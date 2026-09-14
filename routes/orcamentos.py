from io import BytesIO
from datetime import datetime
from flask import Blueprint, request, jsonify, send_file
from functions.salvar_orcamentos import salvar_orcamento
from database.connection import get_db_connection

orcamento_bp = Blueprint("orcamento", __name__ , url_prefix='/orcamentos')


def buscar_orcamento(orcamento_id):
    """Busca um orçamento com seus itens; retorna None se ele não existir."""
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT o.id, o.nome, o.data, o.obra AS obra_id,
                   COALESCE(ob.nome, CAST(o.obra AS TEXT)) AS obra_nome,
                   o.categoria_orcamento AS categoria, o.valor_total AS valor
            FROM orcamentos AS o
            LEFT JOIN categoria_obras AS ob ON ob.id = o.obra
            WHERE o.id = ?
        """, (orcamento_id,))
        orcamento = cursor.fetchone()
        if not orcamento:
            return None
        orcamento = dict(orcamento)
        cursor.execute("""
            SELECT id, orcamento_id, tipo, catalogo_id, nome, categoria, calculo,
                   fator, preco, total, formula, medida_1, medida_2, medida_3, unidade
            FROM orcamento_itens WHERE orcamento_id = ? ORDER BY id
        """, (orcamento_id,))
        orcamento['itens'] = [dict(linha) for linha in cursor.fetchall()]
        return orcamento
    finally:
        conn.close()


def criar_pdf_orcamento(orcamento):
    """Cria um PDF textual simples sem depender de bibliotecas externas."""
    linhas = [
        'ORCAMENTO', '', f"Nome: {orcamento['nome']}",
        f"Obra: {orcamento['obra_nome']}", f"Categoria: {orcamento['categoria']}",
        f"Data: {orcamento['data']}", '', 'ITENS'
    ]
    for indice, item in enumerate(orcamento['itens'], 1):
        linhas.append(f"{indice}. {item['nome']} ({item['tipo']})")
        linhas.append(f"   {item.get('formula') or ''}  |  Total: R$ {float(item['total'] or 0):.2f}")
    linhas += ['', f"VALOR TOTAL: R$ {float(orcamento['valor'] or 0):.2f}", '',
               f"Gerado em {datetime.now().strftime('%d/%m/%Y %H:%M')}"]

    def escapar(texto):
        return str(texto).replace('\\', '\\\\').replace('(', '\\(').replace(')', '\\)')

    paginas = [linhas[pos:pos + 42] for pos in range(0, len(linhas), 42)] or [[]]
    fonte_id = 3 + len(paginas) * 2
    objetos = [b'<< /Type /Catalog /Pages 2 0 R >>']
    filhos = ' '.join(f'{3 + indice * 2} 0 R' for indice in range(len(paginas)))
    objetos.append(f'<< /Type /Pages /Kids [{filhos}] /Count {len(paginas)} >>'.encode())
    for indice, pagina in enumerate(paginas):
        pagina_id, conteudo_id = 3 + indice * 2, 4 + indice * 2
        objetos.append(f'<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] /Resources << /Font << /F1 {fonte_id} 0 R >> >> /Contents {conteudo_id} 0 R >>'.encode())
        comandos = ['BT', '/F1 16 Tf', '50 790 Td']
        for numero, linha in enumerate(pagina):
            if numero == 1:
                comandos += ['/F1 10 Tf']
            comandos += [f'({escapar(linha)}) Tj', '0 -17 Td']
        comandos += ['ET']
        stream = '\n'.join(comandos).encode('latin-1', 'replace')
        objetos.append(f'<< /Length {len(stream)} >>\nstream\n'.encode() + stream + b'\nendstream')
    objetos.append(b'<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>')

    pdf = bytearray(b'%PDF-1.4\n')
    offsets = [0]
    for numero, objeto in enumerate(objetos, 1):
        offsets.append(len(pdf))
        pdf += f'{numero} 0 obj\n'.encode() + objeto + b'\nendobj\n'
    inicio_xref = len(pdf)
    pdf += f'xref\n0 {len(objetos) + 1}\n0000000000 65535 f \n'.encode()
    for offset in offsets[1:]:
        pdf += f'{offset:010d} 00000 n \n'.encode()
    pdf += f'trailer\n<< /Size {len(objetos) + 1} /Root 1 0 R >>\nstartxref\n{inicio_xref}\n%%EOF'.encode()
    return BytesIO(pdf)

@orcamento_bp.route('/salvar_orcamento', methods=['POST'])
def salvar_orcamentos():
    dados = request.get_json(silent=True) or {}

    resposta = salvar_orcamento(
        nome_orcamento=dados.get('nome'),
        data=dados.get('data'),
        obra=dados.get('obra_id'),
        valor_total=dados.get('valor'),
        categoria_orcamento=dados.get('categoria'),
        itens=dados.get('itens', [])
    )

    status = 200 if resposta.get('sucesso') else 400
    return jsonify(resposta), status


@orcamento_bp.route('/listar_orcamentos', methods=['GET'])
def listar_orcamentos():
    """Retorna cada orçamento com seu cabeçalho e seus itens."""
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            SELECT
                o.id,
                o.nome,
                o.data,
                o.obra AS obra_id,
                COALESCE(ob.nome, CAST(o.obra AS TEXT)) AS obra_nome,
                o.categoria_orcamento AS categoria,
                o.valor_total AS valor
            FROM orcamentos AS o
            LEFT JOIN categoria_obras AS ob ON ob.id = o.obra
            ORDER BY o.data DESC, o.id DESC
        """)
        orcamentos = [dict(linha) for linha in cursor.fetchall()]

        for orcamento in orcamentos:
            cursor.execute("""
                SELECT
                    id, orcamento_id, tipo, catalogo_id, nome, categoria,
                    calculo, fator, preco, total, formula,
                    medida_1, medida_2, medida_3, unidade
                FROM orcamento_itens
                WHERE orcamento_id = ?
                ORDER BY id
            """, (orcamento['id'],))
            orcamento['itens'] = [dict(linha) for linha in cursor.fetchall()]

        return jsonify(orcamentos), 200
    finally:
        conn.close()


@orcamento_bp.route('/<int:orcamento_id>', methods=['GET'])
def detalhar_orcamento(orcamento_id):
    orcamento = buscar_orcamento(orcamento_id)
    if not orcamento:
        return jsonify({'sucesso': False, 'erro': 'Orçamento não encontrado.'}), 404
    return jsonify(orcamento), 200


@orcamento_bp.route('/<int:orcamento_id>/pdf', methods=['GET'])
def baixar_orcamento_pdf(orcamento_id):
    orcamento = buscar_orcamento(orcamento_id)
    if not orcamento:
        return jsonify({'sucesso': False, 'erro': 'Orçamento não encontrado.'}), 404
    nome = ''.join(letra if letra.isalnum() else '_' for letra in orcamento['nome'])[:60]
    return send_file(criar_pdf_orcamento(orcamento), mimetype='application/pdf',
                     as_attachment=True, download_name=f'orcamento_{nome or orcamento_id}.pdf')


@orcamento_bp.route('/<int:orcamento_id>', methods=['PUT'])
def atualizar_orcamento(orcamento_id):
    """Atualiza o cabeçalho e substitui os itens do orçamento."""
    dados = request.get_json(silent=True) or {}
    itens = dados.get('itens', [])

    if not isinstance(itens, list) or not itens:
        return jsonify({'sucesso': False, 'erro': 'O orçamento precisa ter ao menos um item.'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            UPDATE orcamentos
            SET nome = ?, data = ?, obra = ?, categoria_orcamento = ?, valor_total = ?
            WHERE id = ?
        """, (
            dados.get('nome'), dados.get('data'), dados.get('obra_id'),
            dados.get('categoria'), dados.get('valor'), orcamento_id
        ))
        if cursor.rowcount == 0:
            conn.rollback()
            return jsonify({'sucesso': False, 'erro': 'Orçamento não encontrado.'}), 404

        cursor.execute('DELETE FROM orcamento_itens WHERE orcamento_id = ?', (orcamento_id,))
        for item in itens:
            cursor.execute("""
                INSERT INTO orcamento_itens (
                    orcamento_id, tipo, catalogo_id, nome, categoria, calculo,
                    fator, preco, total, formula, medida_1, medida_2, medida_3, unidade
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                orcamento_id, item.get('tipo'), item.get('catalogo_id'), item.get('nome'),
                item.get('categoria'), item.get('calculo'), item.get('fator', 0),
                item.get('preco', 0), item.get('total', 0), item.get('formula'),
                item.get('medida_1', 0), item.get('medida_2', 0),
                item.get('medida_3', 0), item.get('unidade')
            ))

        conn.commit()
        return jsonify({'sucesso': True, 'mensagem': 'Orçamento atualizado com sucesso.'}), 200
    except Exception as erro:
        conn.rollback()
        return jsonify({'sucesso': False, 'erro': str(erro)}), 400
    finally:
        conn.close()


@orcamento_bp.route('/<int:orcamento_id>', methods=['DELETE'])
def excluir_orcamento(orcamento_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('DELETE FROM orcamento_itens WHERE orcamento_id = ?', (orcamento_id,))
        cursor.execute('DELETE FROM orcamentos WHERE id = ?', (orcamento_id,))
        if cursor.rowcount == 0:
            conn.rollback()
            return jsonify({'sucesso': False, 'erro': 'Orçamento não encontrado.'}), 404
        conn.commit()
        return jsonify({'sucesso': True, 'mensagem': 'Orçamento removido.'}), 200
    except Exception as erro:
        conn.rollback()
        return jsonify({'sucesso': False, 'erro': str(erro)}), 400
    finally:
        conn.close()
