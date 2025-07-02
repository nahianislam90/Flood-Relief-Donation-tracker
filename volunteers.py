import csv


def add_volunteer():
    name = input("Volunteer Name: ")
    role = input("Role (distribution, cooking, etc.): ")

    with open("data/volunteers.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, role])
    print("✅ Volunteer added!")


def show_volunteers():
    print("\n👥 Volunteer List:")
    try:
        with open("data/volunteers.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No volunteers found.")
