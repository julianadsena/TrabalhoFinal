import sqlite3
from sqlite3.dbapi2 import Cursor

class DataBase():
    def __init__(self,name = "system.db") -> None:
        self.name = name

    def conectar(self):
        self.connection = sqlite3.connect(self.name)
    def close_connection(self):
        try:
            self.connection.close()
        except:
            pass
    def create_table_users(self):
        try:
            cursor = self.connection.cursor ()
            cursor.execute ("""
                CREATE TABLE IF NOT EXISTS users(
                id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                user TEXT UNIQUE NOT NULL,
                senha TEXT NOT NULL,
                access TEXT NOT NULL
                );
            """)
        except AttributeError:
            print("conectar")
    def insert_user(self,name,user,senha,access):
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO users (name, user,senha,access) VALUES (?,?,?,?);
            
            """,(name,user,senha,access))
            self.connection.commit()
            self.close_connection()
        
    def check_user(self,user,senha):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                SELECT * FROM users;
            """)
            for linha in cursor.fetchall():
                if linha[2].upper() == user.upper() and linha[3] == senha and linha[4] == "Administrador":
                    return "Administrador"
                    
                elif linha[2].upper() == user.upper() and linha[3] == "123" and linha[4] == "Atendente":
                    return "user"
                else:
                    continue
            return "usuário sem acesso"
        except: 
            pass
if __name__ == "__main__":
    db = DataBase()
    db.conectar()
    db.create_table_users()
    db.close_connection()