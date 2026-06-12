"""Rental Management module.

TV2: Cser2-hyb
Rule: procedural programming only. Do not use OOP.
"""

from datetime import datetime

DATE_FORMAT = "%Y-%m-%d %H:%M"
LATE_PENALTY_PER_HOUR = 50000


def parse_datetime(date_text):
    """Convert text to datetime using YYYY-MM-DD HH:MM format."""
    return datetime.strptime(date_text, DATE_FORMAT)


def is_rental_id_exists(rental_list, rental_id):
    """Return True if rental_id already exists."""
    for rental in rental_list:
        if rental["rental_id"] == rental_id:
            return True
    return False


def find_available_equipment(equipment_list, equipment_id):
    """Return equipment if it exists and is Available. Otherwise return None."""
    for equipment in equipment_list:
        if equipment["equipment_id"] == equipment_id and equipment["status"] == "Available":
            return equipment
    return None


def calculate_rental_fee(start_time, expected_return_time, hourly_rate):
    """Calculate rental fee based on duration and hourly rate."""
    start_dt = parse_datetime(start_time)
    expected_dt = parse_datetime(expected_return_time)

    duration_seconds = (expected_dt - start_dt).total_seconds()
    duration_hours = duration_seconds / 3600

    if duration_hours <= 0:
        raise ValueError("Expected return time must be after start time.")

    return duration_hours * float(hourly_rate)


def calculate_late_penalty(expected_return_time, actual_return_time):
    """Calculate late penalty. Return 0 if the equipment is not returned late."""
    expected_dt = parse_datetime(expected_return_time)
    actual_dt = parse_datetime(actual_return_time)

    late_seconds = (actual_dt - expected_dt).total_seconds()
    late_hours = late_seconds / 3600

    if late_hours <= 0:
        return 0

    return late_hours * LATE_PENALTY_PER_HOUR


def create_rental_order(rental_list, equipment_list):
    """Create a new rental order."""
    print("\n===== Create Rental Order =====")

    rental_id = input("Rental ID: ").strip()
    if rental_id == "":
        print("Rental ID cannot be empty.")
        return

    if is_rental_id_exists(rental_list, rental_id):
        print("Rental ID already exists.")
        return

    client_name = input("Client name: ").strip()
    if client_name == "":
        print("Client name cannot be empty.")
        return

    equipment_id = input("Equipment ID: ").strip()
    equipment = find_available_equipment(equipment_list, equipment_id)

    if equipment is None:
        print("Equipment not found or unavailable.")
        return

    start_time = input("Start time (YYYY-MM-DD HH:MM): ").strip()
    expected_return_time = input("Expected return time (YYYY-MM-DD HH:MM): ").strip()

    try:
        total_fee = calculate_rental_fee(start_time, expected_return_time, equipment["hourly_rate"])
    except ValueError as error:
        print(f"Invalid rental time: {error}")
        return

    rental = {
        "rental_id": rental_id,
        "client_name": client_name,
        "equipment_id": equipment_id,
        "start_time": start_time,
        "expected_return_time": expected_return_time,
        "actual_return_time": "",
        "status": "Renting",
        "total_fee": total_fee
    }

    rental_list.append(rental)
    equipment["status"] = "Rented"
    print("Rental order created successfully.")
    print(f"Total fee: {total_fee:.2f}")


def return_equipment(rental_list, equipment_list):
    """Return equipment and calculate late penalty if any."""
    print("\n===== Return Equipment =====")

    rental_id = input("Rental ID: ").strip()
    rental = None

    for item in rental_list:
        if item["rental_id"] == rental_id:
            rental = item
            break

    if rental is None:
        print("Rental order not found.")
        return

    if rental["status"] == "Returned":
        print("This rental order has already been returned.")
        return

    actual_return_time = input("Actual return time (YYYY-MM-DD HH:MM): ").strip()

    try:
        penalty = calculate_late_penalty(rental["expected_return_time"], actual_return_time)
    except ValueError:
        print("Invalid actual return time format.")
        return

    rental["actual_return_time"] = actual_return_time
    rental["status"] = "Returned"
    rental["late_penalty"] = penalty

    for equipment in equipment_list:
        if equipment["equipment_id"] == rental["equipment_id"]:
            equipment["status"] = "Available"
            break

    print("Equipment returned successfully.")
    print(f"Late penalty: {penalty:.2f}")


def display_rental_orders(rental_list):
    """Display all rental orders."""
    print("\n===== Rental Orders =====")

    if len(rental_list) == 0:
        print("No rental orders found.")
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
