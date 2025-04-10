from phase3.gui.exercice.models.flight import Flight


def filter_flights(flights: list[Flight], filters: dict) -> list[Flight]:
    origin = filters.get("origin")
    destination = filters.get("destination")
    min_delay = filters.get("min_delay", 0)

    return [
        flight for flight in flights
        if (origin is None or flight.origin == origin)
        and (destination is None or flight.destination == destination)
        and (flight.delay >= min_delay)
    ]
