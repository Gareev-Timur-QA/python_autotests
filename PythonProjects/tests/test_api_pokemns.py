import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '6a7be5ba1148902ddf1962dc277136b6'
HEADER = {'Content-Type ' : 'application/json',
          'trainer_token':TOKEN}
TRAINER_ID = '2648'


def test_status_code():
    response = requests.get(url= f'{URL}/pokemons',params={'trainer_id' : TRAINER_ID })
    assert response.status_code == 200

def test_part_of_response():
        response_get = requests.get(url= f'{URL}/pokemons',params={'trainer_id', TRAINER_ID })
        assert response_get.json()["data"][0]["name"] == 'GOSHA'

@pytest.mark.parametrize('key,value',[('name','GOSHA'),('trainer_id',TRAINER_ID),('id','28335')])        
def test_parametrize(key, value):
      response_parametrize = requests.get(url= f'{URL}/pokemons',params={'trainer_id' : TRAINER_ID })
      assert response_parametrize.json()["data"][0][key] == value
      
        