"""Data Analysis module.

TV3: Titannz
Rule: procedural programming only. Do not use OOP.
"""

from datetime import datetime

DATE_FORMAT = "%Y-%m-%d %H:%M"


def display_equipment_table(equipment_list):
    """Display equipment list in table format."""
    if len(equipment_list) == 0:
        print("No equipment data found.")
        return

    print(f"{'ID':<10} {'Name':<20} {'Power':<10} {'Rate':<12} {'Status':<10}")
    print("-" * 68)
    for equipment in equipment_list:
        print(
            f"{equipment['equipment_id']:<10} "
            f"{equipment['name']:<20} "
            f"{equipment['power_rating']:<10} "
            f"{equipment['hourly_rate']:<12} "
            f"{equipment['status']:<10}"
        )


def display_rental_table(rental_list):
    """Display rental list in table format."""
    if len(rental_list) == 0:
        print("No rental data found.")
        return

    print(f"{'ID':<10} {'Client':<20} {'Equipment':<12} {'Status':<10} {'Fee':<12}")
    print("-" * 70)
    for rental in rental_list:
        print(
            f"{rental['rental_id']:<10} "
            f"{rental['client_name']:<20} "
            f"{rental['equipment_id']:<12} "
            f"{rental['status']:<10} "
            f"{float(rental['total_fee']):<12.2f}"
        )


def get_rental_duration_hours(rental):
    """Return rental duration in hours."""
    try:
        start_time = datetime.strptime(rental["start_time"], DATE_FORMAT)
        expected_return_time = datetime.strptime(rental["expected_return_time"], DATE_FORMAT)
        return (expected_return_time - start_time).total_seconds() / 3600
    except ValueError:
        return 0


def sort_equipment_by_rate(equipment_list):
    """Sort equipment by hourly rental rate from low to high."""
    sorted_list = sorted(equipment_list, key=lambda equipment: float(equipment["hourly_rate"]))
    print("\n===== Equipment Sorted by Hourly Rate =====")
    display_equipment_table(sorted_list)
    return sorted_list


def sort_equipment_by_power(equipment_list):
    """Sort equipment by power rating from low to high."""
    sorted_list = sorted(equipment_list, key=lambda equipment: float(equipment["power_rating"]))
    print("\n===== Equipment Sorted by Power Rating =====")
    display_equipment_table(sorted_list)
    return sorted_list


def sort_rentals_by_duration(rental_list):
    """Sort rental orders by duration from short to long."""
    sorted_list = sorted(rental_list, key=get_rental_duration_hours)
    print("\n===== Rentals Sorted by Duration =====")
    display_rental_table(sorted_list)
    return sorted_list


def sort_rentals_by_client_name(rental_list):
    """Sort rental orders by client name alphabetically."""
    sorted_list = sorted(rental_list, key=lambda rental: rental["client_name"].lower())
    print("\n===== Rentals Sorted by Client Name =====")
    display_rental_table(sorted_list)
    return sorted_list
