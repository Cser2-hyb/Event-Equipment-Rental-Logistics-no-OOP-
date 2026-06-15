'''
variable declaration(khai báo biến):
         add_equipment() — thêm thiết bị với đầy đủ validation
         search_equipment_by_id() — tìm thiết bị theo mã
        search_equipment_by_status() — tìm thiết bị theo trạng thái
         update_equipment() — cập nhật thiết bị có validation
         display_equipment() — hiển thị bảng được định dạng đẹp
'''

equipment_list = [
    {'id': 'TB001', 'name': 'Hammer', 'status': 'Active', 'hourly_rate': 50000.0},
    {'id': 'TB002', 'name': 'Saw', 'status': 'Inactive', 'hourly_rate': 60000.0},
]

def add_equipment():
    print("\n--- ADD NEW EQUIPMENT ---")

    while True:
        equipment_id = input("Enter equipment ID: ").strip()
        if equipment_id == "":
            print("Error: ID cannot be empty!")
            continue

        duplicate_id = any(
            eq["id"].strip().upper() == equipment_id.upper() for eq in equipment_list
        )
        if duplicate_id:
            print("Error: This ID already exists!")
            continue
        break

    while True:
        name = input("Enter equipment name: ").strip()
        if name == "":
            print("Error: Name cannot be empty!")
            continue
        break

    while True:
        status = input("Enter status (Active or Inactive): ").strip()
        if status in ("Active", "Inactive"):
            break
        print("Error: Please enter 'Active' or 'Inactive'!")

    while True:
        hourly_rate_input = input("Enter hourly rate: ").strip()
        try:
            hourly_rate = float(hourly_rate_input)
            if hourly_rate < 0:
                raise ValueError
            break
        except ValueError:
            print("Error: Hourly rate must be a non-negative number!")

    new_equipment = {
        "id": equipment_id,
        "name": name,
        "status": status,
        "hourly_rate": hourly_rate,
    }

    equipment_list.append(new_equipment)
    print("New equipment added successfully!")


def search_equipment_by_id(equipment_list, equipment_id):
    if equipment_id is None:
        return None
    search_id = equipment_id.strip().upper()
    for eq in equipment_list:
        if eq["id"].strip().upper() == search_id:
            return eq
    return None


def search_equipment_by_id_interactive():
    print("\n--- SEARCH BY ID ---")
    search_id = input("Enter equipment ID to search: ").strip()
    eq = search_equipment_by_id(equipment_list, search_id)
    if eq is None:
        print("No equipment found with that ID.")
        return

    print("Found:")
    print(
        f"- ID: {eq['id']}\n"
        f"- Name: {eq['name']}\n"
        f"- Status: {eq['status']}\n"
        f"- Hourly Rate: {eq['hourly_rate']:,.0f}"
    )


def search_equipment_by_status():
    print("\n--- SEARCH BY STATUS ---")
    search_status = input("Enter status to search (Active or Inactive): ").strip()

    if search_status not in ("Active", "Inactive"):
        print("Error: Please enter 'Active' or 'Inactive'!")
        return

    found = False
    for eq in equipment_list:
        if eq["status"] == search_status:
            if not found:
                print(f"Equipment with status '{search_status}':")
            print(
                f"- ID: {eq['id']}\n"
                f"- Name: {eq['name']}\n"
                f"- Status: {eq['status']}\n"
            )
            found = True

    if not found:
        print(f"No equipment found with status '{search_status}'.")


def update_equipment():
    print("\n--- UPDATE EQUIPMENT ---")
    update_id = input("Enter equipment ID to update: ").strip()

    equipment_to_update = None
    for eq in equipment_list:
        if eq["id"].strip().upper() == update_id.upper():
            equipment_to_update = eq
            break

    if equipment_to_update is None:
        print("No equipment found with that ID to update!")
        return

    print(f"Updating equipment: {equipment_to_update['name']}")
    print("(Press Enter to skip without changing)")

    new_name = input("Enter new name: ").strip()
    if new_name != "":
        equipment_to_update["name"] = new_name

    while True:
        new_status = input("Enter new status (Active/Inactive): ").strip()
        if new_status == "":
            break
        if new_status in ("Active", "Inactive"):
            equipment_to_update["status"] = new_status
            break
        print("Error: Only 'Active', 'Inactive', or empty input is allowed!")

    print("Information updated successfully!")


def display_equipment():
    print("\n--- EQUIPMENT LIST ---")
    if len(equipment_list) == 0:
        print("The equipment list is currently empty.")
        return

    for eq in equipment_list:
        print(
            f"- ID: {eq['id']}\n"
            f"- Name: {eq['name']}\n"
            f"- Status: {eq['status']}\n"
            f"- Hourly Rate: {eq['hourly_rate']:,.0f}\n"
        )


if __name__ == "__main__":
    while True:
        print("\n=== EQUIPMENT MANAGEMENT ===")
        print("1. Add new equipment")
        print("2. Search equipment by ID")
        print("3. Search equipment by status")
        print("4. Update equipment information")
        print("5. Display equipment list")
        print("6. Exit program")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_equipment()
        elif choice == "2":
            search_equipment_by_id_interactive()
        elif choice == "3":
            search_equipment_by_status()
        elif choice == "4":
            update_equipment()
        elif choice == "5":
            display_equipment()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please select again (1-6).")
