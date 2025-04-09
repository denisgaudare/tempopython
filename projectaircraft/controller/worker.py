import threading
import time


class RunwayWorker(threading.Thread):
    def __init__(self, airport, id):
        super().__init__(daemon=True)
        self.airport = airport
        self.runway_id = id
        self.running = True

    def run(self):
        while self.running:
            with self.airport.lock:
                flight = None
                if self.airport.landing_queue:
                    flight = self.airport.landing_queue.popleft()
                    action = "landing"
                elif self.airport.takeoff_queue:
                    flight = self.airport.takeoff_queue.popleft()
                    action = "takeoff"

                if flight:
                    print(f"🛬 [Runway {self.runway_id}] {action.upper()} — {flight.name}")
                    flight.status = "on_ground" if action == "landing" else "flying"
                else:
                    print(f"🛬 [Runway {self.runway_id}] LIBRE")

            time.sleep(2)  # simulate time to complete operation

    def stop(self):
        self.running = False