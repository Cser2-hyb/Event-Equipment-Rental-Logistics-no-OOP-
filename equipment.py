"""Equipment Management module.

TV1: nguyenphanleha2k7
Rule: procedural programming only. Do not use OOP.
"""

VALID_STATUSES = ["Available", "Rented"]


def is_equipment_id_exists(equipment_list, equipment_id):
    """Return True if equipment_id already exists."""
    for equipment in equipment_list:
        if equipment["equipment_id"] == equipment_id:
            return True
    return False


def add_equipment(equipment_list):
    """Add a new equipment item to equipment_list."""
    print("\n===== Add Equipment =====")

    equipment_id = input("Equipment ID: ").strip()
    if equipment_id == "":
        print("Equipment ID cannot be empty.")
        return

    if is_equipment_id_exists(equipment_list, equipment_id):
        print("Equipment ID already exists.")
        return

    name = input("Equipment name: ").strip()
    if name == "":
        print("Equipment name cannot be empty.")
        return

    try:
        power_rating = float(input("Power rating: "))
        hourly_rate = float(input("Hourly rental rate: "))

        if power_rating <= 0 or hourly_rate <= 0:
            print("Power rating and hourly rate must be positive numbers.")
            return
    except ValueError:
        print("Invalid number input.")
        return

    status = input("Status (Available/Rented): ").strip()
    if status == "":
        status = "Available"

    if status not in VALID_STATUSES:
        print("Status must be Available or Rented.")
        return

    equipment = {
        "equipment_id": equipment_id,
        "name": name,
        "power_rating": power_rating,
        "hourly_rate": hourly_rate,
        "status": status
    }

    equipment_list.append(equipment)
    print("Equipment added successfully.")


def search_equipment_by_id(equipment_list, equipment_id):
    """Return one equipment dictionary by ID. Return None if not found."""
    for equipment in equipment_list:
        if equipment["equipment_id"] == equipment_id:
            return equipment
    return None


def search_equipment_by_status(equipment_list, status):
    """Return a list of equipment items matching the given status."""
    result = []
    for equipment in equipment_list:
        if equipment["status"] == status:
            result.append(equipment)
    return result


def update_equipment(equipment_list, equipment_id):
    """Update equipment name, power rating, hourly rate, or status."""
    equipment = search_equipment_by_id(equipment_list, equipment_id)

    if equipment is None:
        print("Equipment not found.")
        return

    print("\n===== Update Equipment =====")
    print("Leave input empty to keep old value.")

    new_name = input(f"New name ({equipment['name']}): ").strip()
    if new_name != "":
        equipment["name"] = new_name

    new_power = input(f"New power rating ({equipment['power_rating']}): ").strip()
    if new_power != "":
        try:
            new_power_value = float(new_power)
            if new_power_value <= 0:
                print("Power rating must be positive.")
                return
            equipment["power_rating"] = new_power_value
        except ValueError:
            print("Invalid power rating.")
            return

    new_rate = input(f"New hourly rate ({equipment['hourly_rate']}): ").strip()
    if new_rate != "":
        try:
            new_rate_value = float(new_rate)
            if new_rate_value <= 0:
                print("Hourly rate must be positive.")
                return
            equipment["hourly_rate"] = new_rate_value
        except ValueError:
            print("Invalid hourly rate.")
            return

    new_status = input(f"New status ({equipment['status']}): ").strip()
    if new_status != "":
        if new_status not in VALID_STATUSES:
            print("Status must be Available or Rented.")
            return
        equipment["status"] = new_status

    print("Equipment updated successfully.")


def display_equipment(equipment_list):
    """Display all equipment in a readable table."""
    print("\n===== Equipment List =====")

    if len(equipment_list) == 0:
        print("No equipment found.")
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
