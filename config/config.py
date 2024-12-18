from urllib3.exceptions import InsecureRequestWarning
from datetime import datetime 
import requests
import urllib3
urllib3.disable_warnings(InsecureRequestWarning)

class Config:
    def __init__(self):
        self.base_url = "https://dadosabertos.ans.gov.br/FTP/PDA/informacoes_consolidadas_de_beneficiarios-024"
        self.list_states = ["AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO", "MA", "MG", "MS", "MT", 
                            "PA", "PB", "PE", "PI", "PR", "RJ", "RN", "RO", "RR", "RS", "SC", "SE", "SP", "TO", "XX"]
        self.list_url = self.is_url_available()
        self.limit_mb = 4000
        self.terminated_on_exceed = True
        self.timeout = 60
        self.verify = False
        self.stream = True

    def is_url_available(self):
        list_url = []
        for year in range(2022,datetime.now().year+1):
            for month in range(1,12+1):
                for state in self.list_states:
                    if requests.head(f"{self.base_url}/{year}{month:02d}/", self.timeout, self.verify).status_code == 200:
                        list_url.append(f"{self.base_url}/{year}{month:02d}/pda-024-icb-{state}-{year}_{month:02d}.zip")  
        
        return list_url