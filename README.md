# Launches

O projeto trata-se de uma consulta a API(https://docs.spacexdata.com/#bc65ba60-decf-4289-bb04-4ca9df01b9c1) com o foco de responder as seguintes perguntas:

    • Qual o ano onde houve mais lançamentos?

    • Qual o launch_site onde mais houve lançamentos?

    • Qual foi o total de lançamentos entre os anos de 2019 – 2021?
  
# Estruturação de pastas:

- API:
  Local onde está a comunição por HTTP Request para API pelo método GET, a qual irá retornar um arquivo json com as informações pertinentes.
- tests:
  Testes unitários para cada método presente no código.
- tratamento_infos:
  Possui a divisão em 3 métodos, onde cada um irá solucionar uma pergunta com base no arquivo json gerado pela API.
- Main:
  Por fim, o código main na pasta raiz do projeto, trata-se do arquivo principal onde irá realizar todas as chamadas para a execução do projeto.

# Instruções para instalação e executação do projeto:

- Deve ser realizado o download ou clone do projeto através do git;
- Na pasta raiz do projeto existe um arquivo chamado requirements.txt, nele se encontra um compilado das bibliotecas utilizadas no projeto. Basta rodar a seguir diretamente no terminal da sua ferramenta de visualização do código: pip3 install -r requirements.txt;
- Verificar se a internet está funcionando perfeitamente, pois será necessário para a comunicação com a API;
- Ao final da execução do projeto em caso de funcionamento correto, irá aparecer a seguinte mensagem: "Dados salvos no arquivo respostas.xlsx". Onde estará o arquivo xlsx com as respostas.

