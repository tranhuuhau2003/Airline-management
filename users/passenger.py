# users/passenger.py
class Passenger:
    def __init__(self, name, passenger_id):
        self.name = name
        self.passenger_id = passenger_id
        self.booked_flights = []

    def book_flight(self, flight):
        self.booked_flights.append(flight)
        print(f"{self.name} booked: {flight}")

    def cancel_flight(self, flight):
        if flight in self.booked_flights:
            self.booked_flights.remove(flight)
            print(f"{self.name} canceled: {flight}")
        else:
            print("Flight not booked by this passenger.")
