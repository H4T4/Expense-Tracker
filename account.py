import csv

class Account:
    def __init__(self, balance=0.0, expenses=None):
        self.balance = balance
        self.expenses = expenses if expenses is not None else {}

    def add_expense(self):
        description = input("Describe the expense: ")
        try:
            amount = float(input("What is the amount of the expense? "))
        except ValueError:
            print("Invalid amount. Expense not added.")
            return

        self.balance -= amount
        self.expenses[description] = amount
        print(f"Your new balance is {self.balance:.2f} €.")

    def del_expense(self):
        expense = input("Which expense do you want to delete? ")
        if expense in self.expenses:
            del self.expenses[expense]
            print(f"Deleted expense '{expense}'.")
        else:
            print("Expense not found.")

    def update_expense(self, expense, new_key=None, new_amount=None):
        if expense not in self.expenses:
            print(f"Expense '{expense}' not found.")
            return

        # Rename if provided
        if new_key is not None and new_key.strip():
            self.expenses[new_key] = self.expenses.pop(expense)
            expense = new_key

        # Update amount if provided
        if new_amount is not None:
            try:
                self.expenses[expense] = float(new_amount)
            except ValueError:
                print("Amount must be a number.")

    def display_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
        else:
            print("These are all your expenses:")
            for desc, amt in self.expenses.items():
                print(f" - {desc}: {amt:.2f} €")



    def export_to_csv(self, filename="expenses.csv"):
        if not self.expenses:
            print("No expenses to export.")
            return

        # Define the column headers
        fieldnames = ["id", "date", "description", "amount", "category"]

        # Write expenses to CSV
        with open(filename, mode="w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.expenses)

        print(f"Expenses exported successfully to {filename}.")



def main():
    """
    Main function to run the expense tracker application.
    """
    print("--- Welcome to the Expense Tracker ---")
    try:
        initial_balance = float(input("Enter your initial account balance: "))
    except ValueError:
        print("Invalid input. Starting with a balance of 0.00 €.")
        initial_balance = 0.0

    my_account = Account(balance=initial_balance)

    # Main application loop
    while True:
        print("\nPlease choose an option:")
        print("1. Add Expense")
        print("2. Delete Expense")
        print("3. Update Expense")
        print("4. Display All Expenses")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            my_account.add_expense()
        elif choice == '2':
            my_account.del_expense()
        elif choice == '3':
            exp = input("Which expense do you want to update? ")
            new_name = input("New name (leave blank to keep): ")
            new_amt = input("New amount (leave blank to keep): ")
            my_account.update_expense(
                exp,
                new_key=new_name if new_name.strip() else None,
                new_amount=new_amt if new_amt.strip() else None
            )
        elif choice == '4':
            my_account.display_expenses()
        elif choice == '5':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
    print("Script erfolgreich ausgeführt")
