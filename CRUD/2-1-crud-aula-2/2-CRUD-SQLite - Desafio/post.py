import sqlite3

class Post:
    def __init__(self):
        sql = """
            CREATE TABLE IF NOT EXISTS post (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario_id INTEGER NOT NULL,
                titulo TEXT NOT NULL,          
                texto TEXT DEFAULT '',     
                FOREIGN KEY(usuario_id) REFERENCES usuarios(id) 
            )
        """
        
        
        con = sqlite3.connect("post_db.sqlite")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        con.close()
        
    def add(self, usuario_id, titulo, texto):
        sql = f"""
            INSERT INTO post (usuario_id, titulo, texto)
            VALUES ({usuario_id}, '{titulo}', '{texto}')
        """
        con = sqlite3.connect("post_db.sqlite")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        con.close()
        
    def select(self,id=None, usuario_id=None, titulo=None):
        filter_query = "WHERE "
        filtrar = False
        if id:
            filtrar= True
            filter_query += f"id = {id}"
        if usuario_id:
            if filtrar:
                filter_query += " AND "

            filtrar = True
            filter_query += f"usuario_id = {usuario_id}"
        if titulo:
            if filtrar:
                filter_query += " AND "

            filtrar = True
            filter_query += f"titulo = {titulo}"
            
        sql = f"""
            SELECT id, usuario_id, titulo, texto FROM post 
            {filter_query if filtrar else " "}
        """
        con = sqlite3.connect("post_db.sqlite")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        data = cursor.fetchall()
        con.close()
        for i in data:
            print(f"{i[0]} | {i[1]} | {i[2]} | {i[3]} ")
        
        
    def update(self,id, titulo=None, texto=None):
        query_up = " "
        if titulo:
            query_up += f"titulo = {titulo},"
        if texto:
            query_up += f"texto = {texto},"
        
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
            DELETE FROM post WHERE id = {id}
        """
        con = sqlite3.connect("post_db.sqlite")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        con.close()