from pathlib import Path
import csv
from datetime import datetime

FILE = Path("attendance.csv")


def mark_attendance(student_id):
    today = datetime.now().strftime("%Y-%m-%d")

    if FILE.exists():
        with open(FILE, newline="") as file:
            records = list(csv.DictReader(file))

        if any(
            r["ID"] == student_id
            and r["Date"] == today
            for r in records
        ):
            return "Already marked!"

    new_file = not FILE.exists()

    with open(FILE, "a", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["ID", "Date", "Time"]
        )

        if new_file:
            writer.writeheader()

        now = datetime.now()

        writer.writerow({
            "ID": student_id,
            "Date": today,
            "Time": now.strftime("%H:%M:%S")
        })

    return "Attendance marked!"


print("\n" + "=" * 55)
print("             QR ATTENDANCE SYSTEM")
print("=" * 55)

student_id = input(
    "\nScan / Enter Student ID: "
).strip()

if student_id:
    print(f"\n {mark_attendance(student_id)}")
else:
    print("\nInvalid Student ID!")

print("=" * 55)