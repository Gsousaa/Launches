from Api.Api import get_launches #Chamando as API
from tratamento_infos.infos import * #Chamando as funções
import pandas as pd #Biblioteca para tratamento de dados e tr

#Função central, onde irá chamar os metodos presentes no código para obter os dados

def main():
    data = get_launches()
    period_launch = most_launchs_period(data)
    city = most_city_launch(data)
    year = most_launch_year(data)
    excel = {"Qual o ano onde houve mais lançamentos?": year,
             "Qual o launch_site onde mais houve lançamentos?":city,
             "Qual foi o total de lançamentos entre os anos de 2019 – 2021?": period_launch}
    dataframe = pd.DataFrame(excel, index=[0])


    dataframe.to_excel('respostas.xlsx')

try:
    main()
    print("Dados salvos no arquivo respostas.xlsx")
except BaseException as e:
    print('Erro encontrado: ' + str(e))
