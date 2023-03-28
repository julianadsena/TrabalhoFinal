import sqlite3

class Data_base:

    def __init__(self, name = 'system.db') -> None:        
        self.name = name

    def connect(self):
        self.connection = sqlite3.connect(self.name)

    def close_connection(self):
        try:
            self.connection.close()
        except:
            pass
    def create_atendimento(self):
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Atendimentos(
                ID INT NOT NULL PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
                DATA TEXT,
                NOME TEXT,
                ATENDENTE TEXT,
                PIS/PASEP/CPF/CNPJ TEXT,
                PCD TEXT,
                AMBIENTE_ATEND TEXT,
                NUMDOC TEXT,
                TIPO_ATEND TEXT,
                CBO TEXT,
                TAR_REALIZADA TEXT,
                RESULTADO TEXT,
                MOTIVO TEXT,
                PRIMARY KEY(ID)
                );
            
            
            
            """) 
    def register_atendimento(self, fullDataSet):

        campos_tabela = ('DATA','NOME','ATENDENTE','PIS/PASEP/CPF/CNPJ','PCD','AMBIENTE_ATEND','NUMDOC',
        'TIPO_ATEND','CBO','TAR_REALIZADA','RESULTADO','MOTIVO')

        qntd = ("?,?,?,?,?,?,?,?,?,?,?,?")
        cursor = self.connection.cursor()

        try:
            cursor.execute(f"""INSERT INTO Atendimentos {campos_tabela}
            VALUES({qntd})""", fullDataSet)
            self.connection.commit()
            return("OK")

        except:
            return "Erro"
    def select_all_atendimentos(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Atendimento ORDER BY NOME")
            atendimento = cursor.fetchall()
            return atendimento
        except:
            pass   
    def delete_atendimentos(self, id):

        try:
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM Atendimentos WHERE NUMDOC = '{id}' ")

            self.connection.commit()

            return "Cadastro de atendimento excluido com sucesso!"

        except:
            return "Erro ao Excluir registro!"
    def update_company(self, fullDataSet):

        cursor = self.connection.cursor()
        cursor.execute(f""" UPDATE Atendimentos set
            DATA = '{fullDataSet[1]}',
            NOME = '{fullDataSet[2]}',
            ATENDENTE = '{fullDataSet[3]}',
            PIS/PASEP/CPF/CNPJ = '{fullDataSet[4]}',
            PCD = '{fullDataSet[5]}',
            AMBIENTE_ATEND = '{fullDataSet[6]}',
            NUMDOC = '{fullDataSet[7]}',
            TIPO_ATEND = '{fullDataSet[8]}',
            TAR_REALIZADA = '{fullDataSet[9]}',
            RESULTADO  = '{fullDataSet[10]}',
            MOTIVO  = '{fullDataSet[11]}'
            WHERE ID = '{fullDataSet[0]}'""")
        self.connection.commit()
    def create_table_users(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    user TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    access TEXT NOT NULL
                    
                );
            
            """)
        except AttributeError:
            print("faça a conexão")
    def insert_user(self, name, user, password, access):

        cursor = self.connection.cursor()
        cursor.execute("""
            INSERT INTO users(name, user, password, access) VALUES(?,?,?,?)
        
        """,(name,user, password, access))
        self.connection.commit()
    def check_user(self, user, password):
        try: 
            cursor = self.connection.cursor()
            cursor.execute("""
                SELECT * FROM users;
            
            """)

            for linha in cursor.fetchall():
                if linha[2].upper() == user.upper() and linha[3] == password and linha[4] == "Administrador":
                    return "Administrador"
 
                elif linha[2].upper() == user.upper() and linha[3] == password and linha[4] == "Usuário":        
                    return "user"

                else:
                    continue
            return "sem acesso"
        except:
            pass

if __name__ == "__main__":

    db = Data_base()
    db.connect()
    db.create_atendimento()
    db.create_table_users()
    db.close_connection()