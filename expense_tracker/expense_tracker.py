import json
from datetime import datetime

DATA_FILE = "expenses.json"

class Expense:
    def __init__(self,date,category,amount,description):
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description
    def to_dict(self):
        return {
            "date": self.date,
            "category": self.category,
            "amount": self.amount,
            "description": self.description
        }

    @staticmethod
    def from_dict(data):
        return Expense(
            data["date"], data["category"], data["amount"], data["description"]
        )

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.load_expenses()

    def load_expenses(self):
        try:
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
                self.expenses = [Expense.from_dict(e) for e in data]
        except FileNotFoundError:
            self.expenses = []

    def save_expenses(self):
        with open(DATA_FILE, "w") as f:
            json.dump([e.to_dict() for e in self.expenses], f, indent=4)

    def add_expense(self):
        date_str = input("Enter date (YYYY-MM-DD) [default: today]: ")
        if not date_str:
            date_str = datetime.today().strftime("%Y-%m-%d")

        category = input("Enter category (e.g. Food, Travel): ")
        amount = float(input("Enter amount: "))
        description = input("Enter description: ")

        expense = Expense(date_str, category, amount, description)
        self.expenses.append(expense)
        self.save_expenses()
        print("Expense added successfully!")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses to show.")
            return

        print("\nAll Expenses:")
        for i, e in enumerate(self.expenses, 1):
            print(f"{i}. {e.date} | {e.category} | ${e.amount:.2f} | {e.description}")
        print()

    def run(self):
        while True:
            print("\nExpense Tracker Menu:")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                self.add_expense()
            elif choice == "2":
                self.view_expenses()
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid choice, try again.")

if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.run()