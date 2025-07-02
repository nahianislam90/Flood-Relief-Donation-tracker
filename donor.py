donors = []

def add_donor():
    name = input("Donor Name: ")
    amount = float(input("Donation Amount: "))
    date = input("Donation Date (YYYY-MM-DD): ")
    method = input("Donation Method (cash/online/other): ")

    donor = {
        "name": name,
        "amount": amount,
        "date": date,
        "method": method
    }
    donors.append(donor)
    print(f"Donation from {name} added.\n")

def show_donors():
    if not donors:
        print("No donors yet.\n")
        return
    print("Donors List:")
    for idx, donor in enumerate(donors, 1):
        print(f"{idx}. {donor['name']} donated {donor['amount']} on {donor['date']} via {donor['method']}")
    print()

def main_menu():
    while True:
        print("Flood Relief Tracker")
        print("1. Add Donor")
        print("2. Show Donors")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_donor()
        elif choice == '2':
            show_donors()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main_menu()
