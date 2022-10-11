# Let's see the operators in actoin
### Intro to Data types & Operators
# - `+ - * /`
#
# ###### Comparison Operators
# - `>` greater than
# - `<` less than
# - `==` True or False
# - `>=` greater than or equal
# - `<=` less than or equal
# To comment multiple line `ctr+/`
# a = 24
# b = 16
# user_age = 18
# print(a + b) # outcome added  value of a & b
# print(a - b) # outcome - a from b
# # comparison
# print(a > b) # True
# print(a < b) # False
# print(a != b) # equal

# % operator - find out what it is how it's used in python
# create a print statement to show the use case of it

# # Boolean Builtin methods in Python - Boolean Methods
# # - DRY do not repeat yourself print("")
#
# greeting = "Hello World!"
# print(greeting)
# print(greeting.isalpha())
# print(greeting.islower())
# print(greeting.startswith("H"))
# print(greeting.endswith("!")) # checks if it ends with specific letter
# print(greeting.isdigit())

# String Slicing
# string indexing - starts from 0
# H e l l o   W o r l  d  !
# 0 1 2 3 4 5 6 7 8 9 10 11
#                   -3 -2-1

# greeting = "Hello World!"
# #print(greeting)
# # we have builtin method that checks the len of string
# #print(len(greeting)) #
# print(greeting[-2])
# print(greeting[0:5]) # prints 0-5
# print(greeting[-6:]) #

# String Methods are available

# use var = string "asfdsfaasdfsadfsadf                                 "
white_space = "lot's of spaces at the end                                "
print(len(white_space))
# strip() removes the white spaces at the end of the string
print(len(white_space.strip())) # this will remove all the white spaces at the end
print(print(len(white_space)))

Example_text = "shahrukh here's sOme text with lOt's of text"
# print(Example_text.count("text"))
print(Example_text)
print(Example_text.lower())
print(Example_text.upper())
print(Example_text.capitalize())
print(Example_text.replace("with", ","))























