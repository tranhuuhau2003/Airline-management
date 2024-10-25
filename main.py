# main.py
from flights.flight import Flight
from flights.flight_manager import FlightManager
from users.passenger import Passenger
from transactions.book_ticket import book_ticket
from transactions.cancel_ticket import cancel_ticket

# Tạo các đối tượng ban đầu
flight_manager = FlightManager()
passenger1 = Passenger("Alice", "P001")

# Thêm chuyến bay vào danh sách
flight1 = Flight("FL123", "New York", "London", "2024-11-10 08:00", 5)
flight2 = Flight("FL456", "Paris", "Tokyo", "2024-12-01 22:30", 3)
flight_manager.add_flight(flight1)
flight_manager.add_flight(flight2)

# Đặt vé cho hành khách
book_ticket(passenger1, flight_manager, "New York", "London")
book_ticket(passenger1, flight_manager, "Paris", "Tokyo")

# Kiểm tra chuyến bay còn lại
print("\nCurrent Flights:")
for flight in flight_manager.flights:
    print(flight)

# Hủy vé cho hành khách
cancel_ticket(passenger1, flight_manager, "FL123")

# Kiểm tra chuyến bay sau khi hủy vé
print("\nUpdated Flights:")
for flight in flight_manager.flights:
    print(flight)
