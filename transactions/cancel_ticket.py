# transactions/cancel_ticket.py
from flights.flight_manager import FlightManager
from users.passenger import Passenger

def cancel_ticket(passenger, flight_manager, flight_id):
    for flight in passenger.booked_flights:
        if flight.flight_id == flight_id:
            flight.seats_available += 1
            passenger.cancel_flight(flight)
            return
    print("Flight not found in booked list.")
