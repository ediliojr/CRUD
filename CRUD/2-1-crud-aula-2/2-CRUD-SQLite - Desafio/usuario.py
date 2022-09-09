import sqlite3

class Usuario:
    def __init__(self):
        sql = """
            CREATE TABLE IF NOT EXISTS usuario(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        """
        con = sqlite3.connect("post_db.sqlite")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        con.close()
    
    def add(self, nome, email, username, password):
        sql = f"""
            INSERT INTO usuario(nome, email, username, password)
            VALUES ('{nome}', '{email}', '{username}', '{password}')
        """
        
        con = sqlite3.connect("post_db.sqlite")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        con.close()
        
    def select(self,id=None, nome=None, email=None, username=None):
        filter_query = "WHERE "
        filtrar = False
        if id:
            filtrar= True
            filter_query += f"id = {id}"
        if nome:
            if filtrar:
                filter_query += " AND "

            filtrar = True
            filter_query += f"nome = {nome}"
            
        if email:
            if filtrar:
                filter_query += " AND "

            filtrar = True
            filter_query += f"email = {email}"
            
        if username:
            if filtrar:
                filter_query += " AND "

            filtrar = True
            filter_query += f"username = {username}"
            
            
        sql = f"""
            SELECT id, nome, email, username FROM usuario
            {filter_query if filtrar else " "}
        """
        
        con = sqlite3.connect("post_db.sqlite")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        data = cursor.fetchall()
        con.close()
        for i in data:
            print(f"{i[0]} | {i[1]} | {i[2]} | {i[3]}")
            
    def update(self,id, nome=None, password=None):
        query_up = " "
        if nome:
            query_up += f"nome = {nome},"
        if password:
            query_up += f"password = {password},"
        
        sql = f"""
            UPDATE usuario SET {query_up[:-1]} WHERE id = {id}
        """
        
        con = sqlite3.connect("post_db.sqlite")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        con.close()
    
    def delete(self,id):
        sql = f"""
            DELETE FROM usuario WHERE id = {id}
        """
        con = sqlite3.connect("post_db.sqlite")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        con.close()