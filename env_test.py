# # testing the env with print statement
# # Dynamically typed language
# # Python Variables?
# # To store any data -
# # To store user data - hard code the data - any other type
# # first_name = "Angel" - String
# # name = "Subhaan 32423423423423424324"
#
# # UK_resident = yes or no - Boolean
#
# # DOB = 99 - Int
# # travel = 15.4 - float
# # salary = 40000 Int
# # gross_salary = "salary + travel"
#
# first_name = "Shahrukh" # this is an string
# last_name = "Khan"
# salary = 50 # this is an int
# travel = 3.5 # float
#
# print("shahrukh")
# print(first_name)
# #display the value of var first_name
# print(last_name)
#
# print(salary)
# print(travel)
#
# # how to find out the type of data stored in the var
# # type()
# #print(type(last_name))
#
# # interact with users by taking user data in - input()
# print("Good Morning, Please Enter your Name ")
# name = input() # took user input & stored in the var called name
# print("Hello dear " + name)
#
# # Get user first_name and last_name
# # display the names in the line
# # User DOB
# # course name
# # UK_resident
# #

salary = 1000
travel = 5.4
print(salary + travel)
print(salary > travel)


greeting = "Hello world!          "
       #    01234567891011

#
# print(len(greeting))
# print(greeting[6:])
# print(greeting[-6:])
# print(len(greeting.strip()))

#
# Example_text = "Here's some text with lot's of text"
# print(Example_text.count("text"))
# print(Example_text)
# print(Example_text.lower())
# print(Example_text.upper())





student_1 = {
    "name": "susan",
    "stream": "tech",
    "completed_lesxfssons": 4,
    "completed_lesson_names": ["variables", "data_types", "set up"]
}
print(student_1)
print(student_1["stream"])
student_1["stream"] = "devOps"
print(student_1["stream"])
print(student_1.keys())