# flights/flight_manager.py
from .flight import Flight

class FlightManager:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)
        print(f"Added: {flight}")

    def remove_flight(self, flight_id):
        for flight in self.flights:
            if flight.flight_id == flight_id:
                self.flights.remove(flight)
                print(f"Removed: {flight}")
                return
        print("Flight not found.")

    def search_flight(self, origin, destination):
        for flight in self.flights:
            if flight.origin.lower() == origin.lower() and flight.destination.lower() == destination.lower():
                print(f"Found: {flight}")
                return flight
        print("Flight not found.")
        return None
