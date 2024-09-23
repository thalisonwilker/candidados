from .candidato import Candidato
from .request import candidatos as get_candidatos
import json
from tqdm import tqdm

id_cargo = 13

def pega_candidatos_camara(id_municipio="", id_eleicao="", ano_eleicao=""):

    result = get_candidatos(2024, id_municipio, id_cargo, id_eleicao)

    candidatos_aptos = [c for c in result.get("candidatos", []) if c.get("candidatoApto", True)]
    candidatos_json = []

    print("Total de candidatos aptos à câmara de vereadores:", len(candidatos_aptos))

    contador = 0

    for candidato in tqdm(candidatos_aptos, desc="Processando candidatos à câmara", unit="candidato"):
        contador += 1
        candidado_obj = Candidato(candidato, id_municipio, id_eleicao, id_cargo=id_cargo).data
        dados_consolidados = candidado_obj.get("dados_consolidados", False)

        if not dados_consolidados:
            continue
        candidatos_json.append(candidado_obj)

    candidatos_json.sort(key=lambda x: float(x["total_doacoes_recebido"]), reverse=True)
    print("candidatos_json", len(candidatos_json))
    return candidatos_json
