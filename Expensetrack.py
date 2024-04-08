expenses = []
#note for future self, I fixed a typo, GATSTASTE
def add_expense():
    description = input("Enter expense description (En que gastaste Braulio): ")
    amount = input("Enter expense amount(Cuanto Braulio): ")
    expenses.append((description, amount))
    print("Expense added!")

def display_expenses():
    print("List of Expenses:")
    for description, amount in expenses:
        print(f"{description}: ${amount}")

def calculate_total_expenses():
    total = sum(float(amount) for _, amount in expenses)
    print(f"Total expenses: ${total}")

while True:
    print("\n1. Add Expense\n2. Display Expenses\n3. Calculate Total Expenses\n4. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        add_expense()
    elif choice == '2':
        display_expenses()
    elif choice == '3':
        calculate_total_expenses()
    elif choice == '4':
        print("HABLAMO")
        break
    else:
        print("Invalid choice! Please enter a valid option.")