


import datetime
from .prefeitos import pega_candidatos_prefeitura
from .vereadores import pega_candidatos_camara
import json

LIMITE_RESULTADOS_PREFEITOS = 5
LIMITE_CORTE_VALOR_DOACAO_PREFEITOS = 100

LIMITE_RESULTADOS_VEREADORES = 15
LIMITE_CORTE_VALOR_DOACAO_VEREADORES = 50

ANO = datetime.datetime.now().year
CODIGO_ELEICAO = "2045202024"
CODIGO_CARGO_PREFEITO = "11"
CODIGO_CARGO_VEREADOR = "13"

cidades = [
    # Belém/PA
    "04278:Belem/PA",
    # Ananindeua/PA
    "04154:Ananindeua/PA",
    #Marituba/PA
    "04642:Marituba/PA",
    #Benevides/PA
    "04294:Benevidades/PA",
    #SANTA ISABEL DO PARÁ
    "05290:SANTA ISABEL DO PARÁ/PA",
    #SANTO ANTÔNIO DO TAUÁ
    "05398:SANTO ANTÔNIO DO TAUÁ/PA",
    #SÃO PAULO
    "71072:SÃO PAULO/SP",
    # #RIO DE JANEIRO
    "60011:RIO DE JANEIRO/RJ"
]

def go():
    candidados = {}
    for ciade in cidades:
        cidade_id, cidade = ciade.split(":")
        print("Processando candidatos à prefeitura de:", cidade)
        candidatos_prefeitura = pega_candidatos_prefeitura(id_municipio=cidade_id, id_eleicao=CODIGO_ELEICAO, ano_eleicao=ANO)
        candidatos_prefeitura = [c for c in candidatos_prefeitura if c["total_doacoes_recebido"] > LIMITE_CORTE_VALOR_DOACAO_PREFEITOS]

        print("Processando candidatos à câmara de vereadores de:", cidade)
        candidatos_camara_vereadores = pega_candidatos_camara(id_municipio=cidade_id, id_eleicao=CODIGO_ELEICAO, ano_eleicao=ANO)
        print(candidatos_camara_vereadores)
        candidatos_camara_vereadores = [c for c in candidatos_camara_vereadores if c["total_doacoes_recebido"] > LIMITE_CORTE_VALOR_DOACAO_VEREADORES]

        candidados[cidade_id] = {
            "cidade": cidade,
            "candidatos_prefeitura": candidatos_prefeitura[:LIMITE_RESULTADOS_PREFEITOS],
            "candidatos_camara_vereadores": candidatos_camara_vereadores[:LIMITE_RESULTADOS_VEREADORES]
        }
        with open(f'candidados.json', 'w', encoding='utf-8') as f:
            json.dump(candidados, f, ensure_ascii=False, indent=4)
