"""Main program for Event Equipment Rental & Logistics.

TV4: NTVien207
Rule: procedural programming only. Do not use OOP.
"""

from equipment import (
    add_equipment,
    display_equipment,
    search_equipment_by_id,
    search_equipment_by_status,
    update_equipment,
)
from rental import create_rental_order, display_rental_orders, return_equipment
from file_handler import (
    load_equipment_from_file,
    save_equipment_to_file,
    load_rentals_from_file,
    save_rentals_to_file,
)
from analysis import (
    sort_equipment_by_rate,
    sort_equipment_by_power,
    sort_rentals_by_duration,
    sort_rentals_by_client_name,
)


def equipment_menu(equipment_list):
    """Display and control equipment submenu."""
    while True:
        print("\n===== Equipment Management =====")
        print("1. Add Equipment")
        print("2. Search Equipment by ID")
        print("3. Search Equipment by Status")
        print("4. Update Equipment")
        print("5. Display All Equipment")
        print("6. Back")

        choice = input("Choose option: ").strip()

        if choice == "1":
            add_equipment(equipment_list)
        elif choice == "2":
            equipment_id = input("Enter equipment ID: ").strip()
            equipment = search_equipment_by_id(equipment_list, equipment_id)
            if equipment is None:
                print("Equipment not found.")
            else:
                print(equipment)
        elif choice == "3":
            status = input("Enter status (Available/Rented): ").strip()
            result = search_equipment_by_status(equipment_list, status)
            display_equipment(result)
        elif choice == "4":
            equipment_id = input("Enter equipment ID to update: ").strip()
            update_equipment(equipment_list, equipment_id)
        elif choice == "5":
            display_equipment(equipment_list)
        elif choice == "6":
            break
        else:
            print("Invalid option.")


def analysis_menu(equipment_list, rental_list):
    """Display and control data analysis submenu."""
    while True:
        print("\n===== Data Analysis =====")
        print("1. Sort Equipment by Rental Rate")
        print("2. Sort Equipment by Power Rating")
        print("3. Sort Rentals by Duration")
        print("4. Sort Rentals by Client Name")
        print("5. Back")

        choice = input("Choose option: ").strip()

        if choice == "1":
            sort_equipment_by_rate(equipment_list)
        elif choice == "2":
            sort_equipment_by_power(equipment_list)
        elif choice == "3":
            sort_rentals_by_duration(rental_list)
        elif choice == "4":
            sort_rentals_by_client_name(rental_list)
        elif choice == "5":
            break
        else:
            print("Invalid option.")


def main_menu():
    """Main console menu."""
    equipment_list = load_equipment_from_file()
    rental_list = load_rentals_from_file()

    while True:
        print("\n===== Event Equipment Rental & Logistics =====")
        print("1. Manage Equipment")
        print("2. Create Rental Order")
        print("3. Return Equipment")
        print("4. View Rental Orders")
        print("5. Data Analysis")
        print("6. Save Data")
        print("7. Exit")

        choice = input("Choose option: ").strip()

        if choice == "1":
            equipment_menu(equipment_list)
        elif choice == "2":
            create_rental_order(rental_list, equipment_list)
        elif choice == "3":
            return_equipment(rental_list, equipment_list)
        elif choice == "4":
            display_rental_orders(rental_list)
        elif choice == "5":
            analysis_menu(equipment_list, rental_list)
        elif choice == "6":
            save_equipment_to_file(equipment_list)
            save_rentals_to_file(rental_list)
            print("Data saved successfully.")
        elif choice == "7":
            save_equipment_to_file(equipment_list)
            save_rentals_to_file(rental_list)
            print("Data saved. Exiting program...")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main_menu()
