# import csv and path library
import csv
import file_ops
from pathlib import Path


# Define folder to store csv file
workspace = Path(r"task_submissions\Kanyisola_Fagbayi_task_11_contact_saver\participant_pkg")
csv_file = workspace / "contacts.csv"
csv_file


# Defining a function to get and validate the participant's name
def get_name():

    while True: 
        print("\nWelcome to NCC workshop") # Press 1
        print("\nPress 1 for Registration")

        choice = input("\nplease enter your selection: ")

        if choice == "1":
            try:
                name = str(input("Please enter your name: ").strip()) # Name must be a string and without whitespace
                if (len(name) == 0) or (name.isdigit()== True):         # Name cannot be empty or a digit
                    raise ValueError("Invalid input!\n Enter a name")
                else:
                    return (name)  # prints valid name
            except ValueError as e:
                print(e)
            except Exception as e:
                print("Unexpected error:", e)
                


# Defining a function to get and validate the participant's age
def get_age():

    while True:
        try:
            age= int(input("Please enter your age: ")) # age must be an integer
            if age <= 12:                       # age cannot be less than 12
                print("Too young to register")
            else:
                return (age)        # prints valid age
        except ValueError:
            print("Invalid input, input a number")
        except Exception as e:
            print("Unexpected error:", e)


# Defining a function to get and validate the participant's phone
def get_phone():

    while True:
        try: 
            phone = input("Please enter your Phone: ")
            if (len(phone) != 11) or (phone.isdigit() == False): # Phone must be digits and cannot be empty or less than 11
                raise ValueError("Invalid input! please enter 11 digits")  
            else:
                    return (phone) # prints valid phone
        except ValueError as e:
            print(e)
        except Exception as e:
            print("Unexpected error:", e)


# Defining a function to get and validate the participant's track
def get_track():

    while True:
        try:
            track = str(input("Please enter your track: "))     # Track must be a string and without whitespace
            if (len(track) == 0) or (track.isdigit()== True):   # Track cannot be empty or a digit
                raise ValueError("Invalid input!\n Enter a track")
            else:
                return (track)  # prints valid track
        except ValueError as e:
            print(e)
        except Exception as e:
            print("Unexpected error:", e)


# Main function to control the flow of the program

def main():
    while True:
        try:        # Getting the details of the participant
            name = get_name()
            age = get_age()
            phone = get_phone()
            track = get_track()

            # Save the details in the participant dictionary
            participant = {"Name": name, "Age": age, "Phone": phone, "Track": track}

            try:        # Save the details to a csv file
                file_ops.save_participant(csv_file, participant)
                print("Data written to csv file!")

            # Ask the participant if they want to add another contact
                update_participant = input("Do you want to add another contact? Yes or No: ").lower()
                if update_participant != "yes":      # If no, display the contact and exit the program
                    print("Saved contact")
                    file_ops.load_participant(csv_file)
                    break
            except Exception:
                print("Unexpected error encountered while loading the contact")
        except Exception as e:
            print("Unexpected error:", e) 

# Run the program
if __name__ == "__main__":
     main()





