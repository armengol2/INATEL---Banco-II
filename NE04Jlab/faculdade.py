from database import Database

db = Database("bolt://localhost:7687", "neo4j", "neo4jneo4j") 

queries = [
    "CREATE(:Teacher{name:'Aline',ano_nasc:1998,cpf:'123.456.789-10'})",
    "CREATE(:Teacher{name:'Marisa',ano_nasc:1950,cpf:'012.345.678-91'})",
    "CREATE(:Teacher{name:'Elza',ano_nasc:1987,cpf:'901.234.567-89'})",
    "CREATE(:Teacher{name:'Marcelo',ano_nasc:1978,cpf:'890.123.456-78'})",
    "CREATE(:Teacher{name:'Renzo',ano_nasc:1956,cpf:'789.012.345-67'})",
    "CREATE(:Teacher{name:'Justino',ano_nasc:1995,cpf:'678.901.234-56'})",

    "CREATE(:School{name:'Sanico Teles',address:'R. OlÁvo Marquês',number:181})",
    "CREATE(:School{name:'SinhÁ Moreira',address:'Av. Dr. Delfim Moreira',number:509})",
    "CREATE(:School{name:'Zenaide',address:'Conj. Hab. Gilberto Rossetti',number:332})",
    "CREATE(:School{name:'Luis Machado Filho',address:'R. LuÍs Machado',number:100})",

    "CREATE(:City{name:'Santa Rita do SapucaÍ', cep:'37540-000', population:43753})",
    "CREATE(:City{name:'Serra da Saudade', cep:'35617-000', population:776})",
    "CREATE(:City{name:'Cidadezinha', cep:'13737-635', population:68980})",
    "CREATE(:State{name:'Minas Gerais', country:'Brasil'})",

    "MATCH(t:Teacher{name:'Renzo'}),(s:School{name:'Luis Machado Filho'}) CREATE(t)-[:WORKS]->(s)",
    "MATCH(t:Teacher{name:'Justino'}),(s:School{name:'Zenaide'}) CREATE(t)-[:WORKS]->(s)",
    "MATCH(t:Teacher{name:'Aline'}),(s:School{name:'SinhÁ Moreira'}) CREATE(t)-[:WORKS]->(s)",
    "MATCH(t:Teacher{name:'Marcelo'}),(s:School{name:'Sanico Teles'}) CREATE(t)-[:WORKS]->(s)",
    "MATCH(t:Teacher{name:'Elza'}),(s:School{name:'SinhÁ Moreira'}) CREATE(t)-[:WORKS]->(s)",
    "MATCH(t:Teacher{name:'Marisa'}),(s:School{name:'Sanico Teles'}) CREATE(t)-[:WORKS]->(s)",

    "MATCH(s:School{name:'SinhÁ Moreira'}),(c:City{name:'Santa Rita do SapucaÍ'}) CREATE(s)-[:LOCATES]->(c)",
    "MATCH(s:School{name:'Sanico Teles'}),(c:City{name:'Santa Rita do SapucaÍ'}) CREATE(s)-[:LOCATES]->(c)",
    "MATCH(s:School{name:'Luis Machado Filho'}),(c:City{name:'Serra da Saudade'}) CREATE(s)-[:LOCATES]->(c)",
    "MATCH(s:School{name:'Zenaide'}),(c:City{name:'Cidadezinha'}) CREATE(s)-[:LOCATES]->(c)",

    "MATCH(c:City{name:'Santa Rita do SapucaÍ'}),(st:State{name:'Minas Gerais'}) CREATE(c)-[:BELONGS]->(st)",
    "MATCH(c:City{name:'Serra da Saudade'}),(st:State{name:'Minas Gerais'}) CREATE(c)-[:BELONGS]->(st)",
    "MATCH(c:City{name:'Cidadezinha'}),(st:State{name:'Minas Gerais'}) CREATE(c)-[:BELONGS]->(st)"
]

for query in queries:
    db.execute_query(query)

db.close()