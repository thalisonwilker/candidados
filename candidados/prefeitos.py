import json
from .candidato import Candidato
from .request import candidatos as get_candidatos
from tqdm import tqdm

id_cargo = 11

def pega_candidatos_prefeitura(id_municipio="", id_eleicao="", ano_eleicao=""):

    result = get_candidatos(2024, id_municipio, id_cargo, id_eleicao)

    candidatos = result.get("candidatos", [])

    candidatos_json = []

    contador = 0

    for candidato in tqdm(candidatos, desc="Processando candidatos à prefeitua", unit="candidato"):
        contador += 1
        candidado_obj = Candidato(candidato, id_municipio, id_eleicao, id_cargo=id_cargo).data
        candidatos_json.append(candidado_obj)

    candidatos_json.sort(key=lambda x: float(x["total_doacoes_recebido"]), reverse=True)
    return candidatos_json
