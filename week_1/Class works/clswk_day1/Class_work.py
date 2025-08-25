print("====================================================")
print("Task 1: Write a python program that prints your\n"
"information on separate lines")
print("====================================================\n")
# Add variables
name = "Kanyisola Fagbayi"
Uni = "University of Lagos"
LGA = "Ojo LG"
Favorite_Nigerian_food = "Fried Plantain"
# print output statement
print("Name: " , name)
print("Uni: " , Uni)
print("LGA: " , LGA)
print("Favorite Nigerian Food: " , Favorite_Nigerian_food)

print("\n====================================================")
print("Task 2: Write a python program that stores your name \n"
"and state of origin in variable, print message")
print("====================================================\n")
# Add variables
name = "Kanyisola Fagbayi"
state_of_origin = "Lagos State"
# print output statement using the variables
print("My name is" ,name + "," + " " + "I'm from" , state_of_origin + ".")

print("\n====================================================")
print("Task 3: Print a simple timetable for a week in a\n"
"Nigerian Secondary School using tab spacing and new lines")
print("====================================================\n")
# Add output statement
print("Days\t08:00-09:00\t09:00-10:00\t10:00-10:30\t"
      "10:30-11:30\t11:30-12:30\t12:30-13:30\t13:30-14:30\t14:30")
print("\nMon.\tEng.\t\tEng\t\tS\tB\tBio.\t\tL\tB\tAgric\t\tFrench\t\tCLOSING")
print("\nTues.\tMaths\t\tMaths\t\tH\tR\tBio.\t\tO\tR\tLit-in-Eng.\tAgric.\t\tCLOSING")
print("\nWed.\tGovt.\t\tGovt.\t\tO\tE\tNig. Lang.\tN\tE\tCivic\t\tMarketing\tCLOSING")
print("\nThurs.\tEcons.\t\tEcons.\t\tR\tA\tEng.\t\tG\tA\tLit-in-Eng.\tAgric.\t\tCLOSING")
print("\nFri.\tMaths\t\tNig. Lang.\tT\tK\tCivic\t\t \tK\tP.E\t\tCLOSING\t\tCLOSING")

print("\n====================================================")
print("Task 4: Write a python program that uses variables\n"
"to store:\nYour name\nYour class\nYour best subject\n"
"Use an f-string to format and print them in a sentence")
print("====================================================\n")
# Add input statement
name = "Kanyisola Fagbayi"
Class = "AI Engineer"
best_subject = "Python Programming Language"
# print output statement using an f-string
print(f"My name is '{name}', I am currently enrolled\n"
      f"into an '{Class}' track at NCC Abeokuta.\n"
      f"My best subject so far is '{best_subject}'.")

print("\n====================================================")
print("Task 5: Write a short 3-line poem about Nigeria and\n"
"print it using triple quotes")
print("====================================================\n")
# Add input statement
line_1 = "Nigeria, Nigeria!"
line_2 = "Nigeria is our fathers' land"
line_3 = "Nigeria is my homeland."
# print output statement using doc string
print("""Nigeria, Nigeria!
Nigeria is our fathers' land
Nigeria is my homeland.
      """)
# Print output statement using f-string
print(f"""{line_1}\n{line_2}\n{line_3}""")
print("\n====================================================")