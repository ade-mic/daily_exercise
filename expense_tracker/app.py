#!/usr/bin/env python3
"""
Main Program to run expenses tracker
"""
from tracker import ExpenseTracker

def interactive_mode():
    """Run the Expense Tracker in interactive mode."""
    print("Welcome to the Expense Tracker!")
    tracker = ExpenseTracker(name=input("Enter a name for your tracker: ").strip())

    while True:
        print("\nChoose an action:")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Filter Expenses")
        print("4. Save to File")
        print("5. Load from File")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ").strip()

        try:
            if choice == "1":
                amount = float(input("Enter amount: "))
                category = input("Enter category: ").strip()
                description = input("Enter description (optional): ").strip()
                tracker.add_expense(amount, category, description)
            elif choice == "2":
                tracker.summarize_expenses()
            elif choice == "3":
                start_date = input("Enter start date (YYYY-MM-DD) or leave blank: ").strip() or None
                end_date = input("Enter end date (YYYY-MM-DD) or leave blank: ").strip() or None
                category = input("Enter category to filter by or leave blank: ").strip() or None
                tracker.filter_expenses(start_date, end_date, category)
            elif choice == "4":
                filename = input("Enter filename to save to: ").strip()
                tracker.save_to_file(filename)
            elif choice == "5":
                filename = input("Enter filename to load from: ").strip()
                tracker.load_from_file(filename)
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    interactive_mode()
