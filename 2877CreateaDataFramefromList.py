# Write a solution to create a DataFrame from a 2D list called student_data. This 2D list contains the IDs and 
# ages of some students.
# The DataFrame should have two columns, student_id and age, and be in the same order as the original 2D list.
# The result format is in the following example.

# Example 1:
# Input:
# student_data:
# [
#   [1, 15],
#   [2, 11],
#   [3, 11],
#   [4, 20]
# ]
# Output:
# +------------+-----+
# | student_id | age |
# +------------+-----+
# | 1          | 15  |
# | 2          | 11  |
# | 3          | 11  |
# | 4          | 20  |
# +------------+-----+
# Explanation:
# A DataFrame was created on top of student_data, with two columns named student_id and age.

import pandas as pd

def createDataframe(student_data) -> pd.DataFrame:

    student_id_1 = []
    age_1 = []
    for i in student_data:
        student_id_1.append(i[0])
        age_1.append(i[1])

    pre_df = {'student_id':student_id_1, 'age': age_1}
    data = pd.DataFrame(pre_df)

    return data   
student_data = [
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]

a =createDataframe(student_data)
dataa = list(a.shape)
print(dataa)