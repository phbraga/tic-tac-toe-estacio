
class Jogador:

    def __init__(self, usuario, senha, email, cpf, partidas=0, vitorias=0, derrotas=0, empates=0):
        self.usuario = usuario
        self.senha = senha
        self.email = email
        self.cpf = cpf
        self.partidas = partidas
        self.vitorias = vitorias
        self.derrotas = derrotas
        self.empates = empates