class Account:
    def __init__(self, balance, expenses):
        self.balance = balance
        self.expenses = expenses

        

    def add_expense(self):
        description = str(input("Describe the expense."))
        amount = float(input("What is the amount of the expense?"))

        self.balance -= amount
        self.expenses.append({description : amount})

        print(f"Your new balance is {self.balance} €.")


    def del_expense(self):
        try:
            expense = str(input("Which expense do you want to delete?"))
        except ValueError:
            print("Invalid Input, try again")
        else:
            for name in self.expenses.key:
                if name == expense:
                    self.expenses.remove(name)
                else:
                    pass
                
    def update_expense(self, expense, new_key=None, new_amount=None):
        if expense not in self.expenses:
            raise KeyError(f"Expense '{expense}' not found.")

        # Handle optional renaming
        if new_key is not None and new_key.strip():
            self.expenses[new_key] = self.expenses.pop(expense)
            expense = new_key  # update reference

        # Handle optional amount update
        if new_amount is not None:
            try:
                self.expenses[expense] = float(new_amount)
            except ValueError:
                raise ValueError("Amount must be a number.")


    def display_expenses(self):
        print(f"These are all your expenses: {self.expenses}")


print("skript erfolgreich ausgeführt")



       