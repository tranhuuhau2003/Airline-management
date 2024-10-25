# transactions/book_ticket.py
from flights.flight_manager import FlightManager
from users.passenger import Passenger

def book_ticket(passenger, flight_manager, origin, destination):
    flight = flight_manager.search_flight(origin, destination)
    if flight and flight.seats_available > 0:
        flight.seats_available -= 1
        passenger.book_flight(flight)
    else:
        print("No available seats.")
