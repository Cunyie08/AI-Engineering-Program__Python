# import csv and path library
import csv
from pathlib import Path

# Define folder to store csv file
workspace = Path(r"task_submissions\Kanyisola_Fagbayi_task_11_contact_saver\participant_pkg")
workspace.mkdir(exist_ok=True)
csv_file = workspace / "contacts.csv"
csv_file

# Define column header for the csv file
fieldnames = ["Name", "Age", "Phone", "Track"]


# Function to save a csv_file that collects details of the participant
def save_participant(csv_file,participant):
    if type(participant) == dict: # Converts dictionary of participants to a list
        participant = [participant]
    if csv_file.exists():           # If the file exist, add new data
        with open(csv_file, "a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writerows(participant)
        print ("Contact file successfully created")

    else:                # If file doesn't exist create it and create a header first               
        with open(csv_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(participant)
    print ("Contact file successfully created")
        

# Reading the csv file to display the participants in csv 
def load_participant(csv_file):
    if csv_file.exists():
        with open(csv_file, "r", encoding="utf-8") as f:
            reader = csv.reader(f)        # reading each row

            for row_number, row in enumerate(reader):
                if row_number == 0:         # 0th is the header
                    print(f"Headers: {"|".join(row)}")
                    print("-" * 40) # use line separators
                else:                       # print the rows in a readable format
                    name, age, phone, track = row
                    print(f"{name}\t\t{age}\t\t{phone}\t\t{track}") 
    else:
        print("No participant found yet")

