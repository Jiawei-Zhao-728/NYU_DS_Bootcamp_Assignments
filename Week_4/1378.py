# Pandas Solution for LeetCode 1378: Replace Employee ID with Unique Identifier

import pandas as pd
Employees = pd.DataFrame({
    'id': [1, 7, 11],
    'name': ['Alice', 'Bob', 'Meir']
})
EmployeeUNI = pd.DataFrame({
    'id': [3, 11, 90],
    'unique_id': [1, 2, 3]
})
result = Employees.merge(EmployeeUNI[['id', 'unique_id']], on='id', how='left')
result = result[['unique_id', 'name']]

print(result)

