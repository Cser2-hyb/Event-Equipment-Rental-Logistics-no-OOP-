""" calculate_rental_fee() — tính phí thuê cơ bản
    calculate_late_penalty() — phạt 50,000 VND/giờ trễ (làm tròn lên)
    create_rental_order() — tạo đơn thuê với đầy đủ validation
    return_equipment() — trả thiết bị kèm tính phạt
    display_rental_orders() — hiển thị bảng đơn thuê được định dạng
"""
from datetime import datetime
import math
from Equipment import equipment_list, search_equipment_by_id

# Datetime format used throughout the project
DATETIME_FMT = "%Y-%m-%d %H:%M"

# Late penalty rate per hour (VND)
LATE_PENALTY_RATE = 50000

rental_list = []


def display_rental_orders(rental_list):
  
    if not rental_list:
        print("\n No rental order found")
        return

    print("\n" + "=" * 110)
    print(
        f"  {'Rental ID':<10} {'Client':<18} {'Equip ID':<10} "
        f"{'Start':<18} {'Expected Return':<18} {'Actual Return':<18} "
        f"{'Status':<12} {'Fee (VND)'}"
    )
    print("-" * 110)

    for r in rental_list:
        actual = r["actual_return_time"] if r["actual_return_time"] else "-"
        print(
            f"  {r['rental_id']:<10} "
            f"{r['client_name']:<18} "
            f"{r['equipment_id']:<10} "
            f"{r['start_time']:<18} "
            f"{r['expected_return_time']:<18} "
            f"{actual:<18} "
            f"{r['status']:<12} "
            f"{float(r['total_fee'] or 0):,.0f}"
        )


def calculate_rental_fee(start_time, expected_return_time, hourly_rate):
    start_dt = datetime.strptime(start_time, DATETIME_FMT)
    end_dt = datetime.strptime(expected_return_time, DATETIME_FMT)
    duration_seconds = (end_dt - start_dt).total_seconds()
    duration_hours = duration_seconds / 3600
    return duration_hours * float(hourly_rate)


def calculate_late_penalty(actual_return_time, expected_return_time):
    if not actual_return_time:
        return 0

    actual_dt = datetime.strptime(actual_return_time, DATETIME_FMT)
    expected_dt = datetime.strptime(expected_return_time, DATETIME_FMT)
    if actual_dt <= expected_dt:
        return 0

    late_seconds = (actual_dt - expected_dt).total_seconds()
    late_hours = math.ceil(late_seconds / 3600)
    return late_hours * LATE_PENALTY_RATE


