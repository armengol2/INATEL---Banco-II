from database import Database
from games_database import GamerDatabase

db = Database("bolt://98.82.22.125:7687", "neo4j", "values-boresights-drinks")
db.drop_all()

gamer_db = GamerDatabase(db)

gamer_db.create_player("Rodrigo", "player1")
gamer_db.create_player("Thiaguera", "player2")
gamer_db.create_player("Machine", "player3")

gamer_db.create_match("match1")

gamer_db.register_player_in_match("player1", "match1", 150)
gamer_db.register_player_in_match("player2", "match1", 200)
gamer_db.register_player_in_match("player3", "match1", 180)

print("---- Lista de todos os jogadores do banco ----")
for id, name in gamer_db.get_players():
    print(f"{id}: {name}")

print("---- Informações da partida match1 ----")
for info in gamer_db.get_match_info("match1"):
    print(info)

print("---- Histórico do melhor jogador(Rodrigo) ----")
for hist in gamer_db.get_player_history("player1"):
    print(hist)

gamer_db.update_player_name("player3", "Carlos Eduardo")

db.close()