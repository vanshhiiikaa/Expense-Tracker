#Expense Tracker

import csv
import os


class Expense:
    """Represents a single expense entry."""
    def __init__(self, amount, category, date, note=""):
        self.amount = amount
        self.category = category
        self.date = date
        self.note = note

    def to_dict(self):
        return {"amount": self.amount, "category": self.category,
                "date": self.date, "note": self.note}


class ExpenseTracker:
    """Manages a collection of expenses, with CSV persistence."""
    def __init__(self, filename="expenses.csv"):
        self.filename = filename
        self.expenses = []
        self.load_expenses()

    def add_expense(self, amount, category, date, note=""):
        expense = Expense(amount, category, date, note)
        self.expenses.append(expense)
        self.save_expenses()
        print(f"Added: ₹{amount} for {category} on {date}")

    def save_expenses(self):
        with open(self.filename, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["amount", "category", "date", "note"])
            writer.writeheader()
            for e in self.expenses:
                writer.writerow(e.to_dict())

    def load_expenses(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    self.expenses.append(Expense(
                        float(row["amount"]), row["category"], row["date"], row["note"]
                    ))

    def total_spent(self):
        return sum(e.amount for e in self.expenses)

    def spending_by_category(self):
        totals = {}
        for e in self.expenses:
            totals[e.category] = totals.get(e.category, 0) + e.amount
        return totals

    def show_all(self):
        if not self.expenses:
            print("No expenses recorded yet.")
            return
        print("\n--- All Expenses ---")
        for e in self.expenses:
            note_display = f" | {e.note}" if e.note else ""
            print(f"{e.date} | {e.category} | ₹{e.amount}{note_display}")

    def plot_by_category(self):
        try:
            import matplotlib.pyplot as plt
        except ImportError:
            print("Matplotlib not installed. Run: pip install matplotlib")
            return

        data = self.spending_by_category()
        if not data:
            print("No data to plot yet. Add some expenses first.")
            return

        plt.figure(figsize=(6, 6))
        plt.pie(data.values(), labels=data.keys(), autopct="%1.1f%%", startangle=90)
        plt.title("Spending by Category")
        plt.show()


def main():
    tracker = ExpenseTracker()

    while True:
        print("\n===== Personal Expense Tracker =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Spent")
        print("4. View Spending by Category")
        print("5. Show Spending Chart")
        print("6. Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            try:
                amount = float(input("Enter amount: ₹"))
                category = input("Enter category (e.g. Food, Travel, Bills): ").strip()
                date = input("Enter date (YYYY-MM-DD): ").strip()
                note = input("Enter note (optional): ").strip()
                tracker.add_expense(amount, category, date, note)
            except ValueError:
                print("Invalid amount. Please enter a number.")

        elif choice == "2":
            tracker.show_all()

        elif choice == "3":
            print(f"Total Spent: ₹{tracker.total_spent():.2f}")

        elif choice == "4":
            data = tracker.spending_by_category()
            if not data:
                print("No expenses recorded yet.")
            else:
                print("\n--- Spending by Category ---")
                for category, total in data.items():
                    print(f"{category}: ₹{total:.2f}")

        elif choice == "5":
            tracker.plot_by_category()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()