import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '6a7be5ba1148902ddf1962dc277136b6'
HEADER = {'Content-Type ' : 'application/json',
          'trainer_token':TOKEN}
body_registration = {
    "trainer_token": TOKEN,
    "email": "i_dont_know",
    "password": "i_dont_know"
}
body_confirmation = {
    "trainer_token": TOKEN
}
body_create = {
    "name": "GOSHA",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}
body_change = {
    "pokemon_id": "28333",
    "name": "grinch",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}
pokemon_add_pokeball = {
    "pokemon_id": "28333"
}


'''response = requests.post(url=f'{URL}/trainers/reg',headers=HEADER,json= body_registration)

print(response.text)'''

'''response_confirmation = requests.post(url=f'{URL}/trainers/confirm_email',headers=HEADER,json=body_confirmation)
print(response_confirmation.text)
'''
'''response_create = requests.post(url=f'{URL}/pokemons',headers=HEADER,json=body_create)
print(response_create.text)'''

'''message = response_create.json()['message']
print(message)'''

'''response_change = requests.put(url=f'{URL}/pokemons',headers=HEADER,json=body_change)
print(response_change.text)'''
response_addpokeball = requests.post(url=f'{URL}/trainers/add_pokeball',headers=HEADER,json=pokemon_add_pokeball)
print(response_addpokeball.text)
