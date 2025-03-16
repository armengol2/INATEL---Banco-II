import json
from helper.writeAjson import writeAJson

class ProductAnalyzer:
    def __init__(self, db):
        self.db = db

    def total(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {
                "_id": "$data_compra",
                "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}
            }},
            {"$sort": {"_id": 1}}
        ]

        resultado = list(self.db.collection.aggregate(pipeline))
        resultado_formatado = {item["_id"]: item["total"] for item in resultado}

        writeAJson(resultado_formatado, "vendas_por_dia")

        return resultado_formatado

    def vendido(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {
                "_id": "$produtos.descricao",
                "quantidade_total": {"$sum": "$produtos.quantidade"}
            }},
            {"$sort": {"quantidade_total": -1}},
            {"$limit": 1}
        ]

        resultado = list(self.db.collection.aggregate(pipeline))
        produto = resultado[0] if resultado else {"_id": "Nenhum produto", "quantidade_total": 0}

        writeAJson(produto, "produto_mais_vendido")

        return produto

    def gastao(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {
                "_id": {"cliente": "$cliente_id", "data": "$data_compra"},
                "total_gasto": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}
            }},
            {"$sort": {"_id.data": 1, "total_gasto": -1}},
            {"$group": {
                "_id": "$_id.data",
                "cliente_id": {"$first": "$_id.cliente"},
                "total_gasto": {"$first": "$total_gasto"}
            }}
        ]

        resultado = list(self.db.collection.aggregate(pipeline))

        writeAJson(resultado, "cliente_mais_gastou")

        return resultado

    def maisUm(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {
                "_id": "$produtos.descricao",
                "quantidade_total": {"$sum": "$produtos.quantidade"}
            }},
            {"$match": {"quantidade_total": {"$gt": 1}}},
            {"$sort": {"quantidade_total": -1}}
        ]

        resultado = list(self.db.collection.aggregate(pipeline))

        writeAJson(resultado, "produtos_acima_de_um")

        return resultado