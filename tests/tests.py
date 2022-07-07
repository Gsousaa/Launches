import requests
import json
from tratamento_infos.infos import *

#Teste para validação da API
def test_returnApi():
    response = requests.get("https://api.spacexdata.com/v3/launches")
    print(response.headers["Content-Type"])
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"

#Os testes abaixos são baseados em um arquivo json de teste salvo dentro de sua pasta e servem para validar os métodos.
def test_most_city_launch():
    with open(r"test_data_in.json") as data:
        data_in = json.load(data)
    cidade =  most_city_launch(data_in)
    assert cidade != ""

def test_most_launchs():
    with open(r"test_data_in.json") as data:
        data_in = json.load(data)
    launchs = most_launchs_period(data_in)
    assert launchs > 0

def test_most_launch_year():
    with open(r"test_data_in.json") as data:
        data_in = json.load(data)
    year = most_launch_year
    assert year != ""