class FlightTable:
    def __init__(self):
        self.data = [
            {"Flight ID": "AI161E90", "From": "BLR", "To": "BOM", "Price": 5600},
            {"Flight ID": "BR161F91", "From": "BOM", "To": "BBI", "Price": 6750},
            {"Flight ID": "AI161F99", "From": "BBI", "To": "BLR", "Price": 8210},
            {"Flight ID": "VS171E20", "From": "JLR", "To": "BBI", "Price": 5500},
            {"Flight ID": "AS171G30", "From": "HYD", "To": "JLR", "Price": 4400},
            {"Flight ID": "AI131F49", "From": "HYD", "To": "BOM", "Price": 3499}
        ]

    def search_by_city(self, city):
        result = [flight for flight in self.data if flight["From"] == city or flight["To"] == city]
        return result

    def search_flights_from(self, city):
        result = [flight for flight in self.data if flight["From"] == city]
        return result

    def search_between_cities(self, from_city, to_city):
        result = [flight for flight in self.data if flight["From"] == from_city and flight["To"] == to_city]
        return result

    def print_flight_data(self, flights):
        if not flights:
            print("No flights found.")
            return
        print("Flight ID\tFrom\tTo\tPrice")
        for flight in flights:
            print(f"{flight['Flight ID']}\t\t{flight['From']}\t{flight['To']}\t{flight['Price']}")

if __name__ == "__main__":
    flight_table = FlightTable()

    while True:
        print("\nChoose a search parameter:")
        print("1. Flights for a particular City")
        print("2. Flights From a city")
        print("3. Flights between two given cities")
        print("4. Quit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            city = input("Enter the city name: ")
            flights = flight_table.search_by_city(city)
            flight_table.print_flight_data(flights)
        elif choice == "2":
            city = input("Enter the city name: ")
            flights = flight_table.search_flights_from(city)
            flight_table.print_flight_data(flights)
        elif choice == "3":
            from_city = input("Enter the source city: ")
            to_city = input("Enter the destination city: ")
            flights = flight_table.search_between_cities(from_city, to_city)
            flight_table.print_flight_data(flights)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please choose 1, 2, 3, or 4.")
