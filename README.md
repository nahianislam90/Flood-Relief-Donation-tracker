 Flood Relief Donation Tracker

This is a simple Python app to track donations for a flood relief campaign.

You can:
- Add donor name, amount, date, and method
- See a list of all donors
- See total money collected

Built using Python and Tkinter. Data is saved in a JSON file.


How to Use
1. Install Required Package

Only one package is needed:

bash
pip install pandas
Tkinter comes with Python automatically.

2. Run the App
Make sure you have this file in your folder:

donor_tracker.py (the app code)
Then run:

bash
Copy
Edit
python donor_tracker.py

demo:![Food Relief tracker work](https://github.com/user-attachments/assets/52fd9cfd-c820-4d87-8259-280d383bea7c)
![flood Relief Work](https://github.com/user-attachments/assets/7d3d5aff-63c5-4fc2-ae81-aec5d6744d1f)


3. Add Donors
Type the donor’s name, amount, date (e.g. 2024-07-01), and method (cash/online)

Click Add Donor

4. Show Donors
Click Show All Donors to see the full list and total money collected.
donor_tracker.py     # Main app
donors.json          # Saved donor data
README.md            # This file

