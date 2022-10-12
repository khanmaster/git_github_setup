# Python intro 
## Why Python
### Python use cases
#### Python set up with Pycharm
##### Python Variables 

- Env Testing `print("hello world")`

```python
print("Good Morning, Please Enter your Name ")
name = input() # took user input & stored in the var called name
print("Hello dear " + name)
```
```python
# testing the env with print statement
# Dynamically typed language
# Python Variables?
# To store any data -
# To store user data - hard code the data - any other type
# first_name = "Angel" - String
# name = "Subhaan 32423423423423424324"

# UK_resident = yes or no - Boolean

# DOB = 99 - Int
# travel = 15.4 - float
# salary = 40000 Int
# gross_salary = "salary + travel"

first_name = "Shahrukh" # this is an string
last_name = "Khan"
salary = 50 # this is an int
travel = 3.5 # float

print("shahrukh")
print(first_name)
#display the value of var first_name
print(last_name)

print(salary)
print(travel)

# how to find out the type of data stored in the var
# type()
#print(type(last_name))

# interact with users by taking user data in - input()
print("Good Morning, Please Enter your Name ")
name = input() # took user input & stored in the var called name
print("Hello dear " + name)

# Get user first_name and last_name
# display the names in the line
# User DOB
# course name
# UK_resident

```
#### Git & Github
- add changes to our Git-Hub repo - the changes that we made on localhost

- `git add filename` or `git add .` . means push everything from current location
- `git commit -m "new markdown guide added"`
- now let's send this new data to Github
- `git push -u origin main`
- `git status`
<<<<<<< HEAD
- add `.gitignore` then `add all dependencies in this file to ensure not pushed to github`
- To pull changes from Git-hub `git pull`
=======
### This change is done on Github
>>>>>>> e4e943727b8af19f4143fb220a7df20565dba505

```bash
These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone             Clone a repository into a new directory
   init              Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add               Add file contents to the index
   mv                Move or rename a file, a directory, or a symlink
   restore           Restore working tree files
   rm                Remove files from the working tree and from the index
   sparse-checkout   Initialize and modify the sparse-checkout

examine the history and state (see also: git help revisions)
   bisect            Use binary search to find the commit that introduced a bug
   diff              Show changes between commits, commit and working tree, etc
   grep              Print lines matching a pattern
   log               Show commit logs
   show              Show various types of objects
   status            Show the working tree status

grow, mark and tweak your common history
   branch            List, create, or delete branches
   commit            Record changes to the repository
   merge             Join two or more development histories together
   rebase            Reapply commits on top of another base tip
   reset             Reset current HEAD to the specified state
   switch            Switch branches
   tag               Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)
   fetch             Download objects and refs from another repository
   pull              Fetch from and integrate with another repository or a local branch
   push              Update remote refs along with associated objects

'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
See 'git help git' for an overview of the system.

```

### Intro to Data types & Operators
- `+ - * /`

###### Comparison Operators 
- `>` greater than
- `<` less than
- `==` True or False 
- `>=` greater than or equal 
- `<=` less than or equal

```python
a = 24
b = 16
user_age = 18
print(a + b) # outcome added  value of a & b
print(a - b) # outcome - a from b
# comparison
print(a > b) # True
print(a < b) # False
print(a == b)
```
```python
# Boolean Builtin methods in Python - Boolean Methods
# - DRY do not repeat yourself print("")

greeting = "Hello World!"
print(greeting)
print(greeting.isalpha())
print(greeting.islower())
print(greeting.startswith("H"))
print(greeting.endswith("!")) # checks if it ends with specific letter
print(greeting.isdigit())

```
```python
# String Slicing
# string indexing - starts from 0
# H e l l o   W o r l  d  !
# 0 1 2 3 4 5 6 7 8 9 10 11
#                   -3 -2-1

greeting = "Hello World!"
#print(greeting)
# we have builtin method that checks the len of string
#print(len(greeting)) #
print(greeting[-2])
print(greeting[0:5]) # prints 0-5
print(greeting[-6:]) #

```
```python
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

```
### Concatention & Casting
- adding strings together
- casting/converting data types
```python
# Data Collections
# Lists
# Tuples
# Dict

# Lists
# syntax list_name = ["adfsf", "asdfdsfa", "2dfasdfsa"]

# apply DRY
shopping_list = ["katchup", "fanta", "eggs", "bread"]
    # indexing      0         1        2        3
# print(shopping_list)
# # print(type(shopping_list))
# shopping_list.append("chicken")
# print(shopping_list) # add an item to the list
# print(shopping_list[2])
# shopping_list[2] = "icecream"
# print(shopping_list)
# # find out how to remove an item from the list
#
# # find out how to remove fanta from list
# shopping_list.pop()
# print(shopping_list) # deletes the last item
#
# shopping_list.remove("bread")
# print(shopping_list)

# # Can list have multiple data types
# multiple_type = [1, 2, 3, "one", "five", "ten"]
# print(multiple_type)
# print(multiple_type[2])

# Tuples
# Immutable - cant be changed - edited - added
# user_details = DOB - country name - city name -
# Syntax ("")
essentials = ("milk", "paracetamol", "drinks")
print(essentials)
print(type(essentials))
# what is the diff between Lists & tuples
essentials [0] = "coffee"
print(essentials)
```

#### What is a Dictionary - Data Collection type
#### How to manage Dictionaries - How to manage the data using Dict
#### It works as Key value pair key = value
#### Syntax  = { "name": "Sparta"       }
            # 0        1
###### store student's data - name, course_name, progress, completed_lessons_names
```python

student_1 = {
    "key" : "values",
    "name": "Shahrukh",
    "stream": "DevOps",
    "completed_lessons": 4,
    "completed_lessons_names": ["lists", "tuples", "OOP"]
                             #    0         1          2
}
print(type(student_1))
print(student_1["stream"]) # This will display the value saved inside stream

# # print/display completed_lessons_names
# print(student_1["completed_lessons_names"])
#
# # print/display completed_lessons_names index 0 means lists
print(student_1["completed_lessons_names"][0])
#
student_1["completed_lessons"] = 3
print(student_1["completed_lessons"])
delete an item from the list of completed_lessons_name/key
student_1["completed_lessons_names"].remove("OOP")
print(student_1["completed_lessons_names"])
# Dict Builtin Methods
# display keys only or values
# keys() values()
print(student_1.keys())

# display values only from student_1
print(student_1.values())

#












```

