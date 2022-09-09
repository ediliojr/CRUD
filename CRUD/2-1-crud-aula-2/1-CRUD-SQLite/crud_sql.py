import sqlite3

def create_table():
    sql = """
    CREATE TABLE IF NOT EXISTS movimentacao_finaceira(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT NOT NULL,
            nome TEXT NOT NULL,
            tipo TEXT NOT NULL,
            valor REAL NOT NULL
            )
    """
    con = sqlite3.connect("banco1.sqlite")
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()
    con.close()

def insert(data, nome, tipo,valor):
    sql = f"""
        INSERT INTO movimentacao_finaceira(data,nome,tipo,valor)
        VALUES ('{data}', '{nome}', '{tipo.lower()}', {valor})
    """
    con = sqlite3.connect("banco1.sqlite")
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()
    con.close()
    

def select(id):
    sql = f"""
        SELECT id, data, nome, tipo,valor
        FROM movimentacao_financeira
        WHERE id = {id}
    """
    
    con = sqlite3.connect("banco1.sqlite")
    cursor = con.cursor()
    cursor.execute(sql)
    con.close()

def select_list():
    sql = f"""
        SELECT id, data, nome, tipo,valor
        FROM movimentacao_financeira
        WHERE id = {id}
    """
    
    con = sqlite3.connect("banco1.sqlite")
    cursor = con.cursor()
    cursor.execute(sql)
    con.close()

def update(id,data=None, nome=None, tipo=None,valor=None):
    set_query = ""
    if data:
        set_query += f"data = '{data}',"
    if nome:
        set_query += f"nome = '{nome}',"
    if tipo:
        set_query += f"tipo = '{tipo.lower()}',"
    if valor:
        set_query += f"valor = {valor},"
    
    
    if set_query:
        sql =f"""
            UPDATE movimentacao_financeira
            SET {set_query[:-1]}
            WHERE id={id}
        """
        
        con = sqlite3.connect("banco1.sqlite")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        con.close()

def delete(id):
    
    sql =f"""
        DELETE FROM movimentacao_financeira
        WHERE id={id}
    """
    
    con = sqlite3.connect("banco1.sqlite")
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()
    con.close()

def entradas():
    sql = f"""
        SELECT id, data, nome, tipo,valor
        FROM movimentacao_financeira
        WHERE tipo = 'entrada'
    """
    
    con = sqlite3.connect("banco1.sqlite")
    cursor = con.cursor()
    cursor.execute(sql)
    con.close()

def saidas():
    sql = f"""
        SELECT id, data, nome, tipo,valor
        FROM movimentacao_financeira
        WHERE tipo = 'saida'
    """
    
    con = sqlite3.connect("banco1.sqlite")
    cursor = con.cursor()
    cursor.execute(sql)
    con.close()


if __name__ == "__main__":
    pass
