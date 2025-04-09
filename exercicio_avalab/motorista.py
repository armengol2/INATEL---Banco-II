class Motorista:
    def __init__(self, nome, cnh, corridas=None):
        self.nome = nome
        self.cnh = cnh
        self.corridas = corridas if corridas else []

    def to_dict(self):
        return {
            "nome": self.nome,
            "cnh": self.cnh,
            "corridas": [corrida.to_dict() for corrida in self.corridas]
        }