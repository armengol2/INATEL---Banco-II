class GamerDatabase:
    def __init__(self, database):
        self.db = database

    #Criação das entidades
    def create_player(self, name, player_id):
        query = "CREATE (:Player {name: $name, id: $player_id})"
        parameters = {"name": name, "player_id": player_id}
        self.db.execute_query(query, parameters)

    def create_match(self, match_id):
        query = "CREATE (:Match {id: $match_id})"
        parameters = {"match_id": match_id}
        self.db.execute_query(query, parameters)

    def register_player_in_match(self, player_id, match_id, pontuacao):
        query = """
        MATCH (p:Player {id: $player_id}), (m:Match {id: $match_id})
        CREATE (p)-[:JOGOU {pontuacao: $pontuacao}]->(m)
        """
        parameters = {"player_id": player_id, "match_id": match_id, "pontuacao": pontuacao}
        self.db.execute_query(query, parameters)

    #Leitura das informações
    def get_players(self):
        query = "MATCH (p:Player) RETURN p.name AS name, p.id AS id"
        results = self.db.execute_query(query)
        return [(r["id"], r["name"]) for r in results]

    def get_matches(self):
        query = "MATCH (m:Match) RETURN m.id AS id"
        results = self.db.execute_query(query)
        return [r["id"] for r in results]

    def get_match_info(self, match_id):
        query = """
        MATCH (p:Player)-[j:JOGOU]->(m:Match {id: $match_id})
        RETURN p.name AS player_name, p.id AS player_id, j.pontuacao AS pontuacao
        """
        parameters = {"match_id": match_id}
        return self.db.execute_query(query, parameters)

    def get_player_history(self, player_id):
        query = """
        MATCH (p:Player {id: $player_id})-[j:JOGOU]->(m:Match)
        RETURN m.id AS match_id, j.pontuacao AS pontuacao
        """
        parameters = {"player_id": player_id}
        return self.db.execute_query(query, parameters)

    #Atualização
    def update_player_name(self, player_id, new_name):
        query = "MATCH (p:Player {id: $player_id}) SET p.name = $new_name"
        parameters = {"player_id": player_id, "new_name": new_name}
        self.db.execute_query(query, parameters)

    #Exclusão
    def delete_player(self, player_id):
        query = "MATCH (p:Player {id: $player_id}) DETACH DELETE p"
        parameters = {"player_id": player_id}
        self.db.execute_query(query, parameters)

    def delete_match(self, match_id):
        query = "MATCH (m:Match {id: $match_id}) DETACH DELETE m"
        parameters = {"match_id": match_id}
        self.db.execute_query(query, parameters)