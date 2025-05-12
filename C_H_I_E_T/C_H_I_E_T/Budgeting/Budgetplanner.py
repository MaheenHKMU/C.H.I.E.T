#Budgeting

import json # importing json to store the inputs (complex data type) easily 


# the File to store the budget information
FILENAME = 'budget_planner.json'


def load_budget():
    """Load the budget data from a JSON file."""
    # File I/O this function reads data from a file (Lecture 8)

    try:
        with open(FILENAME, 'r') as file:               #opening the file in read mode to load existing budget data
            return json.load(file)                      # reads the JSON data from the file and converts it into python dictionary.
    except (FileNotFoundError, json.JSONDecodeError):
                                                        # If the file is missing or doesn't work right, it will just return with the default budget setup.
        return {'income': 0, 'expenses': []}


def save_budget(budget):
    """Save the budget data to a JSON file."""
    # File I/O (Lecture 8)

    with open(FILENAME, 'w') as file:                   # this function writes the budget data to a JSON file
        json.dump(budget, file)                         # takes the budget dictionary and converts it to JSON format, then writes it to specified file
                                                        # using JSON allows to easily store and retrieve dictionaries and list


def add_income(budget):
    """Add income to the budget."""
    # Functions - defines a specific task related to budget management (Lecture 7)

    try:
        amount = float(input("Enter the income amount: "))     # this part asks the users for their income amount
        budget['income'] += amount                             # Update income in the budget dictionary
        save_budget(budget)                                    # Call to save the updated budget to the file
        print("Income added successfully!")
    except ValueError:
        print("Invalid input. Please enter a numeric value for income") # this part is all about dealing with errors when the input isn't valid.


def edit_income(budget):
    """Edit the existing income."""
    # Functions 
   
    try:
        new_income = float(input("Enter the new income amount: ")) # Prompt for new income
        budget['income'] = new_income                              # Update income in the budget dictionary
        save_budget(budget)
        print("Income updated successfully!")
    except ValueError:
        print("Invalid input. Please enter a numeric value for income")


def add_expense(budget):
    """Add an expense to the budget."""
    # Functions 

    description = input("Enter the expense description: ")                        # Prompt for expense description
    try:
        amount = float(input("Enter the expense amount: "))
        budget['expenses'].append({'description': description, 'amount': amount}) # Data collection - Append a new expense dictionary to the list of expenses
        save_budget(budget)
        print("Expense added successfully!")
    except ValueError:
        print("Invalid input. Please enter a numeric value for expense amount")


def view_balance(budget):
    """View the current balance."""
    # Decision structure - Used to calculate the balance based on income and expenses (Lecture 4)

    total_expenses = sum(expense['amount'] for expense in budget['expenses']) 
    balance = budget['income'] - total_expenses
    print(f"Current Balance: ${balance:.2f}") # display the balance formatted to 2 decimal places


def view_expenses(budget):
    """View all expenses."""
    # Decision structure: checks if there are any expenses to dispaly (Lecure 4)

    if not budget['expenses']:
        print("No expenses recorded.")
        return
    
    print("\nExpenses:")
    for idx, expense in enumerate(budget['expenses'], start=1): # the "enumerate" is used to iterate over the list of expenses in the "budget['expenses]" dictionary.
    # the above line generates pairs of index and expense. The "start=1" argument means that the indexing will begin at 1 instead of 0.
     
        print(f"{idx}. {expense['description']} - ${expense['amount']:.2f}") # Displays each expense, "idx": the current index 


def edit_expense(budget):
    """Edit an existing expense."""  

    view_expenses(budget)
    if budget['expenses']:
        try:
           index = int(input("Enter the index of the expense to edit: ")) - 1
        
           # Decision Structure - Validate the index 
           if 0 <= index < len(budget['expenses']): # Checks if the index is valid
               new_description = input("Enter the new expense description: ")
               new_amount = float(input("Enter the new expense amount: "))
               budget['expenses'][index] = {'description': new_description, 'amount': new_amount}
               save_budget(budget)
               print("Expense updated successfully!")
           else:
               print("Invalid index. Please enter a valid index.") # Error handling for invalid index
        except ValueError:
            print("Invalid input. Please enter a numeric value for the expense amount.") #Error handling for invalid input


def delete_expense(budget):
    """Delete an expense from the budget."""

    view_expenses(budget)
    if budget['expenses']:
        try:
            index = int(input("Enter the index of the expense to delete: ")) - 1 # get the index to delete
        
            if 0 <= index < len(budget['expenses']): # check if index is valid
                budget['expenses'].pop(index) # Remove expense from the list
                save_budget(budget)
                print("Expense deleted successfully!")
            else:
                print("Invalid index. Please enter a valid index.")  
        except ValueError:
            print("Invalid input. Please enter a numeric value for the index.")        


def menu():
    """Display the menu and handle user choices."""

    budget = load_budget() # Load existing budget data

    while True: # Repetition structure allows continuous interaction until the user exits
        print("\nBudget Planner Menu:")
        print("1. Add Income")
        print("2. Edit Income")
        print("3. Add Expenses")
        print("4. View Balance")
        print("5. View Expenses")
        print("6. Edit Expense")
        print("7. Delete Expense")
        print("8. Exit")
        
        choice = input("Enter your choice (1-8): ") 

        # Condition structures to handle choices given as inputs  
        if choice == '1':
            add_income(budget)
        elif choice == '2':
            edit_income(budget)
        elif choice == '3':
            add_expense(budget)
        elif choice == '4':
            view_balance(budget)
        elif choice == '5':
            view_expenses(budget)
        elif choice == '6':
            edit_expense(budget)
        elif choice == '7':
            delete_expense(budget)
        elif choice == '8':
            print("Exiting the program.")
            break # Exit the loop and end the program
        else:
            print("Invalid choice. Please select a number between 1 and 8.")


if __name__ == "__main__":
    menu() # starts the program by displaying the menu 