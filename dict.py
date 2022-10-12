# What is a Dictionary - Data Collection type
# How to manage Dictionaries - How to manage the data using Dict
# It works as Key value pair key = value
# Syntax  = { "name": "Sparta"       }
            # 0        1
# store student's data - name, course_name, progress, completed_lessons_names
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











