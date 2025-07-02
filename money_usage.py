import csv


def add_expense():
    purpose = input("Purpose: ")
    amount = input("Amount Spent: ")
    date = input("Date (YYYY-MM-DD): ")
    vendor = input("Vendor/Receiver: ")

    with open("data/expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([purpose, amount, date, vendor])
    print("✅ Expense recorded!")


def show_summary():
    total_donated = 0
    total_spent = 0

    try:
        with open("data/donors.csv", "r") as file:
            for row in csv.reader(file):
                if row[1].lower() == "money":
                    try:
                        total_donated += float(row[2])
                    except:
                        pass

        with open("data/expenses.csv", "r") as file:
            for row in csv.reader(file):
                try:
                    total_spent += float(row[1])
                except:
                    pass

        print(f"\n💰 Total Donated: {total_donated}")
        print(f"💸 Total Spent: {total_spent}")
        print(f"💼 Remaining Balance: {total_donated - total_spent}")
    except FileNotFoundError:
        print("No data found.")
