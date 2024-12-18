from config import config
from log import log
from extract import extract
from transform import transform
from load import load
from monitor import monitor
from tqdm import tqdm 
import time

class Main:
    def __init__(self):
        self.log = log.Log()
        self.extract = extract.Extract()
        self.transform = transform.Transform()
        self.load = load.Load()
        self.config = config.Config()
        self.monitor = monitor.Monitor(self.config.limit_mb, self.config.terminated_on_exceed, self.log)

    def init(self):
        try:
            self.log(True, "Iniciando o processo de ETL.")
            self.log(True, "Isso pode demorar um pouco!")
            self.log(True, f"Consumo máximo de memória definido:{config.limit_mb}")
            self.log(True, f"Requisição feita para: {config.base_url}")

            with tqdm(total=len(self.config.list_url), desc="Processando dados", unit="processo") as pbar:
                for url in self.config.list_url:

                    __result_extract = self.extract(url, self.config.stream, self.config.timeout, self.config.verify, self.log).init()
                    __result_transform = self.transform(__result_extract).init()
                    __result_load = self.load(__result_transform).init()

                    del __result_extract
                    del __result_transform
                    del __result_load
                    self.monitor.init()
                    pbar.update(1)
                    time.sleep(2)
            
            self.log(True, "Processo de ETL concluído com sucesso.")
        
        except Exception as e:
            self.log(False, f"Erro fatal durante a execução: {e}")

if __name__ == "__main__":
    Main.init()