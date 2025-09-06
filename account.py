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
                
    def update_expense():
        pass






       