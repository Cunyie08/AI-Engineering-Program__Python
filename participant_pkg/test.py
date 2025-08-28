# def get_age():
#     try:
#         age= int(input("Please enter your age: "))
#         if age >= 16:
#             print(age)
#         else:
#             print("Error!, particpants have to be above 16")
#     except TypeError:
#         print("str only allowed!")
# get_age()



def get_name():
    try:
        name = str(input("Please enter your name: "))
        print(name)
        if name.isdigit():
            raise ValueError("It funds.nsufficien")
    except ValueError as e:
        print(e)
get_name()


# try:
#     name = str(input("Please enter your name: "))
#     print(name)
# except ValueError:
#     print("str only allowed!")