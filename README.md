# Event Equipment Rental & Logistics - No OOP

Python console project for managing event equipment and rental orders.

## Coding Direction

This version uses **procedural programming** only.

Do not use:

```python
class
self
__init__
@property
```

Use:

```python
function
list
dict
csv
try-except
```

## Team Members

| Role | GitHub Username | Responsibility |
|---|---|---|
| TV1 | `nguyenphanleha2k7` | Equipment Management |
| TV2 | `Cser2-hyb` | Rental Management |
| TV3 | `Titannz` | File I/O + Data Analysis |
| TV4 | `NTVien207` | Main Menu + Integration + Report/Slides |

## Project Structure

```text
project/
├── main.py
├── equipment.py
├── rental.py
├── file_handler.py
├── analysis.py
├── data/
│   ├── equipment.csv
│   └── rentals.csv
├── README.md
└── ROADMAP.md
```

## Data Schema

### Equipment

```python
equipment = {
    "equipment_id": "EQ001",
    "name": "Speaker",
    "power_rating": 500,
    "hourly_rate": 100000,
    "status": "Available"
}
```

### Rental

```python
rental = {
    "rental_id": "R001",
    "client_name": "Nguyen Van A",
    "equipment_id": "EQ001",
    "start_time": "2026-06-10 08:00",
    "expected_return_time": "2026-06-10 12:00",
    "actual_return_time": "",
    "status": "Renting",
    "total_fee": 400000,
    "late_penalty": 0
}
```

## How to Run

```bash
python main.py
```

## Branches

| Member | Branch |
|---|---|
| `nguyenphanleha2k7` | `feature/equipment-management` |
| `Cser2-hyb` | `feature/rental-management` |
| `Titannz` | `feature/file-analysis` |
| `NTVien207` | `feature/menu-integration` |

## Git Workflow

```text
Issue → Branch → Code → Commit → Push → Pull Request → Review → Merge
```

## Rules

- Do not push directly to `main`.
- Each member works on their own branch.
- Do not rename dictionary keys without team agreement.
- Do not rename function names without team agreement.
- Test with `python main.py` before creating a Pull Request.
