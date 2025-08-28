

while True:
    try:
        name = str(input("Please enter your name: "))
        if (len(name) == 0) or (name.isdigit()== True):
            raise ValueError("Invalid input!\n")   
    except ValueError as e:
        print(e)
    try:
        age= int(input("Please enter your age: "))
        if age >= 12:
            pass
        else:
            print("Invalid input!, particpants have to be above 12")
    except ValueError:
        print("Invalid input, input a number")


    try: 
        phone = input("Please enter your Phone: ")
        if (len(phone) != 11) or (len(phone)> 11) or (phone.isdigit() == False):
            raise ValueError("Invalid input! please enter 11 digits")   
    except ValueError as e:
        print(e)



    try:
        track = str(input("Please enter your track: ").split())
        if (track.isdigit()== True):
            raise ValueError("Invalid input, please enter your track.")
    except ValueError as e:
        print(e)

