import csv, os, json
from datetime import datetime, timedelta
import time
import getpass

# Global data storage
expenses = []
habits = {}
notes = []
monthly_budget = None
users = {}
session_user = None

# ---------------------- USER AUTHENTICATION ----------------------
def register():
    global users
    username = input("Enter a username: ")
    if username in users:
        print("Username already exists!")
        return
    password = getpass.getpass("Enter a password: ")
    users[username] = password
    print("Registration successful!")

def login():
    global session_user
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    if users.get(username) == password:
        print("Login successful!")
        session_user = username
    else:
        print("Invalid credentials!")

# ---------------------- EXPENSE TRACKER ----------------------
def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    categories = ["Food", "Travel", "Utilities", "Entertainment", "Other"]
    print("Choose a category:")
    for i, c in enumerate(categories, 1):
        print(f"{i}. {c}")
    try:
        category = categories[int(input("Enter category number: ")) - 1]
        amount = float(input("Enter amount: "))
        description = input("Enter description: ")
        expenses.append({"date": date, "category": category, "amount": amount, "description": description})
        print("Expense added!")
    except (ValueError, IndexError):
        print("Invalid input!")

def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return
    print("\nExpenses:")
    for e in expenses:
        print(f"{e['date']} | {e['category']} | ₹{e['amount']} | {e['description']}")

# ---------------------- HABIT TRACKER ----------------------
def track_habit():
    habit = input("Enter habit name: ")
    if habit not in habits:
        habits[habit] = 0
    habits[habit] += 1
    print(f"Updated! {habit}: {habits[habit]} days streak")

def view_habits():
    if not habits:
        print("No habits tracked.")
        return
    print("\nHabit Streaks:")
    for habit, days in habits.items():
        print(f"{habit}: {days} days")

# ---------------------- POMODORO TIMER ----------------------
def pomodoro_timer():
    work_time = 25 * 60
    break_time = 5 * 60
    print("Starting Pomodoro (25 min work, 5 min break)")
    time.sleep(work_time)
    print("Break Time! 5 min")
    time.sleep(break_time)
    print("Pomodoro session complete!")

# ---------------------- NOTES & REMINDERS ----------------------
def add_note():
    note = input("Enter your note: ")
    notes.append(note)
    print("Note added!")

def view_notes():
    if not notes:
        print("No notes found.")
        return
    print("\nYour Notes:")
    for i, note in enumerate(notes, 1):
        print(f"{i}. {note}")

# ---------------------- MENU ----------------------
def menu():
    while True:
        print("\nPersonal Productivity App")
        print("1. Register\n2. Login\n3. Add Expense\n4. View Expenses\n5. Track Habit\n6. View Habits\n7. Pomodoro Timer\n8. Add Note\n9. View Notes\n10. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif session_user:
            if choice == "3":
                add_expense()
            elif choice == "4":
                view_expenses()
            elif choice == "5":
                track_habit()
            elif choice == "6":
                view_habits()
            elif choice == "7":
                pomodoro_timer()
            elif choice == "8":
                add_note()
            elif choice == "9":
                view_notes()
            elif choice == "10":
                print("Exiting...")
                break
            else:
                print("Invalid choice!")
        else:
            print("Please login first!")

if __name__ == "__main__":
    menu()
