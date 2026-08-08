# Personal Expense Tracker 💰

A Python command-line application to track personal expenses — add entries, view spending totals, break down spending by category, and visualize it with a chart. Built using Object-Oriented Programming and CSV file persistence.

## Features

- Add expenses with amount, category, date, and an optional note
- View all recorded expenses
- View total amount spent
- View spending broken down by category
- Visualize spending by category using a Matplotlib pie chart
- Data persists between runs using a CSV file
- Input validation for invalid amounts

## Demo

```
===== Personal Expense Tracker =====
1. Add Expense
2. View All Expenses
3. View Total Spent
4. View Spending by Category
5. Show Spending Chart
6. Exit

Select an option: 1
Enter amount: ₹250
Enter category (e.g. Food, Travel, Bills): Food
Enter date (YYYY-MM-DD): 2026-08-08
Enter note (optional): Lunch with friends
Added: ₹250.0 for Food on 2026-08-08

Select an option: 3
Total Spent: ₹250.00
```

## How It Works

The project is built around two core classes:

- **`Expense`** — represents a single expense entry (amount, category, date, note)
- **`ExpenseTracker`** — manages the full collection of expenses; handles adding entries, calculating totals, category breakdowns, saving/loading from CSV, and generating the pie chart

On startup, the tracker automatically loads any previously saved expenses from `expenses.csv`. Every time a new expense is added, it's immediately saved back to the file, so nothing is lost between runs.

## Getting Started

### Prerequisites
- Python 3.x
- Matplotlib (`pip install matplotlib`)

### Installation
```bash
git clone https://github.com/vanshhiiikaa/Expense-Tracker.git
cd Expense-Tracker
```

### Usage
```bash
python expense_tracker.py
```
Follow the on-screen menu to add expenses, view totals, and generate the spending chart.

## Tech Stack
- Python 3
- Object-Oriented Programming
- `csv` module (data persistence)
- Matplotlib (data visualization)

## Possible Improvements
- [ ] Add ability to delete or edit an existing expense
- [ ] Filter expenses by date range or month
- [ ] Set a monthly budget and get a warning when exceeded
- [ ] Add a bar chart showing spending trend over time
- [ ] Switch from CSV to SQLite for more robust data storage
- [ ] Add unit tests

## Author
**Vanshika**
- GitHub: [@vanshhiiikaa](https://github.com/vanshhiiikaa)
- LinkedIn: [Vanshika Gupta](https://www.linkedin.com/in/vanshika-gupta-4a2002329)

## License
This project is open source and available under the [MIT License](LICENSE).
