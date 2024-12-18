import os
import gc
import psutil

class Monitor:
    def __init__(self, limit_mb, terminated_on_exceed, log):

        self.limit_mb = limit_mb
        self.terminated_on_exceed = terminated_on_exceed
        self.log = log

    def __get_memory_usage(self):
        process = psutil.Process(os.getpid())
        return process.memory_info().rss / (1024 * 1024)
    
    def init(self):
        memory_used = self.__get_memory_usage()

        gc.collect()
        if memory_used > self.limit_mb:
            if self.terminate_on_exceed:
                self.log(False,f"Memória máxima atingida: {memory_used}")
                os._exit(1)
