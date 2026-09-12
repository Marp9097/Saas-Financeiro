# Funções para filtrar transações por período, categoria e obra.

import sqlite3
from database.connection import get_db_connection

def filtrar_transacoes(year, month, category, pasta):
    conn = get_db_connection()
    cursor = conn.cursor()

    meses_dict = {
        "jan":"01", "fev":"02",
        "mar":"03", "abr":"04",
        "mai":"05", "jun":"06",
        "jul":"07", "ago":"08",
        "set":"09", "out":"10",
        "nov":"11", "dez":"12",
    }

    num_month = meses_dict[f"{month}"]
    data_pattern = f"{year}-{num_month}-%"

    cursor.execute("""
    SELECT *  FROM transacoes WHERE pasta LIKE ? AND data LIKE ? AND categoria LIKE ? ORDER BY hora DESC
    """,(pasta, data_pattern, category))

    lista = cursor.fetchall()

    return lista

# Alias mantido para compatibilidade com chamadas antigas.
filter = filtrar_transacoes
