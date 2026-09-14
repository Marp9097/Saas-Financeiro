from database.connection import get_db_connection


def salvar_orcamento(nome_orcamento, data, obra, categoria_orcamento, valor_total, itens):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        if not all([nome_orcamento, data, obra, categoria_orcamento]):
            return {'sucesso': False, 'erro': 'Preencha todos os dados do orçamento.'}

        if not isinstance(itens, list) or not itens:
            return {'sucesso': False, 'erro': 'Adicione pelo menos um item ao orçamento.'}

        cursor.execute("""
            INSERT INTO orcamentos (nome, data, obra, categoria_orcamento, valor_total)
            VALUES (?, ?, ?, ?, ?)
        """, (nome_orcamento, data, obra, categoria_orcamento, valor_total))

        # Este é o ID do orçamento criado acima, usado para todos os seus itens.
        orcamento_id = cursor.lastrowid

        for item in itens:
            cursor.execute("""
                INSERT INTO orcamento_itens (
                    orcamento_id, tipo, catalogo_id, nome, categoria, calculo,
                    fator, preco, total, formula, medida_1, medida_2, medida_3, unidade
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                orcamento_id,
                item.get('tipo'),
                item.get('catalogo_id'),
                item.get('nome'),
                item.get('categoria'),
                item.get('calculo'),
                item.get('fator', 0),
                item.get('preco', 0),
                item.get('total', 0),
                item.get('formula'),
                item.get('medida_1', 0),
                item.get('medida_2', 0),
                item.get('medida_3', 0),
                item.get('unidade')
            ))

        conn.commit()
        return {
            'sucesso': True,
            'mensagem': 'Orçamento salvo com sucesso.',
            'orcamento_id': orcamento_id
        }
    except Exception as erro:
        conn.rollback()
        return {'sucesso': False, 'erro': str(erro)}
    finally:
        conn.close()
