from database import Database

db = Database("bolt://localhost:7687", "neo4j", "neo4jneo4j")

#Questão 1 - A
print(f"-------------------------- Dados do professor renzo --------------------")
query1 = "MATCH (t:Teacher {name: 'Renzo'}) RETURN t.ano_nasc AS ano_nasc, t.cpf AS cpf"
for record in db.execute_query(query1):
    print(f"ano de nascimento: {record['ano_nasc']}, CPF: {record['cpf']}")

#Questão 1 - B
print(f"-------------------------- Nomes que começam com M --------------------")
query2 = "MATCH (t:Teacher) WHERE t.name STARTS WITH 'M' RETURN t.name AS name, t.cpf AS cpf"
for record in db.execute_query(query2):
    print(f"Nome: {record['name']}, CPF: {record['cpf']}")

#Questão 1 - C
print(f"-------------------------- Todas as cidades --------------------")
query3 = "MATCH (c:City) RETURN c.name AS name"
for record in db.execute_query(query3):
    print(f"Cidade: {record['name']}")

#Questão 1 - D
print(f"-------------------------- Escolas especificas --------------------")
query4 = """
MATCH (s:School) 
WHERE s.number >= 150 AND s.number <= 550 
RETURN s.name AS name, s.address AS address, s.number AS number
"""
for record in db.execute_query(query4):
    print(f"escola: {record['name']}, endereço: {record['address']}, número: {record['number']}")

#Questão 2 - A
print(f"--------------------- Professor: mais novo e mais velho ---------------")
query5 = """
MATCH (t:Teacher)
RETURN min(t.ano_nasc) AS mvelho, max(t.ano_nasc) AS mjovem
"""
for record in db.execute_query(query5):
    print(f"mais velho: {record['mvelho']}, mais jovem: {record['mjovem']}")

#Questão 2 - B
print(f"-------------------------- Média aritmetica da população --------------------")
query6 = "MATCH (c:City) RETURN avg(c.population) AS media"
for record in db.execute_query(query6):
    print(f"média: {record['media']}")

#Questão 2 - C
print(f"----------------------- Cidade especifica com nome formatado ----------------")
query7 = """
MATCH (c:City {cep: '37540-000'}) 
RETURN replace(c.name, 'a', 'A') AS formatado
"""
for record in db.execute_query(query7):
    print(f"nome formatado: {record['formatado']}")

#Questão 2 - D
print(f"----------------------- 3° letra do nome de cada professor ------------------")
query8 = """
MATCH (t:Teacher) 
RETURN t.name AS nome, substring(t.name, 2, 1) AS Letra3
"""
for record in db.execute_query(query8):
    print(f"professor: {record['nome']}, 3°letra: {record['Letra3']}")

db.close()