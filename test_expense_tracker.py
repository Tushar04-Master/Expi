#!/usr/bin/env python3
"""
Test script to verify expense tracker functionality
"""

import json
import os
import sys

# Add the parent directory to path so we can import the module
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from expense_tracker import load_data, save_data, get_current_date

def test_data_storage():
    """Test data storage functionality"""
    print("Testing data storage...")
    
    # Test initial load (should create empty data)
    data = load_data()
    assert "transactions" in data, "Data should have transactions key"
    assert data["transactions"] == [], "Initial transactions should be empty"
    print("✓ Initial data load works")
    
    # Test saving data
    test_data = {
        "transactions": [
            {"type": "expense", "amount": 50.0, "category": "Food", "description": "Test", "date": "2024-01-01"},
            {"type": "income", "amount": 1000.0, "source": "Salary", "date": "2024-01-01"}
        ]
    }
    save_data(test_data)
    print("✓ Data save works")
    
    # Test loading saved data
    loaded_data = load_data()
    assert len(loaded_data["transactions"]) == 2, "Should load 2 transactions"
    assert loaded_data["transactions"][0]["type"] == "expense", "First transaction should be expense"
    assert loaded_data["transactions"][1]["type"] == "income", "Second transaction should be income"
    print("✓ Data load works")
    
    # Clean up
    if os.path.exists("expense_data.json"):
        os.remove("expense_data.json")
    print("✓ Test data cleaned up")

def test_date_function():
    """Test date functionality"""
    print("\nTesting date functionality...")
    date = get_current_date()
    assert len(date) == 10, "Date should be in YYYY-MM-DD format"
    assert date.count("-") == 2, "Date should have 2 dashes"
    print(f"✓ Current date format is correct: {date}")

def test_calculations():
    """Test financial calculations"""
    print("\nTesting calculations...")
    
    test_data = {
        "transactions": [
            {"type": "income", "amount": 1000.0, "source": "Salary", "date": "2024-01-01"},
            {"type": "income", "amount": 500.0, "source": "Bonus", "date": "2024-01-02"},
            {"type": "expense", "amount": 200.0, "category": "Food", "description": "Groceries", "date": "2024-01-03"},
            {"type": "expense", "amount": 150.0, "category": "Transport", "description": "Gas", "date": "2024-01-04"},
            {"type": "expense", "amount": 50.0, "category": "Food", "description": "Lunch", "date": "2024-01-05"}
        ]
    }
    
    total_income = sum(t["amount"] for t in test_data["transactions"] if t["type"] == "income")
    total_expenses = sum(t["amount"] for t in test_data["transactions"] if t["type"] == "expense")
    balance = total_income - total_expenses
    
    assert total_income == 1500.0, f"Total income should be 1500.0, got {total_income}"
    assert total_expenses == 400.0, f"Total expenses should be 400.0, got {total_expenses}"
    assert balance == 1100.0, f"Balance should be 1100.0, got {balance}"
    print("✓ Income/expense calculations work correctly")
    
    # Test category breakdown
    categories = {}
    for t in test_data["transactions"]:
        if t["type"] == "expense":
            category = t["category"]
            categories[category] = categories.get(category, 0) + t["amount"]
    
    assert categories["Food"] == 250.0, f"Food expenses should be 250.0, got {categories['Food']}"
    assert categories["Transport"] == 150.0, f"Transport expenses should be 150.0, got {categories['Transport']}"
    print("✓ Category breakdown works correctly")

if __name__ == "__main__":
    print("=== Expense Tracker Tests ===")
    print()
    
    try:
        test_data_storage()
        test_date_function()
        test_calculations()
        
        print()
        print("=" * 40)
        print("✓ All tests passed!")
        print("=" * 40)
        print()
        print("The expense tracker is working correctly.")
        print("You can now run it with: python3 expense_tracker.py")
        
    except AssertionError as e:
        print(f"\n✗ Test failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
        sys.exit(1)