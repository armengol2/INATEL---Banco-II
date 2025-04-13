from neo4j import GraphDatabase
URI = "bolt://localhost:7687"
USER = "neo4j"
PASSWORD = "neoneo4j"

def consul(driver):
    with driver.session() as session:

        resultado1 = session.run("""
            MATCH (r:Pessoa)-[:RESPONSÁVEL_POR]->(p:Pessoa {nome: "Rodrigo Armengol"})
            RETURN r.nome AS nome
        """)
        print("Quem é responsável por mim?")
        for record in resultado1:
            print("->", record["nome"])
        print()

        resultado2 = session.run("""
            MATCH (e:Estudante)
            RETURN COUNT(*) AS total
        """)
        print("Quantos ainda são estudantes?")
        for record in resultado2:
            print("->", record["total"])
        print()

        resultado3 = session.run("""
            MATCH (p:Pessoa)-[:DONO_DE]->(a:Animal {nome: "Billy"})
            RETURN p.nome AS nome
        """)
        print("quem é o dono do Billy?")
        for record in resultado3:
            print("->", record["nome"])
        print()

        resultado4 = session.run("""
            MATCH (a:Animal)
            RETURN a.raça AS raca
        """)
        print("Raça de todos os animais:")
        for record in resultado4:
            print("->", {record['raca']})
        print()

if __name__ == "__main__":
    driver = GraphDatabase.driver(URI, auth=(USER, PASSWORD))
    consul(driver)
    driver.close()