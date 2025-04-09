from pymongo import MongoClient

class Database:
    def __init__(self, db_name='motoristas'):
        try:
            self.client = MongoClient("mongodb://localhost:27017/")
            self.db = self.client[db_name]
            print(f"Conectado ao banco de dados: {db_name}")
        except Exception as e:
            print(f"Erro ao conectar ao MongoDB: {e}")

    def get_collection(self, collection_name):
        return self.db[collection_name]