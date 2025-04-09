import time

from projectaircraft.models.flight import Flight


class ControlTower:
    def __init__(self, airport):
        self.airport = airport

    def request_landing(self, flight:Flight):
        print(f"✈️  Landing request: {flight.name}")
        self.airport.landing_queue.append(flight)

    def request_takeoff(self, flight:Flight):
        print(f"🛫 Takeoff request: {flight.name}")
        self.airport.takeoff_queue.append(flight)

    def process_next_operation(self):
        if self.airport.landing_queue:
            flight = self.airport.landing_queue.popleft()
            print(f"✅ Landing: {flight.name}")
            flight.status = "on_ground"
        elif self.airport.takeoff_queue:
            flight = self.airport.takeoff_queue.popleft()
            print(f"✅ Takeoff: {flight.name}")
            flight.status = "flying"
        else:
            print("🟡 No operations to process right now.")

    def check_status(self):
        for q in (self.airport.landing_queue, self.airport.takeoff_queue):
            for f in q:
                print(f"⚠️ {f.name}/{f.status}", end=".")
        print("")