def create_rental_order(rental_list, equipment_list):
    """Guide the user through creating a new rental order."""
    print("\n--- Create New Rental Order ---")

    while True:
        rental_id = input(" Enter Rental ID: ").strip()
        if not rental_id:
            print("Rental ID cannot be empty.")
            continue

        duplicate = any(
            r["rental_id"].strip().upper() == rental_id.upper()
            for r in rental_list
        )
        if duplicate:
            print(f"Rental ID '{rental_id}' already exists. Please enter a different ID.")
            continue
        break

    while True:
        client_name = input(" Enter client name: ").strip()
        if not client_name:
            print("Client name cannot be empty.")
            continue
        break

    while True:
        equipment_id = input(" Enter Equipment ID: ").strip()
        eq = search_equipment_by_id(equipment_list, equipment_id)
        if eq is None:
            print(f"[!] Equipment ID '{equipment_id}' not found.")
            continue
        if eq["status"] != "Active":
            print(f"[!] Equipment '{equipment_id}' is currently '{eq['status']}' and cannot be rented.")
            continue
        break

    while True:
        start_time = input(" Enter start time (YYYY-MM-DD HH:MM): ").strip()
        try:
            start_dt = datetime.strptime(start_time, DATETIME_FMT)
            break
        except ValueError:
            print("[!] Invalid date format. Please use YYYY-MM-DD HH:MM.")

    while True:
        expected_return_time = input(" Enter expected return time (YYYY-MM-DD HH:MM): ").strip()
        try:
            expected_dt = datetime.strptime(expected_return_time, DATETIME_FMT)
            if expected_dt <= start_dt:
                print("[!] Expected return time must be after start time.")
                continue
            break
        except ValueError:
            print("[!] Invalid date format. Please use YYYY-MM-DD HH:MM.")

    while True:
        hourly_rate_input = input(
            f" Enter hourly rate for '{eq['name']}' (or leave blank for {eq['hourly_rate']:,.0f}): "
        ).strip()
        if hourly_rate_input == "":
            hourly_rate = eq["hourly_rate"]
            break
        try:
            hourly_rate = float(hourly_rate_input)
            if hourly_rate < 0:
                raise ValueError
            break
        except ValueError:
            print("[!] Hourly rate must be a positive number.")

    total_fee = calculate_rental_fee(start_time, expected_return_time, hourly_rate)

    new_rental = {
        "rental_id": rental_id,
        "client_name": client_name,
        "equipment_id": equipment_id,
        "start_time": start_time,
        "expected_return_time": expected_return_time,
        "actual_return_time": "",
        "status": "Renting",
        "total_fee": total_fee,
    }
    rental_list.append(new_rental)
    eq["status"] = "Rented"

    print(f"\n[OK] Rental order '{rental_id}' created for '{client_name}'.")
    print(f"     Equipment: {eq['name']} ({equipment_id.upper()})")
    print(f"     Duration : {start_time} -> {expected_return_time}")
    print(f"     Base Fee : {total_fee:,.0f} VND\n")


# ---------------------------------------------------------------------------
# RETURN EQUIPMENT
# ---------------------------------------------------------------------------

def return_equipment(rental_list, equipment_list):
    """Process equipment return for a given rental ID."""
    print("\n--- Return Equipment ---")

    rental_id = input("  Enter Rental ID to return: ").strip()
    target_rental = None
    for r in rental_list:
        if r["rental_id"].strip().upper() == rental_id.upper():
            target_rental = r
            break

    if target_rental is None:
        print(f"\n[!] Rental ID '{rental_id}' not found.\n")
        return

    if target_rental["status"] == "Returned":
        print(f"\n[!] Rental '{rental_id}' has already been returned.\n")
        return

    print(f"  Expected Return: {target_rental['expected_return_time']}")

    while True:
        actual_return_time = input("  Enter Actual Return Time (YYYY-MM-DD HH:MM): ").strip()
        try:
            actual_dt = datetime.strptime(actual_return_time, DATETIME_FMT)
            start_dt = datetime.strptime(target_rental["start_time"], DATETIME_FMT)
            if actual_dt < start_dt:
                print("  [!] Actual return time cannot be before the rental start time.")
                continue
            break
        except ValueError:
            print("  [!] Invalid date format. Please use YYYY-MM-DD HH:MM.")

    penalty = calculate_late_penalty(actual_return_time, target_rental["expected_return_time"])
    target_rental["actual_return_time"] = actual_return_time
    target_rental["status"] = "Returned"
    total_due = float(target_rental["total_fee"]) + penalty
    target_rental["total_fee"] = total_due

    eq = search_equipment_by_id(equipment_list, target_rental["equipment_id"])
    if eq is not None:
        eq["status"] = "Active"

    print(f"\n[OK] Equipment returned successfully for Rental '{rental_id}'.")
    if penalty > 0:
        print(f"[!] Late Penalty  : {penalty:,.0f} VND")
    print(f"     Total Amount Due: {total_due:,.0f} VND\n")


def main():
    while True:
        print("\n=== RENTAL MENU ===")
        print("1. Create rental order")
        print("2. Return equipment")
        print("3. Display rental orders")
        print("4. Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            create_rental_order(rental_list, equipment_list)
        elif choice == "2":
            return_equipment(rental_list, equipment_list)
        elif choice == "3":
            display_rental_orders(rental_list)
        elif choice == "4":
            print("END")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
