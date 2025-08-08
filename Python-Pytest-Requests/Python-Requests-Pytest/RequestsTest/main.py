import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'YOU_TOKEN'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}

body_add_pokemons = {
    "name": "Пилигрим",
    "photo_id": 362
}

body_newname = {    
    "pokemon_id": "372563",
    "name": "Лимба",
    "photo_id": 47
}

body_pokeboll = {    
    "pokemon_id": "372563"
}

response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_add_pokemons)
print(response.text)

response_newname = requests.put(url = f'{URL}/pokemons',headers = HEADER,json = body_newname)
print(response_newname.text)

response_pokeboll = requests.post(url = f'{URL}/trainers/add_pokeball',headers = HEADER,json = body_pokeboll)
print(response_pokeboll.text)
