# lab2
# Zadanie polega wykorzystaniu context managera jako timera. Tak uzupełnij poniższa klasę aby przeszedł test
# /tests/context_manager/test_lab2.py

import time


class Timer:

    def __enter__(self):
        self.time = time.time()

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.time = int(time.time() - self.time)