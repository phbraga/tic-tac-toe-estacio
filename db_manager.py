import sqlite3 as connector
from jogador import Jogador


class DBManager:

    def __init__(self, database):
        self.connector = None
        self.cursor = None
        self.database = database

        self.connect()

    def connect(self):
        try:
            self.connector = connector.connect(self.database)
            self.cursor = self.connector.cursor()
        except (connector.DatabaseError, connector.IntegrityError) as error:
            print("Falha ao se conectar - ", error)

    def check_connection(self):
        if self.connector is None or self.cursor is None:
            self.connect()

    def disconnect(self):
        try:
            self.connector.close()
            self.cursor.close()

            self.connector = None
            self.cursor = None
        except (connector.DatabaseError, connector.IntegrityError) as error:
            print("Falha ao se desconectar - ", error)

    def cadastro(self, jogador):
        self.check_connection()

        try:
            query = f"INSERT INTO jogador (usuario, pwd, email, cpf) VALUES ('{jogador.usuario}', '{jogador.senha}', '{jogador.email}', '{jogador.cpf}');"
            self.cursor.execute(query)
            self.connector.commit()

        except (connector.IntegrityError, connector.DatabaseError, connector.ProgrammingError) as error:
            print(error)
            return False

        return True

    def login(self, usuario, pwd):
        self.check_connection()

        try:
            query = f"SELECT * FROM jogador WHERE usuario='{usuario}';"
            self.cursor.execute(query)
            registro = self.cursor.fetchone()

            if registro is not None:
                jogador = Jogador(*registro)

                if jogador.senha == pwd:
                    return jogador

        except (connector.IntegrityError, connector.DatabaseError, connector.ProgrammingError) as error:
            print(error)

        return None

    def update(self, jogador):
        self.check_connection()

        try:
            query = f"UPDATE jogador SET partidas='{jogador.partidas}', vitorias='{jogador.vitorias}',  derrotas='{jogador.derrotas}', empates='{jogador.empates}' WHERE usuario='{jogador.usuario}';"
            self.cursor.execute(query)
            self.connector.commit()

        except (connector.IntegrityError, connector.DatabaseError, connector.ProgrammingError) as error:
            print(error)
            return False

        return True



