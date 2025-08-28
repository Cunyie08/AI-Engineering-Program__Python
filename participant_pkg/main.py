from participant_pkg import file_ops



def main():
    file_ops.load_participant()

    while True:
        print("\nWelcome to NCC workshop") # Press 1
        print("1. Registration")
        print("2. Enquiries")

        choice = input("please enter your selection: ")

        if choice == "1":
            try:
                name = str(input("Please enter your name: "))
                if (len(name) == 0) or (name.isdigit()== True):
                    raise ValueError("Invalid input!\n Enter a name")   
            except ValueError as e:
                print(e)

            try:
                age= int(input("Please enter your age: "))
                if age >= 12:
                    pass
                else:
                    print("Error!, particpants have to be above 16")
            except ValueError:
                print("Invalid input, input a number")


            try: 
                phone = input("Please enter your Phone: ")
                if (len(phone) != 11) or (phone.isdigit() == False):
                    raise ValueError("Inavlid input! please enter 11 digits")   
            except ValueError as e:
                print(e)

            try:
                track = str(input("Please enter your track: ").split())
                if (track.isdigit()== True):
                    raise ValueError("Invalid input, please enter your track.")
            except ValueError as e:
                print(e)
        file_ops.row(name,age,phone,track)
        print("Workshop Contact\n")
        print()

# participant_dict = {}

# participant_dict["Name"] = name
# participant_dict["Age"] = age
# participant_dict["Phone"] = phone
# participant_dict["Track"] = track


