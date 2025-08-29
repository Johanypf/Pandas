
import pandas as pd 
data = {
'student_id' : [101,53],
'name' :   ['Ulysses','William'],
'age' : [13,10]
}
data_2 = pd.DataFrame(data)
print(data_2)

data_2["bonus"]= data_2['age'] * 2
print(data_2.drop_duplicates)