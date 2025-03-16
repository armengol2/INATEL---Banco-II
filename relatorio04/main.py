from database import Database
from ProductAnalyzer import ProductAnalyzer

db = Database(database="mercado", collection="compras")
db.resetDatabase()

analyzer = ProductAnalyzer(db)

resultado_vendas = analyzer.total()
print("total de vendas ao dia->", resultado_vendas)

produto_vendido = analyzer.vendido()
print("produto mais vendido de cada compra->", produto_vendido)

cliente_gastador = analyzer.gastao()
print("cliente mais gastão->", cliente_gastador)

produtos_vendidos = analyzer.maisUm()
print("produtos que venderam mais de 1->", produtos_vendidos)