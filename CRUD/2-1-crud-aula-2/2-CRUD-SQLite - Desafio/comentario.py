import sqlite3

class Comentario:
    def __init__(self):
        sql = f"""
            CREATE TABLE IF NOT EXISTS comentario (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario_id INTEGER,
                post_id INTEGER,
                texto TEXT NOT NULL,
                FOREIGN KEY(usuario_id) REFERENCES usuarios(id),
                FOREIGN KEY(post_id) REFERENCES POST(id) 
            )
        """
        con = sqlite3.connect("post_db.sqlite")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        con.close()
        
    def add(self, usuario_id, post_id, texto):
        sql = f"""
            INSERT INTO comentarios (usuario_id, post_id, texto)
            VALUES ({usuario_id}, {post_id}, '{texto}')
        """
        con = sqlite3.connect("post_db.sqlite")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        con.close()
        
    def select(self, post_id):
        sql = f"""
            SELECT id, usuario_id, post_id, texto
            FROM comentario
            WHERE post_id = {post_id}
        """
        con = sqlite3.connect("post_db.sqlite")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        data = cursor.fetchall()
        con.close()
        for i in data:
            pass
        
        
    def delete(self,id, usuario_id):
        sql = f"""
            DELETE FROM comentario
            WHERE id = {id} AND usuario_id = {usuario_id}
        """
        con = sqlite3.connect("post_db.sqlite")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        con.close()