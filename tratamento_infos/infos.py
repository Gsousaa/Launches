#Metodo para realizar a verificação de qual ano ocorreu o maior número de lançamentos
def most_launch_year(data_in):

    data = ([k['launch_year'] for k in data_in if k.get('launch_year')])
    return max(set(data))

#Metodo para verificar a cidade com maior número de lançamentos
def most_city_launch(data_in):

    launchs = ([k['launch_site'] for k in data_in if k.get('launch_site')])
    city_launch = ([k['site_name'] for k in launchs if k.get('site_name')])
    return max(set(city_launch), key = city_launch.count)

#Metodo para verificar a quantidade de lançamentos após 2019
def most_launchs_period(data_in):

    total_launch = len([x for x in data_in if x['launch_year'] >= str(2019) <= str(2021)])
    return total_launch


# print("Ano com mais lançamentos: "+max(set(dados), key = dados.count))
# print("Cidade com mais lançamentos: "+max(set(cidades_lancamentos), key = cidades_lancamentos.count))
# print("Total de Lançamentos: "+ str(total_lancamentos))