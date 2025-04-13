from neo4j import GraphDatabase

URI = "bolt://localhost:7687"
USER = "neo4j"
PASSWORD = "neoneo4j"

def criaNos(driver):
    with driver.session() as session:
        session.run("""
            CREATE 
            (:Pessoa:Estudante {
                nome: "Rodrigo Armengol",
                sexo: "Masculino",
                idade: 22,
                Altura: 1.84
            }),
            (:Pessoa:Engenheira {
                nome: "Nuria Fernandez",
                sexo: "Feminino",
                idade: 50,
                Altura: 1.70
            }),
            (:Pessoa:Empreiteiro {
                nome: "Rogério de Oliveira",
                sexo: "Masculino",
                idade: 55,
                Altura: 1.86
            }),
            (:Pessoa:Estudante {
                nome: "Pedro Armengol",
                sexo: "Masculino",
                idade: 19,
                Altura: 1.83
            }),
            (:Pessoa:Fazendeiro {
                nome: "Roseni de Oliveira",
                sexo: "Masculino",
                idade: 85,
                Altura: 1.80
            }),
            (:Pessoa:Aposentada {
                nome: "Carmen Braga",
                sexo: "Feminino",
                idade: 64,
                Altura: 1.68
            }),
            (:Pessoa:Motorista {
                nome: "Newton Goto",
                sexo: "Masculino",
                idade: 49,
                Altura: 1.70
            }),
            (:Pessoa:Confeiteira {
                nome: "Andreia Fernandez",
                sexo: "Feminino",
                idade: 47,
                Altura: 1.60
            }),
            (:Pessoa:Estudante {
                nome: "Felipe Goto",
                sexo: "Masculino",
                idade: 17,
                Altura: 1.71
            }),
            (:Pessoa:Estudante {
                nome: "Miguel Goto",
                sexo: "Masculino",
                idade: 14,
                Altura: 1.68
            }),
            (:Pessoa:Corretora {
                nome: "Regina de Oliveira",
                sexo: "Feminino",
                idade: 55,
                Altura: 1.68
            }),
            (:Pessoa:Estudante {
                nome: "José Vitor de Oliveira",
                sexo: "Masculino",
                idade: 27,
                Altura: 1.70
            }),
            (:Animal:Cachorro {
                nome: "Nala",
                sexo: "Feminina",
                idade: 10,
                raça: "Beagle"
            }),
            (:Animal:Cachorro {
                nome: "Sheriff",
                sexo: "Masculino",
                idade: 13,
                raça: "Pitbull"
            }),
            (:Animal:Cachorro {
                nome: "Billy",
                sexo: "Masculino",
                idade: 9,
                raça: "Border collie"
            }),
            (:Animal:Passaro {
                nome: "Pirata",
                sexo: "Masculino",
                idade: 30,
                raça: "Papagaio-verdadeiro"
            })
        """)
        print("Membros da árvore adicionados")

def criarRelacao(driver):
    with driver.session() as session:
        ######### Relação 1°: IRMÃO DE ALGUÊM
        session.run("""
            MATCH (p1:Pessoa {nome: "Rodrigo Armengol"}), (p2:Pessoa {nome: "Pedro Armengol"})
            CREATE (p1)-[:IRMÃ_OU_IRMÃO_DE]->(p2)
        """)
        session.run("""
            MATCH (p1:Pessoa {nome: "Felipe Goto"}), (p2:Pessoa {nome: "Miguel Goto"})
            CREATE (p1)-[:IRMÃ_OU_IRMÃO_DE]->(p2)
        """)
        session.run("""
            MATCH (p1:Pessoa {nome: "Rogério de Oliveira"}), (p2:Pessoa {nome: "Regina de Oliveira"})
            CREATE (p1)-[:IRMÃ_OU_IRMÃO_DE]->(p2)
        """)
        session.run("""
            MATCH (p1:Pessoa {nome: "Nuria Fernandez"}), (p2:Pessoa {nome: "Andreia Fernandez"})
            CREATE (p1)-[:IRMÃ_OU_IRMÃO_DE]->(p2)
        """)
        ######### Relação 2°: CASADOS
        session.run("""
            MATCH (p1:Pessoa {nome: "Rogério de Oliveira"}), (p2:Pessoa {nome: "Nuria Fernandez"})
            CREATE (p1)-[:CASADO_COM]->(p2)
        """)
        session.run("""
            MATCH (p1:Pessoa {nome: "Newton Goto"}), (p2:Pessoa {nome: "Andreia Fernandez"})
            CREATE (p1)-[:CASADO_COM]->(p2)
        """)
        session.run("""
            MATCH (p1:Pessoa {nome: "Roseni de Oliveira"}), (p2:Pessoa {nome: "Carmen Braga"})
            CREATE (p1)-[:CASADO_COM]->(p2)
        """)
        ######### Relação 3°: DONOS
        session.run("""
            MATCH (p1:Pessoa {nome: "Roseni de Oliveira"}), (p2:Animal {nome: "Sheriff"})
            CREATE (p1)-[:DONO_DE{desde: 2009}]->(p2)
        """)
        session.run("""
            MATCH (p1:Pessoa {nome: "Roseni de Oliveira"}), (p2:Animal {nome: "Billy"})
            CREATE (p1)-[:DONO_DE{desde: 2012}]->(p2)
        """)
        session.run("""
            MATCH (p1:Pessoa {nome: "Andreia Fernandez"}), (p2:Animal {nome: "Nala"})
            CREATE (p1)-[:DONO_DE{desde: 2010}]->(p2)
        """)
        session.run("""
            MATCH (p1:Pessoa {nome: "Andreia Fernandez"}), (p2:Animal {nome: "Pirata"})
            CREATE (p1)-[:DONO_DE{desde: 1985}]->(p2)
        """)
        ######### Relação 4°: Responsavel por
        session.run("""
            MATCH (p1:Pessoa {nome: "Regina de Oliveira"}), (p2:Pessoa {nome: "José Vitor de Oliveira"})
            CREATE (p1)-[:RESPONSÁVEL_POR]->(p2)
        """)
        session.run("""
            MATCH (p1:Pessoa {nome: "Rogério de Oliveira"}), (p2:Pessoa {nome: "Rodrigo Armengol"})
            CREATE (p1)-[:RESPONSÁVEL_POR]->(p2)
        """)
        session.run("""
            MATCH (p1:Pessoa {nome: "Rogério de Oliveira"}), (p2:Pessoa {nome: "Pedro Armengol"})
            CREATE (p1)-[:RESPONSÁVEL_POR]->(p2)
        """)
        session.run("""
            MATCH (p1:Pessoa {nome: "Newton Goto"}), (p2:Pessoa {nome: "Felipe Goto"})
            CREATE (p1)-[:RESPONSÁVEL_POR]->(p2)
        """)
        session.run("""
            MATCH (p1:Pessoa {nome: "Newton Goto"}), (p2:Pessoa {nome: "Miguel Goto"})
            CREATE (p1)-[:RESPONSÁVEL_POR]->(p2)
        """)
        print("Relacionamentos criados")

if __name__ == "__main__":
    driver = GraphDatabase.driver(URI, auth=(USER, PASSWORD))
    criaNos(driver)
    criarRelacao(driver)
    driver.close()