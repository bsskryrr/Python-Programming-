import datetime

class Vehicle:
    def __init__(self, vehicle_number, owner_name, test_date, pollution_level):
        self.vehicle_number = vehicle_number
        self.owner_name = owner_name
        self.test_date = test_date
        self.pollution_level = pollution_level
        self.valid_until = test_date + datetime.timedelta(days=365)  # valid for 1 year


class PollutionControlSystem:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle_number, owner_name, test_date, pollution_level):
        vehicle = Vehicle(vehicle_number, owner_name, test_date, pollution_level)
        self.vehicles.append(vehicle)
        print(f"Vehicle {vehicle_number} added successfully!")

    def check_validity(self, vehicle_number):
        for vehicle in self.vehicles:
            if vehicle.vehicle_number == vehicle_number:
                if vehicle.valid_until < datetime.date.today():
                    print(f"Pollution test for vehicle {vehicle_number} has expired!")
                else:
                    print(f"Pollution test for vehicle {vehicle_number} is valid until {vehicle.valid_until}")
                return
        print(f"Vehicle {vehicle_number} not found!")

    def generate_report(self):
        print("\nVehicle Pollution Control Report:")
        for vehicle in self.vehicles:
            print(
                f"Vehicle Number: {vehicle.vehicle_number}, "
                f"Owner Name: {vehicle.owner_name}, "
                f"Test Date: {vehicle.test_date}, "
                f"Pollution Level: {vehicle.pollution_level}, "
                f"Valid Until: {vehicle.valid_until}"
            )


def main():
    pollution_control_system = PollutionControlSystem()

    while True:
        print("\nVehicle Pollution Control Record System")
        print("1. Add Vehicle")
        print("2. Check Validity")
        print("3. Generate Report")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            vehicle_number = input("Enter vehicle number: ")
            owner_name = input("Enter owner name: ")
            test_date = datetime.datetime.strptime(input("Enter test date (YYYY-MM-DD): "), "%Y-%m-%d").date()
            pollution_level = input("Enter pollution level: ")
            pollution_control_system.add_vehicle(vehicle_number, owner_name, test_date, pollution_level)

        elif choice == "2":
            vehicle_number = input("Enter vehicle number: ")
            pollution_control_system.check_validity(vehicle_number)

        elif choice == "3":
            pollution_control_system.generate_report()

        elif choice == "4":
            print("Exiting system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
