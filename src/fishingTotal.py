# Author: Scuba
# Date: 4/18/25  

# Program to calculate the total fishing profits in Black Desert Online (BDO)  

# Features:  
# - Calculates profits from fishing  
# - Allows user to input fishing location  
# - Allows user to input date  
# - Stores a running total of profits in a file that can be viewed later  
# - Allows user to view total profits  
# - Allows user to create a new fishing log for a month (ie. April 2025, May 2025, etc.)  

# Example usage:
# create_new_log("April_2025")
# add_fishing_entry("April_2025", "4/18/25", "Velia", 5000)
# view_total_profits("April_2025")

import json
import os
import calendar
from datetime import datetime

# File to store fishing logs
LOG_FILE = "fishing_logs.json"

def load_logs():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_logs(logs):
    with open(LOG_FILE, 'w') as f:
        json.dump(logs, f, indent=4)

def log_fishing_session(month_key, fishing_location, sell_location, date, profit):
    logs = load_logs()
    if month_key not in logs:
        logs[month_key] = []
    logs[month_key].append({
        "date": date,
        "fishing_location": fishing_location,
        "sell_location": sell_location,
        "profit": profit
    })
    save_logs(logs)

def view_total_profits(month_key):
    logs = load_logs()
    if month_key not in logs:
        return f"No logs found for {month_key}."
    total_profit = sum(session["profit"] for session in logs[month_key])
    return f"Total profits for {month_key}: {total_profit:,} silver"

def view_lifetime_profit():
    logs = load_logs()
    if not logs:
        return "No fishing logs found. Lifetime profit: 0 silver."
    total_profit = sum(
        session["profit"]
        for month in logs.values()
        for session in month
    )
    return f"Lifetime profit: {total_profit:,} silver"

def create_new_month_log(month_key):
    logs = load_logs()
    if month_key not in logs:
        logs[month_key] = []
        save_logs(logs)
        return f"New log created for {month_key}."
    return f"Log for {month_key} already exists."

def delete_month_log(month_key):
    logs = load_logs()
    if month_key in logs:
        del logs[month_key]
        save_logs(logs)
        return f"Log for {month_key} deleted."
    return f"No log found for {month_key}."

def display_month_menu(logs, action):
    if not logs:
        print(f"No monthly logs exist. Please create a new log before {action}.")
        return None
    print(f"\nSelect a month to {action}:")
    months = sorted(logs.keys())
    for i, month in enumerate(months, 1):
        print(f"{i}. {month}")
    try:
        choice = int(safe_input("Enter the number of your choice: ")) - 1
        if 0 <= choice < len(months):
            return months[choice]
        print("Invalid choice.")
        return None
    except ValueError:
        print("Please enter a valid number.")
        return None

def parse_month_key(month_key):
    # Extract month and year from "Month Year" format (e.g., "April 2025")
    try:
        month_name, year = month_key.split()
        month_num = list(calendar.month_name).index(month_name)
        return month_num, int(year)
    except (ValueError, IndexError):
        return None, None

def validate_day(day, month, year):
    try:
        day = int(day)
        _, days_in_month = calendar.monthrange(year, month)
        if 1 <= day <= days_in_month:
            return day
        return None
    except ValueError:
        return None

def parse_profit(profit_input):
    try:
        # Remove commas and convert to integer
        profit = int(profit_input.replace(",", ""))
        if profit < 0:
            raise ValueError
        return profit
    except ValueError:
        return None

def safe_input(prompt):
    try:
        return input(prompt)
    except EOFError:
        print("\nInput stream closed unexpectedly. Exiting.")
        exit(1)
    except KeyboardInterrupt:
        print("\nOperation interrupted. Exiting.")
        exit(1)

def main():
    while True:
        print("\nBDO Fishing Profit Calculator")
        print("1. Log a fishing session")
        print("2. View total profits for a month")
        print("3. Create a new monthly log")
        print("4. Delete a monthly log")
        print("5. View lifetime profit")
        print("6. Exit")
        choice = safe_input("Select an option (1-6): ")

        logs = load_logs()

        if choice == "1":
            month_key = display_month_menu(logs, "log a session")
            if not month_key:
                continue
            fishing_location = safe_input("Enter fishing location (e.g., Velia, Epheria, Altinova): ")
            sell_location = safe_input("Enter sell location (e.g., Seoul): ")
            
            # Parse month and year from month_key
            month, year = parse_month_key(month_key)
            if month is None or year is None:
                print("Invalid month format in log. Please create a new log with correct format.")
                continue

            day = safe_input(f"Enter day of the month (1-{calendar.monthrange(year, month)[1]}): ")
            day_num = validate_day(day, month, year)
            if day_num is None:
                print(f"Invalid day. Please enter a number between 1 and {calendar.monthrange(year, month)[1]}.")
                continue

            # Construct date string
            date = f"{year}-{month:02d}-{day_num:02d}"
            try:
                datetime.strptime(date, "%Y-%m-%d")
            except ValueError:
                print("Invalid date constructed. Please try again.")
                continue

            profit_input = safe_input("Enter total profit (in silver, e.g., 1,000,000): ")
            profit = parse_profit(profit_input)
            if profit is None:
                print("Please enter a valid non-negative number (commas allowed, e.g., 1,000,000).")
                continue

            log_fishing_session(month_key, fishing_location, sell_location, date, profit)
            print(f"Session logged! Profit: {profit:,} silver")

        elif choice == "2":
            month_key = display_month_menu(logs, "view profits")
            if month_key:
                print(view_total_profits(month_key))

        elif choice == "3":
            month_key = safe_input("Enter month and year for new log (e.g., April 2025): ")
            print(create_new_month_log(month_key))

        elif choice == "4":
            month_key = display_month_menu(logs, "delete")
            if month_key:
                print(delete_month_log(month_key))

        elif choice == "5":
            print(view_lifetime_profit())

        elif choice == "6":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please select 1-6.")

if __name__ == "__main__":
    main()