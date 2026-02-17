# Quick Start Guide

## Running the Expense Tracker

### On macOS/Linux

```bash
# Make the script executable
chmod +x expense_tracker.py

# Run the expense tracker
./expense_tracker.py

# Or use python directly
python3 expense_tracker.py
```

### On Termux/Android

```bash
# Install Python if not already installed
pkg install python

# Make the script executable
chmod +x expense_tracker.py

# Run the expense tracker
python expense_tracker.py
```

## First Time Usage

1. **Run the script** - The first time you run it, it will create an empty `expense_data.json` file
2. **Add your first expense** - Choose option 1 from the menu
3. **Add your first income** - Choose option 2 from the menu
4. **View your summary** - Choose option 3 to see your financial overview
5. **Browse history** - Choose option 4 to see all your transactions

## Example Workflow

```
$ python3 expense_tracker.py

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

=== EXPENSE TRACKER ===
1. Add Expense
2. Add Income
3. View Summary
4. View History
5. Exit

Choose an option (1-5): 2

=== ADD INCOME ===
Amount: $ 1000.00
Source: Salary
Date (YYYY-MM-DD, default: 2024-01-15): 
✓ Income added successfully!

Press Enter to continue...

=== EXPENSE TRACKER ===
1. Add Expense
2. Add Income
3. View Summary
4. View History
5. Exit

Choose an option (1-5): 3

=== FINANCIAL SUMMARY ===
Total Income:  $1000.00
Total Expenses: $50.00
Balance:       $950.00

=== EXPENSE BREAKDOWN ===
  Food: $50.00

Press Enter to continue...
```

## Tips

- **Use categories** - Group similar expenses (Food, Transport, Entertainment, etc.)
- **Add descriptions** - Helps you remember what the expense was for
- **Use dates** - Track when money comes in and goes out
- **Review regularly** - Check your summary to stay on top of your finances

## Data Backup

Your data is stored in `expense_data.json`. To backup:

```bash
# Copy to a safe location
cp expense_data.json ~/backups/expense_backup.json

# Or email it to yourself
mail -s "Expense Backup" -A expense_data.json your@email.com
```

## Troubleshooting

**Q: The script doesn't run**
A: Make sure you have Python 3 installed. On Termux, run `pkg install python`

**Q: Emojis don't display properly**
A: Your terminal may not support emojis. The tracker will still work fine.

**Q: I deleted the data file**
A: Just start over - the script will create a new one automatically.

**Q: How do I edit a transaction?**
A: Currently, you need to edit the `expense_data.json` file manually with a text editor.

---

Enjoy tracking your expenses! 💰💸