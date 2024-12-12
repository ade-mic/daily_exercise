#!/usr/bin/env python3
"""
A simple expense tracker that helps manage personal expenses by categorizing and summarizing them.

Attributes:
    name (str): The name of the expense tracker.
    start_date (str): The date the tracker was started (in 'YYYY-MM-DD' format).
    expenses (list): A list of expense records, each containing the
      amount, category, description, and date of the expense.

Methods:
    __init__(self, name: str): Initializes the expense tracker with a name and the start date.
    add_expense(self, amount: float, category: str, description: str = ""):
    Adds a new expense with a given amount, category, and optional description.
    save_to_file(self, filename: str): Saves the expense data to a JSON file.
    load_from_file(self, filename: str): Loads expense data from a JSON file.
    summarize_expenses(self): Summarizes the total expenses and expenses by category.
    filter_expenses(self, start_date: str = None, end_date: str = None, category: str = None):
      Filters expenses based on optional start date, end date, and category.
"""

import json
from datetime import datetime


class ExpenseTracker:
    """
    A simple expense tracker that helps manage personal expenses
    by categorizing and summarizing them.

    Attributes:
        name (str): The name of the expense tracker.
        start_date (str): The date the tracker was started (in 'YYYY-MM-DD' format).
        expenses (list): A list of expense records,
          each containing the amount, category, description, and date of the expense.

    Methods:
        __init__(self, name: str): Initializes the expense tracker with a name and the start date.
        add_expense(self, amount: float, category: str, description: str = ""):
          Adds a new expense with a given amount, category, and optional description.
        save_to_file(self, filename: str): Saves the expense data to a JSON file.
        load_from_file(self, filename: str): Loads expense data from a JSON file.
        summarize_expenses(self): Summarizes the total expenses and expenses by category.
        filter_expenses(self, start_date: str = None, end_date: str = None, category: str = None):
          Filters expenses based on optional start date, end date, and category.
    """
    def __init__(self, name: str):
        """
        Initialize the Expense Tracker.

        Args:
            name (str): Name of the expense tracker.
        """
        self.name = name
        self.start_date = datetime.now().strftime("%Y-%m-%d")
        self.expenses = []

    def add_expense(self, amount: float, category: str, description: str = ""):
        """
        Add an expense to the tracker.

        Args:
            amount (float): The expense amount (must be > 0).
            category (str): The category of the expense.
            description (str): Optional description of the expense.
        """
        if amount <= 0:
            raise ValueError("Amount must be greater than zero")
        expense = {
            "amount": amount,
            "category": category,
            "description": description,
            "date": datetime.now().strftime("%Y-%m-%d")
        }
        self.expenses.append(expense)

    def save_to_file(self, filename: str):
        """Save expenses to a file."""
        data = {
            "name": self.name,
            "start_date": self.start_date,
            "expenses": self.expenses
        }
        with open(filename, "w", encoding='utf8') as file:
            json.dump(data, file, indent=4)
        print(f"Expenses saved to {filename}")

    def load_from_file(self, filename: str):
        """Load expenses from a file."""
        try:
            with open(filename, "r", encoding='utf8') as file:
                data = json.load(file)
                self.name = data.get("name", self.name)
                self.start_date = data.get("start_date", self.start_date)
                self.expenses = data.get("expenses", [])
            print(f"Expenses loaded from {filename}")
        except FileNotFoundError:
            print(f"No file found named {filename}. Starting fresh.")

    def summarize_expenses(self):
        """Summarize expenses."""
        total = sum(expense["amount"] for expense in self.expenses)
        categories = {}
        for expense in self.expenses:
            category = expense["category"]
            categories[category] = categories.get(category, 0) + expense["amount"]
        summary = {"total": total, "by_category": categories}
        print(f"Summary: {summary}")
        return summary

    def filter_expenses(self, start_date: str = None, end_date: str = None, category: str = None):
        """Filter expenses."""
        filtered = self.expenses
        if start_date:
            filtered = [e for e in filtered if e["date"] >= start_date]
        if end_date:
            filtered = [e for e in filtered if e["date"] <= end_date]
        if category:
            filtered = [e for e in filtered if e["category"].lower() == category.lower()]
        print(f"Filtered Expenses: {filtered}")
        return filtered
