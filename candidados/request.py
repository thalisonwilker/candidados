
from time import sleep
import random
from candidados import *

sleep_durations = [.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]

TSE_REST_API_URL = 'https://divulgacandcontas.tse.jus.br/divulga/rest/v1'

from tqdm import tqdm
import requests
import json
import random

def request(url):
    try:
        response = requests.get(f'{TSE_REST_API_URL}{url}')
        response.raise_for_status()
        sleep(random.choice(sleep_durations))
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        raise http_err
    except requests.exceptions.RequestException as req_err:
        print(f'Error occurred: {req_err}')
        raise req_err
    except json.JSONDecodeError as json_err:
        print(f'Error decoding JSON: {json_err}')
        raise json_err
    except Exception as err:
        print(f'An unexpected error occurred: {err}')
        raise err

def candidatos(ano, id_municipio_candidatura, codigo_cargo, id_eleicao):
    return request(f'/candidatura/listar/{ano}/{id_municipio_candidatura}/{id_eleicao}/{codigo_cargo}/candidatos')

def detalhes_candidato(ano, id_municipio_candidatura, id_eleicao, id_candidato):
    return request(f'/candidatura/buscar/{ano}/{id_municipio_candidatura}/{id_eleicao}/candidato/{id_candidato}')

def detalhes_receitas_candidato(id_eleicao, ano, id_municipio, id_cargo, numero_partido, numero_candidato, id_candidato):
    return request(f'/prestador/consulta/{id_eleicao}/{ano}/{id_municipio}/{id_cargo}/{numero_partido}/{numero_candidato}/{id_candidato}')