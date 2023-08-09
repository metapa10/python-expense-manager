class Expense:
    def __init__(self, description, amount, category):
        self.description = description
        self.amount = amount
        self.category = category

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def calculate_total(self):
        total = 0
        for expense in self.expenses:
            total += expense.amount
        return total

    def get_expenses_by_category(self, category):
        return [expense for expense in self.expenses if expense.category == category]

# Sample usage
def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Total Expenses")
        print("3. View Expenses by Category")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter expense description: ")
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")
            expense = Expense(description, amount, category)
            tracker.add_expense(expense)
            print("Expense added successfully!")
        
        elif choice == "2":
            total = tracker.calculate_total()
            print(f"Total Expenses: ${total:.2f}")
        
        elif choice == "3":
            category = input("Enter category to view expenses: ")
            expenses_by_category = tracker.get_expenses_by_category(category)
            print(f"Expenses in {category}:")
            for expense in expenses_by_category:
                print(f"{expense.description}: ${expense.amount:.2f}")
        
        elif choice == "4":
            print("Exiting the Expense Tracker. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
