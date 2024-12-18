import requests
import zipfile
import urllib3
from io import BytesIO
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)

class Extract:
    def __init__(self, url, stream, timeout, verify, log):
        self.__url = url
        self.__stream = stream
        self.__timeout = timeout
        self.__verify = verify        
        self.__log = log

    def download_data(self):
        try:
            response = requests.get(self.__url, stream=self.__stream, timeout=self.__timeout, verify=self.__verify)
            response.raise_for_status()
            return BytesIO(response.content)
        except requests.RequestException as e:
            self.__log(False, f"Erro ao baixar os dados em: {self.__url}. Motivo: {e}")

    def extract_and_process_zip(self, zip_content):
        try:
            with zipfile.ZipFile(zip_content) as z:
                for file in z.namelist():
                    if file.endswith('csv'):
                        with z.open(file) as csv_file:
                            return csv_file
        except zipfile.BadZipFile as e:
            self.__log(False, f"Erro ao extrair dados: {e}")

    def init(self):
        __zip_content = self.download_data()
        if __zip_content:
            return self.extract_and_process_zip(__zip_content)