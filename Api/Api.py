import requests #Biblioteca para realizar a requisição HTTP para a API

#Metodo para capturar as informações da API
def get_launches():

    url = "https://api.spacexdata.com/v3/launches"

    response = requests.request("GET",url) #Requisição GET conforme a instrução da documentação
    response_json = response.json() #Conversão dos dados retornados para json

    return response_json



