# Airline Reservation System
# Scenario: You are developing an airline reservation system. 
# Each flight has a unique flight number, a list of reserved seats, and a list of passengers. 
# You need to reserve seats for new passengers and update the flight information accordingly.

# Question: Write a function that takes a dictionary representing the flights 
# (flight numbers as keys and a dictionary with reserved seats and passengers as values),
#  a flight number, a list of new passengers, and a list of seats they wish to reserve. 
# Return whether the reservation was successful and update the flight information.

def reserve_seat(flight_details, flight_number, new_passenger_list, list_of_seat_to_be_reserved):
    available_flights = list(flight_details.keys())
    message = []
    if flight_number in available_flights:
        available_seat = [seat for seat, passenger in flight_details[flight_number].items() if passenger == ""]
        for passenger in new_passenger_list:
            if list_of_seat_to_be_reserved[new_passenger_list.index(passenger)] in available_seat:
                flight_details[flight_number][list_of_seat_to_be_reserved[new_passenger_list.index(passenger)]] = passenger
                available_seat.remove(list_of_seat_to_be_reserved[new_passenger_list.index(passenger)])
                message.append(f"Reservation successful for {passenger} with seat no: {list_of_seat_to_be_reserved[new_passenger_list.index(passenger)]}")
            else:
                message.append(f"Reservation unsuccessful for {passenger}")
    else:
        message = "Flight number unavailable!"
    return flight_details, message

flight_details = {"F001": {"S001": "Ramesh", "S002": "", "S003": "Raju"},
                  "F002": {"S001": "", "S002": "", "S003": "Sanjay"}}

new_passenger = ["Mithra", "Hari", "Saran"]
seat_to_be_reserved = ["S002", "S001", "S002"]

print(reserve_seat(flight_details, "F001", new_passenger, seat_to_be_reserved))
