import csv
EQUIPMENT_HEADERS = ["equipment_id", "name", "power_rating", "hourly_rate", "status"]
RENTAL_HEADERS = ["rental_id", "client_name", "equipment_id", "start_time", "expected_return_time", "status", "total_fee"]
def load_equipment_from_file(filepath="equipment.csv"):
    """Load equipment data from CSV file."""
    equipment_list = []
    try:
        with open(filepath, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Bắt lỗi ValueError nếu dữ liệu trong file bị sai định dạng số
                try:
                    row["power_rating"] = float(row["power_rating"])
                    row["hourly_rate"] = float(row["hourly_rate"])
                    equipment_list.append(row)
                except ValueError:
                    print(f"[Cảnh báo] Bỏ qua thiết bị {row.get('equipment_id', 'Unknown')} do lỗi định dạng số.")
        print(f"Tải thành công {len(equipment_list)} thiết bị từ {filepath}.")
    except FileNotFoundError:
        print(f"[Thông báo] Không tìm thấy '{filepath}'. Sẽ khởi tạo danh sách thiết bị trống.")
    
    return equipment_list
def load_rentals_from_file(filepath="rentals.csv"):
    """Load rental data from CSV file."""
    rental_list = []
    try:
        with open(filepath, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Bắt lỗi ValueError nếu dữ liệu trong file bị sai định dạng số
                try:
                    row["total_fee"] = float(row["total_fee"])
                    rental_list.append(row)
                except ValueError:
                    print(f"[Cảnh báo] Bỏ qua đơn thuê {row.get('rental_id', 'Unknown')} do lỗi định dạng số.")
        print(f"Tải thành công {len(rental_list)} đơn thuê từ {filepath}.")
    except FileNotFoundError:
        print(f"[Thông báo] Không tìm thấy '{filepath}'. Sẽ khởi tạo danh sách đơn thuê trống.")
    
    return rental_list
def save_equipment_to_file(equipment_list, filepath="equipment.csv"):
    """Save equipment data to CSV file."""
    try:
        with open(filepath, mode="w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=EQUIPMENT_HEADERS)
            writer.writeheader()
            for equipment in equipment_list:
                writer.writerow(equipment)
            print(f"Đã lưu {len(equipment_list)} vào {filepath}.")
    except.Exception as e :

        print(f"Error saving data equipment: {e}")
def save_rentals_to_file(rental_list, filepath="rentals.csv"):
    """Save rental data to CSV file."""
    try:
        with open(filepath, mode="w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=RENTAL_HEADERS)
            writer.writeheader()
            for rental in rental_list:
                writer.writerow(rental)
            print(f"Đã lưu {len(rental_list)} vào {filepath}.")
    except Exception as e:
        print(f"Error saving data rentals: {e}")