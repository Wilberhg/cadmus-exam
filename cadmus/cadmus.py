import requests

class VagasCadmus:

    def __init__(self, url) -> None:
        self.url = url

    def get_body(self):
        vagas_cadmus = requests.get(self.url)
        if vagas_cadmus.status_code == 200:
            vagas_cadmus = vagas_cadmus.json()
        else:
            vagas_cadmus = []
        return vagas_cadmus

    def list_values(self, vagas_cadmus):
        vagas_excel = []
        for vaga in vagas_cadmus:
            vagas_excel.append([
                vaga.get("name"),
                vaga.get("cidade_Regi_o__c"),
                vaga.get("descricao_da_vaga__c")
            ])
        return vagas_excel