"""File I/O module.

TV3: Titannz
Rule: procedural programming only. Do not use OOP.
"""

import csv
import os

DATA_FOLDER = "data"
EQUIPMENT_FILE = os.path.join(DATA_FOLDER, "equipment.csv")
RENTALS_FILE = os.path.join(DATA_FOLDER, "rentals.csv")

EQUIPMENT_FIELDS = ["equipment_id", "name", "power_rating", "hourly_rate", "status"]
RENTAL_FIELDS = [
    "rental_id",
    "client_name",
    "equipment_id",
    "start_time",
    "expected_return_time",
    "actual_return_time",
    "status",
    "total_fee",
    "late_penalty"
]


def ensure_data_folder():
    """Create data folder if it does not exist."""
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)


def load_equipment_from_file():
    """Load equipment data from CSV file."""
    equipment_list = []

    try:
        with open(EQUIPMENT_FILE, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row.get("equipment_id", "") != "":
                    row["power_rating"] = float(row["power_rating"])
                    row["hourly_rate"] = float(row["hourly_rate"])
                    equipment_list.append(row)
    except FileNotFoundError:
        return []
    except ValueError:
        print("Warning: Some equipment data is invalid.")

    return equipment_list


def save_equipment_to_file(equipment_list):
    """Save equipment data to CSV file."""
    ensure_data_folder()

    with open(EQUIPMENT_FILE, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=EQUIPMENT_FIELDS)
        writer.writeheader()
        writer.writerows(equipment_list)


def load_rentals_from_file():
    """Load rental data from CSV file."""
    rental_list = []

    try:
        with open(RENTALS_FILE, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row.get("rental_id", "") != "":
                    row["total_fee"] = float(row.get("total_fee", 0) or 0)
                    row["late_penalty"] = float(row.get("late_penalty", 0) or 0)
                    rental_list.append(row)
    except FileNotFoundError:
        return []
    except ValueError:
        print("Warning: Some rental data is invalid.")

    return rental_list


def save_rentals_to_file(rental_list):
    """Save rental data to CSV file."""
    ensure_data_folder()

    normalized_rentals = []
    for rental in rental_list:
        normalized_rental = {}
        for field in RENTAL_FIELDS:
            normalized_rental[field] = rental.get(field, "")
        normalized_rentals.append(normalized_rental)

    with open(RENTALS_FILE, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=RENTAL_FIELDS)
        writer.writeheader()
        writer.writerows(normalized_rentals)
