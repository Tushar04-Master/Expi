#!/usr/bin/env python3
"""
Minimal Terminal Expense Tracker
Works on macOS/Linux terminals and Termux/Android
"""

import json
import os
from datetime import datetime

# Configuration
DATA_FILE = "expense_data.json"

def clear_screen():
    """Clear terminal screen"""
    os.system('clear' if os.name == 'posix' else 'cls')

def get_current_date():
    """Get current date in YYYY-MM-DD format"""
    return datetime.now().strftime("%Y-%m-%d")

def load_data():
    """Load data from JSON file"""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {"transactions": []}
    return {"transactions": []}

def save_data(data):
    """Save data to JSON file"""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def add_expense():
    """Add a new expense"""
    clear_screen()
    print("=== ADD EXPENSE ===")
    
    try:
        amount = float(input("Amount: $ "))
        category = input("Category: ")
        description = input("Description: ")
        date = input(f"Date (YYYY-MM-DD, default: {get_current_date()}): ") or get_current_date()
        
        data = load_data()
        data["transactions"].append({
            "type": "expense",
            "amount": amount,
            "category": category,
            "description": description,
            "date": date
        })
        save_data(data)
        print("✓ Expense added successfully!")
        input("\nPress Enter to continue...")
    except ValueError:
        print("✗ Invalid amount. Please enter a valid number.")
        input("\nPress Enter to continue...")

def add_income():
    """Add new income"""
    clear_screen()
    print("=== ADD INCOME ===")
    
    try:
        amount = float(input("Amount: $ "))
        source = input("Source: ")
        date = input(f"Date (YYYY-MM-DD, default: {get_current_date()}): ") or get_current_date()
        
        data = load_data()
        data["transactions"].append({
            "type": "income",
            "amount": amount,
            "source": source,
            "date": date
        })
        save_data(data)
        print("✓ Income added successfully!")
        input("\nPress Enter to continue...")
    except ValueError:
        print("✗ Invalid amount. Please enter a valid number.")
        input("\nPress Enter to continue...")

def show_summary():
    """Show financial summary"""
    clear_screen()
    print("=== FINANCIAL SUMMARY ===")
    
    data = load_data()
    transactions = data.get("transactions", [])
    
    if not transactions:
        print("No transactions yet.")
        input("\nPress Enter to continue...")
        return
    
    total_income = sum(t["amount"] for t in transactions if t["type"] == "income")
    total_expenses = sum(t["amount"] for t in transactions if t["type"] == "expense")
    balance = total_income - total_expenses
    
    print(f"Total Income:  ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Balance:       ${balance:.2f}")
    print()
    
    # Show expense breakdown by category
    print("=== EXPENSE BREAKDOWN ===")
    categories = {}
    for t in transactions:
        if t["type"] == "expense":
            category = t["category"]
            categories[category] = categories.get(category, 0) + t["amount"]
    
    for category, amount in sorted(categories.items(), key=lambda x: x[1], reverse=True):
        print(f"  {category}: ${amount:.2f}")
    
    input("\nPress Enter to continue...")

def show_history():
    """Show transaction history"""
    clear_screen()
    print("=== TRANSACTION HISTORY ===")
    
    data = load_data()
    transactions = data.get("transactions", [])
    
    if not transactions:
        print("No transactions yet.")
        input("\nPress Enter to continue...")
        return
    
    # Sort by date (newest first)
    sorted_transactions = sorted(transactions, key=lambda x: x["date"], reverse=True)
    
    for i, t in enumerate(sorted_transactions, 1):
        type_icon = "💰" if t["type"] == "income" else "💸"
        print(f"{i}. {type_icon} {t['date']} - {t.get('category', t.get('source', 'N/A'))}")
        print(f"   {t['description'] if 'description' in t else t.get('source', 'N/A')}")
        print(f"   ${t['amount']:.2f}")
        print()
    
    input("\nPress Enter to continue...")

def main_menu():
    """Display main menu"""
    clear_screen()
    print("=== EXPENSE TRACKER ===")
    print("1. Add Expense")
    print("2. Add Income")
    print("3. View Summary")
    print("4. View History")
    print("5. Exit")
    print()
    return input("Choose an option (1-5): ")

def main():
    """Main program loop"""
    while True:
        choice = main_menu()
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            add_income()
        elif choice == "3":
            show_summary()
        elif choice == "4":
            show_history()
        elif choice == "5":
            clear_screen()
            print("Goodbye!")
            break
        else:
            print("✗ Invalid choice. Please try again.")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()