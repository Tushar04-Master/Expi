# Minimal Terminal Expense Tracker

A simple, cross-platform expense tracker that works on macOS/Linux terminals and Termux/Android.

## Features

- ✅ Add expenses with category and description
- ✅ Add income with source
- ✅ View financial summary (income, expenses, balance)
- ✅ View transaction history
- ✅ Expense breakdown by category
- ✅ No dependencies (pure Python 3)
- ✅ Cross-platform compatible

## Installation

### On macOS/Linux

1. Clone or download this repository
2. Make the script executable:
   ```bash
   chmod +x expense_tracker.py
   ```
3. Run the tracker:
   ```bash
   ./expense_tracker.py
   ```

### On Termux/Android

1. Install Termux from F-Droid or Play Store
2. Open Termux and run:
   ```bash
   pkg install python
   pkg install git
   git clone https://github.com/yourusername/expense-tracker.git
   cd expense-tracker
   chmod +x expense_tracker.py
   python expense_tracker.py
   ```

## Usage

When you run the expense tracker, you'll see a menu with these options:

1. **Add Expense** - Record a new expense with amount, category, and description
2. **Add Income** - Record income with amount and source
3. **View Summary** - See your total income, expenses, balance, and expense breakdown
4. **View History** - Browse all your transactions
5. **Exit** - Quit the application

## Data Storage

All your data is stored in `expense_data.json` in the same directory as the script. This file is created automatically when you add your first transaction.

## Example Session

```
=== EXPENSE TRACKER ===
1. Add Expense
2. Add Income
3. View Summary
4. View History
5. Exit

Choose an option (1-5): 1

=== ADD EXPENSE ===
Amount: $ 50.00
Category: Food
Description: Grocery shopping
Date (YYYY-MM-DD, default: 2024-01-15): 
✓ Expense added successfully!

Press Enter to continue...
```

## Requirements

- Python 3 (included on macOS/Linux, available via Termux on Android)
- No additional dependencies needed

## Notes

- The script uses emojis (💰, 💸) for visual appeal. If your terminal doesn't support emojis, they'll display as empty boxes or question marks.
- All data is stored locally on your device.
- Press Enter to continue after each operation.

## License

This is a minimal example. Feel free to modify and extend it as needed!

---