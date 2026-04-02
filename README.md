# TechnoPropertyNepal Land Renting System

## Project Overview
TechnoPropertyNepal is a modular Python application designed to streamline land rental operations. The system manages land availability, processes rental agreements, calculates late fees/fines, and generates professional invoices for both renting and returning transactions.

## Key Features
* **Dynamic Data Management:** Reads and updates land records from a text-based database in real-time.
* **Rental Logic:** Validates land availability by "Kitta Number" and records customer details and rental duration.
* **Return & Fine System:** Automatically calculates fines if land is returned after the agreed duration.
* **Invoice Generation:** Creates unique text-file invoices for every transaction, including timestamps and total costs.
* **Error Handling:** Robust validation for user inputs and file operations.

## Technical Stack
* **Language:** Python 3.x
* **Modules:** `datetime`, `os`
* **Data Storage:** Text-file (.txt) based storage for portability.

## System Logic
1. **Read:** The system parses `land_records.txt` into a dictionary or list for processing.
2. **Operations:** - **Rent:** Checks if status is 'Available'. Updates status to 'Not Available' and generates a 'Rent_Invoice'.
   - **Return:** Calculates the difference between the actual return date and the expected end date to apply fines.
3. **Write:** Updates the master record file and saves the transaction details to a new invoice file.

## Setup & Installation
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/TechnoProperty-Land-Management.git](https://github.com/YOUR_USERNAME/TechnoProperty-Land-Management.git)
