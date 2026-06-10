# Roadmap - Event Equipment Rental & Logistics

> Project direction: procedural programming / no OOP. The source code should use functions, lists, dictionaries, CSV/Text files, and console menus. Do not use `class`, `self`, `__init__`, private attributes, or property decorators.

## Team Members

| Role | GitHub Username | Main Responsibility |
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
└── README.md
```

---

## Phase 1 - Week 2: Project Setup

### Goal
Set up the repository, analyze requirements, and define the initial project structure.

| Member | Tasks |
|---|---|
| `nguyenphanleha2k7` | Analyze equipment fields: equipment ID, power rating, hourly rental rate, current status. |
| `Cser2-hyb` | Analyze rental fields: rental ID, client name, start time, expected return time. |
| `Titannz` | Design CSV/Text data storage structure for equipment and rentals. |
| `NTVien207` | Create GitHub repository structure, README, and initial files. |

### Output
- Repository initialized
- Basic folder structure created
- Initial README and ROADMAP created
- Member responsibilities confirmed

---

## Phase 2 - Week 3-4: Core Feature Development

### Goal
Implement the main functions for each module.

| Member | Module | Tasks |
|---|---|---|
| `nguyenphanleha2k7` | `equipment.py` | Add equipment, search by ID/status, update equipment, display equipment list. |
| `Cser2-hyb` | `rental.py` | Create rental order, check equipment availability, calculate rental fee. |
| `Titannz` | `analysis.py` | Sort equipment by rental rate/power rating, sort rentals by duration/client name. |
| `NTVien207` | `main.py` | Build console menu and connect menu options to module functions. |

### Output
- Basic equipment management works
- Basic rental management works
- Sorting functions work
- Main menu can call module functions

---

## Phase 3 - Week 5-6: File I/O and Validation

### Goal
Add persistent storage and input validation.

| Member | Tasks |
|---|---|
| `nguyenphanleha2k7` | Validate equipment ID uniqueness, valid power rating, valid rental rate, valid status. |
| `Cser2-hyb` | Validate rental ID uniqueness, missing client name, invalid rental time, unavailable equipment. |
| `Titannz` | Implement load/save functions for CSV/Text files and rental history logs. |
| `NTVien207` | Add try-except handling in the menu and handle invalid user options. |

### Output
- Data loads automatically at startup
- Data saves before exit
- Invalid input does not crash the program
- Equipment availability is checked before rental creation

---

## Phase 4 - Week 7: Integration and Testing

### Goal
Merge all modules and test the full program flow.

| Member | Tasks |
|---|---|
| `nguyenphanleha2k7` | Test equipment functions after integration with rentals. |
| `Cser2-hyb` | Test rental creation, rental fee calculation, and equipment status updates. |
| `Titannz` | Test file loading/saving and data persistence after restarting the app. |
| `NTVien207` | Merge code, resolve conflicts, and test `main.py` from start to exit. |

### Output
- Full program runs from `main.py`
- No major menu flow errors
- Data persistence works
- Known bugs are listed in GitHub Issues

---

## Phase 5 - Week 8: Report and Diagrams

### Goal
Prepare the technical report and system diagrams.

| Member | Report Section |
|---|---|
| `nguyenphanleha2k7` | Equipment Management section |
| `Cser2-hyb` | Rental Management, rental fee, late penalty section |
| `Titannz` | File I/O, data analysis, persistent storage section |
| `NTVien207` | Architecture, menu system, flowchart, final PDF formatting |

### Output
- Technical report draft completed
- Flowchart completed
- System architecture described
- Testing table added

---

## Phase 6 - Week 9-10: Final Presentation and Submission

### Goal
Finalize slides, demo script, source code, and LMS submission package.

| Member | Tasks |
|---|---|
| `nguyenphanleha2k7` | Prepare slide and demo for Equipment Management. |
| `Cser2-hyb` | Prepare slide and demo for Rental Management. |
| `Titannz` | Prepare slide and demo for File I/O and Data Analysis. |
| `NTVien207` | Prepare intro/conclusion slides, combine slides, final submission check. |

### Output
- Final source code
- Technical report PDF
- Presentation slides
- Demo script
- Final LMS submission package

---

## Git Workflow

### Branch Naming

| Member | Branch |
|---|---|
| `nguyenphanleha2k7` | `feature/equipment-management` |
| `Cser2-hyb` | `feature/rental-management` |
| `Titannz` | `feature/file-analysis` |
| `NTVien207` | `feature/menu-integration` |

### Basic Rules

1. Work on your own feature branch.
2. Commit small changes with clear messages.
3. Pull latest `main` before opening a pull request.
4. Do not edit another member's module without discussion.
5. Test your module before merging.

---

## Issue List

| Issue | Title | Assignee |
|---:|---|---|
| #1 | Setup project structure and README | `NTVien207` |
| #2 | Implement equipment management module | `nguyenphanleha2k7` |
| #3 | Add equipment search and update functions | `nguyenphanleha2k7` |
| #4 | Implement rental order creation | `Cser2-hyb` |
| #5 | Add rental fee and late penalty calculation | `Cser2-hyb` |
| #6 | Implement file load/save with CSV or TXT | `Titannz` |
| #7 | Implement data analysis and sorting functions | `Titannz` |
| #8 | Build console-based menu system | `NTVien207` |
| #9 | Add input validation and exception handling | `Cser2-hyb`, `NTVien207` |
| #10 | Integrate modules and test full program | All members |
| #11 | Write technical report | All members |
| #12 | Prepare presentation slides and demo | All members |
