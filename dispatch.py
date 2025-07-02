import csv
from datetime import datetime


def add_dispatch():
    dispatch_date = input(
        "Date of Dispatch (YYYY-MM-DD) [leave empty for today]: ")
    if not dispatch_date:
        dispatch_date = datetime.now().strftime('%Y-%m-%d')
    truck_id = input("Truck ID / Plate Number: ")
    destination = input("Destination Area: ")
    rice = input("Rice (kg): ")
    water = input("Water (liters): ")
    clothes = input("Clothes (bags): ")
    medicine = input("Medicine (boxes): ")
    volunteers = input("Volunteers (comma separated): ")
    status = input("Status (Sent/Delivered/Delayed): ")
    notes = input("Notes (optional): ")

    with open("data/dispatch.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([dispatch_date, truck_id, destination, rice,
                        water, clothes, medicine, volunteers, status, notes])
    print("✅ Dispatch logged!")
