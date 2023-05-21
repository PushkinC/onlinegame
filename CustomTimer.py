import time


class Timer:
    def __init__(self):
        self.__start_time = None
        self.data = []

    def start(self):
        self.__start_time = time.perf_counter()

    def stop(self) -> float:
        self.data.append(str(time.perf_counter() - self.__start_time) + '\n')
        return float(self.data[-1])

    def save(self, path):
        with open(path, 'wt') as f:
            f.writelines(self.data)
