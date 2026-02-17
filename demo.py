#!/usr/bin/env python3
"""
Demo script to show expense tracker functionality
"""

import json
import os
import sys

# Import the expense tracker functions
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from expense_tracker import load_data, save_data

def demo():
    """Run a demonstration of the expense tracker"""
    print("=== EXPENSE TRACKER DEMO ===")
    print()
    
    # Clean up any existing data
    if os.path.exists("expense_data.json"):
        os.remove("expense_data.json")
    
    print("1. Starting with empty data...")
    data = load_data()
    print(f"   Transactions: {len(data['transactions'])}")
    print()
    
    print("2. Adding some sample transactions...")
    sample_data = {
        "transactions": [
            {"type": "income", "amount": 3000.0, "source": "Salary", "date": "2024-01-01"},
            {"type": "income", "amount": 500.0, "source": "Freelance", "date": "2024-01-05"},
            {"type": "expense", "amount": 150.0, "category": "Food", "description": "Groceries", "date": "2024-01-02"},
            {"type": "expense", "amount": 80.0, "category": "Transport", "description": "Bus fare", "date": "2024-01-03"},
            {"type": "expense", "amount": 30.0, "category": "Food", "description": "Lunch", "date": "2024-01-04"},
            {"type": "expense", "amount": 200.0, "category": "Entertainment", "description": "Movie tickets", "date": "2024-01-06"}
        ]
    }
    save_data(sample_data)
    print(f"   Added {len(sample_data['transactions'])} transactions")
    print()
    
    print("3. Loading data and calculating summary...")
    data = load_data()
    transactions = data["transactions"]
    
    total_income = sum(t["amount"] for t in transactions if t["type"] == "income")
    total_expenses = sum(t["amount"] for t in transactions if t["type"] == "expense")
    balance = total_income - total_expenses
    
    print(f"   Total Income:  ${total_income:.2f}")
    print(f"   Total Expenses: ${total_expenses:.2f}")
    print(f"   Balance:       ${balance:.2f}")
    print()
    
    print("4. Expense breakdown by category:")
    categories = {}
    for t in transactions:
        if t["type"] == "expense":
            category = t["category"]
            categories[category] = categories.get(category, 0) + t["amount"]
    
    for category, amount in sorted(categories.items(), key=lambda x: x[1], reverse=True):
        percentage = (amount / total_expenses * 100) if total_expenses > 0 else 0
        print(f"   {category}: ${amount:.2f} ({percentage:.1f}%)")
    print()
    
    print("5. Transaction history (newest first):")
    sorted_transactions = sorted(transactions, key=lambda x: x["date"], reverse=True)
    for i, t in enumerate(sorted_transactions, 1):
        type_icon = "💰" if t["type"] == "income" else "💸"
        print(f"   {i}. {type_icon} {t['date']} - {t.get('category', t.get('source', 'N/A'))}")
        print(f"      {t.get('description', t.get('source', 'N/A'))}: ${t['amount']:.2f}")
    print()
    
    print("6. Data is saved to 'expense_data.json'")
    print(f"   File exists: {os.path.exists('expense_data.json')}")
    print()
    
    print("7. Cleaning up demo data...")
    if os.path.exists("expense_data.json"):
        os.remove("expense_data.json")
    print(f"   File removed: {not os.path.exists('expense_data.json')}")
    print()
    
    print("=" * 50)
    print("✓ Demo completed successfully!")
    print("=" * 50)
    print()
    print("To use the expense tracker:")
    print("  1. Run: python3 expense_tracker.py")
    print("  2. Use the menu to add expenses/income")
    print("  3. View your financial summary and history")
    print()

if __name__ == "__main__":
    demo()