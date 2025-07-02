from donor import add_donor, show_donors
from money_usage import add_expense, show_summary
from dispatch import add_dispatch
from volunteers import add_volunteer, show_volunteers


def menu():
    while True:
        print("\n=== FLOOD RELIEF DONATION TRACKER ===")
        print("1. Add Donor")
        print("2. Show Donors")
        print("3. Add Expense")
        print("4. Show Money Summary")
        print("5. Add Dispatch")
        print("6. Add Volunteer")
        print("7. Show Volunteers")
        print("0. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            add_donor()
        elif choice == '2':
            show_donors()
        elif choice == '3':
            add_expense()
        elif choice == '4':
            show_summary()
        elif choice == '5':
            add_dispatch()
        elif choice == '6':
            add_volunteer()
        elif choice == '7':
            show_volunteers()
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("❌ Invalid choice.")


if __name__ == "__main__":
    menu()
