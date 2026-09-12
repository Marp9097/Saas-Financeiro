import sqlite3

# 1. Conecta no mesmo arquivo de banco de dados
conexao = sqlite3.connect("sistema.db")
cursor = conexao.cursor()

# 2. Comando SELECT: Busca a coluna 'nome' e 'valor' da tabela 'declaracoes'
# O asterisco (*) significa "trazer todas as colunas"
cursor.execute("CREATE TABLE IF NOT EXISTS declaracoes (id INTEGER PRIMARY KEY AUTOINCREMENT, recorrente BOOLEAN ,data DATE TEXT NOT NULL, nome TEXT NOT NULL, valor REAL NOT NULL, categoria TEXT NOT NULL)")
cursor.execute("CREATE TABLE IF NOT EXISTS Creditos (id INTEGER PRIMARY KEY AUTOINCREMENT, recorrente BOOLEAN ,data DATE TEXT NOT NULL, nome TEXT NOT NULL, valor REAL NOT NULL, categoria TEXT NOT NULL)")
cursor.execute("CREATE TABLE IF NOT EXISTS arquivos (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, caminho TEXT NOT NULL, id_transacao REAL NOT NULL)")

conexao.commit()
conexao.close()

# 5. Fecha a conexão (não precisa de commit aqui porque não alteramos nada)
conexao.close()


def excluir_tudo():
    # 1. Conecta no mesmo arquivo de banco de dados
    conexao = sqlite3.connect("sistema.db")
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM declaracoes")  # Exclui todos os registros da tabela 'declaracoes'
    cursor.execute("DELETE FROM Creditos")  # Exclui todos os registros da tabela 'Creditos'
    cursor.execute("DELETE FROM arquivos")
    cursor.execute("DELETE FROM categorias")  # Exclui todos os registros da tabela 'categoria'
    cursor.execute("DELETE FROM transacoes")  # Exclui todos os registros da tabela 'transacoes'

    # 3. Salva as alterações no banco de dados
    conexao.commit()

    # 4. Fecha a conexão
    conexao.close()
# Excluir tudo do banco de dados 

if __name__ == "__main__":
    while True:
        #Menu
        print("=== MENU ===")
        print("1. Excluir todos os registros")
        print("2. Mostrar conteúdo dentro do DB")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            excluir_tudo()
            print("Todos os registros foram excluídos.")
        elif opcao == "2":
            # Reutiliza o código de leitura do banco de dados
            conexao = sqlite3.connect("sistema.db")
            cursor = conexao.cursor()
            cursor.execute("SELECT id, nome, valor FROM declaracoes")
            todas_as_linhas = cursor.fetchall()

            print("\n=== LENDO DADOS DO SQLITE ===")
            for linha in todas_as_linhas:
                id_registro = linha[0]
                nome_registro = linha[1]
                valor_registro = linha[2]
                print(f"ID: {id_registro} | Item: {nome_registro} | Preço: R$ {valor_registro}")
            print("=============================\n")

            conexao.close()
        elif opcao == "3":
            print("Saindo do programa.")
            break
        
#Fiz a Parte de Debitos agora vou fazer a parte de Creditos

conexao = sqlite3.connect("sistema.db")
cursor = conexao.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS declaracoes (id INTEGER PRIMARY KEY AUTOINCREMENT, data DATE TEXT NOT NULL, nome TEXT NOT NULL, observacao TEXT, valor REAL NOT NULL)")
cursor.execute("CREATE TABLE IF NOT EXISTS Creditos (id INTEGER PRIMARY KEY AUTOINCREMENT, data DATE TEXT NOT NULL, nome TEXT NOT NULL, observacao TEXT, valor REAL NOT NULL)")
conexao.commit()
conexao.close()
