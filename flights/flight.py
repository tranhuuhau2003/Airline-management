# flights/flight.py
class Flight:
    def __init__(self, flight_id, origin, destination, time, seats_available):
        self.flight_id = flight_id
        self.origin = origin
        self.destination = destination
        self.time = time
        self.seats_available = seats_available

    def __str__(self):
        return f"Flight {self.flight_id} from {self.origin} to {self.destination} at {self.time} - Seats available: {self.seats_available}"
