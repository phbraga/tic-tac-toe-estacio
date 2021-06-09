import db_manager
from jogador import Jogador

db = db_manager.DBManager("tictactoe.db")

# jogador = Jogador(usuario="eduardo",
#                   cpf="99999999999",
#                   email="eduard@gmail.com",
#                   senha="12344321")

# db.cadastro(jogador)

jogador = db.login("eduardo", "12344321")
jogador.partidas += 1
jogador.vitorias += 1

if db.update(jogador):
    print("update 1 realizado com sucesso")

jogador2 = db.login("pedro", "12344321")
jogador2.partidas += 1
jogador2.empates += 1

if db.update(jogador2):
    print("update 2 realizado com sucesso")

db.disconnect()

