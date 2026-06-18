'''
variable declaration(khai báo biến):
         add_equipment() — thêm thiết bị với đầy đủ validation
         search_equipment_by_id() — tìm thiết bị theo mã
        search_equipment_by_status() — tìm thiết bị theo trạng thái
         update_equipment() — cập nhật thiết bị có validation
         display_equipment() — hiển thị bảng được định dạng đẹp
'''   

equipment_list = [
    {'id': 'TB001', 'name': 'Hammer', 'status': 'Active'},
    {'id': 'TB002', 'name': 'Saw', 'status': 'Inactive'},
]
def add_equipment():
    print("\n--- ADD NEW EQUIPMENT ---")
    
    while True:
        equipment_id = input("Enter equipment ID: ")
        
        if equipment_id == "":
            print("Error: ID cannot be empty!")
            continue 
            
        duplicate_id = False
        for eq in equipment_list:
            if eq["id"] == equipment_id:
                duplicate_id = True
                break
        
        if duplicate_id == True:
            print("Error: This ID already exists!")
        else:
            break 

    # Input and validate Name
    while True:
        name = input("Enter equipment name: ")
        if name == "":
            print("Error: Name cannot be empty!")
        else:
            break

    # Input and validate Status
    while True:
        status = input("Enter status (Active or Inactive): ")
        if status == "Active" or status == "Inactive":
            break
        else:
            print("Error: Please enter 'Active' or 'Inactive'!")

    new_equipment = {"id": equipment_id, "name": name, "status": status}
    
    # Append to the main list
    equipment_list.append(new_equipment)
    print("New equipment added successfully!")

def search_equipment_by_id():
    print("\n--- SEARCH BY ID ---")
    search_id = input("Enter equipment ID to search: ")
    
    found = False
    for eq in equipment_list:
        if eq["id"] == search_id:
            print("Equipment found:")
            print(f"- ID: {eq['id']}\n- Name: {eq['name']}\n- Status: {eq['status']}")
            found = True
            break 
            
    if not found:
        print(" No equipment found with this ID.")

def search_equipment_by_status():
    print("\n--- SEARCH BY STATUS ---")
    search_status = input("Enter status to search (Active or Inactive): ")
    
    if search_status != "Active" and search_status != "Inactive":
        print("Error: Please enter 'Active' or 'Inactive'!")
        return
    
    found = False
    for eq in equipment_list:
        if eq["status"] == search_status:
            if found == False:
                print(f"Equipment with status '{search_status}':")
            print(f"- ID: {eq['id']}\n- Name: {eq['name']}\n- Status: {eq['status']}\n")
            found = True
            
    if found == False:
        print(f"No equipment found with status '{search_status}'.")

def update_equipment(): 
    print("\n--- UPDATE EQUIPMENT ---")
    update_id = input("Enter equipment ID to update: ")
    
    # Check if the equipment exists
    equipment_to_update = None
    for eq in equipment_list:
        if eq["id"] == update_id:
            equipment_to_update = eq
            break
            
    if equipment_to_update == None:
        print("No equipment found with that ID to update!")
        return # Exit function immediately

    print(f"Updating equipment: {equipment_to_update['name']}")
    print("(Press Enter to skip without changing)")
    
    # Update Name
    new_name = input("Enter new name: ")
    if new_name != "":
        equipment_to_update["name"] = new_name

    # Update Status (with validation)
    while True:
        new_status = input("Enter new status (Active/Inactive): ")
        if new_status == "": 
            break # User pressed Enter without typing => Keep old status, exit loop
        elif new_status == "Active" or new_status == "Inactive":
            equipment_to_update["status"] = new_status
            break
        else:
            print("Error: Only 'Active', 'Inactive', or empty input is allowed!")

    print("Information updated successfully!")

def display_equipment():
    print("\n--- EQUIPMENT LIST ---")
    if len(equipment_list) == 0:
        print("The equipment list is currently empty.")
        return
    
    for eq in equipment_list:
        print(f"- ID: {eq['id']}\n- Name: {eq['name']}\n- Status: {eq['status']}\n")

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
        search_equipment_by_id()
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