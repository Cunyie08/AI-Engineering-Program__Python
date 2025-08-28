import csv
from pathlib import Path

workspace = Path("participant_pkg")
csv_file = workspace / "contacts.csv"

f= open(csv_file, "w", encoding="utf-8")
f.write("Name,Age,Phone,Track")
f.close()


def save_participant(path,participant_dict):
    rows = list(participant_dict.values())
    if csv_file.exists():
        with open(csv_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(rows)
    print ("Contact file successfully created")


print("\nReading ")
with open(csv_file, "r", encoding="utf-8") as f:
    load_participant = csv.reader(f)

    for row_number, row in enumerate(load_participant):
        if row_number == 0:
            print(f"Headers: {"|".join(row)}")
            print("-" * 40)
        else:
            name, age, phone, track = row
            print(f"{name}\t{age}\t{phone}\t{track}") 

