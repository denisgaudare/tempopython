import threading
import time


class RunwayWorker(threading.Thread):
    def __init__(self, airport, runway_id):
        super().__init__(daemon=True)
        self.airport = 0 # todo ??
        self.runway_id = 0 # todo ??
        self.running = 0 # todo ??

    def run(self):
        while self.running:
            with self.airport.lock:
                # TODO Gerer atterissages et decollages
                pass

            time.sleep(2)  # simulate time to complete operation

    def stop(self):
        self.running = False