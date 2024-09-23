import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
from .request import detalhes_candidato, detalhes_receitas_candidato

class Candidato:
    def __init__(self, data, id_municipio_candidatura, id_eleicao, id_cargo):
        self._data = data
        self.id_municipio_candidatura = id_municipio_candidatura
        self.id_eleicao = id_eleicao
        self.id_cargo = id_cargo

    @property
    def data(self):
        id_candidato = self._data.get("id", "")
        nome_urna = self._data.get("nomeUrna", "")
        nome_coligacao = self._data.get("nomeColigacao", "")
        candidato = {
            "id": id_candidato,
            "nome": nome_urna,
            "coligacao": nome_coligacao,
        }

        # print("recuperando detalhes do candidato", candidato["nome"], candidato)

        detalhes = detalhes_candidato(
            2024, self.id_municipio_candidatura, self.id_eleicao, id_candidato)

        ocupacao = detalhes.get("ocupacao", "")
        totalDeBens = detalhes.get("totalDeBens", 0)

        # print("recuperando obj dos bens do candidato", candidato["nome"])

        partido = detalhes.get("partido", {})

        candidato["ocupacao"] = ocupacao
        candidato["fotinho"] = detalhes.get("fotoUrl")
        candidato["numero_partido"] = partido.get("numero")
        candidato["numero_candidato"] = detalhes.get("numero")
        candidato["total_de_bens_declarados"] = f"{totalDeBens:.2f}"
        candidato["total_de_bens_declarados_str"] = locale.currency(
            totalDeBens, grouping=True)

        # print("recuperando detalhes do candidato", candidato["nome"], candidato)

        numero_partido = candidato.get("numero_partido")
        numero_candidato = candidato.get("numero_candidato")

        detalhes_financeiros = detalhes_receitas_candidato(
            self.id_eleicao, 2024, self.id_municipio_candidatura, self.id_cargo, numero_partido, numero_candidato, id_candidato)

        #print("recuperando detalhes financeiros do candidato", candidato["nome"], detalhes_financeiros)

        dados_consolidados = detalhes_financeiros.get("dadosConsolidados", False)

        if (not dados_consolidados):
            return candidato
        candidato["dados_consolidados"] = True

        #print("tem dados consolidados", candidato["nome"], dados_consolidados)
        total_doacoes_recebido = dados_consolidados.get("totalRecebido", 0) or 0
        total_doacoes_recebido_str = locale.currency(
            total_doacoes_recebido, grouping=True)
        qtd_doacoes_recebido = dados_consolidados.get("qtdRecebido", 0)
        concentracao_despesas = detalhes_financeiros.get(
            "concentracaoDespesas", 0)
        rank_doadores = detalhes_financeiros.get("rankingDoadores", [])

        candidato["total_doacoes_recebido"] = total_doacoes_recebido
        candidato["total_doacoes_recebido_str"] = total_doacoes_recebido_str
        candidato["qtd_doacoes_recebido"] = qtd_doacoes_recebido
        candidato["concentracao_despesas"] = concentracao_despesas
        candidato["rank_doadores"] = rank_doadores

        return candidato
