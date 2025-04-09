from database import Database
from motorista import Motorista
from corrida import Corrida
from passageiro import Passageiro

class MotoristaDAO:
    def __init__(self):
        self.db = Database()
        self.collection = self.db.get_collection('motoristas')

    def criar_motorista(self, nome, cnh):
        motorista = Motorista(nome, cnh)
        self.collection.insert_one(motorista.to_dict())

    def adicionar_corrida(self, cnh, nota, distancia, valor, passageiro_nome, passageiro_documento):
        passageiro = Passageiro(passageiro_nome, passageiro_documento)
        corrida = Corrida(nota, distancia, valor, passageiro)
        self.collection.update_one(
            {"cnh": cnh},
            {"$push": {"corridas": corrida.to_dict()}}
        )

    def listar_motoristas(self):
        return list(self.collection.find())

    def atualizar_motorista(self, cnh, novo_nome):
        self.collection.update_one({"cnh": cnh}, {"$set": {"nome": novo_nome}})

    def deletar_motorista(self, cnh):
        self.collection.delete_one({"cnh": cnh})