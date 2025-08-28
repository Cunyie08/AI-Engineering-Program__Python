print("==============================================================")
print("Q3: SCHOOL REGISTRATION FORM")
print("==============================================================")
# print request statement
first_name = input("Admin: Please can i have your first name?: ") # press enter
last_name = input("Admin: Please can i have your last name?: ")
class_ = input("Admin: What class are you?: ")
state_of_origin = input("Admin: What is your state of origin?: ")


# Print response statement using concatenation
print("Full name: " + first_name + " " + last_name)
print("Class: " + class_)
print("State of Origin: " +  state_of_origin)
# print output sentence using concatenation
print((first_name + " " + last_name + " " + "is a student in" 
      + " " + class_ + " " + "and she is from" + " " + state_of_origin + " " + "state." + "\n").strip())