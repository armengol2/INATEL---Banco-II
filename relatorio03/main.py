from database import Database
from helper.writeAjson import writeAJson

db = Database(database="pokedex", collection="pokemons")

pokemons = db.collection.find()

#Querry 1 -  Pokemons com fraqueza a fogo
fraquezas = ["Fire"]
pokemons = list(db.collection.find({"weaknesses": {"$all": fraquezas}}))
writeAJson(pokemons, "pokemons_com_fraqueza_a_fogo")

#Querry 2 - Pokemons que não vem em ovos
pokemons = list(db.collection.find({"egg": "Not in Eggs"}))
writeAJson(pokemons, "pokemons_que_nao_vem_em_ovos")

#Querry 3 - Pokemons com menos de 0.001% de chance de spawn
pokemons = list(db.collection.find({"spawn_chance": {"$lt": 0.001}}))
writeAJson(pokemons, "pokemons_com_spawn_menor_que_0.001%")

#Querry 4 - Pokemons que começam com a letra R
pokemons = list(db.collection.find({"name": {"$regex": "^R", "$options": "i"}}))
writeAJson(pokemons, "pokemons_que_comecam_com_r")

#Querry 5 - Pokemons sem evolução
pokemons = list(db.collection.find({
    "next_evolution": {"$exists": False},
    "prev_evolution": {"$exists": False}
}))
writeAJson(pokemons, "pokemons_sem_evolucao")
