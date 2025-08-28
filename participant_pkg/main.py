import csv
from pathlib import Path


workspace = Path("participant_pkg")
csv_file = workspace / "participant.csv"

def get_name():
    try:
        name = str(input("Please enter your name: "))
        if (name.isalpha()==False):
            raise ValueError("Invalid input!, enter a name")
    except ValueError as e:
        print(e) 
         


    # except ValueError:
    #     print("str only allowed!")
get_name()

# def get_age():
#     try:
#         age= int(input("Please enter your age: "))
#         if age >= 16:
#             print(age)
#         else:
#             print("Error!, particpants have to be above 16")
#     except ValueError:
#         print("str only allowed!")
# get_age()
    # phone = input("Please enter your Phone: ")
    # if len(phone) != 11:
    #     print(phone)
    # else:
    #     print("Error,phone number incomplete")

    # track = input("Please enter your track: ")
    # if len(track) != 0:
    #     print(track)

    # else:
    #     print("Error! you have not entered your track")



# age = int(input("Please enter your age: "))
# phone = int(input("Please enter your phone number: "))
# track = input("Please enter your track: ")

# participant.append(name)
# participant.append(age)
# participant.append(phone)
# participant.append(track)



participant = {}



# participant_dict = {
#         ["Name", "Age", "Course", "Track"]
# }


# with open(csv_file, "w", newline="", encoding="utf-8") as f:
#     f.write("Name,Age,Phone,Track")

# with open(csv_file, "r", encoding="utf-8") as f:
#     load_participant = f.readlines()