import time


class OpenFlightData:
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.file = open(self.path, 'r', encoding='utf-8')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

class Timer:
    def __enter__(self):
        self.start = time.time()
        print("Début du traitement…")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Terminé en {time.time() - self.start:.2f}s")
