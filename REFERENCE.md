# 📋 Quick Reference Card

## Expense Tracker Commands

### Run the Application
```bash
# On macOS/Linux
./expense_tracker.py

# On Termux/Android
python expense_tracker.py
```

### Run Tests
```bash
python3 test_expense_tracker.py
```

### Run Demo
```bash
python3 demo.py
```

## Menu Options

| Number | Option | Description |
|--------|--------|-------------|
| 1 | Add Expense | Record a new expense with amount, category, and description |
| 2 | Add Income | Record income with amount and source |
| 3 | View Summary | See total income, expenses, balance, and category breakdown |
| 4 | View History | Browse all transactions sorted by date |
| 5 | Exit | Quit the application |

## Data Fields

### For Expenses
- **Amount**: Numeric value (e.g., 50.00)
- **Category**: Type of expense (e.g., Food, Transport, Entertainment)
- **Description**: What the expense was for (e.g., Grocery shopping)
- **Date**: YYYY-MM-DD format (defaults to today)

### For Income
- **Amount**: Numeric value (e.g., 1000.00)
- **Source**: Where the money came from (e.g., Salary, Freelance)
- **Date**: YYYY-MM-DD format (defaults to today)

## Example Usage

### Add an Expense
```
Choose an option (1-5): 1

=== ADD EXPENSE ===
Amount: $ 50.00
Category: Food
Description: Grocery shopping
Date (YYYY-MM-DD, default: 2024-01-15): 
```

### Add Income
```
Choose an option (1-5): 2

=== ADD INCOME ===
Amount: $ 1000.00
Source: Salary
Date (YYYY-MM-DD, default: 2024-01-15): 
```

### View Summary
```
Choose an option (1-5): 3

=== FINANCIAL SUMMARY ===
Total Income:  $1000.00
Total Expenses: $50.00
Balance:       $950.00

=== EXPENSE BREAKDOWN ===
  Food: $50.00
```

## Data Storage

- **File**: `expense_data.json`
- **Format**: JSON (human-readable)
- **Location**: Same directory as the script
- **Backup**: Copy the file to a safe location

## Common Categories

- **Food**: Groceries, dining out, snacks
- **Transport**: Gas, bus fare, taxi, public transport
- **Housing**: Rent, mortgage, utilities
- **Entertainment**: Movies, games, subscriptions
- **Health**: Doctor visits, medication, gym
- **Education**: Books, courses, tuition
- **Shopping**: Clothing, electronics, personal items
- **Other**: Miscellaneous expenses

## Tips

1. **Be consistent** with category names
2. **Add descriptions** to remember what expenses were for
3. **Review weekly** to stay on top of your finances
4. **Backup regularly** your expense_data.json file
5. **Use dates** to track when money was spent/earned

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Script doesn't run | Install Python: `pkg install python` (Termux) or `brew install python` (macOS) |
| Emojis don't display | Your terminal doesn't support emojis (tracker still works) |
| Data file missing | Script creates it automatically on first run |
| Invalid amount error | Enter numbers only (use . for decimals) |

## File Structure

```
expense_tracker.py    # Main application
README.md             # Complete documentation
QUICKSTART.md         # Quick start guide
SUMMARY.md            # Project summary
REFERENCE.md          # This reference card

test_expense_tracker.py # Automated tests
demo.py               # Demonstration script
expense_data.json     # Your transaction data (created automatically)
```

## Support

This is a minimal expense tracker. For issues or questions:
1. Check the README.md for detailed instructions
2. Review the QUICKSTART.md for quick help
3. Look at the demo.py for usage examples
4. The code is simple - you can modify it as needed!

---

**Keep track of your finances!** 💰💸