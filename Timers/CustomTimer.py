import time


class Timer:
    def __init__(self):
        self.__start_time = 0

    def start(self):
        self.__start_time = time.perf_counter()

    def stop(self) -> float:
        return time.perf_counter() - self.__start_time


