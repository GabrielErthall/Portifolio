from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/hello')
def hello_world():
    '''
    Endpoint que exibe uma mensagem incrivel do mundo da programação
    '''
    return {'Hello': 'World'}

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
    '''
    Endpoint para ver os cardapios dos restaurantes
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)

    if response.status_code == 200:
        dados_json = response.json()
        print(dados_json)  
        if restaurante is None:
            return {'Dados': dados_json}

        dados_restaurante = []
        for item in dados_json:
            if item['Company'] == restaurante:
                dados_restaurante.append({
                    "item": item['Item'],
                    "price": item['price'],
                    "description": item['description']
                })
        
        if not dados_restaurante:
            return {'Restaurante': restaurante, 'Mensagem': 'Restaurante não encontrado'}

        return {'Restaurante': restaurante, 'Cardapio': dados_restaurante}
    else:
        print(f'Erro na requisição: {response.status_code} - {response.text}')  
        return {'Erro': f'{response.status_code} - {response.text}'}