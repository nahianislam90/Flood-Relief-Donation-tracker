import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt

# Data lists
donors = []
expenses = []

# Styling colors
BG_COLOR = "#f5f7fa"
BTN_COLOR = "#4CAF50"
BTN_TEXT_COLOR = "#ffffff"
FONT = ("Segoe UI", 10)

# Add donor window
def add_donor():
    def save_donor():
        name = entry_name.get().strip()
        amount_text = entry_amount.get().strip()
        if not name or not amount_text:
            messagebox.showerror("Error", "Please enter name and amount.")
            return
        try:
            amount = float(amount_text)
        except ValueError:
            messagebox.showerror("Error", "Amount must be a number.")
            return
        donors.append({"name": name, "amount": amount})
        messagebox.showinfo("Success", f"Donor {name} added with amount {amount}.")
        donor_win.destroy()
        update_balance()

    donor_win = tk.Toplevel(root)
    donor_win.title("Add Donor")
    donor_win.configure(bg=BG_COLOR)

    tk.Label(donor_win, text="Name:", bg=BG_COLOR, font=FONT).grid(row=0, column=0, padx=10, pady=5, sticky="e")
    entry_name = tk.Entry(donor_win, font=FONT)
    entry_name.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(donor_win, text="Amount:", bg=BG_COLOR, font=FONT).grid(row=1, column=0, padx=10, pady=5, sticky="e")
    entry_amount = tk.Entry(donor_win, font=FONT)
    entry_amount.grid(row=1, column=1, padx=10, pady=5)

    save_btn = tk.Button(donor_win, text="Save", command=save_donor, bg=BTN_COLOR, fg=BTN_TEXT_COLOR, font=FONT)
    save_btn.grid(row=2, column=0, columnspan=2, pady=10)

# Add expense window
def add_expense():
    def save_expense():
        purpose = entry_purpose.get().strip()
        amount_text = entry_amount.get().strip()
        if not purpose or not amount_text:
            messagebox.showerror("Error", "Please enter purpose and amount.")
            return
        try:
            amount = float(amount_text)
        except ValueError:
            messagebox.showerror("Error", "Amount must be a number.")
            return
        expenses.append({"purpose": purpose, "amount": amount})
        messagebox.showinfo("Success", f"Expense '{purpose}' added with amount {amount}.")
        expense_win.destroy()
        update_balance()

    expense_win = tk.Toplevel(root)
    expense_win.title("Add Expense")
    expense_win.configure(bg=BG_COLOR)

    tk.Label(expense_win, text="Purpose:", bg=BG_COLOR, font=FONT).grid(row=0, column=0, padx=10, pady=5, sticky="e")
    entry_purpose = tk.Entry(expense_win, font=FONT)
    entry_purpose.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(expense_win, text="Amount:", bg=BG_COLOR, font=FONT).grid(row=1, column=0, padx=10, pady=5, sticky="e")
    entry_amount = tk.Entry(expense_win, font=FONT)
    entry_amount.grid(row=1, column=1, padx=10, pady=5)

    save_btn = tk.Button(expense_win, text="Save", command=save_expense, bg=BTN_COLOR, fg=BTN_TEXT_COLOR, font=FONT)
    save_btn.grid(row=2, column=0, columnspan=2, pady=10)

# Show donors table
def show_donors():
    window = tk.Toplevel(root)
    window.title("Donor List")
    tree = ttk.Treeview(window, columns=("Name", "Amount"), show="headings")
    tree.heading("Name", text="Name")
    tree.heading("Amount", text="Amount")
    for donor in donors:
        tree.insert("", "end", values=(donor["name"], donor["amount"]))
    tree.pack(fill="both", expand=True)
    window.geometry("300x300")

# Show expenses table
def show_expenses():
    window = tk.Toplevel(root)
    window.title("Expense List")
    tree = ttk.Treeview(window, columns=("Purpose", "Amount"), show="headings")
    tree.heading("Purpose", text="Purpose")
    tree.heading("Amount", text="Amount")
    for expense in expenses:
        tree.insert("", "end", values=(expense["purpose"], expense["amount"]))
    tree.pack(fill="both", expand=True)
    window.geometry("300x300")

# Show pie chart
def show_chart():
    total_donations = sum(d['amount'] for d in donors)
    total_expenses = sum(e['amount'] for e in expenses)
    balance = total_donations - total_expenses

    if total_donations == 0:
        messagebox.showinfo("No Data", "No donation data to show chart.")
        return

    labels = ['Used (Expenses)', 'Remaining Balance']
    sizes = [total_expenses, max(balance, 0)]
    colors = ['#FF6F61', '#6BDE90']

    plt.figure(figsize=(5, 5))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
    plt.title("Donation Usage Chart")
    plt.axis('equal')
    plt.show()

# Update balance labels
def update_balance():
    total_donations = sum(d['amount'] for d in donors)
    total_expenses = sum(e['amount'] for e in expenses)
    balance = total_donations - total_expenses
    label_donations.config(text=f"Total Donations: ${total_donations:.2f}")
    label_expenses.config(text=f"Total Expenses: ${total_expenses:.2f}")
    label_balance.config(text=f"Remaining Balance: ${balance:.2f}")

# Main window
root = tk.Tk()
root.title("Flood Relief Donation Tracker")
root.configure(bg=BG_COLOR)

tk.Label(root, text="Flood Relief Tracker", font=("Segoe UI", 14, "bold"), bg=BG_COLOR, fg="#333").pack(pady=10)

# Buttons
button_frame = tk.Frame(root, bg=BG_COLOR)
button_frame.pack(pady=5)

def make_button(text, cmd):
    return tk.Button(button_frame, text=text, command=cmd, bg=BTN_COLOR, fg=BTN_TEXT_COLOR,
                     font=FONT, relief="flat", width=25)

make_button("➕ Add Donor", add_donor).pack(pady=4)
make_button("📋 Show Donors (Table)", show_donors).pack(pady=4)
make_button("➖ Add Expense", add_expense).pack(pady=4)
make_button("📋 Show Expenses (Table)", show_expenses).pack(pady=4)
make_button("📊 Show Pie Chart", show_chart).pack(pady=8)

# Summary
label_donations = tk.Label(root, text="Total Donations: $0.00", bg=BG_COLOR, font=FONT)
label_donations.pack()
label_expenses = tk.Label(root, text="Total Expenses: $0.00", bg=BG_COLOR, font=FONT)
label_expenses.pack()
label_balance = tk.Label(root, text="Remaining Balance: $0.00", bg=BG_COLOR, font=FONT)
label_balance.pack(pady=(0, 10))

root.geometry("350x500")
root.mainloop()
