'''
variable declaration(khai báo biến):
         add_equipment() — thêm thiết bị với đầy đủ validation
         search_equipment_by_id() — tìm thiết bị theo mã
        search_equipment_by_status() — tìm thiết bị theo trạng thái
         update_equipment() — cập nhật thiết bị có validation
         display_equipment() — hiển thị bảng được định dạng đẹp
'''   

ds_thiet_bi =[
    {'id' : 'TB001', 'name': 'bua', 'status': 'Active'},
    {'id': 'TB002', 'name': 'cua', 'status':'Inactive'},
]
def add_equipment():
    print("\n--- ADD NEW EQUIPMENT ---")
    
    while True:
        ma_id = input("Enter equipment ID: ")
        
        if ma_id == "":
            print("Error: ID cannot be empty!")
            continue # Bắt nhập lại
            
        trung_ma = False
        for tb in ds_thiet_bi:
            if tb["id"] == ma_id:
                trung_ma = True
                break
        
        if trung_ma == True:
            print("Error: This ID already exists!")
        else:
            break 

    # Nhập và kiểm tra Tên
    while True:
        ten = input("Enter equipment name: ")
        if ten == "":
            print("Error: Name cannot be empty!")
        else:
            break

    # Nhập và kiểm tra Trạng thái
    while True:
        trang_thai = input("Enter status (Active or Inactive): ")
        if trang_thai == "Active" or trang_thai == "Inactive":
            break
        else:
            print("Error: Please enter 'Active' or 'Inactive'!")

    thiet_bi_moi = {"id": ma_id, "name": ten, "status": trang_thai}
    
    # Thêm vào danh sách tổng
    ds_thiet_bi.append(thiet_bi_moi)
    print("New equipment added successfully!")

def search_equipment_by_id():
    print("\n--- SEARCH BY ID ---")
    ma_tim = input("Enter equipment ID to search: ")
    
    tim_thay = False
    for tb in ds_thiet_bi:
        if tb["id"] == ma_tim:
            print("Found:")
            print(f"- ID: {tb['id']}\n- Name: {tb['name']}\n- Status: {tb['status']}")
            tim_thay = True
            break # Tìm thấy rồi thì dừng vòng lặp
            
    if tim_thay == False:
        print("No equipment found with that ID.")

def search_equipment_by_status():
    print("\n--- SEARCH BY STATUS ---")
    trang_thai_tim = input("Enter status to search (Active or Inactive): ")
    
    if trang_thai_tim != "Active" and trang_thai_tim != "Inactive":
        print("Error: Please enter 'Active' or 'Inactive'!")
        return
    
    tim_thay = False
    for tb in ds_thiet_bi:
        if tb["status"] == trang_thai_tim:
            if tim_thay == False:
                print(f"Equipment with status '{trang_thai_tim}':")
            print(f"- ID: {tb['id']}\n- Name: {tb['name']}\n- Status: {tb['status']}\n")
            tim_thay = True
            
    if tim_thay == False:
        print(f"No equipment found with status '{trang_thai_tim}'.")

def update_equipment(): 
    print("\n--- UPDATE EQUIPMENT ---")
    ma_sua = input("Enter equipment ID to update: ")
    
    # Tìm xem thiết bị có tồn tại không
    thiet_bi_can_sua = None
    for tb in ds_thiet_bi:
        if tb["id"] == ma_sua:
            thiet_bi_can_sua = tb
            break
            
    if thiet_bi_can_sua == None:
        print("No equipment found with that ID to update!")
        return # Thoát hàm luôn

    print(f"Updating equipment: {thiet_bi_can_sua['name']}")
    print("(Press Enter to skip without changing)")
    
    # Sửa tên
    ten_moi = input("Enter new name: ")
    if ten_moi != "":
        thiet_bi_can_sua["name"] = ten_moi

    # Sửa trạng thái (có kiểm tra nhập đúng quy định)
    while True:
        status_moi = input("Enter new status (Active/Inactive): ")
        if status_moi == "": 
            break # Người dùng không nhập gì => Giữ nguyên, thoát vòng lặp
        elif status_moi == "Active" or status_moi == "Inactive":
            thiet_bi_can_sua["status"] = status_moi
            break
        else:
            print("Error: Only 'Active', 'Inactive', or empty input is allowed!")

    print("Information updated successfully!")

def display_equipment():
        print("\n--- EQUIPMENT LIST ---")
        if len(ds_thiet_bi) == 0:
            print("The equipment list is currently empty.")
            return
        
        for tb in ds_thiet_bi:
            print(f"- ID: {tb['id']}\n- Name: {tb['name']}\n- Status: {tb['status']}\n")

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