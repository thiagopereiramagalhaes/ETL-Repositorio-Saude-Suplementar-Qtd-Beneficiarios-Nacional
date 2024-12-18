import logging

class Log:
    def __init__(self, status, message):
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(message)s",
            handlers=[
                logging.StreamHandler(),  # Log na saída padrão
                logging.FileHandler("process.log")  # Log em arquivo
            ]
        )

        self.__get_log(status, message)

    def __get_log(self,status, message):
        if status:
            logging.info(message)
        else:
            logging.error(message, exec_info=True)