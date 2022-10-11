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






