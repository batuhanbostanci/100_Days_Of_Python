import random
# List Comprehension Part
# list = [new_item in item for list]
numbers = [1, 2, 3]
new_list = [n + 1for n in numbers]

new_numbers = [n * 2 for n in numbers]
name = "batuhan"
# for leeters in name:
#     print(leeters)

letter_list = [letter for letter in name]

bakalim = [n * 2 for n in range(1, 5)]

names = ["Alex", "Beth", "Caroline", "Dave", "Elaonor", "Freddie"]
upper_names = [name.upper() for name in names]

# Dictionary Comprehension Part
# new_dict = {new_key: new_value for (key, value) in dict.items() if test}



# names = ["Alex", "Beth", "Caroline", "Dave", "Elaonor", "Freddie"]
#
# students_score = {student: random.randint(1, 100) for student in names}
# passed_students = {student: score for (student, score) in students_score.items() if score >= 60}
# print(students_score)

##################

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [46, 76, 98]
}

for(key, value) in student_dict.items():
    print(key)

import pandas as pd

# This is for loop for data Frames but it slows when you print this or more data, easy way is basically using iterator
# for rows
student_data_frame = pd.DataFrame(student_dict)
# for(key, value) in student_data_frame.items():
#     print(key)

for(index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row)